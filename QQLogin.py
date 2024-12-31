# -*- coding: utf-8 -*-
"""
本软件仅供学习用途 请勿用作违法行为 后果自负!
Github仓库地址:https://github.com/sun589/QQLogin
作者:sun589
"""
import time
from mitmproxy.tools.main import mitmdump
from mitmproxy import http, options , ctx
from winproxy import ProxySetting
import atexit
import re
from configparser import ConfigParser
import os
import win32api
import psutil
from win32com.client import Dispatch
import win32crypt
import threading
import requests
import ssl
from cryptography import x509

p = ProxySetting()

def set_proxy(ip,port):
    p.enable = True
    p.server = f'{ip}:{port}'
    p.registry_write()

def close_proxy(a=0):
    if p.enable:
        print("[-] 正在关闭代理...")
        p.enable = False
        p.registry_write()

class Listener:

    def load(self, l):
        l.add_option('nickname', str, '0', 'Nickname of the user')
        l.add_option('uin', str, '0', 'UIN of the user')
        l.add_option('clientkey', str, '0', 'Clientkey of the user')

    def request(self, flow: http.HTTPFlow) -> None:
        if re.match(r'https://ssl.ptlogin2.qq.com/jump?.*', flow.request.url):
            print("[+] 检测到开始登录,检查是否登录成功...")

    def response(self, flow: http.HTTPFlow) -> None:
        uin = ctx.options.uin
        clientkey = ctx.options.clientkey
        nickname = ctx.options.nickname
        if re.match(r'https://localhost.ptlogin2.qq.com:\d+/pt_get_uins?.*', flow.request.url):
            flow.response.status_code = 200
            flow.response.reason = 'OK'
            qq = re.findall('"uin":(\d+)',flow.response.text)[0]
            print(f"[+] 已拦截到pt_get_uins请求,当前QQ号为:{qq},正在修改返回值为:{uin}")
            flow.response.set_text(re.sub('"uin":(\d+)', f'"uin":{uin}', flow.response.text))
            flow.response.set_text(re.sub('"account":(\d+)', f'"account":{uin}', flow.response.text))
            flow.response.set_text(re.sub('"nickname":"(.*?)"', f'"nickname":"{nickname}"', flow.response.text))
        elif re.match(r'https://localhost.ptlogin2.qq.com:\d+/pt_get_st?.*', flow.request.url):
            flow.response.status_code = 200
            flow.response.reason = 'OK'
            print(f"[+] 已拦截到pt_get_st请求,正在修改返回值为:{clientkey}")
            flow.response.set_text(f"""var var_sso_get_st_uin = {{
    uin: {uin},
    keyindex: 19
}};
__jp0(var_sso_get_st_uin);""")
            flow.response.headers.set_all('Set-Cookie',[f'clientuin={uin}; path=/; domain=ptlogin2.qq.com; Secure; SameSite=None',f'clientkey={clientkey}; path=/; domain=ptlogin2.qq.com; Secure; SameSite=None'])
        elif re.match(r'https://ssl.ptlogin2.qq.com/jump?.*', flow.request.url):
            if re.match("""ptui_qlogin_CB\('0', '.*', ''\)""",flow.response.text):
                print('[+] 登录成功,感谢您的使用!')
                print(f"[+] 登录返回(包含登录网址):{flow.response.text}")
            else:
                print('[-] 登录失败,请检查clientkey是否正确!')
        elif re.match(r'https://ssl.ptlogin2.qq.com/getface?.*',flow.request.url):
            uin = ctx.options.uin
            print("[+] 检测到获取QQ头像请求,正在修改返回值...")
            flow.response.status_code = 200
            flow.response.reason = 'OK'
            flow.response.set_text(f"""pt.setHeader({{
    "{uin}": "https://q1.qlogo.cn/g?b=qq&nk={uin}&s=100"
}})
""")

addons = [Listener()]

if __name__ == '__main__':
    os.system("title QQ登录器 Github仓库地址:https://github.com/sun589/QQkey_Tool")
    if not os.path.isfile('config.ini'):
        with open('config.ini', 'w', encoding='utf-8') as f:
            f.write("""[account]
# QQ号
uin=0
# QQ号对应的clientkey
clientkey=0

[proxy]
# 代理端口
port=8080

[settings]
# 自动设置代理,1为开启,0为关闭
auto_set_proxy=1
""")
            print("[!] 配置文件config.ini不存在,将写入&使用默认配置!")

    config = ConfigParser()
    config.read('config.ini', encoding='utf-8')
    port = config.get('proxy','port')
    auto_set_proxy = config.get('settings','auto_set_proxy')
    ca_certificates = [x509.load_der_x509_certificate(cert, backend=None).issuer.rfc4514_string() for
                       cert, encoding, trust in ssl.enum_certificates("CA")]
    if not "O=mitmproxy,CN=mitmproxy" in ca_certificates:
        if not os.path.isfile(os.path.join(os.path.expanduser("~"), ".mitmproxy\\mitmproxy-ca-cert.cer")):
            print("[+] 正在生成证书...")
            print("[+] 请在程序关闭后重启以安装证书!")
            threading.Thread(target=lambda: (time.sleep(5),os._exit(0))).start()
            mitmdump(['-p', port, '--quiet'])

        CERT_STORE_PROV_SYSTEM = 0x0000000A
        CERT_STORE_OPEN_EXISTING_FLAG = 0x00004000
        CRYPT_STRING_BASE64HEADER = 0x00000000
        CERT_SYSTEM_STORE_CURRENT_USER_ACCOUNT = 1 << 16
        X509_ASN_ENCODING = 0x00000001
        CERT_STORE_ADD_REPLACE_EXISTING = 3
        CERT_CLOSE_STORE_FORCE_FLAG = 0x00000001

        crtPath = os.path.join(os.path.expanduser("~"), ".mitmproxy\\mitmproxy-ca-cert.cer")

        with open(crtPath, 'r') as f:
            cert_str = f.read()

        cert_byte = win32crypt.CryptStringToBinary(cert_str, CRYPT_STRING_BASE64HEADER)[0]
        store = win32crypt.CertOpenStore(CERT_STORE_PROV_SYSTEM, 0, None,
                                         CERT_SYSTEM_STORE_CURRENT_USER_ACCOUNT | CERT_STORE_OPEN_EXISTING_FLAG, "ROOT")
        print("[+] 正在添加证书...")
        try:
            store.CertAddEncodedCertificateToStore(X509_ASN_ENCODING, cert_byte, CERT_STORE_ADD_REPLACE_EXISTING)
            with open('config.ini','w',encoding='utf-8') as f:
                config.set('settings','installed_cert_already','1')
                config.write(f)
            print("[+] 证书添加成功!")
        except:
            print("[!] 您取消了安装请求,这意味着您可能将无法正常使用本工具!")
        finally:
            store.CertCloseStore(CERT_CLOSE_STORE_FORCE_FLAG)
    try:
        nickname = requests.get(
            f"https://users.qzone.qq.com/fcg-bin/cgi_get_portrait.fcg?uins={config.get('account', 'uin')}",
            proxies={}).text
        nickname = re.findall(r'\[.*,.*,.*,.*,.*,.*,"(.*)",.*\]', nickname)[0]
    except:
        print("[!] 昵称获取失败,将使用QQ号代替!(不影响实际效果)")
        nickname = config.get('account', 'uin')
    classic_ver = '9.7.24' # 旧版最高为9.7.23,因会有小版本号(9.7.23.xxxxx),故为9.7.24
    print("[+] 开始寻找QQ进程...")
    for i in psutil.pids():
        try:
            process = psutil.Process(i)
            if 'QQ.exe' in process.name():
                path = process.exe()
                parser = Dispatch("Scripting.FileSystemObject")
                version = parser.GetFileVersion(path)
                print("[+] 进程寻找完毕!")
                print(f"[+] QQ版本:{version}{' classic' if version <= classic_ver else ' NT'}")
                print(f"[+] QQ路径:{path}")
                if version <= classic_ver:
                    print("[!] 您当前使用的是经典版QQ,可能会出现无法工具正常拦截修改的情况!")
                break
        except:
            pass
    else:
        print("[!] 未找到QQ进程,程序仅在QQ运行情况下才可正常使用!!")
    print("[+] 启动拦截程序...")
    if auto_set_proxy == '1':
        print("[+] 正在设置代理...")
        set_proxy('127.0.0.1',int(port))
        atexit.register(close_proxy)
        win32api.SetConsoleCtrlHandler(close_proxy, True)
    print(f"[+] 当前程序代理已开放至*:{port}")
    mitmdump(['-s',__file__,'-p',port,'--quiet','--set',f'nickname={nickname}','--set',f'uin={config.get("account","uin")}','--set',f'clientkey={config.get("account","clientkey")}'])
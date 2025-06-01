# QQLogin
[![Author-sun589](https://img.shields.io/badge/Author-sun589-52616b.svg?logo=github)](https://github.com/sun589)
[![GitHub License](https://img.shields.io/github/license/sun589/QQkey_Tool?logo=github)](https://github.com/sun589/QQkey_Tool/blob/main/LICENSE)
[![Language-python](https://img.shields.io/badge/Language-python-yellow?logo=python)](https://github.com/sun589/QQkey_Tool)
> 通过mitmproxy实现通过QQkey理论登录任何网站的小工具  
> 更多实用功能(如扫码控号,木马拿Key)见我的另一个仓库[QQkey_Tool](https://github.com/sun589/QQkey_Tool)

<details><summary>免责声明【必读】</summary>

### **本工具仅供学习和技术研究使用，不得用于任何非法行为，否则后果自负。**

**本工具的作者不对本工具的安全性、完整性、可靠性、有效性、正确性或适用性做任何明示或暗示的保证，也不对本工具的使用或滥用造成的任何直接或间接的损失、责任、索赔、要求或诉讼承担任何责任。**

**本工具的作者保留随时修改、更新、删除或终止本工具的权利，无需事先通知或承担任何义务。**

**本工具的使用者应遵守相关法律法规，尊重QQ的版权和隐私，不得侵犯QQ或其他第三方的合法权益，不得从事任何违法或不道德的行为。**

## **本工具的使用者在下载、安装、运行或使用本工具时，即表示已阅读并同意本免责声明。如有异议，请立即停止使用本工具，并删除所有相关文件。**

</details>  

***再次声明:本软件仅用于学习用途,请勿用于违法行为 后果自负!***  
****
## 目录
- [QQLogin](#qqlogin)
  - [使用说明](#使用说明)
  - [常见问题 Q&A](#常见问题)
    - [和QQKey_Tool的Key解析器区别&原理？](#和qqkey_tool的key解析器区别原理)
    - [运行程序后浏览器提示"不安全的连接"](#运行程序后浏览器提示不安全的连接)
****
## 使用说明
从[Release](https://github.com/sun589/QQLogin/releases/latest)下载最新版本，
或者下载源代码，装好依赖，使用`python QQLogin.py`执行  
下载完成后跟着以下步骤走：  
### Step 1. 获取目标的Clientkey和QQ号
开始之前，你先要获取目标的clientkey，推荐使用我的另一个项目[QQkey_Tool](https://github.com/sun589/QQkey_Tool)获取  
clientkey一般是64位，96位和224位，这是要注意的  
### Step 2. 运行程序，生成配置，修改配置，运行使用
准备好key后，接下来就是运行程序了  
> 注意：程序将默认修改代理，在**正常退出**时关闭代理，若程序未正常退出，请重新打开并正常关闭

打开后差不多会像这样:  
  
![image](https://github.com/user-attachments/assets/45d6f98c-f153-4f06-90b4-08ca7989d179)  

这时我们关闭程序,打开config.ini,差不多长这样:  

![image](https://github.com/user-attachments/assets/992aa437-6c40-45b9-bd9e-08b4044e03be)

根据实际情况修改配置后即可正常使用程序了  
视频教程：https://img1.lookpic.cn/2024/12/31/bandicam-2024-12-31-20-32-09-495.mp4  

###### ~~实际上，他不止能登录QQ音乐，他的灵活性很大，怎么用就看你自己了（百度，网易云，4399……）~~  
****
## 常见问题
### 和[QQKey_Tool](https://github.com/sun589/QQkey_Tool)的Key解析器区别&原理？
一般的key解析只能解析腾讯业务(如`QQ空间`、`QQ群`等)可是遇到QQ音乐/网易云等需要[`oAuth`](https://baike.baidu.com/item/oAuth/7153134)登录的地方
会因为无法`callback`导致无法正常登录，本款工具的优势正是本处——通过修改QQ客户端返回的clientkey实现登录任何QQ登录网站
### 运行程序后浏览器提示"不安全的连接"  
![image](https://github.com/user-attachments/assets/335896b6-994a-4fcb-8028-90c2b612fd62)  

如图  
出现以上问题为证书未安装成功,需手动安装  
解决方法如下:
1.按下 `Win`+`r`  
  
![image](https://github.com/user-attachments/assets/e793dcca-90b8-46fa-b863-bd7773e6398b)

2.输入以下命令后点确定：
```
%userprofile%\.mitmproxy\mitmproxy-ca-cert.cer
```

![image](https://github.com/user-attachments/assets/9e3a1a9e-aba3-4001-8249-2dae9fdbd0f8)

然后跟着走：  

![image](https://github.com/user-attachments/assets/da49c9c6-c762-4bb5-812a-729375adf999)  
  
![image](https://github.com/user-attachments/assets/b8f52eae-758b-4fbf-a134-a8189a6c32d9)  

![image](https://github.com/user-attachments/assets/99497102-4205-40dc-aa33-fb4d9dea6636)  

![image](https://github.com/user-attachments/assets/de600f1a-bddc-4f2f-b616-e71e5424de2f)

安装后就解决了：）


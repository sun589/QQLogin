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



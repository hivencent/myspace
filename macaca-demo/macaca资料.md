##macaca

###MAC环境：
ios：

	Mac OS X >= 10.7
	XCode >= 4.6.3
	Apple Developer Tools (iPhone simulator SDK, command line tools)
	
android：

	java 1.8.0_131
	JAVA_HOME is set
	ANDROID_SDK
	    - API leave >= 25
	gradle = 3.5
	    - 地址：https://services.gradle.org/distributions/
	macaca-android = 2.0.36
		- cnpm install macaca-android -g   //npm安装失败，no such file XXX
	app-inspector@2.0.7 


**1. NODE**

	- 官方地址: https://nodejs.org/
	- 安装命令:brew install node
	- node目录   /usr/local/node_modules

**npm**

- 基本信息
	- npm目录   /usr/local/bin/npm
	- node版本：8.5.0
	- npm版本：5.3.0
- 常用命令
	- npm install express -g  #-g全局
	- npm list -g --depth 0  #查看当前目录下已安装的node包



**brew安装**
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall)"



**chrome远程调试**
参考：http://www.cnblogs.com/miss-radish/p/4990871.html


**app-inspect调试**

1. 安装 npm install app-inspector -g
2. adb devices
3. 	app-inspector -u YOUR-DEVICE-ID

	http://localhost:5678/


##macaca API


##app-inspect调试
1. app-inspector --port 56789 -u 63bfec57 --verbose



**问题记录**

1. macaca-android安装失败
	- gradle降级到3.5，使用cnpm安装
2. macaca-android 升级 2.0 后执行用例报错
    - 降级到gradle3.5试试
    - 参考：https://testerhome.com/topics/8561
3. demo
	
4. 没有成功启动macaca server，导致死循环wait server
	暂时解决:手动启动，macaca server -p port --verbose
5. chrome-driver位置
	
	- /usr/local/lib/node_modules/macaca-chrome/node_modules/_macaca-chromedriver@1.0.37@macaca-chromedriver/exec


**与appium和webdriver不同**
1. 手机浏览器测试：
    - 不同切面需要每次都切换到新的WEBVIEW，否则报错找不到元素
    - 调用内置手机浏览器，driver.close()，无法关闭标签页，测试完成后没有扫尾，下次再打开仍然是上次测试的界面。
2. Android：
    -  desired_caps设置简单


参考：

1. 【环境安装】http://www.cnblogs.com/jinjiangongzuoshi/p/6537795.html
2. 【macaca实例】https://github.com/macaca-sample/macaca-test-sample-python
3. Python API文档：https://macacajs.github.io/wd.py/
4. https://testerhome.com/topics/8618
5. macaca isuues：https://github.com/alibaba/macaca/issues
7. **【macaca Document】**https://macacajs.github.io/zh/introduction
8. 【chrome-driver下载地址】http://chromedriver.storage.googleapis.com/index.html?
9. 【Macaca Puppeteer驱动】https://testerhome.com/topics/9753
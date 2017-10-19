##Appium


###使用
1. **指定chrome版本**
    
    - appium --chromedriver-executable /usr/local/lib/node_modules/appium/node_modules/appium-chromedriver/chromedriver/mac/chromedriver2.20

###查看本地APK包名和ACTIVITY
    1. 进入ANDROID_HOME 目录
    2. aapt dump badging ${apk_file_path.apk} 


###遇到的问题总结

1. [debug] [Chromedriver] Webview version: 'Chrome/53.0.2785.49'
[debug] [JSONWP Proxy] Got response with status 200: {"sessionId":"fc4bf239a2b19e7210e7f6af86095be2","status":33,"value":{"message":"session not created exception: please close '' and try again\n  (Driver info: chromedriver=2.30.477690 (c53f4ad87510ee97b5c3425a14c0e79780cdf262),platform=Mac OS X 10.10.5 x86_64)"}}
[Chromedriver] Chromedriver exited unexpectedly with code null, signal SIGTERM
[debug] [Chromedriver] Changed state to 'stopped'
[Chromedriver] Error: session not created exception: please close '' and try again
  (Driver info: chromedriver=2.30.477690 (c53f4ad87510ee97b5c3425a14c0e79780cdf262)
    
    解决：
    
        - 如果是H5测试，chrome版本和chromedriver对应
        - 如果是android，应用内核版本和chromedever对应
	解决2： 更换chromedevice2.20
2. chrome-inspect空白：

	解决： 需翻墙
3. 切换到Webview,一直等待的问题
	
	- 这个问题再android7.0系统出现频路高，6.0系统少。
	- 暂时解决：先切换到NATIVE_APP，再切换到WEBVIEW
	- 解决：appium添加属性recreateChromeDriverSessions = True
	- appium API上说的是每次切换到非chrome-Driver时kill掉session 注意这个设置在appium 1.5版本上才做了处理
	- 参考：https://testerhome.com/topics/6279

com.datebao.datebaoapp.SparkActivity

###资料：

1. chromedriver下载地址：http://chromedriver.storage.googleapis.com/index.html
2.  appium （五）desired_caps参数：http://blog.csdn.net/yejianyun1/article/details/56279051
	- **desired_caps['app']**：指定安装路径，如果是android系统，指定了app-package和app-activity，则不需要指定app
	- **desired_caps['browserName']**：手机浏览器自动化测试，如果是针对应用做自动化测试，那么值为空，iOS系统用safari，android系统可以用：Chrome，Chromium，Browser
	- noReset：不需要在回话前重置应用状态，默认false
	- fullReset：iOS,删除整个模拟器目录。Android，通过卸载重置应用状态，会话结束后自动清除被测应用，默认false。
	- autoWebview：直接切换到WEBVIEW上下文，默认false
	- appActivity：你要从你的应用包中启动的Android Activity名称，它通常需要在前面加 .
3. 【appium支持ANDROID7.0】https://testerhome.com/topics/8419
4. 【UIautomator2.0】https://kkboxsqa.wordpress.com/2017/09/18/appium-and-uiautomator2-part1/
	
###遗留问题
1. 使用unicodeKeyboard后，测试结束后重置输入法不成功。



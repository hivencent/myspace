aliyun机器：
101.200.161.122 (公)
10.44.53.113 (内)

##常用命令
**过滤日志文件**

	cat access.log |awk '{print $13}'| sort | uniq -c |sort -n
	cat /etc/httpd/logs/ip.log |awk '{print $7}'| sort |sort -n | awk -F '=' '{print $2}' | awk -F '&' '{print $1}' | uniq -c | sort -n > phone.log

**rsync同于文件**

	rsync -av ~/Desktop/icaopan_test/ -e ssh root@101.200.161.122:/home/jinlong

#icaopan
-------------

	1. 邮箱：qiye163.com 账号：jinl@icaopan.com  密码：jinlong1990
	2. 数据库： mysql -uadmin -p123456 -h192.168.1.55
	3. 测试机器：
		* 服务：ssh root@192.168.1.96	123456	
		* 任务：192.168.1.64	账号：Administrator  密码：123456
		* 数据库： ssh root@192.168.1.55	123456
	4. 自动化测试机 ：ssh jinlong@192.168.1.219  su - root 密码：123456
	5. jenkins地址：http://192.168.1.219:8181/jenkins/		develop develop && jinlong 123456
	6. MQ地址：http://192.168.1.96:15672/#/queues  账号：admin    密码：admin

## 线上理财120
	
	1. 理财平台SVN地址：https://192.168.1.222/svn/finance/trunk
	
**测试服**

		* 10.10.63.171/120.132.60.113 	#测试服test_120server UHbxoxc5
		* 前台：http://10.10.63.171     #1601033353/a123456
			* 后台：http://10.10.63.171/confidential   #admin/123456
		* 数据库IP ：mysql -up2puser3 -pPassw0rd -h120.132.60.113  #测试


### jenkins构建策略：

		1. Build periodically：0 8 * * *      #每天8点构建
		2. Poll SCM：*/30 * * * *		#每30分钟监听svn一次，如果有则构建 
	
			例子：
			第1列分钟1～59
			第2列小时1～23（0表示子夜）
			第3列日1～31
			第4列月1～12
			第5列星期0～6（0表示星期天）
			第6列要运行的命令
			
			下面是crontab的格式：
			分 时 日 月 星期 要运行的命令
			这里有crontab文件条目的一些例子：
			00 01 * * * /usr/local/apache/bin/apachectl restart
			上面的例子表示每晚的21:30重启apache。
			45 4 1,10,22 * * /usr/local/apache/bin/apachectl restart
			上面的例子表示每月1、10、22日的4 : 45重启apache。
			10 1 * * 6,0 /usr/local/apache/bin/apachectl restart
			上面的例子表示每周六、周日的1 : 10重启apache。
			0,30 18-23 * * * /usr/local/apache/bin/apachectl restart
			上面的例子表示在每天18 : 00至23 : 00之间每隔30分钟重启apache。
			0 23 * * 6 /usr/local/apache/bin/apachectl restart
			上面的例子表示每星期六的11 : 00 pm重启apache。
			* */1 * * * /usr/local/apache/bin/apachectl restart
			每一小时重启apache
			* 23-7/1 * * * /usr/local/apache/bin/apachectl restart
			晚上11点到早上7点之间，每隔一小时重启apache
			0 11 4 * mon-wed /usr/local/apache/bin/apachectl restart
			每月的4号与每周一到周三的11点重启apache
			0 4 1 jan * /usr/local/apache/bin/apachectl restart
			一月一号的4点重启apache

**数据库迁移测试环境228**

		# 从171迁移过来
		* 机器：	ssh root@192.168.1.228 123456
		* 数据库：
			* 外网地址：119.253.45.146
			* mysql -uYcfuser01 -pLCxmby009 -h192.168.1.232  ycf

**开发本地数据库**
		* 开发的数据库  IP：192.168.1.230  
		* 用户名：ycfdev  密码： ycfdev123  库名：ycf_dev
		
**LC2.0开发联调环境**
		
		* 测试服_205：
		      内网IP ：10.10.192.205/120.132.55.23  root  G9uN89A4  
		* 用户名：root 密码统一为：www.icaopan.net
		* 数据库IP ：
				1. 【本地外网】mysql -up2puser3 -pPassw0rd -h119.253.45.146 -P45452
				2. root密码：sw1988914
				* mysql机器内网地址：ssh root@192.168.1.232  密码：123456
		* 部署：source ~/Desktop/env/bin/activate && fab -f ~/Desktop/icaopan_licai/trunk/deploy/fabfile_lc.py deploy --set group=staging_205
		
		
**测试task机器**
		* 10.10.222.11  root  密码：www.baidu.net

**预生产服务器**
		
			* 10.10.156.119/123.59.40.91  Y0VD2pd7
	
**线上老数据库**

		* 数据库IP ： mysql -uroot -pICAOPAN2015 -h 10.10.161.14  

**线上新数据库** 
		
		* 数据库IP ： mysql -uroot -pwwwycf365com -h 10.10.199.99
	
**线上服务器**

		* WEB1：10.10.197.113  密码：SIca8SQ1  
		* WEB2：10.10.22.185 密码：LBmGUvx9
		* 线上理财后台：http://10.10.187.251/confidential/  HqxcAxg7

**性能测试**

		* Agent1：10.10.77.215:   administrator   JNOtPr57
		* Agent2：10.10.84.203:	  administraror    V1Wplkj7
		* 测试机：10.10.223.36		root  woshibangbangde
		* 数据库：10.10.178.86  用户名 root  密码：yaliceshimysql


**SSH通道**

		* 自动化测试服192.168.1.219和UCloud测试服10.10.63.171,已打通。
		* 自动化测试服192.168.1.219和UCloud开发联调环境10.10.192.205,已打通
		* 自动化测试服192.168.1.219和UCloud预生产10.10.156.119,已打通。
		* 自动化测试服192.168.1.219和UCloud线上WEB1 10.10.197.113,已打通。
		* 自动化测试服192.168.1.219和UCloud线上WEB2 10.10.22.185,已打通。
		* UCloud测试服10.10.63.171和UCloud线上后台机器10.10.187.251，已打通。
		* 预生产119和线上3个机器（113&185&251），已打通
	
**VPN配置**

		* 192.168.1.219已经和所有UCLOUD机器打通
		* 192.168.1.219和测试服：10.10.63.171，已经配置
		* 192.168.1.219和预生产：10.10.156.119，已经配置

		
		
    
## 自动化测试服219
	1. mysql:service mysqld status 
	2. mysql -uroot -p -h127.0.0.1 -P3306 
	3. 代码目录：/var/deploy/p2p/p2p
		account  我的账户
		cms 新闻
		log 日志
		margin  用户资金查询
		p2p 项目标的/资金业务
		pay 支付
		preorder  投标记录
		profile  用户信息
		rest  接口
		root 配置
		sms  短信
		static  样式/配置/首页


#工作问题记录
## SVN常用命令：
	
	**svn 安装**
 	 yum -y install subversion

	1. svn revert $file    #单个撤销修改
	2. svn revert -R .		#撤销所有文件
	2. svn add fabfile_lc.py			#添加文件
	3. svn commit -m 'test' /deploy/fabfile_lc.py  #提交代码
	4. svn up			#更新代码
	5. svn switch https://192.168.1.222/svn/finance/branches/version-1.0 #切换分支
	6. svn delete .git && svn ci -m 'delete .git' #删除.git目录

	
## Django单元测试：
	1.  python manage.py test：执行所有的测试用例
	2.  python manage.py test app_name, 执行该app的所有测试用例
	3.  python manage.py test app_name.case_name: 执行指定的测试用例


### Django model 常用方法记录
	1.  得到模型中的所有记录　　publisher_list = Publisher.objects.all()
	2.  保存模型的一个对象　　publish.save()
	3.  模型数据的过滤　　Publisher.objects.filter(name='Apress')        #返回一个对象列表，如果记录不存在的话，它会返回[]
	4.  得到特定记录　　Publisher.objects.get(name="Apress")             #get方法是从数据库的取得一个匹配的结果，返回一个对象，如果记录不存在的话，它会报错
	5.  数据记录排序　　Publisher.objects.all().order_by("name")
	6.  数据记录逆向排序　　Publisher.objects.all().order_by("-name")
	7.  返回限制记录　　Publisher.objects.order_by('name')[0]　　
	                Publisher.objects.order_by('name')[0:2]
	8.  快捷更新记录　　Publisher.objects.filter(id=52).update(name='Apress Publishing')
	9.  删除记录　　Publisher.objects.all().delete()
	10. Foreign Key 反向得到记录　　publisher.book_set.all()
	　　 a.  book_set 只是一个 QuerySet，所以它可以像QuerySet一样,能实现数据过滤和分切
	　　 b.  publisher.book_set.filter(name__icontains='django')
	　　 c.  属性名称book_set是由模型名称的小写(如book)加_set组成的
	11. 访问多对多值(Many-to-Many Values)
	　　  book.authors.all()
	　　b ook.authors.filter(first_name='Adrian')
	12. 反向查询
	　　  author.book_set.all()


### django modles之objects数据管理器（数据筛选）：
	1.  Entry.objects.filter(id__gt=4) ==> SELECT ... WHERE id > 4;
	2.  Entry.objects.filter(id__gte=4) ==> SELECT ... WHERE id >= 4;
	3.  Entry.objects.filter(id__lt=4) ==> SELECT ... WHERE id < 4;
	4.  Entry.objects.filter(id__lte=4) ==> SELECT ... WHERE id <= 4;
	5.  Entry.objects.filter(headline__startswith='Will') ==> SELECT ... WHERE headline LIKE 'Will%';
	6.  Entry.objects.filter(headline__endswith='Will') ==> SELECT ... WHERE headline LIKE '%Will';

### django 数据库迁移：
1. 新的命令

Django 1.7 为我们带来了三个新命令:
	 
	sncdb: 仅仅是创建数据库里没有的表，它并不对已存在的数据表进行同步修改，也不处理数据模型的删除。
    migrate: 用于执行迁移动作，具有syncdb的功能
    makemigrations: 基于当前的model创建新的迁移策略文件
    sqlmigrate: 显示迁移的SQL语句，具有sqlall的功能
    sqlall yourappname来测试模型新的CREATE TABLE语句
    manage.py dbshell 根据setting配置，开启数据库交互模式

值得注意的是, migration是基于App的, 因此, 我们可以针对某些app不启用migration功能.

2. 如何使用

migrations的使用非常简单: 修改model, 比如增加field, 然后运行

	python manager.py makemigrations

你的model会被扫描, 然后与之前的版本作比较, 在app的migrations目录下生成本次迁移文件.

我们建议查看一下该迁移文件, 确保没有问题. 然后运行:

	python manager.py migrate

migrate命令会进行比较, 并应用该迁移.

##部署测试环境&&预生产：
### 1. 部署流程

**搭建服务器python依赖环境**

	1. 包管理工具、requirements.text第三方包

**测试环境部署流程**
	
	219服务器：
	1. 远程登录测试服219服务器checkout代码，删除.svn文件。备份上次代码。
	2. 将checkout代码scp到线上服务器/opt下
	线上服务器：
	1. 远程登录线上服务器，创建日志目录，创建apache组和用户，赋目录该权限等
	2. 将scp的最新代码cp到预部署目录/var/deploy/p2p/p2p
	3. 检查是否有virtualenv，如果有，激活virtualenv环境
	4. 进入预部署目录，配置代码环境（root/settings.py的环境信息）
	5. 生成静态文件放到静态文件目录/var/static/p2p/
	6. 备份部署目录/var/wsgi/p2p
		* 删除上次备份代码
		* 将目前代码备份p2p-backup
		* 将预部署目录/var/deploy/p2p所有代码复制到部署目录/var/wsgi/p2p
	7. 拷贝apache配置文件/etc/httpd/conf.d/
	8. 重启apache服务
	
**线上部署流程**
	
	
	1. 机器：
		* WEB1：10.10.197.113  		 #对外
		* WEB2：10.10.22.185 		 #对外
		* 线上理财后台：10.10.187.251 	#对内 
	2. 流程：
		* scp预生产运行代码到3台机器
		* WEB1和WEB2设置后台不能访问，后台机器可以访问后台
		* 其他和预生产部署一样

**回滚流程**
	
	线上服务器：
	1. 将刚刚部署的代码备份（p2p_failed+日期）
	2. 将上次成功代码重命名p2p
	3. 重启apache服务
	
### 2. python升级到2.7后的各种问题
	* 前提：升级python2.7.6
	* 安装python2.7.6前先安装openssl openssl-devel，或安装2.7后重新编辑python
	1. 安装easy_install   
		* 用ez_**脚本安装或yum install python-setuptools-devel
		* 报错：AttributeError: 'NoneType' object has no attribute 'decompressobj'
		* 原因：python2.6.6 安装完成的时候已经有zlib的包了，但是python2.7.7 是新安装的，没有引入zlib的包
		* 解决：重新编译安装python2.7.6 
	2. 安装pip：easy_install pip
		* 报错：zipimport.ZipImportError: can't decompress data; zlib not available
		* 原因: 不详
		* 解决：把/usr/local/bin/pip2.7 做软连接到/usr/bin/pip
		* 报错：No module named pkg_resources
		* 解决：http://stackoverflow.com/questions/7446187/no-module-named-pkg-resources	
	3. 安装mysql-python
		* 报错：EnvironmentError: mysql_config not found
		* 原因：装的MySQL是没有mysql_config这个文件
		* 解决：yum install python-devel   yum install mysql-devel
	
	4.   安装lxml报错：ERROR: /bin/sh: xslt-config: command not found
		* 解决：http://blog.csdn.net/azhao_dn/article/details/7501432
	5. python manage.py collectstatic --noinput报错
		* 报错：TypeError: encode() argument 1 must be string without null bytes, not unicode
		* 解决：卸载原有旧本本lxml（3.3.4），用easy_install安装最新版本：easy_install lxml（及依赖包）
		* 原因：不详
	 
	6. 配置apache
	7. Django / Apache / mod_wsgi: No module named importlib
		* 升级Django到1.8
	
		升级django-adminplus (0.3)
		升级django-appconf
		pip install --upgrade
	9. 解决apache启动仍然是旧版本python（2.6）
		* 报错： 
			* No module named importlib
			* undefined symbol: PyUnicodeUCS2_DecodeLatin1
		* 编译安装mod_wsgi-4.4.13版本
		* 编译报错：http://www.it165.net/os/html/201403/7542.html
			* 启动后会报错：Invalid command 'WSGISocketPrefix', perhaps misspelled or 			defined by a module not included in the server configuration
	
			* 解决：httpd.conf中增加：LoadModule wsgi_module modules/mod_wsgi.so
		*[解决的] 安装httpd-devel包，重新编译安装
		
	10 apche重启报错
		* 报错
		Starting httpd: httpd: apr_sockaddr_info_get() failed for websys
		httpd: Could not reliably determine the server's fully qualified domainname, using 127.0.0.1 for ServerName
		* 解决
		httpd.conf 中ServerName 设置：localhost:80
		/etc/hosts 添加127.0.0.1 主机名
		* 引用：http://suo.iteye.com/blog/1096296
	
### 3. 当前需要解决的问题：
	1. 测试环境虚拟环境是python2.6，升级到2.7 #done
	2. 增加预生产和线上数据库				#todo
	3. 测试服python manager.py collectstatic报错，重新安装环境 #done
	4. p2p数据库备份				#done
	5. 优化部署脚本

## jenkins配置
### 集成svn监听

	1. jenkins自带svn插件
		* Repository URL：svn地址：https://192.168.1.222/svn/finance/trunk
		* enter credential：设置svn账号，密码。
		* 配置Poll SCM时间（监听，如果有更新则部署）
### 构建上下游任务
	1. 插件：Parameterized Trigger Plugin
		* 选择任务

### jenkins读取HTML测试报告
	1. 下载jenkins插件：HTML Publisher Plugin
	2. 配置插件：
		- job中“增加构建后操作步骤”，选择该插件
		- HTML directory to archive：选择HTML文件夹位置
		- Index page[s]：选择具体HTML文件
		- Report title：输入显示的title
		- 勾选，Keep past HTML reports：显示所有成功的存档

## 在linux-server下运行webdriver，安装：Xvfb、firefox
### 下载firefox
	* yum install firefox

### 下载Xvfb（虚拟现实框架）
	* 参考：
	1. sudo yum install xorg-x11-server-Xvfb
	2. 添加环境变量：
	   export DISPLAY=:1
	   export BROWSER_PATH=/usr/lib64/firefox/
	   PATH=$PATH:$BROWSER_PATH
	3. Xvfb后台启动：
	   Xvfb :1 -screen 0 800x600x24&
	   Xvfb -ac :1 -screen 1 1280x1024x24&
	4. firefox后台启动：firefox &

### jenkins ssh远程执行脚本报错
	错误： raise WebDriverException("The browser appears to have exited "
		WebDriverException: Message: The browser appears to have exited before we could connect. If you specified a log_file in the FirefoxBinary constructor, check it for details.	
	解决： 在脚本中引入~/.bash_profile等配置文件
	
	
##安装jenkins
#### yum安装
	1. sudo wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat/jenkins.repo  
	2. sudo rpm --import http://pkg.jenkins-ci.org/redhat/jenkins-ci.org.key  
	3. sudo yum install jenkins  
	4. rpm -ql jenkins  
**启动**：service jenkins start/stop/restart
**地址**：http://ip:端口号访问了

## OSCENT安装数据库

	1. yum  install mysql  mysql-devel  php php-mysql mysql-server -y
	2. /etc/init.d/mysqld status  #查看状态
	3. services mysqld start
	4. mysql -u root@localhost   #登录（不是root权限）
	5. CREATE DATABASE IF NOT EXISTS ycf DEFAULT CHARSET utf8 COLLATE utf8_general_ci;		#创建数据库
	6. insert into mysql.user(Host,User,Password) values("localhost","p2puser3",password("Passw0rd"));  #创建用户
	7. GRANT ALL ON *.* TO p2puser3@'%' IDENTIFIED BY 'admin' WITH GRANT OPTION;
	8. flush privileges;			#刷新配置

	问题：没有mysql库，不是root用户权限的问题
		* 如果安装过mysql，删除mysql配置信息
			http://www.linuxidc.com/Linux/2011-10/45061.htm

export JAVA_HOME=/usr/java/jdk1.7.0_79
export JRE_HOME=/usr/java/jdk1.7.0_79/jre
export CLASSPATH=$CLASSPATH:.:$JAVA_HOME/lib:$JAVA_HOME/jre/lib
export CATALINA_BASE=/usr/apache-tomcat-7.0.63/tomcat/
export CATALINA_HOME=/usr/apache-tomcat-7.0.63/tomcat/                                                                                                                       
export JAVA_TOOL_OPTIONS="-Dfile.encoding=UTF-8"
export DISPLAY=:1
export BROWSER_PATH=/usr/lib64/firefox/
export PATH=$PATH:$BROWSER_PATH



select purchase_id,count(purchase_id ) from lc_interest where create_time like '2015-10-30%' GROUP BY purchase_id HAVING count(purchase_id)>=1;


##生成静态文件命令
	
	python manage.py collectstatic

	招商银行		6225882708965808
	农业银行		6228481998735516373
	update profile_userprofile set id_number = 'test_124' where id_number = '220202199002135415';
	update pay_card set no = 'test123' where no = '6228481998735516373';
	
	
### 益财富部署流程
	
**上线前确认：**
	
	1. 数据库是否有改动
	2. 是否增加服务（如crontab，task等）
	3. 是否需要安装新依赖包
	3. MQ是否有变动（如地址,账号密码）
	4. 是否需要初始化数据
	
**部署流程：**

	1. 进入测试服务器192.168.1.219 用户名：root 密码：123456
	2. 激活python虚拟环境：source /home/jinlong/env/bin/activate
	3. 进入/home/jinlong/trunk目录执行部署	
		* 测试环境： fab -f deploy/fabfile_lc.py deploy --set group=staging_205
		  测试环境密码：G9uN89A4
		* 预生产环境： fab -f deploy/fabfile_lc.py deploy --set group=pre_production
		  预生产环境密码：Y0VD2pd7
		  1. 检查预生产的settings文件production = True
		  2. 修改settings文件mysql密码（production）
		  3. 修改完成后重启服务
		* 线上环境：fab -f deploy/fabfile_lc.py deploy --set group=production
		  先输入预生产密码：Y0VD2pd7
		  再分别输入线上密码（10.10.22.185，10.10.187.251（这是后台机器））：
		  10.10.22.185密码：LBmGUvx9 	10.10.187.251密码：HqxcAxg7
		* 如果10.10.187.251/confidential部署后访问不到，需要登录机器重启apache：service httpd restart

	
	检查点：
	1. 线上主功能：登录、注册、充值、申购（定期，活期）、提现等
	2. 线上APP主功能同上
	3. 线上短信功能正常下发
	4. 线上task正常运行（看日志）
	



### 图形验证码不显示，报错解决
	图形验证码显示不出来
	解决：
	1.	删除Pillow包 ：pip uninstall Pillow
	2. 删除	yum remove freetype-devel
	3. 先安装：yum install -y freetype-devel
	4. 在安装Pillow： pip install Pillow
	
	参考：http://blog.sina.com.cn/s/blog_55646c980101545d.html
	
	freetype-devel-2.3.11-15.el6_6.1.x86_64 

### 添加windows字体
	参考文档：http://www.th7.cn/system/lin/201410/72208.shtml


### 益财富性能测试

	1. 调试性能测试脚本
	2. 解决csrf跨站登录问题
		* 关闭CSRF功能 ：
		  http://taotaocoder.blog.163.com/blog/static/200228274201221701756767/
		* 关闭CSRF保护，视图函数添加@csrf_exempt修饰符
	3. non-GUI命令
		* sh /Users/jinlong/Desktop/jmeter/apache-jmeter-2.13/bin/jmeter -n -t  /Users/jinlong/Desktop/jmeter/record_script/首页.jmx -R 10.10.77.215 -l /Users/jinlong/Desktop/jmeter/report/index.jtl	
	4. 分布式性能测试
		http://blog.sina.com.cn/s/blog_6a7f29120100zm8r.html	


	优化：
	* 首页加上所有接口的请求		done
	* 针对数据库性能测试


### Firefox FTP
	https://ftp.mozilla.org/pub/firefox/releases/


### 测试初始化sql
update profile_userprofile set id_number = 'testa1' where id_number  = 371327198809290047;
update pay_card set no = 'testa1' where no = 6222023100084841001;

#### 常用SQL
	* 查询用户申购成功：select * from product_purchase where user_id = (select user_id from profile_userprofile where phone = 14022628975) and status = 2;
	* 更改用户活期申购时间：update product_purchase set transfer_date = '2016-01-24 16:32:54' ,interest_date = '2016-01-25 00:00:00' where user_id = (select user_id from profile_userprofile where phone = 14012907918) and status = 2
	* 更改定期申购时间：update product_purchase set interest_date = '2016-01-22 00:00:00',expire_date='2016-01-25 00:00:00' where id = 6711;	* 查询用户加息券： select * from interest_usercouponmap where user_id =1000000957\G;
	* 删除微信登录数据：delete from wechat_weixinuser where user_id = (select user_id from profile_userprofile where phone like '%6217');
	* select * from product_purchase where user_id = (select user_id from profile_userprofile where phone = 14045343202) and status = 2\G;
### 测试定期宝跑批初始化
	1. 修改product_purchase的transfer_date  #3.0不用修改了，



ssh root@192.168.1.228 "sh /home/jinlong/replace_setting.sh && service httpd restart"

	
## 记WEB挂掉
	原因：后台导出利息数据，重复操作，造成数据库压力过大
	1. 重启后台机器
	2. 卸载前台挂载：umount /var/media
	3. 重新挂载后台nfs系统：mount -t nfs 10.10.187.251:/var/media  /var/media  -o proto=tcp -o nolock
	4. 查看是否挂在上：mount -l


## iptables
	service iptables status/start/stop
	iptables -L #规则列表
	iptables -I INPUT -s 218.88.16.150 -j DROP  #插入限制IP访问规则
	iptables -D INPUT -s 220.177.113.189 -j DROP   #解除
		
## apache配置
**自动跳转到HTTPS**

	https://qiaodahai.com/apache-htaccess-http-jump-to-https.html
**apache显示外网IP**

	LogFormat "%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-Agent}i\" \"%{x-forwarded-for}i\"" combined2
	CustomLog "logs/access.log" combined2
**apache日志不记录图片、js、css等**

	地址：http://www.centoscn.com/apache/2014/0727/3357.html）
	
**apche rewrite重写**

	地址：
	http://kazge.com/archives/744.html
	https://www.zybuluo.com/phper/note/73726
	rewritecond讲解：http://www.skygq.com/2011/02/21/apache%E4%B8%ADrewritecond%E8%A7%84%E5%88%99%E5%8F%82%E6%95%B0%E4%BB%8B%E7%BB%8D%E8%BD%AC/
	

## vim配置：
	1. https://github.com/yangyangwithgnu/use_vim_as_ide/blob/master/.vimrc
	2. http://www.cnblogs.com/ma6174/archive/2011/12/10/2283393.html
	
	
## CentOS设置服务开机启动的方法
	http://blog.phpha.com/backup/archives/1458.html
	开机启动服务：
	1. nfs  #done			linux文件共享系统



##jenkins构建参数
	https://wiki.jenkins-ci.org/display/JENKINS/Building+a+software+project
   
##selenium测试报告
	https://github.com/SahaginOrg/sahagin-java/blob/master/wiki-images/SahaginReport.jpg
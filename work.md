#icaopan
-------------

	1. 邮箱：qiye163.com 账号：jinl@icaopan.com  密码：jinlong1990
	2. 数据库： mysql -uadmin -p123456 -h192.168.1.55
	3. 测试机器：
		* 服务：ssh root@192.168.1.96	123456	
		* 任务：192.168.1.64	账号：Administrator  密码：123456
		* 数据库： ssh root@192.168.1.55	123456
	4. 自动化测试机 ：ssh jinlong@192.168.1.219  su - root 密码：123456
	5. jenkins地址：http://192.168.1.219:8181/jenkins/
	6. MQ地址：http://192.168.1.96:15672/#/queues  账号：admin    密码：admin

## 线上理财120

	1. 理财平台SVN地址：https://192.168.1.222/svn/finance/trunk
	2. 服务器：
		* 10.10.22.185/120.132.60.239		#备用测试环境
		* 10.10.63.171/120.132.60.113 	#测试服test_120server 
		* 10.10.156.119  					#预生产
		* 10.10.192.205  					#线上
		* 用户名：root 密码统一为：www.icaopan.net
	3. 网站地址：
		* 前台：http:// 120.132.60.113     #1601033353/a123456
		* 后台：http:// 120.132.60.113/confidential   #admin/admin

    
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


#工作记录
## SVN常用命令：
	1. svn revert $file    #撤销修改
	2. svn add fabfile_lc.py			#添加文件
	3. svn commit -m 'test' /deploy/fabfile_lc.py  #提交代码
	4. svn up			#更新代码

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



###部署预生产：
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

#### 当前需要解决的问题：
	1. 测试环境虚拟环境是python2.6，升级到2.7 #done
	2. 增加预生产和线上数据库	#todo
	3. 测试服python manager.py collectstatic报错，重新安装环境 #done



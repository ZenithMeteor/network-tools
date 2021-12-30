# network-tools

https://gitee.com/heguangchuan/rainmeter/blob/master/07-mongodb.md

https://chentsungyu.github.io/2019/09/12/Python/%5BPython%5D%20MongoDB%20%E8%B3%87%E6%96%99%E6%93%8D%E4%BD%9C/

安装
上传压缩包到Linux中，解压

cd /usr/local/mongodb
tar -xvf mongodb-linux-x86_64-4.0.10.tgz
新建几个目录，分别用来存储数据和日志、配置

mkdir -p /usr/local/mongodb/data
mkdir -p /usr/local/mongodb/log
mkdir -p /usr/local/mongodb/conf
新建并修改配置文件

vim /usr/local/mongodb/conf/mongod.conf
内容如下：

systemLog:
  #MongoDB发送所有日志输出的目标指定为文件
  destination: file
  path: "/usr/local/mongodb/log/mongod.log"
  logAppend: true
storage:
  #mongod实例存储其数据的目录
  dbPath: "/usr/local/mongodb/data"
  journal:
    #启用或禁用持久性日志以确保数据文件保持有效和可恢复。 
    enabled: true
processManagement: 
   #启用在后台运行mongos或mongod进程的守护进程模式。 
   fork: true
net:
   #服务实例绑定的IP，默认是localhost 
   bindIp: 0.0.0.0
   port: 27017
启动MongoDB服务

/usr/local/mongodb/mongodb-linux-x86_64-4.0.10/bin/mongod -f /usr/local/mongodb/conf/mongod.conf
如果启动后不是 successfully ，则是启动失败了。原因基本上就是配置文件有问题

关闭服务
通过mongo客户端中的shutdownServer命令来关闭服务

//客户端登录服务，注意，这里通过localhost登录，如果需要远程登录，必须先登录认证才行。 
mongo --port 27017 
//#切换到admin库 
use admin 
//关闭服务 
db.shutdownServer()
数据修复
果一旦是因为数据损坏，则需要进行如下操作

删除lock文件
rm -f  /usr/local/mongodb/data/*.lock
修复数据
/usr/local/mongdb/bin/mongod --repair --dbpath=/usr/local/mongodb/data


------------------
java -version
Our output will be similar to:

openjdk version “1.8.0_191”
----------------------------
https://www.elastic.co/guide/cn/elasticsearch/guide/current/running-elasticsearch.html
https://medium.com/@geniojay/graylog-server-%E5%AE%89%E8%A3%9D%E7%AF%87-%E4%B8%80-3144a94090da

編輯相關設定
#vim /etc/elasticsearch/elasticsearch.yml
修改cluster設定
cluster.name: graylog
修改IP和port
network.host: 192.168.1.2 (自己的IP)
http.port: 9200
------------------
https://packages.graylog2.org/packages
https://www.graylog.org/downloads-2
https://docs.graylog.org/en/4.1/pages/installation/manual_setup.html
*** https://www.codenong.com/cs107091470/
https://blog.csdn.net/abu935009066/article/details/119024223
rpm -ivh graylog-4.1-repository_latest.rpm

PdJ670sinGo3XZD68YC0eF50oRs9szcCjKkCckkiifENGpVX8miwuiBbBsOjSjmO

【Flask 教學】實作 GCP 部署 Flask + Nginx + uWSGI
https://www.maxlist.xyz/2020/06/17/flask-nginx-uwsgi-on-gcp/
Flask想上線? 你還需要一些酷東西
https://minglunwu.github.io/notes/2021/flask_plus_wsgi.html#0

app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hour=2)在兩個小時後過期
app.config['PERMANENT_SESSION_LIFETIME'] = 7200  # 失效時間 秒

核心的关键库就是pyautogui，其实如果只是浏览器点赞的话，用selenium就够了，用这个的话不会占用鼠标和键盘事件，还可以继续用电脑干其他事。

setInterval(func, ms) 1000=1s
onload()

####

PROMPT = ['.*>\s*','.*#\s*','Password: ']

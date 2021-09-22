# network-tools

https://gitee.com/heguangchuan/rainmeter/blob/master/07-mongodb.md

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

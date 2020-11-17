## Flask + SQLAlchemy 简易demo(丐中丐版)使用说明

demo写的low，**_不喜勿喷_**

为什么前端不做的好看些？
    ~~我一个后端还是做中间件的，web应用本来就超纲了，你还要老子写花里胡哨的前端？虽然我会，但是我就是不写，爱找谁写找谁写~~
    别问，问就是不会

为什么没有注册？
    ~~登录写好了，注册照着抄作业都不想抄？你还会个啥？你还是个啥？~~
    您好，作业自己做。

为什么没有文件上传功能？
    ~~原来有，但是被我删了，上传到本地有意思吗？阿里云 OSS 不香吗？~~
    可以，但没有必要

为什么不做细节优化？比如全局异常的处理？
    不想写，懒得写

### 1. 环境搭建：
    进入当前项目根目录
        使用 source venv/bin/activated 激活虚拟环境，
        如果失败，回到项目根目录
            使用 pip install -r requirements.txt 安装依赖
            
### 2.修改配置
    将根目录下的 settings.py 文件里 SQLALCHEMY_DATABASES['default']['uri'] 的数据库连接串更改为自己的连接串（你的没动，给你注释了，直接粘过去就行）
    mysql+pymysql://root:root@localhost:3306/test?charset=utf8mb4
    连接串说明：
        mysql+pymysql:使用pymysql连接mysql数据库
        root:用户名
        root:密码
        @localhost：连接本机ip
        3306：mysql端口号
        test:test数据库
        charset=utf8mb4:设置数据库编码方式为 utf8mb4 （真·utf8）
    即：
        mysql+pymysql://mysql用户名:mysql密码@要连接数据库的ip地址:mysql端口号/数据库名(?charset=utf8mb4，选填)
        
### 3.启动项目
    方式 (1):
        进入项目根目录，使用 python app.py 命令进行启动
    方式 (2):
        找到根目录的 app.py文件，点进去后点击入口函数左侧的绿色箭头，进行启动项目
    注意：方式 2 pycharm 可以使用，vscode 未知是否可行，建议第一种
    
### 4.如何访问
    打开浏览器，地址栏输入： localhost:5000 即可

### 5.来都来了，不点个star？？？对得起我吗
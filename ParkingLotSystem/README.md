### 文件描述文档：

#### 文件正常执行条件为

-   数据库文件正常导入、数据库成功连接



#### 文件运行

-   文件运行由__init__.py  开始，也可直接运行Newlogin.py 
-   进入登录页面，未注册用户执行注册按钮，即执行NewSignUp.py
-   可切换至注册页面， 在成功添加注册信息后返回登入页面
-   可以选择以何种身份登入，
    -   以用户身份登录，执行User_page.py
    -   用户界面
        -   包含预约、缴费功能
            -   点击预约，即执行Reserve_page.py
            -   点击缴费，即执行out_pay.py
    -   以操作员身份登入，由于操作员需要由管理员来进行注册，先描述管理员操作
    -   以管理员身份登入，即执行admin_page.py
    -   管理员界面
        -   包含管理操作员，管理收费标准，查看车辆信息。
            -   点击管理操作员，即执行admin_setmanager.py
                -   包含添加管理员界面，即执行admin_addmanager.py
            -   点击更改收费标准，即执行admin_fixcharge.py
            -   点击查看车辆信息，即执行admin_allspot.py
    -   操作员界面，执行manager_page.py
        -   包含入场管理、出场管理
            -   点击入场管理，即执行managein_page.py
            -   点击出场管理，即执行manageout_page.py
    -   对于current_user.txt 文件，即记录登录时所登入的用户相关信息
    -   对于db.py文件，即将对数据库的操作进行封装，

讲至于此，所有界面对应的代码文件已经描述清楚了，如需要对页面进行细致的理解，执行文件即可。





### 写在最后

此项目包含的   需求分析+相关面向对象的设计 图描述+数据库设计+代码的编写   所用的时长不超过6天，可能有许多功能没有实现，但我们第二阶段的时间也这么点，之后也不会对代码内容进行改进。

那么如果代码正好传到你的手里，希望能够对它进行学习，充分利用这篇项目提高自己的同时也希望能够将它更进一步的完善，于此我们共勉。

江西财经大学 NB311寝室 +  软件工程实训第七小组 ：江彪、叶宇成风、黄怡轩，

全体成员敬上

2W notes:模块和类
1.1模块
模块类似于将一种东西对应到另外一种的方式，即“从Y获取X"的概念，主要特性如下：
1，模块是包含函数和变量的Python文件
2，可以导入这个文件
3，然后可以使用.操作符访问模块中的函数和变量。
1.2类
类和模块差不多，理解为俄罗斯套娃吧，一个大的套着小的，然后再小的包。。
1.2.1 对象
为什么要再括号里放object? 待理解。。

继承了object的类是新式类，由于他们都是object的派生类，便于统一操作。py2由于一些类不继承object，就弄了一些内置函数
https://docs.python.org/release/2.2.3/whatsnew/sect-rellinks.html

3w notes: Socket,UDP
1，Python中如何获得IP地址
import socket
socket.gethostname()
socket.gethostbyname(socket.getfqdn())
2,UDP:User Datagram protocol.用户数据报协议。
它与TCP协议一样用于处理数据包，是一种无连接的协议。在OSI模型中，在第四层——传输层，处于IP协议的上一层。UDP有不提供数据包分组、组装和不能对数据包进行排序的缺点，也就是说，当报文发送之后，是无法得知其是否安全完整到达的。
4W notes: Bottle,HTTP协议
1,HTTP超文本传输协议（HTTP，HyperText Transfer Protocol)。
1.1Web服务端与客户端通过HTTP协议传输数据，相当于两个人交流的语言。
1.2 HTTP主要方法：客户端通过以下方法与服务端交互
GET-从服务器上获取一个资源（一般是网页）
POST-向服务器提交数据（可能会创建一个新的资源）
PUT-向服务器提交数据
DELET-删除指定资源
HEAD-只请求网页的头部信息
1.3 HTTP状态码
-200 正常，请求成功
-301 永久移动，一般用于域名重定向
-304 未修改，一般用于缓存
-403禁止访问
-

2，API





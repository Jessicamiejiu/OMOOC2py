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


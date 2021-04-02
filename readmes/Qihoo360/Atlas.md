We have build another interesting project [pika](https://github.com/Qihoo360/pika). Pika is a nosql compatible with redis protocol with huge storage space. You can have a try.

### 1.Brief introduction

Atlas is a MySQL protocol-based database middleware project developed and maintained by infrastructure team of the Web platform Department in QIHU 360 SOFTWARE CO. LIMITED(NYSE:QIHU). It fixed lots of bugs and added lot of new functions on the basis of MySQL-Proxy 0.8.2. Currently the project has been widely applied in QIHU, many MySQL business has connected to the Atlas platform. The number of read and write requests forwarded by Atlas has reached billions.
 
### 2.Major functions

1.Read/Write Splitting.

2.Load balancing and failover handling.

3.IP filtering.

4.Data sharding

5.DBA can online or offline the backend database server smoothly.

6.Remove the failed database server automatically.

7.Config file reload without downtime.

### 3.The improvement of Atlas compared with Mysql-proxy

1.Rewrite all lua code with C, Lua is only used for management interface.

2.Rewrite the network model and the threading model.

3.Implement the connection pool.

4.Optimize the locking mechanism, performance improved immensely.

### 4.Detailed descriptions about Atlas

[1.The installing of Atlas](https://github.com/Qihoo360/Atlas/wiki/Installing-Atlas)

[2.The Architecture Of Atlas](https://github.com/Qihoo360/Atlas/wiki/The-Architecture-Of-Atlas)

[3.The FAQs about the main features of Atlas](https://github.com/Qihoo360/Atlas/wiki/The-FAQs-about-the-main-features-of-Atlas)

[4.The FAQs Of Running Atlas](https://github.com/Qihoo360/Atlas/wiki/The-FAQs-Of-Running-Atlas)

### 5.Requirement and feedback

If You have new functional requirements about Atlas in the production environment, or find a bug in the process of using Atlas. Welcome to send a mail to g-atlas[at]360.cn, we will reply as soon as possible. Also you can contact us in [Google group](https://groups.google.com/forum/#!forum/atlas-proxy). Enthusiastic user has established a QQ group:326544838, the developers of Atlas have also been in the QQ group.

### 6.The origin of the name

In Greek mythology, Atlas was the primordial Titan who held up the celestial spheres. He is also the titan of astronomy and navigation.

### 7.Other language version

[简体中文](README_ZH.md)
 

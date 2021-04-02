# 统计学习方法（第一版）习题解答
&emsp;&emsp;李航老师的《统计学习方法》是机器学习领域的经典入门教材之一。  
&emsp;&emsp;本书全面系统地介绍了统计学习的主要方法，特别是监督学习方法，包括感知机、k近邻法、朴素贝叶斯法、决策树、逻辑斯谛回归与最大熵模型、支持向量机、提升方法、EM算法、隐马尔可夫模型和条件随机场等。除第1章概论和最后一章总结外，每章介绍一种方法。叙述从具体问题或实例入手，由浅入深，阐明思路，给出必要的数学推导，便于读者掌握统计学习方法的实质，学会运用。为满足读者进一步学习的需要，书中还介绍了一些相关研究，给出了少量习题，列出了主要参考文献。  
&emsp;&emsp;**申明：** 习题解答主要参考了文献1中的内容。

## 使用说明
&emsp;&emsp;统计学习方法习题解答，主要完成了该书（第一版）的全部习题，并提供代码和运行之后的截图，里面的内容是以统计学习方法的内容为前置知识，该习题解答的最佳使用方法是以李航老师的《统计学习方法》为主线，并尝试完成课后习题，如果遇到不会的，再来查阅习题解答。  
&emsp;&emsp;如果觉得解答不详细，可以[点击这里](https://github.com/datawhalechina/statistical-learning-method-solutions-manual/issues)提交你希望补充推导或者习题编号，我们看到后会尽快进行补充。

### 在线阅读地址
在线阅读地址：https://datawhalechina.github.io/statistical-learning-method-solutions-manual

## 目录
- 第1章 [统计学习方法概论](https://datawhalechina.github.io/statistical-learning-method-solutions-manual/#/chapter1/chapter1)
- 第2章 [感知机](https://datawhalechina.github.io/statistical-learning-method-solutions-manual/#/chapter2/chapter2)
- 第3章 [k近邻法](https://datawhalechina.github.io/statistical-learning-method-solutions-manual/#/chapter3/chapter3)
- 第4章 [朴素贝叶斯法](https://datawhalechina.github.io/statistical-learning-method-solutions-manual/#/chapter4/chapter4)
- 第5章 [决策树](https://datawhalechina.github.io/statistical-learning-method-solutions-manual/#/chapter5/chapter5)
- 第6章 [Ligistic回归与最大熵模型](https://datawhalechina.github.io/statistical-learning-method-solutions-manual/#/chapter6/chapter6)
- 第7章 [支持向量机](https://datawhalechina.github.io/statistical-learning-method-solutions-manual/#/chapter7/chapter7)
- 第8章 [提升方法](https://datawhalechina.github.io/statistical-learning-method-solutions-manual/#/chapter8/chapter8)
- 第9章 [EM算法及其推广](https://datawhalechina.github.io/statistical-learning-method-solutions-manual/#/chapter9/chapter9)
- 第10章 [隐马尔可夫模型](https://datawhalechina.github.io/statistical-learning-method-solutions-manual/#/chapter10/chapter10)
- 第11章 [条件随机场](https://datawhalechina.github.io/statistical-learning-method-solutions-manual/#/chapter11/chapter11)

## 选用的《统计学习方法》版本
<img src="https://github.com/datawhalechina/statistical-learning-method-solutions-manual/blob/master/res/statistical-learning-method-book.jpg?raw=true" width="336" height= "500">


> 书名：统计学习方法<br/>
> 作者：李航<br/>
> 出版社：清华大学出版社<br/>
> 版次：2012年3月第1版<br/>
> 勘误表：http://blog.sina.com.cn/s/blog_7ad48fee01017dpi.html<br/>

## 参考文献
1. [李航《统计学习方法》习题笔记](https://sine-x.com/statistical-learning-method)
2. [李航《统计学习方法笔记》中的代码、notebook、参考文献、Errata](https://github.com/SmirkCao/Lihang)  
3. [CART剪枝详解](https://blog.csdn.net/wjc1182511338/article/details/76793164)
4. [CART剪枝算法详解](http://www.pianshen.com/article/1752163397/)

## Notebook运行环境配置
1. 安装相关的依赖包
    ```shell
    pip install -r requirements.txt
    ```
2. 安装graphviz（用于决策树展示）  
    可参考博客：https://blog.csdn.net/HNUCSEE_LJK/article/details/86772806

## 协作规范
1. 由于习题解答中需要有程序和执行结果，采用jupyter notebook的格式进行编写（文件路径：notebook/notes），然后将其导出成markdown格式，再覆盖到docs对应的章节下。
2. 目前已完成全部习题解答，需要进行全部解答校对。
3. 可按照Notebook运行环境配置，配置相关的运行环境。
4. 校对过程中，在数学概念补充上，尽量使用初学者（有高数基础）能理解的数学概念，如果涉及到推导和证明，可附上参考链接。

### 主要贡献者（按首字母排名）
 [@胡锐锋-天国之影-Relph](https://github.com/Relph1119)

## 关注我们
<div align=center><img src="https://raw.githubusercontent.com/datawhalechina/pumpkin-book/master/res/qrcode.jpeg" width = "250" height = "270" alt="Datawhale，一个专注于AI领域的学习圈子。初衷是for the learner，和学习者一起成长。目前加入学习社群的人数已经数千人，组织了机器学习，深度学习，数据分析，数据挖掘，爬虫，编程，统计学，Mysql，数据竞赛等多个领域的内容学习，微信搜索公众号Datawhale可以加入我们。"></div>

## LICENSE
[GNU General Public License v3.0](https://github.com/datawhalechina/statistical-learning-method-solutions-manual/blob/master/LICENSE)
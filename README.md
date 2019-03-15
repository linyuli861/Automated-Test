# Automated-Test
## Web自动化测试框架

### 测试框架：
python3+Selenium+unittest+HTMLTestRunner+pageObject  Web自动化测试框架

（selenium+unittest搭建的WebUI自动化测试框架）

    环境部署： python3、selenium3 
    开发工具： Pycharm
    集成工具： Jenkins
    测试代码托管平台：GitHub
    通过主从服务器执行测试
    
### 测试代码结构:

![Image text](https://raw.githubusercontent.com/linyuli861/Automated-Test/master/z-README-image/structure.png)

* common文件夹存放公有元素，如url，测试报告发送邮件地址，使用信息等；

* file文件夹存放测试过程中需要使用的文件，如图片，txt，zip文件等

* page文件夹用于存放测试过程中需要使用的页面元素

* report文件夹用于存放测试生成的测试报告

* testcase文件夹中存放测试用例

* HTMLTestRunner.py是将测试结果生成为html版的测试报告的文件

* run.py 执行run.py文件可以执行全部测试用例

### 生成的测试报告例子如下所示

![Image text](https://raw.githubusercontent.com/linyuli861/Automated-Test/master/z-README-image/report.png)

### 发送邮件如下所示：

调用common中的sendEmail，向指定邮箱发送最新的测试报告文件

![Image text](https://raw.githubusercontent.com/linyuli861/Automated-Test/master/z-README-image/email.jpg)

### PageObject设计模式

由于Web页面自动化测试的过程中会存在许多重复的元素，且很多Web页面测试的元素值不稳定，经常变更，
为了使得Web页面自动化测试的代码更具有健壮性，因此使用PageObject设计模式，
将web自动化测试的测试用例和测试用例中需要使用到的元素解耦。

*解耦后的代码方便修改，增强了自动化测试代码的复用性。*

 
 








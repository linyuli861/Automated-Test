# Automated-Test
页面自动化测试框架

测试框架：
python3+Selenium+unittest自动化UI测试框架

（selenium+unittest搭建的WebUI自动化测试框架）

    环境部署： python3、selenium3 
    开发工具： Pycharm
    集成工具： Jenkins
    测试代码托管平台：GitHub
    通过主从服务器执行测试
    
测试代码结构:

![](https://raw.githubusercontent.com/linyuli861/Automated-Test/master/z-README-image/structure.png)

> common文件夹存放公有元素，如url，测试报告发送邮件地址，使用信息等；

> file文件夹存放测试过程中需要使用的文件，如图片，txt，zip文件等

> page文件夹用于存放测试过程中需要使用的页面元素

> report文件夹用于存放测试生成的测试报告

> testcase文件夹中存放测试用例

> HTMLTestRunner.py是将测试结果生成为html版的测试报告的文件

> run.py 执行run.py文件可以执行全部测试用例

生成的测试报告例子如下所示

![](https://raw.githubusercontent.com/linyuli861/Automated-Test/master/z-README-image/report.png)



 
 








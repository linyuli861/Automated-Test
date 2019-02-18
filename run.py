# coding=utf-8
import HTMLTestRunner
import unittest
import os,time


listaa = "./report/"


def createsuite():
    testunit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(listaa,pattern='test_*.py',top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit


now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
filename="./report/"+now+"_result.html"
fp=open(filename, 'wb')

runner=HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'搜索功能测试报告',
    description=u'用例执行情况：')

runner.run(createsuite())

fp.close()
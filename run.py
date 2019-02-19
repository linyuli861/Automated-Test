import unittest
import HTMLTestRunner
import time


def get_test_cases(dirpath):
    test_cases = unittest.TestSuite()
    suites = unittest.defaultTestLoader.discover(dirpath, 'test_*.py', top_level_dir=dirpath)
    for suite in suites:
        test_cases.addTests(suite)
    return test_cases


if __name__ == '__main__':
    cases = get_test_cases('../testcase')
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = '../report/' + now + 'report.html'  # 设置报告文件名
    f = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title=u'TEST', description=u'详细测试结果如下:')
    runner.run(cases)

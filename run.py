import unittest
import HTMLTestRunner
import time
from common.sendEmail import SendEmail


def get_test_cases(dirpath):
    # dirpath是存放测试用例的文件路径
    test_cases = unittest.TestSuite()
    # 测试用例均使用"test_"开头命名
    suites = unittest.defaultTestLoader.discover(dirpath, 'test_*.py', top_level_dir=dirpath)
    for suite in suites:
        test_cases.addTests(suite)
    return test_cases


if __name__ == '__main__':
    cases = get_test_cases('../testcase')
    now = time.strftime("%Y-%m-%d %H_%M_%S")  # 报告生成时间
    test_reports_address = '../report'      # 测试报告存放位置
    filename = '../report/' + now + 'report.html'  # 设置报告文件名
    f = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title=u'Web自动化测试', description=u'详细测试结果如下:')
    runner.run(cases)
    f.close()
    # time.sleep(6)
    # # 查找最新生成的测试报告地址
    # new_report_addr = SendEmail().acquire_report_address(test_reports_address)
    # # 自动发送邮件
    # SendEmail().send_email(new_report_addr)

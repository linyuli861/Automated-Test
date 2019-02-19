# coding=utf-8
from HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
import time
import unittest


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.url = "https://www.baidu.com/"
        self.driver.get(self.url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    def test_search(self):
        self.driver.find_element_by_id("kw").send_keys("hello")
        self.driver.find_element_by_id("su").click()
        time.sleep(2)
        self.assertIn("hello", self.driver.page_source)

    def test_search1(self):
        self.driver.find_element_by_id("kw").send_keys("hello")
        self.driver.find_element_by_id("su").click()
        time.sleep(2)
        self.assertIn("hello1232323", self.driver.page_source)

    def test_search2(self):
        self.driver.find_element_by_id("k").send_keys("hello")
        self.driver.find_element_by_id("su").click()
        time.sleep(2)
        self.assertIn("hello1232323", self.driver.page_source)


if __name__ == '__main__':
    # now = time.strftime("%Y-%m-%d-%H-%M-%S")
    # suite = unittest.TestSuite()
    # suite.addTest(TestLogin("test_search"))
    # suite.addTest(TestLogin("test_search1"))
    # suite.addTest(TestLogin("test_search2"))
    # path = "../report/" + now + "result.html"
    # fp = open(path, 'wb')
    #
    # runner = HTMLTestRunner(stream=fp, title=u"Web页面自动化测试", description=u"测试查询功能")
    # runner.run(suite)
    # fp.close
    unittest.main()


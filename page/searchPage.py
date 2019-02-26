from common.pageObject import PageObject, PageElement
from common.url import *


class SearchPage(PageObject):

    # 测试网址
    base_url = Url.base_url
    url = base_url+'/'

    # 查询元素
    search = PageElement(id="kw")
    wrong_search = PageElement(id="k")
    search_btn = PageElement(id='su')

    # 查询内容
    search_content = "hello"

    # 断言
    search_content_assert = "hello"
    search_content_assert_wrong = "hello12232423423"

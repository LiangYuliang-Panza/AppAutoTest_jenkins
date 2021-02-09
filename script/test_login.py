import os

import pytest


class TestLogin(object):

    def test_001(self):
        assert 0

    def test_002(self):
        assert 1

    def test_003(self):
        assert 1


if __name__ == '__main__':
    pytest.main(['--alluredir', 'report/result', 'test_login.py'])
    # 将json转换成HTML文件
    split = 'allure ' + 'generate ' + './report/result ' + '-o ' + './report/html ' + '--clean'
    os.system(split)  # system函数可以将字符串转化成命令在服务器上运行

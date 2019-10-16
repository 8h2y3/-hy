# 导包

import unittest
from tools.HTMLTestRunner import HTMLTestRunner
from youran.hh import Testadd

# 定义测试套件
suite = unittest.TestSuite()
suite.addTest(Testadd("test01"))
# 定义测试套件的路径
file_path = "../report/report.html"

with open(file_path, "wb") as f:
    runner=HTMLTestRunner(f,title="数据保护伞", description="描述")
    runner.run(suite)

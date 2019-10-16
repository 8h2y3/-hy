import unittest
import time
class Testadd(unittest.TestCase):
    # 初始化，就是前置处理
    # def setUp(self):
    #     print("杨满满是猪")
    # # 后置处理，就是值爱所有的测试用例执行完之后，执行的
    # def tearDown(self):
    #     print("猪满满")
    # def test01(self):
    #     print("猪猪")
    # def test02(self):
    #     print("满满等于猪猪")
    @classmethod
    def setUpClass(cls):
        print("满满")
    @classmethod
    def tearDownClass(cls):
        print("yueyue")
    def test01(self):
        print("12345")
        self.assertEqual(self, 1, 1, "true")
    def test02(self):
        print("fsjfsnsvn")
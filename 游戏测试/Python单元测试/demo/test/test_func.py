# coding:utf-8
import unittest
import unittest.mock as mock
from module.func import *

class TestFunc(unittest.TestCase):
    def setUp(self):
        '''
        前置执行
        :return:
        '''
        print('执行setUp')

    def tearDown(self):
        '''
        后置执行
        :return:
        '''
        print('执行tearDown')

    # 测试一元一次方程的求解
    @unittest.expectedFailure   # 预测错误
    def test_one_equation(self):
        print('执行test1')
        # 断言该方程求解应该为-1.8
        self.assertEqual(one_equation(5 , 9) , -1.8)
        # 断言该方程求解应该为-2.5
        self.assertTrue(one_equation(4 , 10) == -2.5 , .00001)
        # 断言该方程求解应该为27/4
        self.assertTrue(one_equation(4 , -27) == 27 / 4)
        # 断言当a == 0时的情况，断言引发ValueError
        with self.assertRaises(ValueError):
            one_equation(0 , 9)

    # 测试一元二次方程的求解
    def test_two_equation(self):
        print('执行test2')
        r1, r2 = two_equation(1 , -3 , 2)
        self.assertCountEqual((r1, r2), (1.0, 2.0), '求解出错')
        r1, r2 = two_equation(2 , -7 , 6)
        self.assertCountEqual((r1, r2), (1.5, 2.0), '求解出错')
        # 断言只有一个解的情形
        r = two_equation(1 , -4 , 4)
        self.assertEqual(r, 2.0, '求解出错')
        # 断言当a == 0时的情况，断言引发ValueError
        with self.assertRaises(ValueError):
            two_equation(0, 9, 3)
        # 断言引发ValueError
        with self.assertRaises(ValueError):
            two_equation(4, 2, 3)

    #测试存在内在依赖的用例
    @mock.patch("module.func.multiply")  # 使用全地址，否则报错
    def test_add_and_multiply(self, mock_multiply):
        x = 3
        y = 5
        mock_multiply.return_value = 15   # 设置mock对象返回值
        addition, multiple = add_and_multiply(x, y)

        mock_multiply.assert_called_once_with(3, 5) # 判断传参是否正常
        self.assertEqual(8, addition)
        self.assertEqual(15, multiple)

import unittest
from login_demo import Login
class TestLogin(unittest.TestCase):
    def test_assertEqual(self):
        self.assertEqual("登录成功",Login("小明","123456").ReturnLoginResult1())

    def test_assertIn(self):
        self.assertIn("登录成功",Login("小明","123456").ReturnLoginResult2())


if __name__=='__main__':
    unittest.main(verbosity=2)
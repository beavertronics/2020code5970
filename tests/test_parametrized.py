# vim: set sw=4 noet ts=4 fileencoding=utf-8:
import unittest
from parametrized import ParametrizedTestCase

class Test_Test(ParametrizedTestCase):
	def test_something(self):
		print('param = ' + str(self.param))
		self.assertEqual(1, 1)

if __name__ == '__main__':
	suite = unittest.TestSuite()
	suite.addTest(ParametrizedTestCase.parametrize(Test_Test, param=42))
	suite.addTest(ParametrizedTestCase.parametrize(Test_Test, param=13))
	unittest.TextTestRunner(verbosity=2).run(suite)
	

# vim: set sw=4 noet ts=4 fileencoding=utf-8:

# Source: https://eli.thegreenplace.net/2011/08/02/python-unit-testing-parametrized-test-cases/
# This class can be inherited INSTEAD of unittest.TestCase when making a
# file for TestCase. Then create a test suite with import unittest
# unittest.TestSuite().addTest(ParametrizedTestCase.parametrize(
#	Your_Test_Class, param) and it will run all tests in Your_Test_Class and
# make the param you pass in available to the methods in Your_Test_Class.

import unittest

class ParametrizedTestCase(unittest.TestCase):
	""" TestCase classes that want to be parametrized should
		inherit from this class.
	"""
	def __init__(self, methodName='runTest', param=None):
		super(ParametrizedTestCase, self).__init__(methodName)
		self.param = param

	@staticmethod
	def parametrize(testcase_klass, param=None):
		""" Create a suite containing all tests taken from the given
			subclass, passing them the parameter 'param'.
		"""
		testloader = unittest.TestLoader()
		testnames = testloader.getTestCaseNames(testcase_klass)
		suite = unittest.TestSuite()
		for name in testnames:
			suite.addTest(testcase_klass(name, param=param))
		return suite


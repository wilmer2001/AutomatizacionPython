from unittest import TestLoader, TestSuite, runner
from pyunitreport import HTMLTestRunner
from automatizacion import AssertionsTest
from searchtest import SearchTest
from Register_new_user import RegisterNewUser

automatizacion_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)
Register_new_user_test = TestLoader().loadTestsFromTestCase(RegisterNewUser) 


smoke_test = TestSuite([automatizacion_test, search_test, Register_new_user_test])

Kwargs ={
    'output': 'smoke-report'
}

runner = HTMLTestRunner(**Kwargs)
runner.run(smoke_test)
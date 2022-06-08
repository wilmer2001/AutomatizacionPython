from unittest import TestLoader, TestSuite, runner
from pyunitreport import HTMLTestRunner
from automatizacion import AssertionsTest
from searchtest import SearchTest

automatizacion_test = TestLoader().loadTestsFromTestCase(AssertionsTest)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)

smoke_test = TestSuite([automatizacion_test, search_test])

Kwargs ={
    'output': 'smoke-report'
}

runner = HTMLTestRunner(**Kwargs)
runner.run(smoke_test)
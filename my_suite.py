import unittest

import HtmlTestRunner

from Proiect_final_TA.TestBookExpress import TestBookExpress
from Proiect_final_TA.TestBookExpressSearch import TestBookExpressSearch
from Proiect_final_TA.Test_JavaScript_Alerts import Test_JavaScript_Alerts


class Proiect_final_TA(unittest.TestCase):
    def test_suite(self):
        teste_de_rulat = unittest.TestSuite()
        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(TestBookExpress),
            unittest.defaultTestLoader.loadTestsFromTestCase(TestBookExpressSearch),
            unittest.defaultTestLoader.loadTestsFromTestCase(Test_JavaScript_Alerts)
        ])
        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Unit Tests Results',
            report_name='unittests_report'
        )
        runner.run(teste_de_rulat)

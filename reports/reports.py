import unittest
import xmlrunner  # For generating XML reports

from api.test_cases.test_suite.test_suites import create_test_suite


def run_tests():
    suite = create_test_suite()

    # Adding this for Textual report
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # adding this fo XML report
    with open('test_report.xml', 'wb') as output_file:
        xml_runner = xmlrunner.XMLTestRunner(output=output_file)
        xml_runner.run(suite)

    return result

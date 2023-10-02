import unittest
import xmlrunner  # For generating XML reports (optional)

from tests.test_suite.test_suites import create_test_suite


def run_tests():
    suite = create_test_suite()

    # Textual report
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # XML report (optional)
    with open('test_report.xml', 'wb') as output_file:
        xml_runner = xmlrunner.XMLTestRunner(output=output_file)
        xml_runner.run(suite)

    return result

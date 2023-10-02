import unittest
from tests.test_get_Aud_by_id import TestAPIClient  # Import your test class

def create_test_suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite((TestAPIClient)))
    return suite

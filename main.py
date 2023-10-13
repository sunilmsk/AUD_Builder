from reports.reports import run_tests

if __name__ == "__main__":
    test_result = run_tests()

    # Check the test result and exit with an appropriate code
    if test_result.wasSuccessful():
        exit(0)  # All test_cases passed
    else:
        exit(1)  # Some test_cases failed
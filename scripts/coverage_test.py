import sys
from unittest import main

from coverage import Coverage

cov = Coverage(source=['backend'])
cov.start()

test = main(
    module=None, exit=False,
    argv=['unittest', 'discover', '-s', 'tests']
)
# test code
if not test.result.wasSuccessful():
    sys.exit(1)

cov.stop()
# test coverage
if cov.report() < 100.0:
    sys.exit(2)

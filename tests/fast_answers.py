# Runs tests for problem solutions that have an answer defined.  The idea is
# ultimately some of these might not have a runtime that is reasonable for
# tests.  Those will be marked to not be run.  Currently there are not test
# that are slow enough to not be run every time.
import sys
import os
sys.path.append(os.path.join('..', 'src'))

import re
import unittest

class TestEulerSolutions(unittest.TestCase):
    # We use this as a template for our tests.
    def _test_solutions(self, test_spec):
        os.chdir(test_spec[0])
        answer = os.popen('python ' + test_spec[1]).read()
        self.assertTrue(answer.strip() == test_spec[2])

def problem_runner_factory(problem_spec):
    def problem_runner(x):
        TestEulerSolutions._test_solutions(x, problem_spec)
    return problem_runner

# We want to generate our test functions dynamically.  unittest walks this
# before setUp is called so we need to build these on module load.
for filesystem_entry in os.listdir(os.path.join('..', 'src')):
    filesystem_path = os.path.join(os.getcwd(), '..', 'src', filesystem_entry)
    if os.path.isdir(filesystem_path):
        dir_entries = os.listdir(filesystem_path)
        if 'problem.txt' in dir_entries:
            problem_number = filesystem_entry
            problem_path = os.path.join(filesystem_path, 'problem.txt')
            problem = open(problem_path).read()
            answer = re.search('Answer: (.*)', problem)
            if not answer:
                print("missing answer in {0}".format(problem_path))
                continue
            problem_spec = (filesystem_path,
                    'problem_{0}.py'.format(int(problem_number)),
                    answer.groups(1)[0])
            setattr(TestEulerSolutions, 'test_{0}'.format(problem_number),
                    problem_runner_factory(problem_spec))

if __name__ == '__main__':
    unittest.main()

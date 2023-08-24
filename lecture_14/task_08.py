import doctest
import unittest

import prime


def load_test(loader, testes, ignore):
    testes.addTests(doctest.DocTestSuite(prime))
    testes.addTests(doctest.DocFileSuite('prime.md'))
    return testes


if __name__ == '__main__':
    unittest.main(verbosity=2)

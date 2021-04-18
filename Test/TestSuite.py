#!/usr/bin/env python3
import unittest
from Test_Archivo_crontab import TestArchivo_crontab
from Test_Sincronizacion import TestSincronizacion
from Test_LibrosJSON import TestLibrosJSON


def my_suite():
    suite = unittest.TestSuite()
    result = unittest.TestResult()
    suite.addTest(unittest.makeSuite(TestArchivo_crontab))
    suite.addTest(unittest.makeSuite(TestLibrosJSON))
    suite.addTest(unittest.makeSuite(TestSincronizacion))
    runner = unittest.TextTestRunner()
    print(runner.run(suite))


if __name__ == '__main__':
    my_suite()

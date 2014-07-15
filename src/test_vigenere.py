#!/usr/bin/env python

import sys
import unittest
import vigenere

class TestDES(unittest.TestCase):
    def test_clean(self):
        string1 = 'test string'
        key1    = 'your king'
        string2 = 'Hello World!'
        key2    = 'your queen'
        string3 = 'THE QUICK BROWN FOX'
        key3    = 'FINE2134'
        string4 = 'L3Pt 0V3R tH3 L4Zy D0G'
        key4    = 'Breathe Sl0wly'
        string5 = '23140951230991320459-'
        key5    = 'NULL4'
        assert(vigenere.clean(string1 , key1) == ('teststring'       , [ord(x) for x in 'yourking']))
        assert(vigenere.clean(string2 , key2) == ('helloworld'       , [ord(x) for x in 'yourqueen']))
        assert(vigenere.clean(string3 , key3) == ('thequickbrownfox' , [ord(x) for x in 'fine']))
        assert(vigenere.clean(string4 , key4) == ('lptvrthlzydg'     , [ord(x) for x in 'breatheslwly']))
        assert(vigenere.clean(string5 , key5) == (''                 , [ord(x) for x in 'null']))

    def test_shift_byte(self):
        ib1 = 'a'
        ib2 = 'g'
        ib3 = 'r'
        ib4 = 'z'
        assert(vigenere.shift_byte(ib1, ord('e'), False) == 'e')
        assert(vigenere.shift_byte(ib2, ord('k'), True) == 'w')
        assert(vigenere.shift_byte(ib3, ord('i'), False) == 'z')
        assert(vigenere.shift_byte(ib4, ord('z'), True) == 'a')

if __name__ == "__main__":
    unittest.main()

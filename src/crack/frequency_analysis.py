#!/usr/bin/env python

import sys

def main():
    analyzer = Frequency('sherlockholmes.txt')
    length, adict, fdict = analyzer.analyze(True)
    important_list = []
    for item in fdict:
        important_list.append((item, fdict[item]))
    for item in sorted(important_list, key=lambda tup: tup[1]):
        print item

class Frequency:

    def __init__(self, bookPath=None, charlist=None):
        '''
        Instantiate our dicts
        '''
        self.book     = bookPath
        self.charlist = charlist
        self.freq_dict = {'a':0.0, 'b':0.0, 'c':0.0,
                         'd':0.0, 'e':0.0, 'f':0.0,
                         'g':0.0, 'h':0.0, 'i':0.0,
                         'j':0.0, 'k':0.0, 'l':0.0,
                         'm':0.0, 'n':0.0, 'o':0.0,
                         'p':0.0, 'q':0.0, 'r':0.0,
                         's':0.0, 't':0.0, 'u':0.0,
                         'v':0.0, 'w':0.0, 'x':0.0,
                         'y':0.0, 'z':0.0}

        self.alpha_dict = {'a':0, 'b':0, 'c':0,
                          'd':0, 'e':0, 'f':0,
                          'g':0, 'h':0, 'i':0,
                          'j':0, 'k':0, 'l':0,
                          'm':0, 'n':0, 'o':0,
                          'p':0, 'q':0, 'r':0,
                          's':0, 't':0, 'u':0,
                          'v':0, 'w':0, 'x':0,
                          'y':0, 'z':0,}

        self.alpha_list = ['a', 'b', 'c', 'd',
                           'e', 'f', 'g', 'h',
                           'i', 'j', 'k', 'l',
                           'm', 'n', 'o', 'p',
                           'q', 'r', 's', 't',
                           'u', 'v', 'w', 'x',
                           'y', 'z']

    def analyze(self, throttle=False):
        letter_list = [chr(x) for x in range(0, 128)]
        if throttle:
            letter_list = [chr(x) for x in range(97, 123)]
        if self.charlist:
            text = ''.join(self.charlist)
        elif self.book:
            text = open(self.book, 'r').read()
        else:
            return None

        length = 0
        for byte in text:
            letter = byte
            if throttle:
                letter = byte.lower()
            if letter in letter_list:
                length += 1
                try:
                    self.alpha_dict[letter] += 1.0
                except KeyError:
                    self.alpha_dict[letter] = 1.0
                self.freq_dict[letter]   = (self.alpha_dict[letter] / length) * 100
        return length, self.alpha_dict, self.freq_dict

if __name__ == "__main__":
    sys.exit(main())

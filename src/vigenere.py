#!/usr/bin/env python

'''
    VIGENERE SQUARE:
        a b c d e f g h i j k l m n o p q r s t u v w x y z
        b c d e f g h i j k l m n o p q r s t u v w x y z a
        c d e f g h i j k l m n o p q r s t u v w x y z a b
        d e f g h i j k l m n o p q r s t u v w x y z a b c
        e f g h i j k l m n o p q r s t u v w x y z a b c d
        f g h i j k l m n o p q r s t u v w x y z a b c d e
        g h i j k l m n o p q r s t u v w x y z a b c d e f
        h i j k l m n o p q r s t u v w x y z a b c d e f g
        i j k l m n o p q r s t u v w x y z a b c d e f g h
        j k l m n o p q r s t u v w x y z a b c d e f g h i
        k l m n o p q r s t u v w x y z a b c d e f g h i j
        l m n o p q r s t u v w x y z a b c d e f g h i j k
        m n o p q r s t u v w x y z a b c d e f g h i j k l
        n o p q r s t u v w x y z a b c d e f g h i j k l m
        o p q r s t u v w x y z a b c d e f g h i j k l m n
        p q r s t u v w x y z a b c d e f g h i j k l m n o
        q r s t u v w x y z a b c d e f g h i j k l m n o p
        r s t u v w x y z a b c d e f g h i j k l m n o p q
        s t u v w x y z a b c d e f g h i j k l m n o p q r
        t u v w x y z a b c d e f g h i j k l m n o p q r s
        u v w x y z a b c d e f g h i j k l m n o p q r s t
        v w x y z a b c d e f g h i j k l m n o p q r s t u
        w x y z a b c d e f g h i j k l m n o p q r s t u v
        y z a b c d e f g h i j k l m n o p q r s t u v w x
        z a b c d e f g h i j k l m n o p q r s t u v w x y
'''

import sys
import argparse

def main():
    args  = get_args()
    final = vigenere_shift(args)
    print final

def clean(message, key):
    '''
    Clean our message and key so they're pretty.
    :param dictionary: args

    See rot13 for description
    '''
    dirty_text = list(message)  # [97-122]
    dirty_key  = list(key)
    def num_det(letter):
        if ord(letter.lower()) >= 97 and ord(letter.lower()) <= 122:
            return letter.lower()
        else:
            return ''
    clean_text = ''.join([num_det(char) for char in dirty_text])
    clean_key  = [ord(character) for character in
                    list(''.join([num_det(char) for char in dirty_key]))]
    return clean_text, clean_key

def vigenere_shift(args):
    '''
    Shift our message and return
    :param dictionary: args
    '''
    clean_text, clean_key = clean(args.message, args.key)
    letter                = 0
    ciphertext            = ''
    for byte in clean_text:
        chr_enc = shift_byte(byte, clean_key[letter], args.decrypt)
        ciphertext += chr_enc
        letter = (letter + 1) % len(clean_key)  # Cycle keyword
    return ciphertext

def shift_byte(byte, shift, decrypt):
    '''
    Shift our byte using the correct alphabet in the correct direction
    :param string: byte
    :param int: shift
    :param decrypt: bool


    See rot13 for description
    '''
    nRangeByte = (ord(byte) + 7) % 26
    nRangeShift = (shift + 7) % 26
    if decrypt:
        encoded_byte = chr(((nRangeByte - nRangeShift) % 26) + 97)
    else:
        encoded_byte = chr(((nRangeByte + nRangeShift) % 26) + 97)
    return encoded_byte

def get_args():
    default_message = 'The Quick Brown fox lept Over THE lazy dog'
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--encrypt',
                        action='store_true',
                        help='Encrypt')
    parser.add_argument('-d', '--decrypt',
                        action='store_true',
                        help='Decrypt')
    parser.add_argument('-k', '--key',
                        type=str, default='Ki5Ng',
                        help='The keyword for encryption or decryption')
    parser.add_argument('-f', '--filename',
                        type=str, default=None,
                        help='This is the name of the read/write file')
    parser.add_argument('-m', '--message',
                        type=str,
                        default=default_message,
                        help='Message to encode')
    args = parser.parse_args()

    if args.encrypt is False and args.decrypt is False:
        args.encrypt = True
    if args.decrypt and args.message is default_message:
        args.message = 'dprweqpqlzbcxnbdvmczydrxdprrkhljyo'
    if args.filename:
        args.message = open(args.filename, 'r').read()
    return args

if __name__ == "__main__":
    sys.exit(main())

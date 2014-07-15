# !/usr/bin/env python

import sys
import frequency_analysis

key_length = 3                                                          # Temp value. This could be rewritten for brute
cipherpath = './ciphertext.txt'

def main():
    ciphertext = open(cipherpath, 'r').read()[:-1]                      # Purge last char '\n'
    alpha_sets = []                                                     # List of modular chars
    for number in range(key_length):                                    # Grab modular chars and append to list
        alpha_set = []                                                  # Essentially creating individual alphabet sets
        for index in range(0, len(ciphertext), key_length):             # Increment by keylength
            try:
                alpha_set.append(ciphertext[number + index])
            except:
                pass
        alpha_sets.append(alpha_set)
    alpha_dicts = []
    for i in range(key_length):                                         # Do this for each set
        analyser = frequency_analysis.Frequency(charlist=alpha_sets[i])
        length, alpha_dict, freq_dict = analyser.analyze()              # Get analysis from module
        frequencies = [(item, freq_dict[item]) for item in freq_dict]   # List of tuples to sort
        frequencies.sort(key=lambda tup: tup[1])                        # Sort list by frequency
        frequencies.reverse()
        r_dict = set_up_replace_dict(frequencies)                       # Create replace dictionary
        alpha_dicts.append(r_dict)                                      # Append dict to list
    plaintext = ''
    for i in range(len(ciphertext)):
        index = i % key_length                                          # Index loops [0, key_length]
        plaintext += alpha_dicts[index][alpha_sets[index].pop(0)]       # Grab current dict[current character] and append to plaintext
    print plaintext


def set_up_replace_dict(frequencies):
    r_dict = {'a':'', 'b':'', 'c':'',
              'd':'', 'e':'', 'f':'',
              'g':'', 'h':'', 'i':'',
              'j':'', 'k':'', 'l':'',
              'm':'', 'n':'', 'o':'',
              'p':'', 'q':'', 'r':'',
              's':'', 't':'', 'u':'',
              'v':'', 'w':'', 'x':'',
              'y':'', 'z':''}
    sorted_alphabet = ['e', 't', 'a', 'o', 'i', 'h',
                       'n', 's', 'r', 'd', 'l', 'u',
                       'm', 'w', 'c', 'y', 'f', 'g',
                       'p', 'b', 'v', 'k', 'x', 'j',
                       'q', 'z']
    for number in range(len(frequencies)):
        r_dict[frequencies[number][0]] = sorted_alphabet[number]
    return r_dict

if __name__ == "__main__":
    sys.exit(main())

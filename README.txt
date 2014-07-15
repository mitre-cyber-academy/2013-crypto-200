Name: Le Chiffre Indéchiffrable

Description: You are a French mathematician in the year 1623 and a friend of yours is infatuated with cryptography. He recently read a book about modern cryptography, and has encrypted a message in hopes that you can't break it. Can you prove him wrong?

To Build: No building necessary. To rebuild do:
    ./transposition.py -k gaz -f plaintext.txt > ciphertext.txt

How to Solve: In order to solve this one, the user must first determine what method was used to encrypt. Based on the name, they can easily determine that it is the vigenere cipher. Once this has been accomplished, a brute force strategy must be used to perform frequency analysis on the three different alphabets, or use a different strategy.

What to Distribute: ciphertext.txt

Flag: MCA-50524E47 (Points to PRNG)

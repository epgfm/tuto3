#! /usr/bin/env python
# coding: utf-8

import argparse


def decrypt_char(c, shift):
    ''' (str, int) -> str

    Return character c shifted by shift places.

    >>> decrypt_char("B", 1)
    'A'
    >>> decrypt_char("C", 2)
    'A'
    >>> decrypt_char("A", 2)
    'Y'
    '''
    # Your code here



# Décrypte un text en fonction d'une clé
def decrypt_string(text, shift):
    ''' (str, int) -> str

    >>> decrypt_string('CPC', 1)
    'BOB'
    >>> decrypt_string('XLMW MW E XIWX', 4)
    'THIS IS A TEST'
    '''
    # Your code here



if __name__ == "__main__":

    import doctest
    res = doctest.testmod()
    print res

    # On parse les argument
    # -m pour le fichier encodé
    parser = argparse.ArgumentParser(description="Caesar decode program")
    parser.add_argument("-m", type=str, help="File to decode", required=True)
    args = parser.parse_args()

    # Le nom du fichier encodé
    enc_msg_file = args.m

    # On lit le fichier
    enc_msg = ""
    with open(enc_msg_file, "r") as f:
        enc_msg = f.read().strip()

    # On normalize
    enc_msg.upper()

    # On teste tous les 26 décallages possibles
    # en appelant la fonction de décryptage
    for i in range(27):
        print decrypt_string(enc_msg, i)
    



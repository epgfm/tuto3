#! /usr/bin/env python
# coding: utf-8

import argparse


def encrypt_char(c, shift):
    ''' (str, int) -> str

    Return character c shifted by shift places.

    >>> encrypt_char("A", 1)
    'B'
    >>> encrypt_char("A", 2)
    'C'
    >>> encrypt_char("Z", 2)
    'B'
    '''
    # your code here



def encrypt_string(string, shift):
    ''' (str, int) -> str

    Returns a shifted version of string msg.

    >>> encrypt_string("BOB", 1)
    'CPC'
    >>> encrypt_string("THIS IS A TEST", 4)
    'XLMW MW E XIWX'
    '''
    # your code here



# Programme principal
if __name__ == "__main__":

    import doctest
    res = doctest.testmod()
    print res

    # On récupère les arguments du programme
    # -d : spécifier le décallage
    # -m : spécifier le fichier texte contenant le message
    parser = argparse.ArgumentParser(description="encrypt_string code program")
    parser.add_argument("-d", type=int, help="How to shift the message", required=True)
    parser.add_argument("-m", type=str, help="File to encode", required=True)
    args = parser.parse_args()



    # On récupère le nom du fichier du message
    msg_file = args.m
    # On crée un autre nom de fichier pour la version codée
    enc_msg_file = "enc_" + msg_file

    # Lecture du message
    msg = ""
    with open(enc_msg_file, "r") as f:
        msg = f.read()


    # Normalisation, on passe tout en majuscule
    msg = msg.upper()    

    # Récupère le décallage donné en paramètre du programme
    d = args.d


    # Lance la fonction de codage
    msg_code = encrypt_string(msg, d)

    # Affiche les 2 versions
    print("Original : {}\nCode : {}".format(msg, msg_code))


    # Ecrit dans un fichier le message codé
    with open(enc_msg_file, "w") as f:
        f.write(msg_code)



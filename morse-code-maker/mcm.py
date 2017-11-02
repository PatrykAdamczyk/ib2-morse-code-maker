#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SYNOPSIS

    mcm

DESCRIPTION

    Translator Morse <> Tekst

AUTHOR

    Patryk Adamczyk <patrykadamczyk@paip.com.pl>

LICENSE

    PAiP Open Source License

VERSION

    v.1.0.0.0
"""
import sys
from libs.pwm_morse import *

def main(args):
    """Główna Funkcja Programu"""
    stringer = input("Type what you want translate: ")
    val = input("What you want? (E or e - To Morse | D or d - From Morse): ")
    if str(val).lower() == "e":
        kod = Morse(stringer,True)
        print(kod.encrypted)
    elif str(val).lower() == "d":
        kod = Morse(stringer)
        print(kod.decrypted)
    else:
        raise Exception("Error MCM#1: Not supported action")
    sys.exit()

if __name__ == '__main__':  # pragma: no cover
    sys.exit(main(sys.argv))

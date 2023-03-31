#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Generate random words, numbers, and special characters for a password.

Uses `wonderwords` to generate a randomly-capitalized adjective and nouns,
`random` to randomly generate four numbers and two special characters (using 
`string`). The password is then put together and copied to the clipboard via
`pyperclip`. 

Typical usage example:
    python password_generator.py
"""
import random
import string

import pyperclip
import wonderwords


def main():
    """Generate a random combination of the following form:
    [adjective] [noun] [special char] [numbers] [special char]
    """
    adjectives = wonderwords.RandomWord(
        adjective=wonderwords.Defaults.ADJECTIVES)
    nouns = wonderwords.RandomWord(noun=wonderwords.Defaults.NOUNS)
    adjective = ''.join(random.choice(
        (str.upper, str.lower))(char) for char in adjectives.word()
    )
    noun = ''.join(random.choice(
        (str.upper, str.lower))(char) for char in nouns.word()
    )
    numbers = ''.join(map(str, random.sample(range(0, 9), 4)))
    symbols = random.sample(string.punctuation, 2)

    password = adjective + noun + symbols[0] + numbers + symbols[1]
    pyperclip.copy(password)
    print(f'Generated password: {password}. Copied to clipboard')


if __name__ == '__main__':
    main()

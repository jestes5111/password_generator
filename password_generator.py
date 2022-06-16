#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Generate random words for a password."""

__file__ = 'password_generator.py'
__author__ = 'Jesse Estes'
__credits__ = ['Jesse Estes']
__license__ = 'MIT'
__version__ = '1.0.0'
__maintainer__ = 'Jesse Estes'
__email__ = 'jestes5111@gmail.com'
__status__ = 'Prototype'

# --------------------------------------------------------------------------- #
#                                  Imports                                    #
# --------------------------------------------------------------------------- #
# Standard libraries
import random
import string

# Third-party libraries
import pyperclip
import wonderwords

# Owned libraries

# --------------------------------------------------------------------------- #
#                                    Code                                     #
# --------------------------------------------------------------------------- #
def main():
  """Generate a random combination of the following form:
  [adjective] [noun] [special char] [numbers] [special char]
  """
  # Create the list of adjectives and nouns
  adjectives = wonderwords.RandomWord(adjective=wonderwords.Defaults.ADJECTIVES)
  nouns = wonderwords.RandomWord(noun=wonderwords.Defaults.NOUNS)

  # Generate an adjective and a noun
  adjective = adjectives.word()
  noun = nouns.word()
  
  # Generate four random numbers (arbitrary, can change if desired)
  numbers = random.sample(range(0, 9), 4)

  # Generate two random symbols
  symbols = random.sample(string.punctuation, 2)

  # Randomly capitalize letters in each word
  adjective = ''.join(random.choice(
    (str.upper, str.lower))(char) for char in adjective
  )
  noun = ''.join(random.choice((str.upper, str.lower))(char) for char in noun)

  # Convert the list of numbers to a single string
  numbers = ''.join(map(str, numbers))

  # Create the password
  password = adjective + noun + symbols[0] + numbers + symbols[1]

  # Copy the password to the clipboard
  pyperclip.copy(password)

  # Inform the user
  print(f'Generated password: {password}. Copied to clipboard')

if __name__ == '__main__':
  main()
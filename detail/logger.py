#!/usr/bin/env python3

"""
Minimum Logger object that can be passed to other objects
"""

class LMDrunLogger():
    def __init__(self):
        self.__contents__ = ''

    def log(self, message):
        self.__contents__ += message + '\n'

    def print(self):
        print(self.__contents__)

    def save(self, filename):
        filename.parent.mkdir(exist_ok=True)
        with open(filename, 'w') as file:
            file.write(self.__contents__)
        print(f'Log successfully saved to {filename.absolute()}!')

if __name__ == "__main__":
    print("Sorry, this module can't be run directly")

"""Word Finder: finds random words from a dictionary."""

import fileinput
import random

class WordFinder:
    """
        Returns words at random from given list
        file path is ~/bootcamp/python/python-oo-practice/words.txt
        """

    def __init__(self, filename):
        "Instantiate and print count of words read"
        file = open(filename)

        self.words = self.words_list(file)

        print(f"{len(self.words)} words read")


    def words_list(self, file):
        "create a list of words from file, strip unnecessary characters"
        return [line.strip() for line in file]

    def random(self):
        "return a word at random from list"
        return random.choice(self.words)


class SpecialWordFinder(WordFinder):
    """
        Returns word at random from file, ignoring blank lines or lines starting with
        # signs.
        """

    def words_list(self, file):
        "create a list of words from file, strip unnecessary characters"
        return [line.strip() for line in file
                if line.strip() != '' and not line.startswith("#")]
                


            



        



         
         
 

    

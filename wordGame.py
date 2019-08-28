# import necessary modules
import json
import random
import nltk # natural language tool kit
from nltk.corpus import words
import time
# download word database
#nltk.download('words')


class WordGameUI:
    """
    A game that gives a player a collection of letters to form
    words with, and confirms if the words formed are valid words.
    """

    class _WordGame:

        """
        Non public class which controls most of the game processes 
        """

        def __init__(self):
            """
            constructor for the WordGame class
            """
            # create necessary containers
            #self.diction = dict() # collection of words
            self.possi_words = set() # possible words
            self._task = list() # letters given to player
            self.eng_word = words.words()

            # open json file
            f = open('dictionary.json', 'r')
            # load the json file
            self.diction = json.load(f)
            
            #close opened file
            f.close()

        def _set_task(self):
            """
            generates the letters given to a player to form words with
            """
            # determines the no of letters to be given to player
            l = random.randint(5,12)
            i = 0
            # generates the list of letters
            while i < l:
                rl = chr(random.randint(65,90))
                self._task.append(rl) # rl - random letter
                #print(rl)
                i += 1

            

        def _get_task(self):
            """
            getter method for the task attribute
            """
            return self._task

#----------------------------------------------

        def _is_eng(self, w):
            """
            validates if word formed are true english words
            """
            return w in self.eng_word


    def __init__(self):
        """
        user interface for the word game
        """

        # instantiate the WordGame class
        self.wg = self._WordGame()
        self.score = 0 # player's score
        self.targ = set() # collection of english words
        self.lives = 3

#-----------------------------------------------------

    def _compare(self, lt, wd):
        i = 0 # counter
        ltc = lt.copy()
        # adds 1 to i if a letter in a word is in d array
        for l in wd:
            if l in ltc:
                i += 1
                ltc.pop(ltc.index(l))
        # word can be form if i = len(wd)
        return i

#--------------------------------------------------------

    def give_test(self):
        """
        public interface that give test to users
        """
        # assign a task to user
        self.wg._set_task()
        # display task to user
        #print("""form a word from the given characters. \n""", self.wg._get_task())

        #---------- checking algorithm ---------------
        # get the keys of the dictionary and add to targ
        for k in self.wg.diction.keys():
            self.targ.add(k)

        # add word contained in nltk dictionary
        for kk in self.wg.eng_word:
            self.targ.add(kk.upper())

        # each element in target
        for el in self.targ:
            task_copy = self.wg._get_task()
            word_len = len(el)

            # add word to pw if all char of el are in col
            if self._compare(task_copy, el) == word_len:
                if len(el) > 1:
                    self.wg.possi_words.add(el)

        if len(self.wg.possi_words) < 1:
            # generate another set of letters recursively
            self.wg._task = []
            self.give_test()
        else:
            # display task to user
            print("""form a word from the given characters. \n""", self.wg._get_task())

#--------------------------------------------------------

    def proc(self):
        """
        recieves input and gives the appropriate response
        """
        ans = str(input('enter your answer here: '))
        ans = ans.upper()
        print(ans)
        # if word is in both dictionaries 
        if ans in self.wg.possi_words:
                print('correct')
                # score is 1 per char of word formed
                self.score += (len(ans) * 1)
                # empty possi_words array
                self.wg.possi_words = set()
        else:
            print('wrong!')
            # subtract 1 from live
            self.lives -= 1
            # empty possi_words array
            self.wg.possi_words = set()
            if self.lives == 0:
                raise ValueError('invalid word')

#-----------------------------------------------------------

    def startt(self):
        """
        starts the game
        """
        try:
            # introduction
            player = input('Enter your game name: ')
            print('welcome to EA WordGame {}!'.format(player))
            time.sleep(2)
            print('i hope you enjoy it')
            time.sleep(3)
            print('Loading...pls wait.....')
            while self.lives > 0:
                self.give_test()
                print('{} words can be formed, here they are:- '.format(len(self.wg.possi_words)), self.wg.possi_words)
                self.proc()
                # empty the list of letters
                self.wg._task = []
        except ValueError:
            print('Game over!')
            print('score:',self.score)        



        






#--------------- Test suit ---------
if __name__ == "__main__":

    WordGameUI().startt()
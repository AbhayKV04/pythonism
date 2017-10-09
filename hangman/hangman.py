# Hangman game

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  " + str(len(wordlist)) + " words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()


def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    # for each letter in secret word
    for letter in secretWord:        
        # check if the letter is among the guessed letters
        if letter not in lettersGuessed:            
            # return False if not found
            return False
    
    # secret word has been guessed, return True
    return True


def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    
    string = ''
    
    # for each letter in secret word
    for letter in secretWord:        
        # if the letter is among guessed letters
        if letter in lettersGuessed:            
            # append the letter to the string
            string += letter
        else:
            # append underscore to the string
            string += '_ '
    
    # return final string
    return string


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    
    string = ''
    lowercaseAlphabets = 'abcdefghijklmnopqrstuvwxyz'
    
    # for each letter in lowercase alphabets
    for letter in lowercaseAlphabets:
        # if the letter is not among guessed letters
        if letter not in lettersGuessed:
            # append the letter to string
            string += letter
    
    # return final string
    return string
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * Let the user know how many letters the secretWord contains.

    * Asks the user to supply one guess (i.e. letter) per round.

    * The user receives feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, displays to the user the partially guessed word so far,
      as well as letters that the user has not yet guessed.
    '''
    
    # helper variables
    guessesLeft = 8
    lettersGuessed = []
    
    # welcome user
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long.')
    print('-------------')
    
    # while there are guesses left
    while guessesLeft:        
        # show number of guesses & available letters and prompt for input
        print('You have ' + str(guessesLeft) + ' guesses left.')
        print('Available letters: ' + str(getAvailableLetters(lettersGuessed)))
        userGuess = input('Please guess a letter: ').lower()
        
        # if input is already guessed
        if userGuess in lettersGuessed:
            print("Oops! You've already guessed that letter: " + str(getGuessedWord(secretWord, lettersGuessed)))
        else:
            # append the input to guessed letters list
            lettersGuessed.append(userGuess)
            
            # if user's input is correct
            if userGuess in secretWord:
                print('Good guess: ' + str(getGuessedWord(secretWord, lettersGuessed)))
            else:
                # if user's input is wrong
                print('Oops! That letter is not in my word: ' + str(getGuessedWord(secretWord, lettersGuessed)))
                # decrement number of guesses
                guessesLeft -= 1
        
        print('-------------')
        
        # if the word is guessed correctly
        if isWordGuessed(secretWord, lettersGuessed):
            print('Congratulations, you won!')    
            break
    
    # if user fails to guess the correct word
    if not guessesLeft:
        print('Sorry, you ran out of guesses. The word was ' + str(secretWord) + '.')


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
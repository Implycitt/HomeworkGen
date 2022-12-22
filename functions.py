'''
Author: Quentin Bordelon
2022-12-22
'''
import pydictionary, sys

class Vocab:
    
    sys.stdin = open("input.txt", 'r').readlines()
    sys.stdout = open("output.txt", 'w')

    def define(word):
        findword = pydictionary.Dictionary(word)
        meaning = findword.meanings()
        return meaning[0]

    def sentence(word):
        return
    
    def format():
        for count, i in enumerate(sys.stdin):
            if count == 0:
                print(f'\t\t\t\t\t\tVocabulary')
            meaning = Vocab.define(i)
            print(f"\t{count+1}. {i[:-1]}: {meaning}")
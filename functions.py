'''
Author: Quentin Bordelon
Start Date: 2022-12-22
V1: 2022-12-23
'''

import pydictionary, os, openai

class Vocab:
    
    with open("input.txt", 'r') as file:
        words = file.read().strip().split('\n')

    def define(word):
        findword = pydictionary.Dictionary(word)
        meaning = findword.meanings()
        return meaning[0]

    def sentence(word):
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt= f"write a sentence with the word {word}",
        temperature=0.8,
        max_tokens=60,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0
        )
        return response.get("choices")[0].get("text").split('. ')[0][2:]
    
    def format():
        fout = open("output.txt", 'w')
        for count, i in enumerate(Vocab.words):
            if count == 0:
                fout.write(f'\t\t\t\t\t\tVocabulary\n')
            meaning = Vocab.define(i)
            Sentence = Vocab.sentence(i)
            fout.write(f"\t{count+1}. {i}: {meaning} {Sentence}\n")
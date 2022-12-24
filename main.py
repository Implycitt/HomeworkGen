from functions import Vocab, openai

openai.api_key = input("Please enter your openAI API key: ")
vocab = Vocab.format()
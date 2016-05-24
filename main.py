# -*- coding: utf-8 -*-

"""
Currently just a testing harness for other modules
"""
import tweets
import emotionDatabase
import markovify

# tweets.postTweet("Testing")
# emotionDatabase.createHappy()

# emotionDatabase.createExistential()


def strip_non_ascii(string):
    ''' Returns the string without non ASCII characters'''
    stripped = (c for c in string if 0 < ord(c) < 127)
    return ''.join(stripped)


with open('emotions/existential.txt', encoding='utf-8') as f:
    text = f.read()

text = strip_non_ascii(text)


text_model = markovify.Text(text)

sentence = text_model.make_short_sentence(140)

print(sentence.encode('utf-8'))

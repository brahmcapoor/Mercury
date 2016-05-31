from random import choice
import tweets

"""
Deals with various aspects of selecting moods
"""
moods = [
    'happy',
    'existential',
    'contemptuous',
    'sad',
    'innovative',
    'disgusted',
    'surprised',
    'inspirational',
    'romantic',
    'philosophical',
    'wise']


def moodList():
    return moods


def generateDatabase():
    emotionDatabase.create_emotion_database(moods)


def choose_random_mood():
    return choice(moods)


def change_mood():
    mood = choose_random_mood()
    # tweets.update_description(("Today I'm feeling {}").format(mood))

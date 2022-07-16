import random
import tweepy
from PyDictionary import PyDictionary
from random_words import RandomWords
import datetime
import time
from ka import keep_alive

keep_alive()

# Twitter Setup
consumer_key = "CONSUMER_KEY"
consumer_secret_key = "CONSUMER_SECRET_KEY"
access_token = "ACCESS_TOKEN"
access_token_secret = "ACCESS_TOKEN_SECRET"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)


# Actual Code
def load_random_word():
    rw = RandomWords()
    dictionary = PyDictionary()

    word = rw.random_word()
    definitions = dictionary.meaning(word)

    try:
        part_of_speech = random.choice(list(definitions.keys()))
        definition = random.choice(definitions[part_of_speech])
    except:
        return "NULL_DEFINITION"

    return {
        "word": word,
        "definition": definition.capitalize(),
        "part_of_speech": part_of_speech
    }


while True:
    if 8 <= datetime.datetime.now().hour <= 10:
        word_of_the_day = load_random_word()

        while word_of_the_day == "NULL_DEFINITION":
            word_of_the_day = load_random_word()

        # Twitter Post
        wotd_tweet = f'Today\'s #WordOfTheDay is {word_of_the_day["word"]}! ({word_of_the_day["part_of_speech"]}) \n\n{word_of_the_day["definition"]}.'
        api = tweepy.API(auth)
        api.update_status(wotd_tweet)

    time.sleep(1.75 * 3600) # Sleep for 1.45 hours

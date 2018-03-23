import string
import json
from collections import Counter
import nltk
from nltk.corpus import stopwords

def tokenize_tweet(tweet):
	"""returns a tokenized (list) version of a tweet"""
	return nltk.word_tokenize(tweet)

def cleanse_tweet(tweet):
	"""given a tweet as a tokenized list, removes uneccesary words"""
	#Note: I added some words of my own to filter, because useless strings
	#such as "n't" or "http" were appearing in the list of most common words
	stop_words = stopwords.words('english') + list(string.punctuation) + ['“','”', 'http', "'s", '``', 'realdonaldtrump', '...', "n't", "''", "rt"]
	return [word for word in tweet if word not in stop_words]

def printable_tweet(tweet):
	"""Strips tweet of any non-printable characters and converts to lowercase"""
	printable = set(string.printable)
	return "".join(list(filter(lambda x: x in printable, tweet))).lower()

def count_words(tweet):
	return Counter(tweet)

def print_most_common(frequencies, num=20):
	"""Prints num most common words and their respective frequencies"""
	counts = []
	for word, count in frequencies.most_common():
		counts.append([word, count])
	for i in range(num):
		print(counts[i])

if __name__ == "__main__":
	raw_data = json.load(open('obamatweets.json'))
	tweets = []
	for x in raw_data:
		#strip just the tweet text, append to list of tweets
		tweets.append(printable_tweet(x["text"]))

	frequencies = Counter()
	for tweet in tweets:
		#Tokenize the tweet
		tweet = tokenize_tweet(tweet) 
		#Cleanse the tweet
		tweet = cleanse_tweet(tweet)
		#Combine the frequencies of each tweet
		frequencies += count_words(tweet)
	print_most_common(frequencies)

# calculating vader sentiments for the tweets and the news texts

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json

analyzer = SentimentIntensityAnalyzer()

# opening necessary files

inputTweet = open("Texts.txt", "r")
outputTweet = open("TextsVADER.json", "w")

# defining a function to analyze the sentence and write the vader scores back into a text file
def analyze(inp, opt):
	for sentence in inp:
		vs = analyzer.polarity_scores(sentence)
		print(str(vs))
		json.dump(vs, opt)
		opt.write('\n')

analyze(inputTweet, outputTweet)
inputTweet.close()
outputTweet.close()

# repeating process for NEWS section too

inputNews = open("NewsExtractedText.txt", "r")
outputNews = open("NewsVADER.json", "w")

analyze(inputNews, outputNews)

inputNews.close()
outputNews.close()

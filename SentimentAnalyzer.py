from nltk.sentiment.vader import SentimentIntensityAnalyzer
class SentimentAnalyzer:
    comments={}

    def analyzeSentiment(text):
        score= SentimentIntensityAnalyzer().polarity_scores(text)
        return score['compound']
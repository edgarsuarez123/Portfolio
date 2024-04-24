from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Initialize the VADER sentiment analyzer
analyzer = SentimentIntensityAnalyzer()

# Sample text
text = "I love this movie! It's so awesome."

# Analyze sentiment
sentiment_score = analyzer.polarity_scores(text)

# Print sentiment score
print("Sentiment Score:", sentiment_score)

# Determine sentiment label
if sentiment_score['compound'] >= 0.05:
    print("Positive Sentiment")
elif sentiment_score['compound'] <= -0.05:
    print("Negative Sentiment")
else:
    print("Neutral Sentiment")

import nltk
import pandas as pd
import sys

filename = sys.argv[1]

# Need to do nltk.download('vader_lexicon')
def nltk_sentiment(sentence):
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    
    nltk_sentiment = SentimentIntensityAnalyzer()
    score = nltk_sentiment.polarity_scores(sentence)
    return score

with open(filename, 'r') as f:
    line = f.readlines()

nltk_results = [nltk_sentiment(row) for row in line]
results_df = pd.DataFrame(nltk_results)
text_df = pd.DataFrame(line, columns = ['text'])
nltk_df = text_df.join(results_df)

# Write data to excel spreadsheet

nltk_df.to_csv(filename + '.csv', sep=',')

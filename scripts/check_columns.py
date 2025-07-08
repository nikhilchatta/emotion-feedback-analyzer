import pandas as pd

emotion = pd.read_csv("./data/combined_emotion.csv")
sentiment = pd.read_csv("./data/combined_sentiment.csv")

print("Emotion columns:", emotion.columns.tolist())
print("Sentiment columns:", sentiment.columns.tolist())


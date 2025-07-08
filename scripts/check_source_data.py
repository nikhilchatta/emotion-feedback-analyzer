import pandas as pd

# Load CSVs
emotion = pd.read_csv("./data/combined_emotion.csv")
sentiment = pd.read_csv("./data/combined_sentiment.csv")

# Print info
print("✅ Emotion file shape:", emotion.shape)
print("✅ Sentiment file shape:", sentiment.shape)

print("\n🧾 Emotion columns:", emotion.columns.tolist())
print("📄 Sentiment columns:", sentiment.columns.tolist())

print("\n🟡 Sample emotion:")
print(emotion.head())

print("\n🟠 Sample sentiment:")
print(sentiment.head())

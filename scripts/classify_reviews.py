import pandas as pd
from transformers import pipeline

# Load pre-trained Hugging Face pipelines
print("Device set to use cpu")
emotion_model = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)
sentiment_model = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

# Urgency keyword set
urgency_keywords = {"urgent", "asap", "immediately", "now", "help", "emergency", "quick", "soon", "fast", "support"}

def is_urgent(text):
    return any(word in text.lower() for word in urgency_keywords)

def classify_row(row):
    text = row["clean_text"] if "clean_text" in row else row["text"]
    
    try:
        emotion = emotion_model(text)[0][0]["label"]
    except:
        emotion = "unknown"
    
    try:
        sentiment = sentiment_model(text)[0]["label"]
    except:
        sentiment = "unknown"

    urgency = "urgent" if is_urgent(text) else "not_urgent"

    return pd.Series([emotion, sentiment, urgency], index=["predicted_emotion", "predicted_sentiment", "predicted_urgency"])

def main():
    df = pd.read_csv("./data/cleaned_merged_dataset.csv")
    
    if "clean_text" not in df.columns:
        df["clean_text"] = df["text"]

    print("Running classification on", len(df), "rows...")

    results = df.apply(classify_row, axis=1)
    df = pd.concat([df, results], axis=1)

    df.to_csv("./data/final_classified_reviews.csv", index=False)
    print("✅ Classification complete! Output saved to data/final_classified_reviews.csv")

if __name__ == "__main__":
    main()

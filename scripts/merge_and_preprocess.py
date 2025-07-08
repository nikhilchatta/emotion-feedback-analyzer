import pandas as pd
import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-zA-Z\s]", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    stop_words = set(stopwords.words("english"))
    return " ".join([word for word in text.split() if word not in stop_words])

def load_and_preprocess():
    sentiment_df = pd.read_csv("./data/combined_sentiment.csv")
    sentiment_df.rename(columns={"sentence": "text"}, inplace=True)
    sentiment_df["clean_text"] = sentiment_df["text"].apply(clean_text)
    sentiment_df.to_csv("./data/cleaned_merged_dataset.csv", index=False)
    print("✅ Preprocessed sentiment-only dataset saved to ./data/cleaned_merged_dataset.csv")

if __name__ == "__main__":
    load_and_preprocess()

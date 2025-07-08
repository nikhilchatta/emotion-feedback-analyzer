import pandas as pd
import streamlit as st
import plotly.express as px

# Load data
df = pd.read_csv("./data/final_classified_reviews.csv")

st.set_page_config(page_title="Emotion-aware Feedback Analyzer", layout="wide")
st.title("🧠 Emotion-aware Feedback Dashboard")

# =================== Summary Metrics ===================
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🔢 Total Reviews", len(df))
with col2:
    st.metric("😊 Positive Sentiment", (df['predicted_sentiment'] == 'positive').sum())
with col3:
    st.metric("🚨 Urgent Flags", (df['predicted_urgency'] == 'urgent').sum())

# =================== Emoji-based Emotion Counts ===================
st.subheader("😃 Emotion Distribution")
emoji_map = {
    "joy": "😄", "anger": "😠", "sadness": "😢", "fear": "😨",
    "surprise": "😲", "love": "❤️", "disgust": "🤢", "neutral": "😐", "unknown": "❓"
}
df["emotion_display"] = df["predicted_emotion"].apply(lambda e: f"{emoji_map.get(e, '❓')} {e}")
emotion_counts = df["emotion_display"].value_counts().reset_index()
emotion_counts.columns = ["Emotion", "Count"]
fig_emotion = px.bar(emotion_counts, x="Emotion", y="Count", color="Emotion", title="Emotions with Emoji Badges")
st.plotly_chart(fig_emotion, use_container_width=True)

# =================== Sentiment Pie ===================
st.subheader("🧭 Sentiment Overview")
sentiment_counts = df["predicted_sentiment"].value_counts().reset_index()
sentiment_counts.columns = ["Sentiment", "Count"]
fig_sentiment = px.pie(sentiment_counts, names="Sentiment", values="Count", title="Sentiment Distribution")
st.plotly_chart(fig_sentiment, use_container_width=True)

# =================== Urgency Heatmap ===================
st.subheader("🔥 Urgency and Emotion Heatmap (Simulated Timeline)")
df["Index"] = df.index
heatmap_data = df.groupby(["Index", "predicted_urgency"]).size().reset_index(name="count")
fig_heatmap = px.density_heatmap(heatmap_data, x="Index", y="predicted_urgency", z="count", color_continuous_scale="Reds")
st.plotly_chart(fig_heatmap, use_container_width=True)

# =================== Raw Data View ===================
with st.expander("📄 Show Raw Data Table"):
    st.dataframe(df)

# =================== Alert Section ===================
st.subheader("⚠️ Real-Time Alerts")
if (df['predicted_sentiment'] == 'negative').mean() > 0.4:
    st.error("🚨 High negative sentiment detected! More than 40% of reviews are negative.")
if (df['predicted_urgency'] == 'urgent').mean() > 0.2:
    st.warning("⚠️ Urgent feedback spike: Over 20% marked as urgent.")




# Emotion-aware Feedback Analyzer 🧠💬

🎯 Analyze customer feedback for **emotion**, **sentiment**, and **urgency** in real time.

🌐 Live Demo: [https://emotionfeedbackanalyzer.streamlit.app](https://emotionfeedbackanalyzer.streamlit.app)

---

## 📌 Overview

This app uses pre-trained NLP models from Hugging Face to:
- Detect **emotion** (e.g., joy, anger, sadness)
- Classify **sentiment** (positive, negative, neutral)
- Identify **urgent** messages using keyword matching

It visualizes everything through an interactive Streamlit dashboard with:
- Emoji-based emotion bar charts
- Sentiment pie chart
- Urgency heatmap
- Real-time alerts on spikes

---

## 🚀 Features

✅ Real-time NLP using Hugging Face Transformers  
✅ Urgency detection via keywords like "urgent", "asap", "help"  
✅ Interactive Streamlit dashboard  
✅ Emoji-based visualizations  
✅ Data table with expandable details  
✅ Deployed on Streamlit Cloud  

---

## 📂 Project Structure

```

emotion-feedback-analyzer/
├── app/
│   └── dashboard.py              # Streamlit frontend
├── data/
│   └── final\_classified\_reviews.csv
├── scripts/
│   ├── classify\_reviews.py       # Runs emotion/sentiment/urgency classification
│   ├── merge\_and\_preprocess.py   # Preprocess source data
│   └── check\_source\_data.py      # Verify dataset integrity
├── requirements.txt
└── README.md

````

---

## 🛠 Tech Stack

- **Language**: Python
- **Libraries**: Streamlit, Hugging Face Transformers, Plotly, Pandas, NLTK
- **Models**:  
  - `j-hartmann/emotion-english-distilroberta-base` (Emotion)  
  - `cardiffnlp/twitter-roberta-base-sentiment` (Sentiment)
- **Deployment**: Streamlit Cloud

---

## ⚙️ Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/YOUR_USERNAME/emotion-feedback-analyzer.git
cd emotion-feedback-analyzer
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the app

```bash
streamlit run app/dashboard.py
```

---

## 🧪 Test Your Own Data

Replace `data/final_classified_reviews.csv` with your own CSV.
Make sure it has a `text` column or adapt the preprocessing script accordingly.

---

## 📸 Preview

![image](https://github.com/user-attachments/assets/35c6f019-49ac-4cea-bef2-d7a44b48ca0e)
![image](https://github.com/user-attachments/assets/54a3653d-f822-4899-8414-806984b44904)
![image](https://github.com/user-attachments/assets/43210580-2f7b-472e-a1cf-86f9c36523d9)
![image](https://github.com/user-attachments/assets/389cd799-a8f1-4f79-8485-9532e1d3ad83)




---

## 📄 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgements

* Hugging Face Transformers
* Streamlit
* NLTK & Plotly




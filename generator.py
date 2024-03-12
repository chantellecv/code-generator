import streamlit as st
from textblob import TextBlob

# Function to analyze sentiment
def analyze_sentiment(email_text: str):
    analysis = TextBlob(email_text)
    sentiment_polarity = analysis.sentiment.polarity
    sentiment_subjectivity = analysis.sentiment.subjectivity

    if sentiment_polarity > 0:
        sentiment_label = 'Positive'
    elif sentiment_polarity == 0:
        sentiment_label = 'Neutral'
    else:
        sentiment_label = 'Negative'

    return sentiment_label, sentiment_polarity, sentiment_subjectivity

# Streamlit app layout
st.title('Email Sentiment Analysis App')

# Textarea for user input
email_input = st.text_area("Paste your email text here:")

# Analyze button
if st.button('Analyze'):
    if email_input:
        sentiment_label, sentiment_polarity, sentiment_subjectivity = analyze_sentiment(email_input)
        st.success(f'Sentiment: {sentiment_label}')
        st.info(f'Polarity: {sentiment_polarity:.2f}')
        st.info(f'Subjectivity: {sentiment_subjectivity:.2f}')
    else:
        st.error('Please paste some text to analyze.')
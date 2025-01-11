import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
ps = PorterStemmer()

Tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))

st.title('Email/SMS spam classifier')
sms_input = st.text_input('Enter the message')


def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)
if st.button('predict'):

    transform_sms = transform_text(sms_input)
    vector_input = Tfidf.transform([transform_sms])
    result = model.predict(vector_input)
    if result == 1:
        st.header('spam')
    else:
        st.header('not spam')




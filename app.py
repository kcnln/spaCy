import streamlit as st
import pandas as pd
import numpy as np
import spacy
from spacy.lookups import Lookups
from spacy.tokens import Token
Token.set_extension("ipa_", default=False, force=True)


def text_lemmatizer(input_text):
    nlp = spacy.blank("cy")
    nlp.add_pipe("lemmatizer", config={"mode": "lookup"})
    nlp.initialize()
    doc = nlp(input_text)
    lemmas = [token.lemma_ for token in doc]
    lemmas = (" ".join(i for i in lemmas))
    return lemmas
    
    
def text_transcriber(input_text):
    nlp = spacy.blank("cy")
    nlp.add_pipe("transcriber", config={"mode": "lookup"})
    nlp.initialize()
    doc = nlp(input_text)
    ipas = [token._.ipa_ for token in doc]
    ipas = (" / ".join(i for i in ipas))
    return ipas


def main():
    st.title("Spacy Experiments")
    st.subheader("Lemmatization and IPA Transcription")
    
    operation = st.radio("What would you like to do?", ('Lemmatize', 'Transcribe to IPA'))

    if operation == 'Lemmatize':
        st.subheader("Lemmatize your text!")
        sentence = st.text_input("Text string to analyze:", "Sut wyt ti heddiw?")
        if st.button("Lemmatize!"):
            lemma_result = text_lemmatizer(sentence)
            st.success(lemma_result)
    elif operation == 'Transcribe to IPA':
        st.subheader("Transcribe your text!")
        sentence = st.text_input("Text string to analyze:", "Sut wyt ti heddiw?")
        if st.button("Transcribe!"):
            ipa_result = text_transcriber(sentence)
            st.success(ipa_result)

if __name__ == '__main__':
    main()

import streamlit as st 
import os


# NLP Pkgs
from textblob import TextBlob 
#mport spacy
from gensim.summarization import summarize

# Sumy Pkg
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer


# Sumy Summarization
def sumy_summarizer(docx):
	parser = PlaintextParser.from_string(docx,Tokenizer("english"))
	lex_summarizer = LexRankSummarizer()
	summary = lex_summarizer(parser.document,3)
	summary_list = [str(sentence) for sentence in summary]
	result = ' '.join(summary_list)
	return result




def main():
	""" NLP Based App with Streamlit """

	# Title
	st.title("NLPiffy with Streamlit")
	st.subheader("Natural Language Processing On the Go..")

	
	
	# Sentiment Analysis
	if st.checkbox("Show Sentiment Analysis"):
		st.subheader("Analyse Your Text")

		message = st.text_area("Enter Text","Type Here ..")
		if st.button("Analyze"):
			blob = TextBlob(message)
			result_sentiment = blob.sentiment
			st.success(result_sentiment)

	


	st.sidebar.subheader("About App")
	st.sidebar.text("NLPiffy App with Streamlit")
	st.sidebar.info("Cudos to the Streamlit Team")
	

	

if __name__ == '__main__':
	main()
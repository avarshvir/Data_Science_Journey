"""
Sentiment Analysis is a process of extracting emotions or sentiments from a raw text using
Natural Language Processing (NLP) and Computational Linguistics. People express their opinions
and feelings on various social media platforms such as Twitter, Facebook, Instagram, etc.
Social Media Sentiment Analysis can help organizations or marketers to understand how people
perceive or feel about their brand, products, services, etc.
"""
# Import Required Libraries
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import string
#import nltk
#from wordcloud import WordCloud

#%matplotlib inline

# Read the dataset
df = pd.read_csv('https://raw.githubusercontent.com/dD2405/Twitter_Sentiment_Analysis/master/train.csv')

print(df.head())
print(df.tail())
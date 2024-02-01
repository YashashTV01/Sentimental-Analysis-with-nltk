import string
from collections import Counter

import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Read the text from the file
text = open('read.txt', encoding='utf-8').read()

# Convert text to lowercase
lower_case = text.lower()

# Remove punctuation
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# Tokenize the cleaned text
tokenized_words = word_tokenize(cleaned_text, "english")

# Remove stop words
final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

# Lemmatization - Convert words to their base form
lemma_words = []
for word in final_words:
    word = WordNetLemmatizer().lemmatize(word)
    lemma_words.append(word)

# Emotion analysis
emotion_list = []
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in lemma_words:
            emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print(w)

# Function to perform sentiment analysis using VADER
def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    if score['neg'] > score['pos']:
        print("Negative Sentiment")
    elif score['neg'] < score['pos']:
        print("Positive Sentiment")
    else:
        print("Neutral Sentiment")

# Perform sentiment analysis on the cleaned text
sentiment_analyse(cleaned_text)

# Plot the emotions bar graph
fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('bargraph.png')
plt.show()

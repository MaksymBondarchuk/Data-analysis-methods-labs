import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

reviews = pd.read_csv('reviews_filtered.csv')

star_counts = reviews['stars'].value_counts()

star_counts.sort_index().plot(kind='bar')

# task, filter the 'text' column using the 'stars' column to create Series of good and bad review text
# call the results good_review_text and bad_review_text, respectively
# two lines of code here:
good_review_text = reviews[reviews['stars'] == 5]['text']
bad_review_text = reviews[reviews['stars'] <= 3]['text']

# print(good_review_text.head(3))
print(type(good_review_text))
print(good_review_text.shape)
print(bad_review_text.shape)
print(good_review_text.head())

good_review_text = good_review_text[:1000]
bad_review_text = bad_review_text[:1000]
# print(good_review_text.shape)
# print(bad_review_text.shape)
# print(good_review_text.head())

good_text = good_review_text.str.cat()
bad_text = bad_review_text.str.cat()

print(good_text)
print(len(good_text))
# print(bad_text)
# print(len(bad_text))

good_wordcloud = WordCloud(max_words=50).generate(good_text)
plt.imshow(good_wordcloud, interpolation='bilinear')

good_wordcloud.to_file("good_wordcloud.png")

bad_wordcloud = WordCloud(max_words=50).generate(bad_text)
plt.imshow(bad_wordcloud, interpolation='bilinear')

bad_stopwords = set(['pizza', 'food', 'order', 'place'])
bad_stopwords.update(["and", "the", "to", "that", "as", "in", "it"])
better_wordcloud = WordCloud(stopwords=bad_stopwords, max_words=50).generate(good_text)
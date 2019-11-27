import pandas as pd

businesses = pd.read_csv('italian_pizza.csv')
print(businesses.head())

business_ids = businesses['business_id'].values
print(business_ids[:5])

review_reader = pd.read_json('JSON/review_10000.json', lines=True, chunksize=1000000)

reviews = [chunk[chunk['business_id'].apply(lambda x: x in business_ids)] for chunk in review_reader]
# reviews = []
# for chunk in review_reader:
#     new_chunk = chunk[chunk['business_id'].apply(lambda x: x in business_ids)]
#     print(chunk.shape)
#     print(chunk.info())
#     print(new_chunk.shape)
#     print(type(new_chunk))
#     print(len(new_chunk.values))
#     print(new_chunk.values[0])
#     print(type(new_chunk.values[0]))
print()
print(reviews[0])
print(type(reviews))
print(len(reviews))
print()

reviews = pd.concat(reviews)
print(type(reviews))
print(reviews.shape)
# print(reviews.shape)
# print(reviews.head())
# print(reviews.info())

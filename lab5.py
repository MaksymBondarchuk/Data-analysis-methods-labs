import pandas as pd

businesses = pd.read_csv('italian_pizza.csv')
print(businesses.head())

business_ids = businesses['business_id'].values
print(business_ids[:5])

review_reader = pd.read_json('JSON/review.json', lines=True, chunksize=100000)

reviews = [r for chunk in review_reader for r in chunk[chunk['business_id'].apply(lambda x: x in business_ids)].values]
# reviews = []
# for chunk in review_reader:
#     new_chunk = chunk[chunk['business_id'].apply(lambda x: x in business_ids)]
#     print(chunk.shape)
#     print(new_chunk.shape)
#     print(type(new_chunk.values))
#     print(len(new_chunk.values))
print()
print(type(reviews))
print(len(reviews))
print()

reviews = pd.DataFrame(reviews)
print(reviews.shape)
print(reviews.head())

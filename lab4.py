import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

business = pd.read_json('JSON/business.json', lines=True)

print(business.shape)
print(business.head())
print(business.info())

drop_cols = ["address", "attributes", "hours", "is_open", "latitude", "longitude", "name", "postal_code"]

business = business.drop(drop_cols, axis=1)

print(business.head())
print(business.categories[0])
print(type(business.categories[0]))
print(business.categories[0][0])
business['categories'] = business['categories'].str.split(', ')
print(business.categories[0])
print(business['categories'].head())

print(business.shape)
print(pd.isna(business['categories']).sum())
business = business[~pd.isna(business['categories'])]
print(business.head())
print(business.shape)
print(pd.isna(business['categories']).sum())

business = business.loc[business['categories'].apply(lambda x: 'Restaurants' in x), :]

# Збережіть потрібний business ID у файл
italian_pizza = business.loc[business['categories'].apply(lambda x: 'Pizza' in x or 'Italian' in x), :]
print(italian_pizza.head())
print(italian_pizza.shape)

# print(italian_pizza.info())
italian_pizza.to_csv(path_or_buf='italian_pizza.csv', index=False, columns=('business_id', 'review_count', 'stars', 'state'))

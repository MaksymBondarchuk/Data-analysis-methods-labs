import numpy as np
import pandas as pd
import matplotlib.pyplot

business = pd.read_json('JSON/business.json', lines=True)

print(business.shape)
print(business.head())
print(business.info())

# drop_cols = ["address", "attributes", "hours", "is_open", "latitude", "longitude", "postal code"]
# # del business[drop_cols]
# business = business.drop(drop_cols, axis=1)
# # business = business.drop(["address", "attributes"], axis=1)
# print(business.head())
# print(business.info())
# print(business['categories'])
# category_counts = business['categories'].apply(pd.Series).stack().reset_index(drop=True).value_counts().nlargest(20)
# print(category_counts)
# print(type(category_counts))
# category_counts.plot(kind='bar')

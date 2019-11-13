import numpy as np
import pandas as pd

pets = pd.DataFrame({'sex': np.array(['M', 'M', 'F', 'M', 'F', 'F', 'F', 'M', 'F', 'M']),
                     'age': np.array([21, 45, 23, 56, 47, 70, 34, 30, 19, 62]),
                     'pets': np.array([['cat', 'dog'],
                                       ['hamster'],
                                       ['cat', 'gerbil'],
                                       ['fish', 'hamster', 'gerbil'],
                                       ['cat'],
                                       ['dog'],
                                       ['dog'],
                                       ['cat'],
                                       ['rabbit', 'cat'],
                                       ['dog']])})

# Task 1
print('Task 1')
print(pets)
print(pets.loc[pets['age'].idxmin()]['sex'])

# Task 2
print('\nTask 2')
pets['num_pets'] = pets['pets'].str.len()
print(pets)

# Task 3
print('\nTask 3')
pet_series = pets['pets'].apply(pd.Series).stack().reset_index(drop=True)
print(pet_series)
print(pet_series.value_counts()[0])

# Task 4
print('\nTask 4')
# test = pets[pets['pets'].apply(lambda p: 'dog' in p).reset_index(drop=True)]
# print(test)
# print(test['age'].mean())
print(pets[pets['pets'].apply(lambda p: 'dog' in p).reset_index(drop=True)]['age'].mean())

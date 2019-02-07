import random
import numpy as np
# list = np.random.randint(low=1, high=101, size=5)
# print(list)
# sort_list = np.sort(list)
# print(sort_list)
# print(len(list))
# print(type(list))

resultList=random.sample(range(1,101),100)
print(resultList)
print(type(resultList))
list = np.array(resultList)
print(list)
print(type(list))
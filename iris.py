import sys
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

iris = pd.read_csv("iris.csv", \
                   names=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth', 'Species'])


Iris_setos = iris.iloc[0:50]
Iris_versicolor = iris.iloc[51:100]
Iris_virginica = iris.iloc[101:150]


data = [["꽃받침의 길이", np.mean(Iris_setos['SepalLength'].values.tolist()), np.var(Iris_setos['SepalLength'].values.tolist())],
        ["꽃받침의 너비", np.mean(Iris_setos['SepalWidth'].values.tolist()), np.var(Iris_setos['SepalWidth'].values.tolist())],
        ["꽃잎의 길이", np.mean(Iris_setos['PetalLength'].values.tolist()), np.var(Iris_setos['PetalLength'].values.tolist())],
        ["꽃잎의 너비", np.mean(Iris_setos['PetalWidth'].values.tolist()), np.var(Iris_setos['PetalWidth'].values.tolist())]]

df = pd.DataFrame(data, columns=['항목', '평균', '분산'])
print("\n\nIris_setos\n")
print(df)
print("-----------------------------------\n")


attribute_list = []
attribute_list.append(iris['SepalLength'].values.tolist())
attribute_list.append(iris['SepalWidth'].values.tolist())
attribute_list.append(iris['PetalLength'].values.tolist())
attribute_list.append(iris['PetalWidth'].values.tolist())

data = [["꽃받침의 길이", np.mean(attribute_list[0]), np.var(attribute_list[0])],
        ["꽃받침의 너비", np.mean(attribute_list[1]), np.var(attribute_list[1])],
        ["꽃잎의 길이", np.mean(attribute_list[2]), np.var(attribute_list[2])],
        ["꽃잎의 너비", np.mean(attribute_list[3]), np.var(attribute_list[3])]]

df = pd.DataFrame(data, columns=['항목', '평균', '분산'])
print("전체\n")
print(df, "\n-----------------------------------\n")
print("1. 꽃받침의 길이\n2. 꽃받침의 너비\n3. 꽃잎의 길이\n4. 꽃잎의 너비\n")

# a, b = map(int, sys.stdin.readline().split())
# plt.plot(attribute_list[a-1], attribute_list[b-1], 'ro')
# plt.show()

fig = plt.figure(figsize=(5, 5))
ax = fig.gca(projection='3d')


ax.scatter(attribute_list[0], attribute_list[1], attribute_list[2], marker='o', color = 'orange')
ax.scatter(attribute_list[0], attribute_list[1], attribute_list[2], marker='o', color = 'purple')
ax.scatter(attribute_list[0], attribute_list[1], attribute_list[2], marker='o', color = 'orange')

plt.show()
import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from copy import deepcopy

iris = pd.read_csv("iris.csv", \
                   names=['SepalLength', 'SepalWidth', 'PetalLength', 'PetalWidth'])

colors = ['blue', 'orange', 'green']


def euclidean_distance(a, b):
  return math.sqrt(sum([(x - y) ** 2 for x, y in list(zip(a, b))]))


k = 3
x = iris['PetalLength'].values.tolist()
y = iris['PetalWidth'].values.tolist()

plt.xlabel('petal length (cm)')
plt.ylabel('petal width (cm)')



# 랜덤으로 초기 중심값 설정
# centroids_x = np.round(np.random.uniform(min(x), max(x), k),3)  # 리스트 x에서 최솟값, 최댓값 내에서 k(3)개의 랜덤값을 뽑아옴
# centroids_y = np.round(np.random.uniform(min(y), max(y), k),3)  # 리스트 y에서 최솟값, 최댓값 내에서 k(3)개의 랜덤값을 뽑아옴

centroids_x = [6.552, 3.484, 2.141]
centroids_y = [1.351, 0.585, 1.004]
# [6.552 3.484 2.141][0.95 0.947 2.481]
# [6.143 2.74  1.158][1.351 0.585 1.004]
# [6.333 2.195 1.895][1.849 1.14 1.29]
centroids = list(zip(centroids_x, centroids_y))  # 초기 중심값 좌표 생성

# 모든 petal 의 길이와 너비 좌표 생성
petal_length_width = np.array(list(zip(x, y)))

centroids_old = np.zeros(np.shape(centroids))
labels = np.zeros(len(iris))
error = np.zeros(k)
item = 0

# 초기 error 값 세팅
for i in range(k):
  error[i] = euclidean_distance(centroids_old[i], centroids[i])

# error가 0이 될때(거리가 똑같아짐)까지
while error.all() != 0:
  for i in range(len(petal_length_width)):  # 모든 데이터를 순회
    distances = np.zeros(k)
    for j in range(k):
      distances[j] = euclidean_distance(petal_length_width[i], centroids[j])  # 3개의 중심점과 각각 거리 계산
    labels[i] = np.argmin(distances)  # 그 중 최소값의 인덱스를 저장 (0, 1, 2)

  object = []
  points = []
  average_distance = []

  centroids_old = deepcopy(centroids)

  for i in range(k):
    total_distance = 0
    count = 0
    for j in range(len(petal_length_width)):  # 모든 데이터들을 순회
      item += 1
      if labels[j] == i:
        count += 1
        points.append(petal_length_width[j])  # 각 클래스에 속한 데이터들을 골라 points에 저장
        total_distance += euclidean_distance(petal_length_width[j], centroids[i])  # 중심값과 각 데이터들의 거리 합
    average_distance.append(round(total_distance / count , 3))
    centroids[i] = np.mean(points, axis=0)  # 클래스 별로 평균, 새로운 중심값으로 설정

  print(average_distance)

  for i in range(k):
    error[i] = euclidean_distance(centroids_old[i], centroids[i])  # 기존 중심값과 현재 중심값의 거리 계산 (0이면 루프 탈출)

  # 그래프로 나타내기
  new_x = []
  new_y = []
  for i in centroids:
    new_x.append(i[0])
    new_y.append(i[1])
  
  for i in range(k):
    points = np.array([petal_length_width[j] for j in range(len(petal_length_width)) if labels[j] == i])
    plt.scatter(points[:, 0], points[:, 1], c=colors[i], alpha=0.5)
  plt.scatter(new_x, new_y, c='red', s=100)
  plt.xlabel('petal length (cm)')
  plt.ylabel('petal width (cm)')
  plt.show()
  
  


print('\n\n\n', centroids_x, centroids_y)

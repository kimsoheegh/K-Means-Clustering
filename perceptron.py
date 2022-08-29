import numpy as np
import random

# 퍼셉트론 AND 게이트
data = [[1,0,0], [1,0,1], [1,1,0], [1,1,1]]

target = [0, 0, 0, 1]
learning_rate = 0.1

w1 = 0.5
w2 = 0.3
w3 = 0.2


while True :

  count = 0
  i = 0
  while i<4:
    ret = np.array(data[i], ndmin=2)
    weight = np.array(
      [
        [w1],
        [w2],
        [w3]
      ]
    )

    sum = 0
    for x_value in ret:
      array = x_value @ weight
      sum += array

    if (sum < 0):
      output = 0;
    else:
      output = 1

    if(output!=target[i]):
      count = count+1


    w1 = ((target[i] - output) * learning_rate * data[i][0]) + w1
    w2 = ((target[i] - output) * learning_rate * data[i][1]) + w2
    w3 = ((target[i] - output) * learning_rate * data[i][2]) + w3

    i=i+1

  print("\n\n\n")
  if (count/4 < 0.0000001 or count == 0):
    print('weight : ', w1, ', ', w2, ', ', w3)
    print(count / 4)
    break
  print('weight : ', w1, ', ', w2, ', ', w3)
  print(count/4)
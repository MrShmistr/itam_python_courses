# -*- coding: utf-8 -*-
"""homework_1_1_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AfM2JJ7VCX5E06DyBNbIaHcESTGB7Ley
"""

numbers = input().split()
int_lst = [int(x) for x in numbers]
neg = 0
eigh = 0
chet = 0
for x in int_lst:
  if x < 0:
    neg +=1
  elif x > 8:
    eigh += 1
  elif (x % 2) == 0:
    chet += 1
print(neg, eigh, chet)
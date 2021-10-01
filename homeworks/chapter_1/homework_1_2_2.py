# -*- coding: utf-8 -*-
"""homework_1_2_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AfM2JJ7VCX5E06DyBNbIaHcESTGB7Ley
"""

numbers = int(input())
offline = 0
online = 0
unknown = 0
for x in range(numbers):
  user = input().split()
  true = user.count('True')
  false = user.count('False')
  if true == 1 and false == 0:
    offline += 1
  elif true == 0 and false == 1:
    online += 1
  elif true >= 1 and false >= 1:
    four_element = user[3]
    if 'True' in four_element:
      offline += 1
    elif 'False' in four_element:
      online += 1
    else:
      unknown += 1
print(offline, online, unknown)
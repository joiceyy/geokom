#!/usr/bin/env python
# coding: utf-8

# In[1]:


def get_grade_score(score):
  grade = 'E'
  if (score>=80):
    grade = 'A'
  elif (score>=75):
    grade = 'A-'
  elif (score>=70):
    grade = 'B+'
  elif (score>=65):
    grade = 'B'
  elif (score>=60):
    grade = 'B-'
  elif (score>=55):
    grade = 'C+'
  elif (score>=50):
    grade = 'C'
  elif (score>=45):
    grade = 'D'
  return grade

print(get_grade_score(98))
print(get_grade_score(79))
print(get_grade_score(73))
print(get_grade_score(68))
print(get_grade_score(64))
print(get_grade_score(56))
print(get_grade_score(52))
print(get_grade_score(49))
print(get_grade_score(42))
print(get_grade_score(38))
print(get_grade_score(20))
# A = 80
# A- = 75
# B+ = 70
# B = 65
# B- = 60
# C+ = 55
# C = 50
# D = 45
# E = 35


# In[ ]:





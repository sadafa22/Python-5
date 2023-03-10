# -*- coding: utf-8 -*-
"""Q2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N0XH5PphZUtx9G8NiZdt1dcOsG_VXAPv
"""

class SentimentLexicon():
  def __init__(self,D,File1,File2):
    self.D = D
    self.File1 = File1
    self.File2 = File2
  
  def reader(self,File1,File2):
    n = (self.File1).readlines()
    p = (self.File2).readlines()


    for i in n[31:]:
      if i in (self.D):
        self.D[i]-=1
      else:
        self.D[i] = -1
    
    for i in p[30:]:
      if i in (self.D):
        self.D[i]+=1
      else:
        self.D[i] = 1
    
    return self.D

class Classifier():
  def __init__(self,dictionary,str1):
    self.dictionary = dictionary
    self.str1 = str1
  
  def classify(self,str1):
    count = 0
    
    for i in str1:
      if i == '.':
        str2=str1.replace(".",'') 
      elif i == ',':
        str2=str1.replace(",",'')
      elif i == '!':
        str2=str1.replace("!",'')
    
    o = str2.split()
    
    l = list(self.dictionary.keys())
    nlist = []
    Plist = []
    Nlist = []
    count = 0

    for i in l:
      nlist.append(i.strip())
    
    for i in nlist[4782:]:
      Plist.append(i)
    for i in nlist[:4782]:
      Nlist.append(i)

    for i in o:
      if i in Plist:
        count = count + 1

    for i in o:
      if i in Nlist:
        count = count - 1
      if i == 'not':
        count = 1
        break
      
    u = {}
    u['text'] = str1
    u['sentiment'] = 0
    if count < 0:
      u['sentiment'] = -1
    elif count > 0:
      u['sentiment'] = 1
    elif count == 0:
      u['sentiment'] = 0
    
    return u

f1 = open("negative-words.txt")
f2 = open("positive-words.txt")
d = {}

S = SentimentLexicon(d,f1,f2)
H = S.reader(f1,f2)
#print(H)

C = Classifier(H,"I love Spyder.")
t = C.classify("I love spyder.")
print(t)

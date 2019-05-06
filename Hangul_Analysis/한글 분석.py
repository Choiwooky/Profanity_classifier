#!/usr/bin/env python
# coding: utf-8

# ## https://konlpy-ko.readthedocs.io/ko/v0.5.1/#start 참고

# In[ ]:


pip install konlpy


# In[1]:


from konlpy.tag import Okt #윈도우 사용가능 태깅 중 제일 빠름
from konlpy.utils import pprint


# In[2]:


okt = Okt()


# In[3]:


pprint(okt.morphs(u'장대한 생물 진화사를 치킨으로 정리해버리는 씹좆간쉨ㅋㅋㅋㅋ'))


# In[4]:


pprint(okt.nouns(u'장대한 생물 진화사를 치킨으로 정리해버리는 씹좆간쉨ㅋㅋㅋㅋ'))


# In[5]:


pprint(okt.phrases(u'장대한 생물 진화사를 치킨으로 정리해버리는 씹좆간쉨ㅋㅋㅋㅋ'))


# In[6]:


pprint(okt.pos(u'장대한 생물 진화사를 치킨으로 정리해버리는 씹좆간쉨ㅋㅋㅋㅋ'))


# In[7]:


pprint(okt.pos(u'장대한 생물 진화사를 치킨으로 정리해버리는 씹좆간쉨ㅋㅋㅋㅋ',norm = True))


# In[8]:


pprint(okt.pos(u'장대한 생물 진화사를 치킨으로 정리해버리는 씹좆간쉨ㅋㅋㅋㅋ',stem = True))


# In[9]:


pprint(okt.pos(u'장대한 생물 진화사를 치킨으로 정리해버리는 씹좆간쉨ㅋㅋㅋㅋ',norm = True, stem = True))


# In[10]:


pprint(okt.pos(u'장대한 생물 진화사를 치킨으로 정리해버리는 씹좆간쉨ㅋㅋㅋㅋ',norm = True, stem = True, join = True))


# In[11]:


from konlpy.tag import Kkma # 좀 느리지만 정확한 분석


# In[12]:


kkma = Kkma()


# In[13]:


pprint(kkma.morphs(u'장대한 생물 진화사를 치킨으로 정리해버리는 씹좆간쉨ㅋㅋㅋㅋ'))


# In[14]:


pprint(kkma.nouns(u'장대한 생물 진화사를 치킨으로 정리해버리는 씹좆간쉨ㅋㅋㅋㅋ'))


# In[15]:


pprint(kkma.pos(u'장대한 생물 진화사를 치킨으로 정리해버리는 씹좆간쉨ㅋㅋㅋㅋ'))


# In[ ]:


pip install hgtk


# ### https://github.com/bluedisk/hangul-toolkit 참고

# In[16]:


import hgtk
import numpy as np


# ###### 초성, 중성, 종성 리스트를 자모 리스트로 합본

# In[17]:


jong_list = hgtk.const.JONG[1:]
jamo = (hgtk.const.CHO,hgtk.const.JOONG,tuple(jong_list))
jamo[0].index("ㅅ")


# In[19]:


# 연습용 임시 문장
#tmp = kkma.pos(u'장대한 생물 진화사를 치킨으로 정리해버리는 씹ㅈ간쉨ㅋㅋㅋㅋ')
tmp = kkma.pos(u'ㅈ간이 미안해ㅠㅠ')
analy_sentence = []
for i in tmp:
    if i[1] == 'NNG' or i[1] == 'UN':
        analy_sentence.append(i[0])
print("raw_list :",analy_sentence)
processed_sentence = []
for word in analy_sentence:
    processed_sentence.append(hgtk.text.decompose(word))
pprint(processed_sentence)
decom_sentence = "".join(processed_sentence)
print("글자 수 :",decom_sentence.count('ᴥ'))


# ## 1번 방법 np.shape(글자수, 3(초성,중성,종성), 총 28자리)

# In[20]:


final_data = np.zeros((decom_sentence.count('ᴥ'),3,28))
count, i = 0, 0
print(decom_sentence)
for c in decom_sentence:
    if c == 'ᴥ':
        count += 1
        i = 0
        continue
    final_data[count,i,jamo[i].index(c)] = 1
    i += 1
final_data


# ## 2번 방법 np.shape(글자수,각 자모 인덱스 3개(초성, 중성, 종성))

# In[22]:


final_data = np.zeros((decom_sentence.count('ᴥ'),3))
count, i = 0, 0
print(decom_sentence)
for c in decom_sentence:
    if c == 'ᴥ':
        count += 1
        i = 0
        continue
    final_data[count,i] = jamo[i].index(c)+1 #공백과 첫번째 인덱스를 구분하기 위해서
    i += 1
final_data


# In[ ]:





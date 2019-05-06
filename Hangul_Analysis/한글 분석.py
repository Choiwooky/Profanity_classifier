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


pprint(okt.pos(u'개씹 진부한 닳고닳은 레파토리라 존나 지루한데 힛갤이라 참고봤더만 끝까지 걍 식상하네. 모든컷이 다 어디서 본거 씹아류 수준인데 그냥 김치문화수준이 이거뜨면 우르르 베끼고 따라하고 똑같은거만 찍어내면 개돼지마냥 좋다고 쳐 보고 걍 종특인듯'))


# In[12]:


from konlpy.tag import Kkma # 좀 느리지만 정확한 분석


# In[13]:


kkma = Kkma()


# In[14]:


pprint(kkma.morphs(u'장대한 생물 진화사를 치킨으로 정리해버리는 씹좆간쉨ㅋㅋㅋㅋ'))


# In[15]:


pprint(kkma.nouns(u'장대한 생물 진화사를 치킨으로 정리해버리는 씹좆간쉨ㅋㅋㅋㅋ'))


# In[16]:


pprint(okt.pos(u'장대한 생물 진화사를 치킨으로 정리해버리는 씹좆간쉨ㅋㅋㅋㅋ'))


# In[17]:


pprint(okt.pos(u'개씹 진부한 닳고닳은 레파토리라 존나 지루한데 힛갤이라 참고봤더만 끝까지 걍 식상하네. 모든컷이 다 어디서 본거 씹아류 수준인데 그냥 김치문화수준이 이거뜨면 우르르 베끼고 따라하고 똑같은거만 찍어내면 개돼지마냥 좋다고 쳐 보고 걍 종특인듯'))


# In[ ]:





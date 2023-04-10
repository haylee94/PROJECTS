# 네이버 API에서 추출한 리뷰데이터로 트렌드 키워드 분석(자연어처리)

import matplotlib as mpl
import matplotlib.pyplot as plt
plt.style.use('seaborn-white')
import matplotlib.font_manager as fm
import pandas as pd # pandas 모듈 로드
from pandas import json_normalize
import json  # json 모듈 로드
from collections import Counter
from wordcloud import WordCloud



# 한국어 자연어처리 konlpy, 형태소 분석기 Mecab 설치
!set -x \
&& pip install konlpy \
&& curl -s https://raw.githubusercontent.com/konlpy/konlpy/master/scripts/mecab.sh | bash -x


# 형태소분석기
from konlpy.tag import Mecab
tokenizer = Mecab()

# json파일, 불러오기
json_file_path="/Users/Haylee/Desktop/AIB/cp1/CHECK_IN/SEOUL/0. data/서울맛집_naver_blog.json" # 파일로드 (파일명 : NY.GDP.MKTP.CD.json )

with open(json_file_path,'r') as j:
    contents=json.loads(j.read())  # open : r - 읽기모드, w-쓰기모드, a-추가모드 

df = json_normalize(contents) #Results contain the required data
print(df)

df['description'] = df['description'].str.replace("/", " ")

# 결측값 확인, 제거
df['description'].isnull().sum()
df= df.dropna()


# 형태소 분석을 이용한 명사분석
nouns = []
for review in df['description']:
  for noun in tokenizer.nouns(review):
    nouns.append(noun)

# 불용어사전 만들기 -> 사전내용 추가적 관리 필요
stop_words = "맛집 도 는 다 의 가 이 은 한 에 하 고 을 를 인 듯 과 와 네 들 듯 지 임 게"
stop_words = stop_words.split(' ')

# 불용어를 제외한 형태소 분석 수행
nouns = []
for review in df['description']:
  for noun in tokenizer.nouns(review):
    if noun not in stop_words:
      nouns.append(noun)


# 단어 빈도수 측정
nouns_counter = Counter(nouns)
top_nouns = dict(nouns_counter.most_common(50))


# 워드클라우드 설치
!pip install wordcloud


wc = WordCloud(background_color='white', font_path='./font/NanumBarunGothic.ttf')
wc.generate_from_frequencies(top_nouns)

# 워드클라우드 시각화 할 때는 이미지 시각화 함수인 imshow() 함수를 사용
figure = plt.figure(figsize=(12,12))
ax = figure.add_subplot(1,1,1)
ax.axis('off')
ax.imshow(wc)
plt.show()

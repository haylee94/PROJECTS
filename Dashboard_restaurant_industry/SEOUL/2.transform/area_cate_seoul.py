# 수집한 데이터 전처리

import pandas as pd
import numpy as np


def get_area_cate_seoul():
    """
    정제된 데이터를 불러오는 함수
    """
    # csv파일, 데이터 구분을 ',' 로 해둔 파일.
    df = pd.read_csv('/Users/Haylee/Desktop/AIB/cp1/CHECK_IN/SEOUL/0. data/소상공인시장진흥공단_상가(상권)정보_서울_202209.csv')

    return df


def data_transform(df):
    # 음식점 데이터만 사용, 특정 컬럼만 사용
    df.loc[df['상권업종대분류명'] == '음식']
    df[['상호명', '상권업종중분류명', '상권업종소분류명', '표준산업분류명', '행정동명', '위도', '경도']]

    # 카테고리 데이터 묶어주기 -> 코사인유사도 사용
    df['cate_mix'] = df['cate_1'] + df['cate_2'] +  df['cate_3']
    df['cate_mix'] = df['cate_mix'].str.replace("/", " ")

    # 결측값 확인, 제거
    df['cate_mix'].isnull().sum()
    df.dropna()
    df.reset_index(drop=True)

    return df


def cate_rename_seoul():
    df = df.rename(columns = {"상호명" : "name", 
                        "상권업종중분류명" : "cate_1",
                        "상권업종소분류명" : "cate_2",
                        "표준산업분류명" : "cate_3",
                        "행정동명" : "dong",
                        "위도" : "lon",
                        "경도" : "lat",
                        "cate_mix" : "cate_mix"
                        })
    return df




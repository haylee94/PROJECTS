# 수집한 데이터 전처리

import pandas as pd
import numpy as np


def get_area_pop_seoul():
    """
    정제된 데이터를 불러오는 함수
    """
    # csv파일, 데이터 구분을 ',' 로 해둔 파일.
    df = pd.read_csv('/Users/Haylee/Desktop/AIB/cp1/CHECK_IN/SEOUL/0. data/202212_202212_주민등록인구및세대현황_월간.csv', encoding='CP949')

    return df


def area_rename():
    df = df.rename(columns = {"행정구역" : "행정구역", 
                        "2022년12월_총인구수" : "총인구수",
                        "2022년12월_세대수" : "세대수",
                        "2022년12월_세대당 인구" : "세대당인구",
                        "2022년12월_남자 인구수" : "남자인구수",
                        "2022년12월_여자 인구수" : "여자인구수",
                        "2022년12월_남여 비율" : "남여비율",
                        })
    return df





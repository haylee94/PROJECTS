import pandas as pd
import numpy as np
from plotnine import *
import folium # 지도표현을 위해
from folium.plugins import MarkerCluster
from flask import Flask, render_template # 웹페이지 연결 위해


app = Flask(__name__)

@app.route('/map')
def map(request):
    start_coords = (37.5,127.1) # 경도, 위도(시작위치)
    folium_map = folium.Map(location=start_coords, zoom_start=14)
    maps=folium_map._repr_html_()  #지도를 템플릿에 삽입하기위해 iframe이 있는 문자열로 반환 (folium)
    return render_template(request,'../templates/index.html',{'map' : maps})


# 전처리 후 적재한 데이터 불러오기(postgresql 연결)
df = pd.read_csv('/Users/Haylee/Desktop/AIB/cp1/test/row.csv') 

# 상호명으로는 업종 구분이 어려운 경우가 있어 name_cate컬럼을 생성
df["name_cate"] = df["name"] + "(" + df["cate_2"] + ")"
df

# {'name_cate':[lon경도, lat위도]} 형태로 만들기 -> folium활용
df= df[['name_cate','lon','lat']]
df

# df를 dictionary 변경
df_dict = df.set_index('name_cate').T.to_dict('list')
df_dict

# 각각의 마커를 마커클러스터에 추가
m1 = folium.Map(location=(37.5,127.1), zoom_start=14) # 경도, 위도(시작위치)

marker_cluster = MarkerCluster().add_to(m1)

for msg, loc in df_dict.items():
    print(msg, loc)
    folium.Marker(location = loc, popup = folium.Popup(msg, max_width=200)).add_to(marker_cluster)


if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template
import pandas as pd
import folium # 지도표현을 위해
from folium.plugins import MarkerCluster
app = Flask(__name__)


@app.route('/map')
def create_map():
    df = pd.read_csv('/Users/Haylee/Desktop/AIB/cp1/CHECK_IN/SEOUL/0. data/area_seoul.csv') # 전처리 후 적재한 데이터 불러오기(postgresql 연결 보완)
    
    # 상호명으로는 업종 구분이 어려운 경우가 있어 name_cate컬럼을 생성
    df["name_cate"] = df["name"] + "(" + df["cate_2"] + ")"

    # {'name_cate':[lon경도, lat위도]} 형태로 만들기 -> folium활용
    df= df[['name_cate','lon','lat']]

    # df를 dictionary 변경
    df_dict = df.set_index('name_cate').T.to_dict('list')

    # 각각의 마커를 마커클러스터에 추가
    m1 = folium.Map(location=(37.5,127.1), zoom_start=14) # 경도, 위도(시작위치)

    marker_cluster = MarkerCluster().add_to(m1)

    for msg, loc in df_dict.items():
        print(msg, loc)
        folium.Marker(location = loc, popup = folium.Popup(msg, max_width=200)).add_to(marker_cluster)

    return m1



@app.route('/')
def render_the_map():
    return render_template('the_map.html')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Blueprint, request, jsonify, render_template
import pickle
import numpy as np
import pandas as pd

bp = Blueprint('predict', __name__, url_prefix='/predict')
model = pickle.load(open('ML배포/model/model.pkl', 'rb'))


@bp.route('/', methods=['POST','GET'])
def pred():
    if request.method == 'POST':
               
        arr = [{"나이": request.form["나이"],
            "성별코드": request.form["성별코드"],
            "담보": request.form["담보"]]


        # data1 = request.form["id"]
        # data2 = request.form["amount_tsh"]
        # data3 = request.form["construction_year"]
      
        # arr = np.array([[data1, data2, data3]])

        X_test = pd.DataFrame(arr)
        
        # x = request.form
        # for key, value in x.items:
        #     X_test[key] = value
        prediction = model.predict(X_test)
        
    return render_template('predict.html', data = prediction)
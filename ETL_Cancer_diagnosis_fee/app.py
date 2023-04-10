from flask import Flask, request, jsonify, render_template
import pickle


# create flask app
app = Flask(__name__)

# load the pickle model
model = pickle.load(open("model.pkl", "rb"))

@app.route("/")
def Home():
    return render_template('index.html')

@app.route("/predict", methods = ["GET", "POST"])
def predict(x):
    prediction = model.predict(x)
    return render_template('index.html', prediction_text = "예상 가입금액의 평균 {}".format(prediction))

if __name__ == "__main__":
    app.run(debug=True)

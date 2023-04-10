import pandas as pd
from sklearn.preprocessing import StandardScaler
from category_encoders import OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# load the csv file
df = pd.read_csv('project_finaldata.csv')

# data select, df.describe()=>25%기준 삭제
df = df[df['가입금액'] != 0]
df = df[df['가입금액'] < 13000000]

X = df[["나이", "성별코드"]]
y = df["가입금액"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# scaling
od = OrdinalEncoder()
X_train = od.fit_transform(X_train)
X_test = od.transform(X_test)

# instantiate the model, fit
rf = RandomForestClassifier(
    random_state=42, criterion='entropy', oob_score=True, n_jobs=-1, max_depth=10, n_estimators = 400, min_samples_split=8, min_samples_leaf=8)
rf.fit(X_train, y_train)

# make pickle file of our model
pickle.dump(rf, open("model.pkl", "wb"))
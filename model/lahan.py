import pandas as pd 
from sklearn.preprocessing import LabelEncoder 
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('kebaran lahan.csv')


X = df.drop(['Kebakaran Lahan'],axis=1)
y = df['Kebakaran Lahan']


label = LabelEncoder()
for i in X.columns:
    X[i] = label.fit_transform(X[i])
    


model = DecisionTreeClassifier(criterion='entropy',max_depth=3)

model.fit(X,y)


def prediksi(input):
    feature = pd.DataFrame(columns=[
    'Tanggal',
    'Daerah', 
    'Kelembaban Tanah', 
    'Suhu Udara', 
    'Kecepatan Angin', 
    'Curah Hujan', 
    'Vegetasi Kering',
    ])
    feature.loc[len(feature)] = input
    for i in feature.columns:
        feature[i] = label.fit_transform(feature[i])
    predict = model.predict(feature)
    return predict

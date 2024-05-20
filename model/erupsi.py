import pandas as pd 
from sklearn.preprocessing import LabelEncoder 
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('erupsi.csv')


X = df.drop(['Prediksi'],axis=1)
y = df['Prediksi']


label = LabelEncoder()
for i in X.columns:
    X[i] = label.fit_transform(X[i])
    


model = DecisionTreeClassifier(criterion='entropy',max_depth=3)

model.fit(X,y)


def prediksi(input):
    feature = pd.DataFrame(columns=[
    'Tanggal',
    'Daerah',
    'Aktivitas Seismik',
    'Deformasi Tanah',
    'Emisi SO2',
    'Emisi CO2',
    ])
    feature.loc[len(feature)] = input
    for i in feature.columns:
        feature[i] = label.fit_transform(feature[i])
    predict = model.predict(feature)
    return predict
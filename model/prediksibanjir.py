import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

df = pd.read_csv('banjir.csv')
df = df.drop(['No','Daerah'],axis=1)

X = df.drop(['kerentanan'], axis=1)
y = df['kerentanan']

a = ['Tekstur tanah','Penggunaan Lahan','Curah Hujan']
label = LabelEncoder()
for i in a:
    X[i] = label.fit_transform(df[i])

model = DecisionTreeClassifier(criterion='entropy',max_depth=4)
model.fit(X,y)

def prediksi(input):
    feature = pd.DataFrame(columns=[
        'Tekstur tanah',
        'kemiringan lereng',
        'Penggunaan Lahan',
        'Kelembaban Udara',
        'Tekanan Udara',
        'Suhu Udara',
        'Curah Hujan',
        ])
    feature.loc[len(feature)] = input
    for i in feature.columns:
        feature[i] = label.fit_transform(feature[i])
    predict = model.predict(feature)
    return predict


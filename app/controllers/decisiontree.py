from fileinput import filename
from app.models.data_tk import data_tipekepribadian
from app.controllers import soalController
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pickle

data = pd.read_csv("app\controllers\FIX DATASET.data")

label_atribut = data[['dominance', 'influance', 'steadiness', 'compliance']]
label_hasil = data['tipe_kepribadian']

x_train, x_test, y_train, y_test = train_test_split(label_atribut, label_hasil, test_size=0.1)

hasil = DecisionTreeClassifier(criterion='entropy', max_depth=12, max_leaf_nodes=201, random_state=300)
hasil.fit(x_train, y_train)

# skor = hasil.score(x_test,y_test)

# print(skor)
    

def get_xtest():

    x_test['tipe_kepribadian'] = y_test.values

    xtest = x_test.values

    return xtest


def get_akurasi():
    # from sklearn.metrics import classification_report

    # Y_hasil = hasil.predict(x_test)

    # hasil_report = hasil.score(x_test, y_test)

    skor = pickle.load(open('app\controllers\skor_testing.pkl', 'rb'))

    return skor
import pickle
from app.controllers import soalController
import numpy as np
from app.models.data_tk import data_tipekepribadian
from sklearn.tree import _tree


def index():
    model = pickle.load(open('app\controllers\model.pkl', 'rb'))
    return model

def klasifikasipekerjaan():
    deskripsi_hasil = data_tipekepribadian.query.all()
    bagian_dominance = soalController.bagian_dominance()
    bagian_influance = soalController.bagian_influance()
    bagian_steadiness = soalController.bagian_steadiness()
    bagian_compliance = soalController.bagian_compliance()

    model = index()

    arr = np.array([[bagian_dominance, bagian_influance, bagian_steadiness, bagian_compliance]])
    klasifikasi = model.predict(arr)

    for deskripsi_hasil in deskripsi_hasil:
        if deskripsi_hasil.tipe_kepribadian == klasifikasi:
            hasil_klasifikasi = deskripsi_hasil.rekomendasi_pekerjaan

    return hasil_klasifikasi

def get_rules(tree, feature_names, class_names):
    tree_ = tree.tree_
    feature_name = [
        feature_names[i] if i != _tree.TREE_UNDEFINED else "undefined!"
        for i in tree_.feature
    ]

    paths = []
    path = []
    
    def recurse(node, path, paths):
        
        if tree_.feature[node] != _tree.TREE_UNDEFINED:
            name = feature_name[node]
            threshold = tree_.threshold[node]
            p1, p2 = list(path), list(path)
            p1 += [f"({name} <= {np.round(threshold, 3)})"]
            recurse(tree_.children_left[node], p1, paths)
            p2 += [f"({name} > {np.round(threshold, 3)})"]
            recurse(tree_.children_right[node], p2, paths)
        else:
            path += [(tree_.value[node], tree_.n_node_samples[node])]
            paths += [path]
            
    recurse(0, path, paths)

    # sort by samples count
    samples_count = [p[-1][1] for p in paths]
    ii = list(np.argsort(samples_count))
    paths = [paths[i] for i in reversed(ii)]
    
    rules = []
    for path in paths:
        rule = "if "
        
        for p in path[:-1]:
            if rule != "if ":
                rule += " and "
            rule += str(p)
        rule += " then "
        if class_names is None:
            rule += "response: "+str(np.round(path[-1][0][0][0],3))
        else:
            classes = path[-1][0][0]
            l = np.argmax(classes)
            rule += f"class: {class_names[l]} (proba: {np.round(100.0*classes[l]/np.sum(classes),2)}%)"
        rule += f" | based on {path[-1][1]:,} samples"
        rules += [rule]
        
    return rules

def extract_rules():
    model = index()
    rules = get_rules(model, feature_names=['dominance','influance','steadiness','compliance'], class_names=['dominance steadiness influance', 'steadiness compliance dominance', 'steadiness dominance', 'compliance dominance influance', 'influance dominance compliance', 'dominance compliance influance', 'influance steadiness dominance', 'compliance dominance', 'compliance influance steadiness', 'dominance steadiness compliance', 'compliance influance dominance', 'dominance', 'compliance steadiness', 'influance compliance dominance', 'steadiness dominance compliance', 'influance dominance steadiness', 'steadiness compliance influance', 'steadiness', 'dominance influance steadiness', 'dominance influance compliance', 'influance dominance', 'influance compliance steadiness', 'steadiness influance', 'steadiness influance dominance', 'compliance dominance steadiness', 'influance', 'dominance compliance steadiness', 'compliance steadiness dominance', 'compliance steadiness influance', 'steadiness compliance', 'steadiness influance compliance', 'compliance influance', 'steadiness dominance influance', 'dominance steadiness', 'influance steadiness compliance', 'compliance', 'dominance compliance', 'influance steadiness', 'influance compliance', 'dominance influance'])

    return rules
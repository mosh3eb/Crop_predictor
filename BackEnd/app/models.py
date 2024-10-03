import pickle

decision_tree_model = pickle.load(open("../Models/DecisionTree.pkl", "rb"))
logistic_regression_model = pickle.load(open("../Models/LogisticRegression.pkl", "rb"))
nb_classifier_model = pickle.load(open("../Models/NBClassifier.pkl", "rb"))
random_forest_model = pickle.load(open("../Models/RandomForest.pkl", "rb"))

models = {
    "decision_tree": decision_tree_model,
    "logistic_regression": logistic_regression_model,
    "nb_classifier": nb_classifier_model,
    "random_forest": random_forest_model,
}
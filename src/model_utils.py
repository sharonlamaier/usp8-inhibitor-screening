import pickle
def load_model(pkl):
    with open(pkl, 'rb') as file:
        loaded_model = pickle.load(file)
    return loaded_model
    
def predict_proba(fp,loaded_model):
    predictions = loaded_model.predict_proba(fp)
    predictions_list = []
    for i in range(len(predictions)):
        predictions_list.append(predictions[i][1])
    return predictions_list


def predict_activity(predictions, threshold):
    binary_list = []
    for i in range(len(predictions)):
        if predictions[i]>= threshold:
            binary_list.append(1)
        else:
            binary_list.append(0)
    return binary_list
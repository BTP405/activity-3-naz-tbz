import pickle

def pickle_message(message):
    return pickle.dumps(message)

def unpickle_message(data):
    return pickle.loads(data)
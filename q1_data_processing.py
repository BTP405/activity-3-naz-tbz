import pickle

def pickle_data(data, filename):
    """Pickles the data and saves it to the specified file."""
    with open(filename, 'wb') as f:
        pickle.dump(data, f)
    print("Data pickled successfully.")

def unpickle_data(filename):
    """Unpickles data from the specified file."""
    with open(filename, 'rb') as f:
        data = pickle.load(f)
    print("Data unpickled successfully.")
    return data
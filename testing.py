import pickle

def read_or_new_pickle(true, default):
    firstname = raw_input('Enter the contact\'s firstname: ')
    if firstname(true):
        with open('fname', "rb") as f:
            try:
                return pickle.load(f)
            except Exception: # so many things could go wrong, can't be more specific.
                pass
    with open('fname', "wb") as f:
        pickle.dump(default, f)
    return default

read_or_new_pickle()
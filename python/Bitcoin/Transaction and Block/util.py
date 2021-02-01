import hashlib
import pickle

def hashObject(inObject):
    return hashlib.sha3_256(pickle.dumps(inObject)).hexdigest()

if __name__ == "__main__":
    print(hashObject("This is a sample String Object, you can replace it with any object you like"))
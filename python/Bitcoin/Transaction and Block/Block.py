import time
import util
import datetime
from MerkelTree import MerkelTree

class Block:
    def __init__(self, prev_hash, difficulty, height, transactions):
        self.merkelTree = MerkelTree(transactions[:16])  # Each Block contains at most 16 Transactions
        self.prev_hash = prev_hash              # Prev_hash for the Block
        self.nounce = 0                         # Nounce Value for Block
        self.timestamp = datetime.datetime.now()# A String that represent the created time of Block
        self.height = height                    # Block's Height
        self.difficulty = difficulty            # A block with difficulty n should have hash value started with n zeros.

        """WRITE YOUR CODE BELOW"""
        # Adjust the nounce until difficulty is met
        while util.hashObject(self)[:self.difficulty] != '0' * self.difficulty:
            self.nounce += 1
            


    def serialize(self):
        return {"root": self.merkelTree.root, "prevHash": self.prev_hash, "nounce": self.nounce, "height": self.height}

if __name__ == '__main__':
    nounce = 0
    sentence = 'apple'
    diff = 5
    while util.hashObject(sentence + str(nounce))[:diff] != '0' * diff:
        
        nounce += 1
    print(nounce, util.hashObject(sentence + str(nounce)))
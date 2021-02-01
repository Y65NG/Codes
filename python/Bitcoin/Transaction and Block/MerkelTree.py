import util

class MerkelTree:
    def __init__(self, transactions):
        """
        self.transactions - a list of transaction object
        self.tree = [
            [nodes in height 4], 
            [nodes in height 3], 
            ..., 
            [node in height 0 (root)]
        ]

                    [self.tree[4][0]]
                        /   \
        [self.tree[3][0]]   [self.tree[3][1]]
            /   \                   /   \
                        ...
        
        * For future use, your code should save all the nodes in tree.
        * Remember to assign the value on root to self.root at last
        """
        for _ in range(16 - len(transactions)): transactions.append("EMPTY PLACEHOLDER")
        self.transactions = transactions    # list<Transaction>
        self.tree = []
        self.root = None
        ###### DO NOT MODIFY LINES ABOVE ######
        """ WRITE YOUR CODE BELOW """
        for height in range(5):
            self.tree.append([])
            if height == 0:
                for Tx in self.transactions:
                    self.tree[0].append(util.hashObject(Tx))
            else:
                index = 0
                while index < 2 ** (5 - height):
                    self.tree[height].append(util.hashObject(self.tree[height - 1][index] + self.tree[height - 1][index + 1]))
                    index += 2
        self.root = self.tree[-1][0]
        # print(self.tree)

    
    def getRelatedNodes(self, index):
        relatedNodes = []
        for height in range(len(self.tree) - 1):
            if index % 2:
                relatedNodes.append(self.tree[height][index - 1])
            else:
                relatedNodes.append(self.tree[height][index + 1])
            index  = index // 2
        return relatedNodes

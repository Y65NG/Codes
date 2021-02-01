"""
Ledger class for GZFLS_Blockchain Project, store all the Transactions and validate each input Transaction automatically.
"""
from RSA_func import decryptObject
from Transaction_exceptions import *


class Ledger(dict):
    def __init__(self):
        super().__init__(self)
    
    def addTransaction(self, currTransaction):
        """
        :param: Transaction - a transaction object that needs to be added into the Ledger
        :return: None

        In this function, you should check whether the input function is valid. If not, raise corresponding exceptions
        as described in part 1.3.1 of project requirement.
        """
        """WRITE YOUR CODE BELOW"""
        
        self.checkIsBalance(currTransaction)
        self.checkIsUnused(currTransaction)
        self.checkInSig(currTransaction)
        self[currTransaction.getTxn()] = currTransaction

                
    def checkIsBalance(self, currTransaction):
        """
        :param: Transaction - a transaction object that needs to be added into the Ledger
        :return: None

        In this function, you should check whether the input transaction is balance on Input Amount and Output Amount. If
        the transaction is not balanced, raise TransactionNotBalanceError(). If it is balanced, return None
        """
        """ WRITE YOUR CODE BELOW """
        if not currTransaction.isCoinBase:
            totalin = 0
            totalout = 0
            #print(currTransaction)
            for inTran in currTransaction.inTransaction:
                Txn, index, Signature = inTran
                #print(inTran)
                if Txn not in self: raise TransactionInNotExist()
                #print(self[Txn].outTransaction)
                totalin += self[Txn].outTransaction[index][0]
            for outTran in currTransaction.outTransaction:
                totalout += outTran[0]
            if totalin != totalout: raise TranactionNotBalanceError()

    
    def checkIsUnused(self, currTransaction):
        """
        :param: Transaction - a transaction object that needs to be added into the Ledger
        :return: None

        In this function, you should check whether each entry that .inTransaction points to is unUsed. If any of
        the entry is already used, raise TransactionDoubleSpendError.
        """
        """ WRITE YOUR CODE BELOW """
        if not currTransaction.isCoinBase:
            for inTran in currTransaction.inTransaction:
                Txn, index, Signature = inTran
                if Txn not in self: raise TransactionInNotExist()
                if self[Txn].outTransaction[index][2]: 
                    raise TransactionDoubleSpendError()
                    break
                

    def checkInSig(self, currTransaction):
        """
        :param: Transaction - a transaction object that needs to be added into the Ledger
        :return: None

        In this function, you should check whether each signature in entry of .inTransaction is valid. If any of
        the signature is invalid, raise TransactionSignatureError.
        """
        """ WRITE YOUR CODE BELOW """
        if not currTransaction.isCoinBase:
            for Txn, index, Signature in currTransaction.inTransaction:
                if Txn not in self: raise TransactionInNotExist()
                pubKey, isUsed = self[Txn].outTransaction[index][1:]
                if isUsed or decryptSignature(Signature, pubKey) != self[Txn].getTxn(): 
                    raise TransactionSignatureError()
        else:
            if currTransaction.myPubKey[1] != currTransaction.myPrivateKey[1]: raise TransactionSignatureError

    
    def checkRecursiveTx(self, Transaction):
        """
        :param: Transaction - a transaction object that needs to be added into the Ledger
        :return: None

        In this function, you will check the transaction and their upperstream transactions recursively until you meet
        the transaction from COINBASE. Any transaction from COINBASE is directly considered as valid transaction. If the
        transaction is valid after checking recursively, raise corresponding Exceptions, otherwise, return nothing.
        """
        """ WRITE YOUR CODE BELOW """
        if Transaction.isCoinBase: return
        self.checkIsBalance(Transaction)
        self.checkIsUnused(Transaction)
        self.checkInSig(Transaction)
        for intx in Transaction.inTransaction:
            self.checkRecursiveTx(self[intx[0]])

    
    def getBalanceStat(self):
        """
        :param: Nothing
        :return: A dictionary that represent the total usable (unused) coins in the ledger. The key is the public key of
        receiver while the value is balance (amount of money) under each public key.
        """
        """ WRITE YOUR CODE BELOW """
        result = {}
        temp = 0
        for tx in self.values():
            for amount, pubKey, isUsed in tx.outTransaction:
                if not isUsed:
                    result.update(pubKey = temp + amount)
                    temp = amount
                    # if pubKey not in result: result[pubKey] = amount + temp
                    # else: result[pubKey] += amount + temp
                    # temp = amount
        return result

    

    
    def __str__(self):
        result ="| Status | Current Number of Transaction Stored: {}\n".format(len(self))
        result +="------------ Transactions Stored in Ledger Below ----------\n"
        result +="| Ledger Balence Statistics: " + str(self.getBalanceStat()) + "\n"
        for Txn in self.keys():
            result += str(self[Txn])
            result += "\n|\n"
        result +="------------ Transactions Stored in Ledger Above ----------\n"
        return result
        
    def __repr__(self):
        return str(self)
    
    def exportFile(self, fileName="Ledger.txt"):
        with open(fileName, "w") as exportFile:
            exportFile.write(str(self))

def isCoinBase(transaction):
    return transaction.isCoinBase

def decryptSignature(signature, pubKey: tuple):
    """
    :param: signature - a tuple of tokens formed by encryptObject in RSA_func.py, pubKey - a tuple of integers that contain
    (pubKey, N)
    :return: the decryption result of encrypted message.

    If decryption fail, the normal Exception will be raised instead of the TransactionSignatureError. You can use a
    try:
        ...
    except:
        ...
    structure to 'catch' the exception raised by decryptObject and then raise the TransactionSignatureError instead.
    """
    """ WRITE YOUR CODE HERE """
    # print('\ndecrypt:\n', decryptObject(signature, *pubKey), '\n', signature)
    try:
        return decryptObject(signature, *pubKey)
    except: raise TransactionSignatureError()

if __name__ == "__main__":
    A = Ledger()
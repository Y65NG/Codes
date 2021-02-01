from Transaction import Transaction
from Ledger import Ledger
from RSA_func import *

if __name__ == "__main__":
    names = ["A", "B", "C"]
    RSA_keys = dict()
    for name in names:
        RSA_keys[name] = generateMyKeys()

    A_pubKey, A_privateKey = (RSA_keys["A"][1], RSA_keys["A"][2]), (RSA_keys["A"][0], RSA_keys["A"][2])
    B_pubKey, B_privateKey = (RSA_keys["B"][1], RSA_keys["B"][2]), (RSA_keys["B"][0], RSA_keys["B"][2])
    C_pubKey, C_privateKey = (RSA_keys["C"][1], RSA_keys["C"][2]), (RSA_keys["C"][0], RSA_keys["C"][2])

    #### INITIALIZE WITH SOME TRANSACTIONS ####
    allTransaction = Ledger()
    for i in range(5):
        for name in names:
            newTx = Transaction(allTransaction, 20, 0, 0, (RSA_keys[name][1], RSA_keys[name][2]), isCoinBase=True)
            allTransaction.addTransaction(newTx)
    ###########################################

    # A -- 50 --> B
    newTx = Transaction(allTransaction, 50, A_pubKey, A_privateKey, B_pubKey)
    allTransaction.addTransaction(newTx)
    
    # B -- 25 --> C
    newTx = Transaction(allTransaction, 25, B_pubKey, B_privateKey, C_pubKey)
    allTransaction.addTransaction(newTx)

    # Tampered Transaction Test
    # B --- 10 ---x---> A
    newTx = Transaction(allTransaction, 10, B_pubKey, B_privateKey, A_pubKey)
    # newTx.outTransaction[0][0] = 20
    try:
        allTransaction.addTransaction(newTx)
    except:
        pass

    print(RSA_keys)
    allTransaction.exportFile()
    print("\n")
    print(allTransaction.getBalanceStat())
    
    

class BlockchainError(Exception):
    def __init__(self, message): super().__init__(message)

class TranactionNotBalanceError(BlockchainError):
    def __init__(self, message="The Transaction is not Balanced, check the init function in Transaction Class."):
        self.message = message
        super().__init__(self.message)


class TransactionDoubleSpendError(BlockchainError):
    def __init__(self, message="At least one of the input in given transaction is already used, transaction is not recorded by Ledger."):
        self.message = message
        super().__init__(self.message)


class TransactionInNotExist(BlockchainError):
    def __init__(self, message="At least one of the input of given Transaction is not recorded in the Ledger, transaction is not recorded by Ledger."):
        self.message = message
        super().__init__(self.message)


class TransactionSignatureError(BlockchainError):
    def __init__(self, message="Signature in the given inTransaction fail to Pass the Signature Pass."):
        self.message = message
        super().__init__(self.message)

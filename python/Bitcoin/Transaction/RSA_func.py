import pickle

from RSA_util import getRandomBigPrime, calcPhi

# In this file, you will write the implementation of RSA_Client class. For the Autograder to run properly,
# DO NOT MODIFY the given function signature and class name.
#
# To help you write this project, we have provided several utility functions in file RSA_util.py
# The function you can use are:
#   >>> getBigRandomPrime()
#   return a 256-bit random number
#   >>> calcPhi(a: int, b: int)
#   return Phi(a) * Phi(b)
#   >>> extendEuclidean(e: int, phi: int)
#   return d, k, where d * e - k * phi = 1


def extendEuclidean(e: int,phi: int):
    """
    :params: Two integer e and phi are input as parameters. Given these two parameters, calculate two integer d and k
    such that e * d + k * phi = 1
    :returns: a tuple of two integers, which contains d and k separately.

    Doctest Below

    Testcase 1
    >>> d, k = extendEuclidean(13, 25)
    >>> assert (d * 13 + k * 25 == 1), "extendEuclidean() Fail to past Test case #1"

    Testcase 2
    >>> d, k = extendEuclidean(14528, 360931)
    >>> assert (d * 14528 + k * 360931 == 1), "extendEuclidean() Fail to past Test case #2"
    """
    assert e > 0 and phi > 0, "You are passing negative number into the function. This is invalid for function."

    x,y,gcd = Euclidean(e,phi)
    index = 0
    while(x < 0):
        x = x+phi*index
        y = y-e*index
        index += 1
    return x, y # x * e - y * phi = 1

def Euclidean(e: int,phi: int):
    if phi == 0 :
        return (1,0,e)
    x,y,gcd = Euclidean(phi,e%phi)
    return (y,x-e//phi*y,gcd)


def generateMyKeys():
    """
    :params: This function takes in no parameter.
    :returns: This function will return a tuple of form (int, int, int). The 0th value represents the generated private
    key. The 1st value represents the generated public key, and 2nd value represent the common value for both encryption
    and decryption.
    """
    """ WRITE YOUR CODE BELOW """
    # publicKey = 0           # you can delete this line if necessary
    # privateKey = 0          # you can delete this line if necessary
    # n = 0                   # you can delete this line if necessary

    p = getRandomBigPrime()
    q = getRandomBigPrime()
    n = p * q
    phi = calcPhi(p, q)
    publicKey = getRandomBigPrime(bitLength=16)
    privateKey, k = extendEuclidean(publicKey, phi)

    """ WRITE YOUR CODE ABOVE """
    return (privateKey, publicKey, n)

def encryptInt(message: int, publicKey: int, n: int):
    """
    Given the public key of receiver and the value of n, this function will encrypt the input parameter 'message' and
    return the encrypted value, which will be an integer.
    """
    assert message < n, "The input message is bigger than the selected n. This will lead to incorrect result" \
                        " even if you have correct implementation. Change to a smaller message or a bigger n."
    """ WRITE YOUR CODE BELOW """

    encryptMsg = (message ** publicKey) % n

    """ WRITE YOUR CODE ABOVE """
    return encryptMsg

def decryptInt(message: int, privateKey: int, n: int):
    """
    Given the private key of receiver and n, the receiver will be able to decrypt the message he received.
    :returns: The decrypted message, which will be an integer.
    """
    assert message < n, "The input message is bigger than the selected n. This will lead to incorrect result" \
                        " even if you have correct implementation. Change to a smaller message or a bigger n."
    """ WRITE YOUR CODE BELOW """

    decryptMsg = (message ** privateKey) % n

    """ WRITE YOUR CODE ABOVE """
    return decryptMsg

################################# YOU SHOULD NOT MODIFY FUNCTIONS BELOW ###################################

def encryptObject(msg_object: object, publicKey: int, n: int):
    return [encryptInt(token, publicKey, n) for token in longMsgIterator(msg_object)]

def decryptObject(msg_list: list, privateKey: int, n: int):
    token_combiner = tokensCombiner()
    for token in msg_list: token_combiner.addToken(token, privateKey, n)
    return convertIntegerToObject(token_combiner.getNum())


############################# YOU SHOULD NOT READ & MODIFY FUNCTIONS BELOW ################################

def convertObjectToInteger(obj: object):
    return int.from_bytes(pickle.dumps(obj), byteorder="little")

def convertIntegerToObject(integer: int):
    max_len, curr_len = 1024 ** 3, 64
    while curr_len < max_len:
        try:
            resObject = pickle.loads(integer.to_bytes(curr_len, byteorder='little'))
            break
        except OverflowError as e:
            curr_len = curr_len ** 2
    return resObject


class longMsgIterator:
    def __init__(self, msg: object):
        self.message = msg
        self.msgInt = convertObjectToInteger(msg)

    def __iter__(self): return self

    def __next__(self):
        if self.msgInt == 0: raise StopIteration
        token = self.msgInt % 100000
        self.msgInt -= token
        if self.msgInt > 100000: self.msgInt = self.msgInt // 100000
        return token

class tokensCombiner:
    def __init__(self):
        self.num = 0
        self.pow = 0
    def addToken(self, token, privateKey:int, n:int, token_size=5):
        self.num += decryptInt(token, privateKey=privateKey, n=n) * (10 ** self.pow)
        self.pow += token_size
    def getNum(self): return self.num

##################################### TEST ###########################################

if __name__ == "__main__":
    import doctest
    # Simple doctest to check each function saperately
    print("Running Simple Doctest to check functions separately...")
    doctest.testmod()

    print("\nRunning a actual case of RSA encryption-decryption pipeline...\n")

    # Initialize Test Objects
    A_private, A_public, A_n = generateMyKeys()
    B_private, B_public, B_n = generateMyKeys()
    C_private, C_public, C_n = generateMyKeys()

    # Initialize Message Object
    obj = ["Hello World", "Implementation Test",
           "If you see this, you have passed implementation test."]
    print("Test case input Object - ", obj)
    print("Encryption Test Running, please wait ...", end="")


    # Encryption Process A ---> Public Env ---> B
    try:
        encryptMsg = encryptObject(obj, B_public, B_n)
        print("\rThese are the encrypted tokens send from A to B if your code is running properly."
              "\n", encryptMsg)
    except Exception as e:
        raise Exception("Your implementation have some problem, the decryption process FAIL. We "
                        "have terminate further test. \nDetailed Exception:\n", e)

    # Decryption Process A ---> Public Env ---> B
    try:
        print("Tokens received, decrypting, please wait ...", end="")
        receive_obj = decryptObject(encryptMsg, B_private, B_n)
        print("\rReceived Object: ", receive_obj)
    except Exception as e:
        raise Exception("Your implementation have some problem, the decryption process FAIL. We"
                        " have terminated further test. \nDetailed Exception:\n", e)

    # Malicious User C attack test
    try:
        print("We are testing if a malicious third-party can steal the encrypt message between"
              " A and B, please wait ...", end="")
        steal_obj = decryptObject(encryptMsg, B_public, B_n)
        print(steal_obj)
        raise Exception("Your implementation have some problem. An unauthorized third party can "
                        "steal the message object without difficulty.")
    except:
        print("\rThe malicious third-party failed to steal encrypted message between A and B.")
        print("Congratulation! Your implementation has passed all the test cases.")


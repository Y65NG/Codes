import re
from collections import Counter #用了个计数的库

def words(text): return re.findall(r'\w+', text.lower()) #数据预处理 只要英文单词 小写

WORDS = Counter(words(open('big.txt').read())) #txt是个大文本 作为先验统计 每个词出现频率

def P(word, N=sum(WORDS.values())):  # N总单词数 每个单词出现概率
    "Probability of `word`."
    return WORDS[word] / N

def correction(word):  #哪个频率高
    "Most probable spelling correction for word."
    return max(candidates(word), key=P)

def candidates(word):  #所有候选  只返回在字典中的字
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word)) or known(edits2(word)) or [word])

def known(words): #在表里的子字符串
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word): #一个单词出现的所有一个编辑距离情况
    "All edits that are one edit away from `word`."
    letters    = 'abcdefghijklmnopqrstuvwxyz'
    splits     = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes    = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces   = [L + c + R[1:]           for L, R in splits if R for c in letters]
    inserts    = [L + c + R               for L, R in splits for c in letters]
    return set(deletes + transposes + replaces + inserts)

def edits2(word): #两个编辑距离错误
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word) for e2 in edits1(e1))
    
while True:
	print(correction(input())) 

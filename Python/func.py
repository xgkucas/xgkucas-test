import re, collections

def tokens(text):
    """
    Get all words from the corpus
    """
    return re.findall('[a-z]+', text.lower())
 
with open('big.txt', 'r') as f:
    WORDS = tokens(f.read())
WORD_COUNTS = collections.Counter(WORDS)


def known(words):
    """
    Return the subset of words that are actually
    in our WORD_COUNTS dictionary.
    """
    return {w for w in words if w in WORD_COUNTS}


def edits0(word):
    """
    Return all strings that are zero edits away
    from the input word (i.e., the word itself).
    """
    return {word}
 

def edits1(word):
    """
    Return all strings that are one edit away
    from the input word.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
 
    def splits(word):
        """
        Return a list of all possible (first, rest) pairs
        that the input word is made of.
        """
        return [(word[:i], word[i:]) for i in range(len(word) + 1)]
 
    pairs = splits(word)
    deletes = [a + b[1:] for (a, b) in pairs if b]
    transposes = [a + b[1] + b[0] + b[2:] for (a, b) in pairs if len(b) > 1]
    replaces = [a + c + b[1:] for (a, b) in pairs for c in alphabet if b]
    inserts = [a + c + b for (a, b) in pairs for c in alphabet]
    return set(deletes + transposes + replaces + inserts)


def edits2(word):
    """
    Return all strings that are two edits away
    from the input word.
    """
    return {e2 for e1 in edits1(word) for e2 in edits1(e1)}


def correct(word):
    """
    Get the best correct spelling for the input word
    """
    # Priority is for edit distance 0, then 1, then 2
    # else defaults to the input word itself.
    candidates = (known(edits0(word)) or
                  known(edits1(word)) or
                  known(edits2(word)) or
                  [word])
    return max(candidates, key=WORD_COUNTS.get)


def correct_match(match):
    """
    Spell-correct word in match,
    and preserve proper upper/lower/title case.
    """
 
    word = match.group()
 
    def case_of(text):
        """
        Return the case-function appropriate
        for text: upper, lower, title, or just str.:
        """
        return (str.upper if text.isupper() else
                str.lower if text.islower() else
                str.title if text.istitle() else
                str)
 
    return case_of(word)(correct(word.lower()))


def correct_text_generic(text):
    """
    Correct all the words within a text,
    returning the corrected text.
    """
    return re.sub('[a-zA-Z]+', correct_match, text)


def detect_En(line_num,text,fname):
    if text is None:
        return
    original_word_list =re.findall("[a-zA-Z]+",text)
    for original_word in original_word_list:
        correct_word = correct_text_generic(original_word)
        if original_word == correct_word:
            continue
        else:
            with open('%s.txt'%fname, 'a+', encoding='utf-8') as f:
                tplt = "{:<8}\t{:<17}\t{:<15}\n"
                f.write(tplt.format(line_num, original_word, correct_word))
                #f.write(tplt.format('第%d行 Orginial word: %s\t Correct word: %s\n' % (line_num, original_word, correct_word)))
                f.close()
        #print('第%d行 Orginial word: %s\t Correct word: %s'%(line_num, original_word, correct_word))

#定位注释位置
def count(file,fname):
    dic = {}
    flag = 0 #标志位
    total = 0 #总行数
    countPound = 0 #注释行数
    countBlank = 0 #空行数
    line = open(file,'r',encoding='utf-8') #打开文件，因为注释有中文所以使用utf-8编码打开
    for li in line.readlines(): #readlines()一次性读完整个文件
        total += 1
        if not li.split(): #判断是否为空行
            countBlank +=1
        li.strip()


        #flag = 1进行单行匹配。flag =0进行多行匹配
        if flag == 0:
            res = re.search("\/\/.*",li) #判断//
            if res:
                dic[total] = res.group()
                detect_En(total,res.group(),fname)
                #print(res.group())
                #print(1)
                countPound += 1
            else:
                res = re.search("\/\*.*",li)  #判断开始/*
                if res:
                    dic[total] = res.group()
                    detect_En(total,res.group(),fname)
                    #print(res.group())
                    countPound += 1
                    flag = 1
            
        else:
            dic[total] = li
            detect_En(total,li,fname)
            #print(li)
            countPound += 1
            res = re.search(".*\*\/$",li)   #判断结束位*/
            if res:
                flag = 0
      

    # print("countBlank:%d" % countBlank)
    # print("countPound:%d" % countPound)
    print("total:%d" % total)
    return(dic)


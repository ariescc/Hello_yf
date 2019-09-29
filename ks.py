import re
import nltk

nltk.download('averaged_perceptron_tagger')

prep = set(('on','in','to','of','up','down','by','with','about','without','into','from','away','off'))
lc = set(('and', 'or'))
bd = set((',','.',';','\''))
dc = set(('it','I','you','they','he','she','it'))
fin = open('article.txt', 'r')
fout = open('terms.txt', 'w')

# 读取文章内容
words = fin.read()

terms = set()
for idx in range(len(words)):
    if (words[idx] in prep) == True and \
        (words[idx-1][-1:] in bd) == False and \
        (words[idx-1] in dc) == False and \
        (words[idx-1] in prep) == False and \
        (words[idx-1] in lc) == False:
        # fout.write(words[idx-1]+' '+words[idx])
        terms.add(words[idx-1]+' '+words[idx])
        # fout.write('\n')
    elif (words[idx] in prep) == True and \
        (words[idx-1][-2:] == 'ly'): # 如果当前是介词，并且前一个单词以ly结尾，大概率为副词，则再向前提取一个单词组成动宾短语
        terms.add(words[idx-2]+' '+words[idx-1]+' '+words[idx])
for term in terms:
    fout.write(term+'\n')

# 提取动词
tokens = nltk.word_tokenize(words)
pos_tags = nltk.pos_tag(tokens)
for word, pos in pos_tags:
    if (pos == 'VB' or pos == 'VBD'):
        print(word, pos)

# 根据单词结尾ed or d判断动词
# should, be + 动词

fin.close()
fout.close()

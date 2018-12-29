import string
import re
import nltk

begin = "@"
end = " "
text = open("tweet.txt","r").read().split()

def preproc(text):
    for line in text:
        for word in line:
            if word in string.ascii_letters or word in string.digits:
                if line in text:
                    text.remove(line)
        if line in "RT":
            text.remove(line)
        if line in "http":
            text.remove(line)
    j= []
    for i in range(len(text)):
        # アルファベットと半角英数と記号と改行とタブを排除
        a = re.sub('(%s.*%s)' % (begin,end), '', text[i])
        a = re.sub(r'[a-zA-Z0-9¥"¥.¥,¥@]+', '', a)
        a = re.sub(r'[!"“#$%&()\*\+\-\.,\/:;<=>?@\[\\\]^_`{|}~]', '', a)
        a = re.sub(r'[\r|\t]', '', a)
        # 日本語以外の文字を排除(韓国語とか中国語とかヘブライ語とか)
        jp_chartype_tokenizer = nltk.RegexpTokenizer(u'([ぁ-んー]+|[ァ-ンー]+|[\u4e00-\u9FFF]+|[ぁ-んァ-ンー\u4e00-\u9FFF]+)')
        a = "".join(jp_chartype_tokenizer.tokenize(a))
        j.append(a)
    return j

text = preproc(text)

f =  open('new_tweet.txt', 'w')
for i,x in enumerate(text):
    if x == "":
        pass
    else :
        f.write(str(x)+"。"+"\n")
f.close()

#j=[]
#text = open("new_tweet.txt","r").read().split()
"""
for i in range(len(text)):
    '\n'.join(filter(lambda x: x.strip(), text[i].split('\n')))
    #a = re.sub('[\r\n]+$', '', text[i])
    #j.append(a)
"""
"""
text = []
f =  open('new_tweet.txt', 'r')
for i in f.readlines():
    i=i.strip()#末尾の改行を除去、
    #i=i.split("\t")#tab区切りでリストを作成、ちなみに改行コードは\n
    if i == [""]:
        pass
    else:
        i = i+"\n"
        text.append(i)
f.close()

f =  open('new_tweet.txt', 'w')
for x in text:
    f.write(str(x))
f.close()
"""

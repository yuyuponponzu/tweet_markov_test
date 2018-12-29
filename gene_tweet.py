# -*- coding: utf-8 -*-
#辞書の読み込み
import json
dic = open("markov-blog.json" , "r")#crontabを使う場合は、絶対パスに書き換える
dic = json.load(dic)

#文章を生成
tweets_list = []
import random
def word_choice(sel):
    keys = sel.keys()
    ran = random.choice(list(keys))
    return ran

def make_sentence(dic):
    ret = []
    if not "@" in dic: return "no dic"
    top = dic
    w1 = word_choice(top)
    w2 = word_choice(top[w1])
    ret.append(w1)
    ret.append(w2)
    while True:
        w3 = word_choice(dic[w1][w2])
        ret.append(w3)
        if w3 == "。": break
        w1, w2 = w2, w3
    tweets_list.append(ret)
    return "".join(ret)


f =  open('ai_tweet.txt', 'w')
for i in range(700):
    s = make_sentence(dic)
    print(s)

    f.write(s+"\n")
f.close()

# tweet_takahiro
雑です<br>

## ツイートの取得
http://www.twimemachine.com/user/AI_junk88_takah/ <br>
ここで全ツイートを取得（全部コピーしてる）<br>

## AI(ではないけど，マルコフ連鎖)によるツイート生成
1.tweet.txt というテキストファイルに，コピーしたツイートを全部張る<br>
1.preproc_txt.pyでnew_tweet.txt(簡単にする為に日本語以外の文字や数字を全て除外，もっと良いのを作りたいならここを弄ればちゃんとできる)<br>
1.make_dict.pyでマルコフ連鎖用の辞書作成<br>
1.gene_tweet.pyで辞書に沿ってツイート生成（現状，初句(w1)はランダム選択だから不自然になることも．文終了のトリガーは理系ぶって「．」）<br>
1.ai_tweet.txtに任意の行数分の自動生成文ができる<br>

## bot化
https://twittbot.net<br>
ここで複数行入力で一括登録<br>

## 補足
ちゃんとbot化したければAPI取得の申請が必要（リプの対応まで可能）<br>
たまに長いわけのわからない文ができるのは，preprocが激甘だから<br>
意味的な理解まで含めたAIを作るならマルコフ連鎖じゃなくてLSTM<br>

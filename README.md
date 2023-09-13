テスト

## ツイートの取得
twitterからtweetデータをダウンロードし， tweet.jsを https://17number.github.io/tweet-js-loader/ でcsv化
その後， python extract_for_csv.py > tweet.txt でツイートを生成する

## マルコフ連鎖によるツイート生成
1. tweet.txt というテキストファイルに，コピーしたツイートを全部張る
1. preproc_txt.pyでnew_tweet.txt
1. make_dict.pyでマルコフ連鎖用の辞書作成
1. 初句(w1)はランダム選択でgene_tweet.pyで辞書に沿ってツイート生成
1. ai_tweet.txtに任意の行数分の自動生成文ができる

## bot化
https://twittbot.net<br>
ここで複数行入力で一括登録<br>
(ここもよさそう　https://metabirds.net/admin/bot_random.php)<br>

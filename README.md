# Django_pagination_sample

## セットアップ
```
# 任意のGit用ディレクトリへ移動
>cd path\to\dir

# GitHubからカレントディレクトリへclone
path\to\dir>git clone https://github.com/thinkAmi-sandbox/Django_permissions_sample.git

# virtualenv環境の作成とactivate
# *Python3.5は、`c:\python35-32\`の下にインストール
path\to\dir>virtualenv -p c:\python35-32\python.exe env
path\to\dir>env\Scripts\activate

# requirements.txtよりインストール
(env)path\to\dir>pip install -r requirements.txt

# マイグレーション
(env)path\to\dir>python manage.py migrate

# 初期データのロード
(env)path\to\dir>python manage.py loaddata initial_data.json

# 開発サーバの起動
(env)path\to\dir>python manage.py runserver

# 開発サーバのURLを既定のブラウザで開く
# (別のコマンドプロンプトを開いて実行)
>start http://localhost:8000/mysite/prev-next
>start http://localhost:8000/mysite/prev-next-desc
>start http://localhost:8000/mysite/all
>start http://localhost:8000/mysite/pure
>start http://localhost:8000/mysite/bootstrap-pure
>start http://localhost:8000/mysite/share
```

　  
## テスト環境

- Windows10
- Python 3.5.1
- Django 1.9.2

　  
## 関係するブログ

[Djangoで、Paginatorやdjango-pure-paginationを使ってページングしてみた - メモ的な思考的な](http://thinkami.hatenablog.com/entry/2016/02/04/231901)
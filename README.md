# Djangoの公式チュートリアルを実施
https://docs.djangoproject.com/ja/4.2/intro/

## 所感
- 公式のチュートリアルというのは他にもrailsなどあると思うが、初めて取り組んだ。
- 理解が難しいことが多いと感じたが、その分勉強になる内容も多いと感じた。
- これからも動画教材、書籍、公式チュートリアルとそれぞれのメリットがあると思うので、上手く使って勉強していきたい。

## Djangoの概要
- Instagram, edX, などで使用されるWebフレームワーク
- MVTC(model, view, templates, urls.py)のフレームワーク

#### models.py
- ORM(object relational mapping)によりデータを扱うことができる
- モデル→マイグレーション（railsなど多くはmigration→modelの記述）
- モデルの設計
```
from django.db import models

class Article(models.Model):
    pub_date = models.DateField()
    headline = models.CharField(max_length=200)
    content = models.TextField()
    reporter = models.ForeignKey(Reporter, on_delete=models.CASCADE)

    def __str__(self):
        return self.headline
```
- モデルのインストール
テーブルの作成と、マイグレーションの実行
```
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```

#### admin.py
- 便利な管理者ツール
    - モデルが定義されると、Django は自動的にプロ仕様の管理者サイトを作成する。（認証されたユーザがオブジェクトを追加、変更、削除できる）必要なステップは、管理サイトにモデルを登録することだけ。

#### urls.py
- 以下のように記述する。
urlpatterns = [
    path("articles/<int:year>/", views.year_archive),
    path("articles/<int:year>/<int:month>/", views.month_archive),
    path("articles/<int:year>/<int:month>/<int:pk>/", views.article_detail),
]

#### views.py
- function based viewとclass based viewがある。
- function based view
    def set_goal:

- class based view
    class set_goal(CreateView):


#### templates
- base.html
    - 共通する見た目の部分を定義しておく。
    - 以下のように記述し他のビューから呼び出して使う
        - `{% extends 'base.html' %}`
    

## Django_Tutorial_PollsApp
#### tutorial_1 　Djangoプロジェクト・アプリのスタート
- 使用コマンドや開発の流れ
```
mkdir tutorial_1
cd tutorial_1
<!-- Djangoのプロジェクト作成 -->
django-admin startproject polls tutorial_1
```
```
<!-- サーバーを立ち上げる -->
python3 manage.py runserver
```
```
<!-- pollsアプリを作る -->
python3 manamge.py startapp polls
```
```
<!-- views.pyの作成 -->
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```
```
個々のアプリのURLconf. 取り急ぎ全てのアクセスでindex.htmlを表示
<!-- polls.urls.pyの作成 -->
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```
```
djangoプロジェクトのグローバルURLconf, include()でdjangoアプリのURLconfを参照する
<!-- tutorial_1/urls.pyの作成 -->
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```


- 疑問点.
    - Web サーバのドキュメントルート下 (/var/www といった場所) とは何か。

- ポイント
    - include()
      - djangoプロジェクトのグローバルURLconfに、 include()でdjangoアプリのURLconf(urlpatterns[])を参照する
    - path()の引数: route
        - リクエストを処理するとき、Django は urlpatterns のはじめのパターンから開始し、リストを順に下に見ていく。要求された URL を一致するものを見つけるまで各パターンと比較する。パターンはGETやPOSTのパラメーター、ドメイン名を検索しない。例えば、 https://www.example.com/myapp/ へのリクエストにおいては、URLconfは myapp/ を見る。 https://www.example.com/myapp/?page=3 へのリクエストにおいても、URLconfは myapp/ を見る。
    - path()の引数: view
        - 
    - path()の引数: kwargs(=keyword arguments)
        - 任意のキーワード引数を辞書として対象のビューに渡す
    - path()の引数: name
- 感想


#### tutorial_2　 データベースの設定
- 使用コマンドや開発の流れ
```
<!-- DBにテーブルを作成する -->
python3 manage.py migarate
```

```
<!-- polls.models.pyの編集 -->
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

```
<!-- アプリをプロジェクトに含めるため tutorial_1/settings.pyを編集。 -->
INSTALLED_APPS = [
    "polls.apps.PollsConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```

```
<!-- モデルの変更をマイグレーションファイルの形で保存する。 -->
python3 manage.py makemigrations polls
```

```
<!-- マイグレーションファイルを実行し、テーブルをDBに作成 -->
python3 manage.py migrate
```

```
<!-- 管理ユーザーを作成する -->
python3 manage.py createsuperuser
```

```
<!-- polls/adimin.pyの編集 -->
<!-- 先ほど作ったpollアプリをadmin上で編集できるようにする -->
from django.contrib import admin

from .models import Question

admin.site.register(Question)
```

- 疑問点.
    - 

- ポイント.
    - 
- 感想
    - 



#### tutorial_3 View
- 使用コマンドや開発の流れ
```

```

```

```

```

```

- 疑問点.
```
def detail(reuquest, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("qestion does not exist.")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"quesiton": question})
```
    # 上記について、次のことが指摘されているが、今はあまり理解できていない。
     - なぜ ObjectDoesNotExist 例外を高水準で自動的にキャッチせず、ヘルパー関数 get_object_or_404() を使うのでしょうか、また、なぜモデル API に ObjectDoesNotExist ではなく、 Http404 を送出させるのでしょうか?

- ポイント.
    - 
- 感想
    - 



#### tutorial_4
- 使用コマンドや開発の流れ
```

```

```

```

```

```

- 疑問点.
    - 

- ポイント.
    - 
- 感想
    - 





#### tutorial_5
- 使用コマンドや開発の流れ
```

```

```

```

```

```

- 疑問点.
    - 

- ポイント.
    - 
- 感想
    - Djangoでのテストコードの書き方を勉強した
    - ブラックボックステスト（境界値テスト）
    - ビューに対するテスト
        - Djangoクライアントテスト




#### tutorial_6
- 使用コマンドや開発の流れ
```

```

```

```

```

```

- 疑問点.
    - 

- ポイント.
    - 






#### tutorial_7
- 使用コマンドや開発の流れ
```

```

```

```

```

```

- 疑問点.
    - 

- ポイント.
    - 




#### tutorial_8
- 使用コマンドや開発の流れ
```

```

```

```

```

```

- 疑問点.
    - 

- ポイント.
    - 


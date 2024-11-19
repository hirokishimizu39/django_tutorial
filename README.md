# Djangoの公式チュートリアルを実施
https://docs.djangoproject.com/ja/4.2/intro/


## Djangoの概要
- Instagram, edX, などで使用されるWebフレームワーク

#### models.py
- ORMによりデータを扱うことができる
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
$ python manage.py makemigrations
$ python manage.py migrate
```

#### admin.py
- 便利な管理者ツール
    - モデルが定義されると、Django は自動的にプロ仕様の本番仕様の administrative interface 1 -- 認証されたユーザがオブジェクトを追加、変更、削除できるウェブサイトを作成される。必要なステップは、管理サイトにモデルを登録することだけ。

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
    
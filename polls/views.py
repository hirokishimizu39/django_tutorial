from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.http import HttpResponse
from .models import Question
from django.template import loader

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("qestion does not exist.")
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"quesiton": question})
    # 上記について、右記のことが指摘されているが、今はあまり理解できていない。なぜ ObjectDoesNotExist 例外を高水準で自動的にキャッチせず、ヘルパー関数 get_object_or_404() を使うのでしょうか、また、なぜモデル API に ObjectDoesNotExist ではなく、 Http404 を送出させるのでしょうか?なぜなら、それはモデル層とビュー層とを密結合させることになるからです。Django の最も重要な設計目標の一つは、疎結合を維持することです。 django.shortcuts には結合がコントロールされたいくつかのモジュールが用意されています。

def results(reuquest, question_id):
    response = "you're looking at results of question %s."
    return HttpResponse(results % question_id)

def vote(request, question_id):
    return HttpResponse("you're voiting on question %s." % question_id)
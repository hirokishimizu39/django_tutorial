from django.shortcuts import render, get_object_or_404
from django.db.models import F
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Question, Choice
from django.views import generic

# Create your views here.
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html")
#     context = {
#         "latest_question_list": latest_question_list,
#     }
#     return render(request, "polls/index.html", context)
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"
    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]

# def detail(request, question_id):
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("qestion does not exist.")
#     question = get_object_or_404(Question, pk=question_id)
#     print(question.id)
#     print("ンンンンンンンンンンンンンンンンンンンンンンンンンンンンンンンンンん")
#     return render(request, "polls/detail.html", {"quesiton": question})
#     # 上記について、右記のことが指摘されているが、今はあまり理解できていない。なぜ ObjectDoesNotExist 例外を高水準で自動的にキャッチせず、ヘルパー関数 get_object_or_404() を使うのでしょうか、また、なぜモデル API に ObjectDoesNotExist ではなく、 Http404 を送出させるのでしょうか?なぜなら、それはモデル層とビュー層とを密結合させることになるからです。Django の最も重要な設計目標の一つは、疎結合を維持することです。 django.shortcuts には結合がコントロールされたいくつかのモジュールが用意されています。
class DetailView(generic.DetailView):
    model = Question
    template_anme = "polls/detail.html"

# def results(reuquest, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {"question": question})
class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
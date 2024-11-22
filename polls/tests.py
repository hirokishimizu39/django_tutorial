from django.test import TestCase

# Create your tests here.
import datetime
from django.utils import timezone
from .models import Question
from django.urls import reverse


def create_question(question_text, days):
    """
    Create a question with the give `question_text` and published the given number of `days` 
    offset to now(negative for questions published in the past, positive for questions that 
    have yet to be published)
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Question.objects.create(question_text=question_text, pub_date=time)


class QuestionModelTests(TestCase):
    """
   # ブラックボックステスト
    - 同値分析
      - 有効同値クラス
      - 無効同値クラス
    - 限界値分析
    """

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time_of_30days_later = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time_of_30days_later)
        self.assertIs(future_question.was_published_recently(), False)
        
    # 限界値分析。境界値（無効=False）
    def test_was_published_rencently_with_old_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time_of_older_than_1day = timezone.now() - datetime.timedelta(days=1, seconds=1)
        recent_question = Question(pub_date=time_of_older_than_1day)
        self.assertIs(recent_question.was_published_recently(), False)
    
    
    # 限界値分析。境界値（有効=True）
    def test_was_published_rencently_with_recent_question(self):
        """
        was_published_recently() returrns True for qestions whose pub_date is within the last day
        """
        time_within_last_day = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_question = Question(pub_date=time_within_last_day)
        self.assertIs(recent_question.was_published_recently(), True)
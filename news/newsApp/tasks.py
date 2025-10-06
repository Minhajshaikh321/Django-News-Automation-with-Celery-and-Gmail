from celery import shared_task
from .services import fetch_news

@shared_task
def fetch_news_task():
    result=fetch_news()
    print(result)
    return 
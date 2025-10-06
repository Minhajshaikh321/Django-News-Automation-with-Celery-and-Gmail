import requests
from datetime import datetime
from .models import News
from django.core.mail import send_mail
from django.conf import settings
import itertools

NEWS_API_KEY=''
NEWS_URL='https://newsapi.org/v2/top-headlines'
# COUNTRIES=['us','gb','in','ca','au']

def fetch_news():
    params={
        "country":"us",
        "apiKey": NEWS_API_KEY,
        "pageSize":3
    }

    try:
        response=requests.get(NEWS_URL,params=params,timeout=10)

        data=response.json()
        # print('Request URL:', response.url)
        # print('Response data:',data)

        if data.get('status')=="ok": 
            for article in data["articles"]:
                    created=News.objects.get_or_create(
                        url=article["url"],
                        defaults={
                            "title":article.get("title") or "No Title",
                            "author":article.get("author") or "Unknown",
                            "description":article.get("description") or "",
                            "published_date":article.get("publishedAt") or "DD/MM/YYYY",
                            "source":article["source"].get("name") or "Unknown source",
                        },
                    )
                
                    subject = f"News article: {article.get('title') or 'No Title'}"

                    body = f"""
                        <h2>{article.get('title') or 'No Title'}</h2>
                        <p>{article.get('description') or ''}</p>
                        <p>Content: {article.get('content') or 'No content written for this article'}</p>
                        <p><b>Source:</b> {article['source'].get('name') or 'Unknown source'}</p>
                        <p>Article pulished date- {article.get('publishedAt') or ''}</p>
                        <p><a href="{article['url']}">Read full article</a></p>
                        <p style="color:green;"><i>Author name: {article.get('author') or 'Unknown Author'}</i></p>
                        """
                    
                    recipient_list=['user1@example.com','user2@example.com']
                    send_mail(
                        subject,
                        message=article['description'] or "See HTML version.", 
                        from_email="coder@example.com",
                        recipient_list=recipient_list,
                        html_message=body  
                    )
                    
            return "News updated!"


    except requests.exceptions.Timeout:
        print('news api not responding')

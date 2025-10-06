🚀 Features

✅ Automatically fetches news headlines using NewsAPI

✅ Stores news articles in the Django database

✅ Sends summarized news to email recipients

✅ Uses Celery for background task management

✅ Uses Celery Beat for hourly scheduling

✅ Works asynchronously — no delays in your web app

### Commands to Run This Project
```bash
# 1. Run Django server
python manage.py runserver

# 2. Start Celery Worker
celery -A news worker -l info --pool=solo

# 3. Start Celery Beat Scheduler
celery -A news beat -l info

```
Now your project will:

1-Fetch latest news from NewsAPI every hour

2-Save it to your database

3-Send the news to recipients via Gmail
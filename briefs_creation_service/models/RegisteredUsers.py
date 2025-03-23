from django.db import models

# Model for users registered for the cronjob
class RegisteredUser(models.Model):
    ru_id = models.CharField(max_length=100, unique=True)  # Unique identifier for the user
    ru_scheduled_time = models.TimeField()  # UTC time for scheduling the brief creation (e.g., 08:00:00)
    ru_news_detail = models.TextField(default="")

    def __str__(self):
        return f"User: {self.ru_id} (Scheduled at {self.ru_scheduled_time})"

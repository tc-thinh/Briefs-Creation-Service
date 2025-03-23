from django.db import models
from django.utils import timezone
from briefs_creation_service.models.RegisteredUsers import RegisteredUser

# Define ENUM choices
class BriefType(models.TextChoices):
    # actual value stored - human readable label
    TASK = 'task', 'Task Brief'
    EVENT = 'event', 'Event Brief'
    NEWS = 'news', 'News Brief'

# Model for briefs (one brief per type per user per day)
class Brief(models.Model):
    b_id = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    ru_id = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE)  # Link to the user
    b_brief_type = models.CharField(
        max_length=10, 
        choices=BriefType.choices
    )  # Type of brief (ENUM-like)
    b_date = models.DateField(default=timezone.now)  # Date of the brief
    b_content = models.TextField()  # AI-generated brief content
    b_created_at = models.DateTimeField(auto_now_add=True)  # When the brief was generated

    class Meta:
        unique_together = ('ru_id', 'b_brief_type', 'b_date')  # Ensures one brief per type per user per day

    def __str__(self):
        return f"{self.get_b_brief_type_display()} for {self.ru_id} on {self.b_date}"
    
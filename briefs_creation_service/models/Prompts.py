from django.db import models

# Model for storing prompts for engineering purposes
class Prompt(models.Model):
    p_name = models.CharField(max_length=50, unique=True)  # Unique identifier for the prompt (e.g., "task_prompt")
    p_text = models.TextField()  # The actual prompt text for OpenAI
    p_created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of creation
    p_updated_at = models.DateTimeField(auto_now=True)  # Timestamp of last update

    def __str__(self):
        return f"Prompt: {self.p_name}"

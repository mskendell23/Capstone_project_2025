from django.db import models

# Create models with fields.
class Quote(models.Model):
    CATEGORY_CHOICES = [
        ("Motivation", "Motivation and Life Wisdom"),
        ("Love", "Love & Relationships"),
        ("Faith", "Faith & Religion"),
    ]

    text = models.TextField()
    author = models.CharField(max_length=255, blank=True, null=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:50]}... - {self.author}"

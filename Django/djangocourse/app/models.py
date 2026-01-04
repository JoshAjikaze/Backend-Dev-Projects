from django.db import models
from django.contrib.auth.models import AbstractUser

ARTICLE_STATUS = (
    ("draft", "Draft"),
    ("inprogress", "In Progress"),
    ("published", "Published"),
)


# Create your models here.
class CustomUserModel(AbstractUser):
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="customuser_set",  # <--- Add this line
        blank=True,
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
        related_query_name="user",
    )

    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="customuser_permissions_set",  # <--- It's also a good idea to add one here for user_permissions
        blank=True,
        help_text="Specific permissions for this user.",
        related_query_name="user",
    )


class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(blank=True)
    word_count = models.IntegerField()
    twitter_post = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=ARTICLE_STATUS, default="draft")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

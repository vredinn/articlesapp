from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=255, blank=False)
    description = models.TextField(blank=True)
    public_date = models.DateTimeField(
        blank=False, auto_now_add=True
    )  # Changed to DateTimeField
    image = models.ImageField(upload_to="images", blank=True)
    category = models.ForeignKey(
        Category,
        related_name="articles",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.id} {self.title}"


class Comment(models.Model):
    article = models.ForeignKey(
        Article, related_name="comments", on_delete=models.CASCADE
    )
    username = models.CharField(max_length=255, blank=False)
    comment_date = models.DateTimeField(
        blank=False, auto_now_add=True
    )  # Changed to DateTimeField
    comment_text = models.TextField(blank=False)

    def __str__(self):
        return f"{self.username} в {self.comment_date} в статье {self.article}"

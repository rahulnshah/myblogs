from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class CodeSnippet(models.Model):
    LANGUAGE_CHOICES = [
        ('python', 'Python'),
        ('javascript', 'JavaScript'),
        ('html', 'HTML'),
        ('css', 'CSS'),
        ('java', 'Java'),
        ('cpp', 'C++'),
        ('csharp', 'C#'),
        ('ruby', 'Ruby'),
        ('php', 'PHP'),
        ('swift', 'Swift'),
        ('go', 'Go'),
        ('rust', 'Rust'),
        ('sql', 'SQL'),
    ]
    
    post = models.ForeignKey(Post, related_name='snippets', on_delete=models.CASCADE)
    language = models.CharField(max_length=50, choices=LANGUAGE_CHOICES, default='python')
    description = models.CharField(max_length=200, blank=True)
    code = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Code snippet for {self.post.title}"


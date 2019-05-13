from django.db import models

# Create your models here.
class Fest(models.Model):
    date = models.IntegerField()
    place = models.CharField(max_length=20)
    booth_num = models.IntegerField()
    name = models.CharField(max_length=50)
    sold_out = models.IntegerField()
    password = models.IntegerField()
    detail = models.TextField()

    def __str__(self):
        return self.name

class Board(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Comment(models.Model):
    post = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, related_name = 'comments')
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_contents = models.CharField(max_length=400)
    dropdown = models.CharField(max_length=10)

    class Meta:
        ordering = ['-comment_date']

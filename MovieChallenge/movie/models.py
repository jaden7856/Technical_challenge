from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    rating = models.CharField(max_length=50, blank=True, null=True)
    genres = models.CharField(max_length=100)
    summary = models.TextField(blank=True, null=True)
    reviews = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = "Movies"
    

class MovieReviews(models.Model):
    movie = models.ForeignKey("Movie", on_delete=models.CASCADE)
    text = models.TextField(blank=True, null=True)
    rating = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "Reviews"
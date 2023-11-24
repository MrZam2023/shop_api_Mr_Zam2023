from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


    @property
    def rating(self):
        stars = [review.stars for review in self.reviews.all() if review.stars is not None]
        if not stars:
            return 0
        else:
            return round(sum(stars) / len(stars), 2)

class Review(models.Model):
    text = models.TextField(null=True)
    stars = models.IntegerField(choices=([i, i ] for i in range(1, 6)), default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return self.text
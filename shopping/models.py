from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class List(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ListItem(models.Model):
    title = models.CharField(max_length=127)
    category = models.ForeignKey(
        Category,
        related_name="list_items",
        on_delete=models.CASCADE)
    parent = models.ForeignKey(
        List,
        related_name='items',
        on_delete=models.CASCADE
    )
    last_used = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} ({self.category})'
    


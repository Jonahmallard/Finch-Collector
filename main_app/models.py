from django.db import models

from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Finch(models.Model): 
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    age = models.IntegerField()
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id': self.id})

class Feeding(models.Model):
    date = models.DateField('feeding date')
    meal = models.CharField(
      max_length=1,
      # add the 'choices' field option
      choices=MEALS,
      # set the default value for meal to be 'B'
      default=MEALS[0][0]
    )
    # Create a finch_id FK
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)
    
    def __str__(self):
        # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_meal_display()} on {self.date}"
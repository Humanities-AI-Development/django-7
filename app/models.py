from django.db import models

class App(models.Model):
    title=models.CharField(max_length=100)
    text=models.TextField()
    degree=models.CharField(
        max_length=100,
        choices=(('0','0%'),('10','10%'),("20","20%"),("30","30%"),
        ("40","40%"),("50","50%"),("60","60%"),("70","70%"),("80","80%"),
        ("90","90%"),("100","100%"),("120","limit-break"),),
        null=True,
    )
    
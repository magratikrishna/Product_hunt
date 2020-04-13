from django.db import models
from django.contrib.auth.models import User
# We are calling a hunter but this is going to be a user, so in order to have this work we need to import a user model
# we don't have model that we created but Django has

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete = models.CASCADE)
# hunter is gonna be equal to a foreign key, this is basically you are on way to connect multiple models inside of a database.
# which is saying okay the hunter should be an actual user objet over here in a database, the foreign key is basically
# saying get the idea of other models so we can reference it. So what actually gonna store here inside of the database, inside
#  of a product is the ID number of the different user when it comes to the hunter right here. so just remeber if you're in a
# particular model in a database, class table whatever you wanna call it, it has an ID which can also be called a primary key,
# if you have one property pointing to another model it's called a foreign key of it points to the ID of another property,
# it's kind of primary key and foreign key.....

# There are different kinds of delete out there, in our case here if the user delete their accounts their products also get deleted.

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %y')

# Product class

# title
# url
# pub_date
# votes_total
# image
# icon
# body
# pub_date_pretty
# hunter

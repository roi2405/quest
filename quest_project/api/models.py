from django.db import models
import string
import random

from api.constants import EDUCATION_MAX_LENGTH, NAME_MAX_LENGTH, OCCUPATION_MAX_LENGTH, CITY_MAX_LENGTH, COUNTRY_MAX_LENGTH, USER_ID_LENGTH

def is_unique_user_id_possible():
    return True  # should implement

def generate_unique_user_id():
    if not is_unique_user_id_possible():
        raise ValueError("Can't create a user, need to increase the user_id length.")
    
    while True:
        user_id = "".join(random.choices(string.ascii_uppercase, k=USER_ID_LENGTH))
        if User.objects.filter(user_id=user_id).count() == 0:  # doesn't exist in the database.
            return user_id
        
def get_all_class_fields(class_, fields_to_remove=None):
    if fields_to_remove is None:
        fields_to_remove = []
    
    class_fields = [field for field in dir(class_) if not (field.startswith('__') and field.endswith('__'))]  # filtering all the default attrs.
    for field in fields_to_remove:
        if field in class_fields:
            class_fields.remove(field)
    return tuple(class_fields)

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=NAME_MAX_LENGTH, unique=False, default="")
    # education = models.CharField(max_length=EDUCATION_MAX_LENGTH, unique=False, default="")
    # occupation = models.CharField(max_length=OCCUPATION_MAX_LENGTH, unique=False, default="")
    # city = models.CharField(max_length=CITY_MAX_LENGTH, unique=False, default="")
    # country = models.CharField(max_length=COUNTRY_MAX_LENGTH, unique=False, default="")
    # user_id = models.CharField(max_length=USER_ID_LENGTH, unique=True, default=generate_unique_user_id)  # maybe use 'id' and 'primary_key=True'
    created_at = models.DateField(auto_now_add=True)

    #should be hidden if viewing a user and not creating one.
    # mail = models.CharField(max_length=NAME_MAX_LENGTH, unique=True, null=True)

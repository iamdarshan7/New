from django.db import models
# Create your models here.


# for about.html

class AboutSec1(models.Model):
    sec1_title = models.CharField(max_length=100, )
    sec1_image = models.ImageField(upload_to="Images/")
    
    
    def __str__(self):
        return self.sec1_title
    
    


class AboutSec2(models.Model):
    sec2_title  = models.CharField(max_length=100, blank=True, null=True)
    sec2_desc = models.TextField(blank=True, null=True)
    sec2_dynamic_image = models.ImageField(upload_to="Images/", blank=True, null=True)
    sec2_dynamic_title  = models.CharField(max_length=100)
    sec2_dynamic_desc = models.TextField()
    
    Icon_choice = (
    ("computer", "computer"),
    ("support", "support"),
    ("process", "process"),
    ("development", "development"),
    )


    sec2_dynamic_icon_choice = models.CharField(max_length=11, choices=Icon_choice)

    def __str__(self):
        return self.sec2_dynamic_title

    



class AboutSec3(models.Model):
    sec3_title  = models.CharField(max_length=100, blank=True, null=True)
    sec3_desc = models.TextField( blank=True, null=True)
    sec3_dynamic_title  = models.CharField(max_length=100)
    sec3_dynamic_desc = models.TextField()
    sec3_dynamic_image = models.ImageField(upload_to="Images/")

    def __str__(self):
        return self.sec3_dynamic_title

     
    

    

class AboutSec4(models.Model):
    sec4_title = models.CharField(max_length=100, blank=True, null=True)
    sec4_image = models.ImageField(upload_to="Images/", blank=True)
    sec4_dynamic_value = models.IntegerField()
    sec4_dynamic_title  = models.CharField(max_length=100)
    sec4_dynamic_desc = models.TextField()
    sec4_dynamic_image = models.ImageField(upload_to="Images/", blank=True, null=True)

    def __str__(self):
        return self.sec4_dynamic_title

     
    
   

class AboutSec5(models.Model):
    sec5_title = models.CharField(max_length=100,blank=True, null=True)
    sec5_desc = models.TextField(blank=True, null=True)
    sec5_dynamic_desc = models.TextField()
    sec5_dynamic_title  = models.CharField(max_length=100)
    sec5_dynamic_image = models.ImageField(upload_to="Images/", blank=True, null=True)
    
    def __str__(self):
        return self.sec5_dynamic_title


class AboutSec6(models.Model):
    sec6_title = models.CharField(max_length=100, blank=True, null=True)
    sec6_dynamic_image = models.ImageField(upload_to="Images/")
    sec6_dynamic_desc = models.TextField(blank=True, null=True)
    sec6_dynamic_name_person  = models.CharField(max_length=100)
    sec6_dynamic_profession  = models.CharField(max_length=100)
    
    def __str__(self):
        return self.sec6_dynamic_profession

      


        # for team.html

class Teamsec1(models.Model):
    sec1_title = models.CharField(max_length=100)
    sec1_image = models.ImageField(upload_to="Images/")

    def __str__(self):
        return self.sec1_title

class Teamsec2(models.Model):
    sec2_title = models.CharField(max_length=100, blank=True, null=True)
    sec2_name = models.CharField(max_length=100)
    sec2_image = models.ImageField(upload_to="Images/")

    def __str__(self):
        return 'Team Section 2 with {}'.format(self.sec2_name)


    

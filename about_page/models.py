from django.db import models
from ckeditor.fields import RichTextField

class Navigation(models.Model):
  is_active = models.BooleanField(default=True,unique=True,null=True)
  logo = models.ImageField(upload_to="Images/") 

class AboutMain(models.Model):
   is_active = models.BooleanField(default=True,unique=True,null=True) 
   top_heading = models.CharField(max_length=100)
   top_bg_image = models.ImageField(upload_to="Images/", null=True)

   sec1_title = models.CharField(max_length=100)
   sec1_desc = RichTextField()

   Icon_choice = (
    ("computer", "computer"),
    ("support", "support"),
    ("process", "process"),
    ("development", "development"),
    )
   sec1_inner1_image = models.ImageField(upload_to="Images/", null=True) 
   sec1_inner1_icon_choice = models.CharField(max_length=11, choices=Icon_choice) 
   sec1_inner1_title = models.CharField(max_length=100)
   sec1_inner1_desc = RichTextField()
   sec1_inner1_sub_desc = RichTextField()
   sec1_inner2_icon_choice = models.CharField(max_length=11, choices=Icon_choice) 
   sec1_inner2_title = models.CharField(max_length=100)
   sec1_inner2_desc = RichTextField()
   sec1_inner2_sub_desc = RichTextField()
   sec1_inner2_image = models.ImageField(upload_to="Images/", null=True) 
   sec1_inner3_icon_choice = models.CharField(max_length=11, choices=Icon_choice) 
   sec1_inner3_title = models.CharField(max_length=100)
   sec1_inner3_desc = RichTextField()
   sec1_inner3_sub_desc = RichTextField()
   sec1_inner3_image = models.ImageField(upload_to="Images/", null=True) 
   sec1_inner4_icon_choice = models.CharField(max_length=11, choices=Icon_choice) 
   sec1_inner4_title = models.CharField(max_length=100)
   sec1_inner4_desc = RichTextField()
   sec1_inner4_sub_desc = RichTextField()
   sec1_inner4_image = models.ImageField(upload_to="Images/", null=True) 
   
   sec2_title = models.CharField(max_length=100)
   sec2_desc = RichTextField()

   sec3_heading = models.CharField(max_length=100)
   sec3_bg_image = models.ImageField(upload_to="Images/", null=True)
   sec3_inner1_title = models.CharField(max_length=100)
   sec3_inner1_desc = RichTextField()
   sec3_inner1_value = models.IntegerField()
   sec3_inner2_title = models.CharField(max_length=100)
   sec3_inner2_desc = RichTextField()
   sec3_inner2_value = models.IntegerField()
   sec3_inner3_title = models.CharField(max_length=100)
   sec3_inner3_desc = RichTextField()
   sec3_inner3_value = models.IntegerField()
   sec3_inner4_title = models.CharField(max_length=100)
   sec3_inner4_desc = RichTextField()
   sec3_inner4_value = models.IntegerField()

   sec4_heading = models.CharField(max_length=100)
   sec4_title = models.CharField(max_length=100) 
   sec4_inner1_title = models.CharField(max_length=100)
   sec4_inner1_desc = RichTextField()
   sec4_inner2_title = models.CharField(max_length=100)
   sec4_inner2_desc = RichTextField()
   sec4_inner3_title = models.CharField(max_length=100)
   sec4_inner3_desc = RichTextField()
   sec4_inner4_title = models.CharField(max_length=100)
   sec4_inner4_desc = RichTextField()
   
   sec5_heading = models.CharField(max_length=100)
   sec5_bg_image = models.ImageField(upload_to="Images/", null=True) 
  
   def __str__(self):
     return self.top_heading


class AboutCarousel(models.Model):
   sec2_inner_title = models.CharField(max_length=100)
   sec2_inner_desc = RichTextField()
   sec2_inner_image = models.ImageField(upload_to="Images/", null=True)

   sec5_inner_name = models.CharField(max_length=100)
   sec5_inner_profession = models.CharField(max_length=100)
   sec5_inner_desc = RichTextField()
   sec5_inner_sub_desc = RichTextField()
   sec5_inner_image = models.ImageField(upload_to="Images/", null=True)
  


  #  for team.html
class Teamsec1(models.Model):
    is_active = models.BooleanField(default=True,unique=True,null=True) 
    sec1_title = models.CharField(max_length=100)
    sec1_image = models.ImageField(upload_to="Images/")

    def __str__(self):
        return self.sec1_title

class Teamsec2(models.Model):
    sec2_title = models.CharField(max_length=100)
    sec2_name = models.CharField(max_length=100)
    sec2_image = models.ImageField(upload_to="Images/")

    def __str__(self):
        return self.sec2_title

  # For mission-and-vision.html
class MissionVision(models.Model):
   top_heading = models.CharField(max_length=100)
   top_bg_image = models.ImageField(upload_to="Images/")
   


  #  For Testimonial.html
class Testimonial(models.Model):
  is_active = models.BooleanField(default=True,unique=True,null=True) 
  top_heading = models.CharField(max_length=100)
  top_bg_image = models.ImageField(upload_to="Images/")

  sec_title = models.CharField(max_length=100)
  sec_desc  = RichTextField()

  def __str__(self):
    return self.top_heading


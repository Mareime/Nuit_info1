from django.db import models

# Create your models here.
class Compt(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=10,default='user')
    
class Question(models.Model):
    les_question=models.TextField()
    choix1=models.CharField(max_length=255)
    choix2=models.CharField(max_length=255)
    choix3=models.CharField(max_length=255)
    reponce_user=models.CharField(max_length=255)
    vrai_reponce=models.CharField(max_length=255)
    id_compt=models.ForeignKey('Compt',on_delete=models.CASCADE)

class Fiche(models.Model):
    nom=models.FileField(upload_to='pdf/')
    id_compt=models.ForeignKey('Compt',on_delete=models.CASCADE)
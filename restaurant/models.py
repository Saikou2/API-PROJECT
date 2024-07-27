from django.db import models
import uuid

# Create your models here.
class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=11,null=True)
    address = models.TextField(blank=True)


class Commande(models.Model):
    num_commande = models.UUIDField(default=uuid.uuid4)
    client = models.ForeignKey(Client, related_name='commandes', on_delete=models.CASCADE)

class Menu(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    prix = models.FloatField()
    commande = models.ManyToManyField(Commande)

class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    address = models.TextField(blank=True)

class Produit(models.Model):
    libelle = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    prix = models.FloatField()
    fournisseur = models.ForeignKey(Fournisseur, related_name='produits', on_delete=models.CASCADE)
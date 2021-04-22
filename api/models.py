from django.db import models



class Tutor(models.Model):
    razao_social = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=14)
    email = models.EmailField(max_length=50)
    telefone = models.CharField(max_length=50)
    endereco = models.CharField(max_length=100)


    def __str__(self):
        return self.razao_social

class Pet(models.Model):
    
    ESPECIES = [
        ('0', "Cachorro"),
        ('1', "Gato"),
        ('2', "Pássaro"),
    ]

    PORTE = [
        ('P', 'Pequeno'),
        ('M', 'Médio'),
        ('G', 'Grande'),
    ]

    SEXO = [
        ('M', 'Masculino'),
        ('F', 'Médio'),
    ]

    PESO = [
        ('P','1 ~ 7kg'),
        ('M','7 ~ 18kg'),
        ('G','> 18kg'),
    ]

    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100, blank=False, null=False)
    especie = models.CharField(max_length=20, choices=ESPECIES)
    raca = models.CharField(max_length=30)
    idade = models.IntegerField()
    sexo = models.CharField(max_length=10)
    porte = models.CharField(max_length=20, choices=PORTE)
    peso = models.CharField(max_length=20, choices=PESO)
    descricao = models.TextField()

    def __str__(self):
        return self.name
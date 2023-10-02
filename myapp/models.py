from django.db import models

class Evento(models.Model):
    nome = models.CharField(max_length=200)
    date_pub = models.DateTimeField("My datetime")
    organizador = models.ForeignKey(
        'User',
        on_delete=models.CASCADE,
    )

class Palestrante(models.Model):
    user_id = models.ForeignKey(
        "Users",
        on_delete=models.CASCADE,
    )
class Atividade(models.Model):
    descricao = models.TextField()
    nome = models.CharField(max_length=200)
    nome = models.CharField(max_length=200)
    data_pub = models.DateTimeField("My datetime")
    inicio = models.DateTimeField("My datetime")
    fim = models.DateTimeField("My datetime")
    palestrante = models.ForeignKey(
        'Palestrante',
        on_delete=models.CASCADE,
    )

class Participante(models.Model):
    user = models.ForeignKey(
        'Users',
        on_delete=models.CASCADE,
    )
    Atividade = models.ForeignKey(
        'Atividade',
        on_delete=models.CASCADE,
    )
    data_reg = models.DateTimeField("My datetime")
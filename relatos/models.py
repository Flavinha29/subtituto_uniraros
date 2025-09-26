from django.db import models
from django.conf import settings
from django.utils import timezone


class Relato(models.Model):
    paciente = models.ForeignKey('accounts.Paciente', on_delete=models.CASCADE, related_name='relatos')
    titulo = models.CharField(max_length=255)
    texto = models.TextField()
    data_postagem = models.DateTimeField(default=timezone.now)
    aprovado = models.BooleanField(default=False)  # aprovação pelo admin
    publicado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    relato = models.ForeignKey(Relato, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    texto = models.TextField()
    data = models.DateTimeField(default=timezone.now)

class Curtida(models.Model):
    relato = models.ForeignKey(Relato, on_delete=models.CASCADE, related_name='curtidas')
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('relato', 'usuario')

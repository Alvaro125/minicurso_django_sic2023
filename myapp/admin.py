from django.contrib import admin

from .models import Atividade,Evento,Palestrante,Participante

admin.site.register(Atividade)
admin.site.register(Evento)
admin.site.register(Participante)
admin.site.register(Palestrante)


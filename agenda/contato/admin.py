from __future__ import unicode_literals
from django.contrib import admin
from agenda.contato.models import Contato, Tarefa, Conta

class ContatoAdmin(admin.ModelAdmin):
    model = Contato
    list_display = ['contato_nome', 'contato_nascimento', 'contato_email', 'contato_estado_civil', 'contato_favorito']
    list_filter = ['contato_sexo', 'contato_estado_civil']
    search_fields = ['contato_nome']
    save_on_top = True
admin.site.register(Contato, ContatoAdmin)

class TarefaAdmin(admin.ModelAdmin):
    model = Tarefa
    list_display = ['tarefa_nome', 'tarefa_data_inicio', 'concluido']
    search_fields = ['tarefa_nome']
    save_on_top = True
admin.site.register(Tarefa, TarefaAdmin)

class ContaAdmin(admin.ModelAdmin):
    model = Conta
    list_display = ['conta_nome', 'conta_data_vencimento', 'pago']
    search_fields = ['conta_nome']
    list_filter = ['pago']
    save_on_top = False
admin.site.register(Conta, ContaAdmin)



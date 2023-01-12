from django.contrib import admin

from api.models import Tutor, Pet


admin.site.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    fields = ('razao_social', 'cnpj', 'email', 'telefone', 'endereco')
    

admin.site.register(Pet)
class PetAdmin(admin.ModelAdmin):
    fields = ('tutor', 'name', 'especie', 'raca', 'idade', 'sexo', 'porte', 'peso', 'descricao')

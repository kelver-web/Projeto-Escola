from django.contrib import admin
from .models import Aluno, Turma, Disciplina, Professor

# Register your models here.

class AlunoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobrenome', 'sexo', 'status', 'turma', 'data_de_admissao']

class TurmaAdmin(admin.ModelAdmin):
    list_display = ['nome']

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'sobrenome', 'email', 'telefone']

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Turma, TurmaAdmin)
admin.site.register(Disciplina)
admin.site.register(Professor, ProfessorAdmin)

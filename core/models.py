from django.db import models
from django.utils import timezone

# Create your models here.
class Professor(models.Model):
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    email = models.EmailField()
    telefone = models.CharField(max_length=11)

    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'

    def __str__(self):
        return self.nome


class Disciplina(models.Model):
    nome = models.CharField(max_length=100)
    professor = models.ForeignKey('Professor', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Disciplinas'

    def __str__(self):
        return self.nome


class Turma(models.Model):
    nome = models.CharField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"
        

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    STATUS = (
        ("ativo", "Ativo"),
        ("inativo", "Inativo"),
    )
    SEXO = (
        ("M", "Masculino"),
        ("F", "Feminino"),
    )
    numero_registro = models.CharField('Número de registro',max_length=200, unique=True)
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    data_nasc = models.DateField('Data de nascimento', default=timezone.now)
    sexo = models.CharField('Sexo', max_length=1, choices=SEXO, default='Masculino')
    data_de_admissao = models.DateField('Data de admissão', default=timezone.now)
    telefone = models.CharField('telefone', max_length=11)
    endereco = models.CharField('endereço', max_length=200)
    turma = models.ForeignKey('Turma', on_delete=models.CASCADE)
    disciplina = models.ManyToManyField('Disciplina')
    status = models.CharField('status', max_length=7, choices=STATUS, default='ativo')

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return f'{self.nome} {self.sobrenome}'

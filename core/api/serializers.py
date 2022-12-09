from rest_framework.serializers import ModelSerializer
#from rest_framework.fields import SerializerMethodField
from core.models import Aluno, Turma, Disciplina, Professor




class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'


class AlunoDetailSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'
        depth = 2


class EditarlunoSerializer(ModelSerializer):
    disciplina = AlunoDetailSerializer(many=True)
    class Meta:
        modol = Aluno
        fields = '__all__'


class TurmaSerializer(ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'


class DisciplinaSerializer(ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'


class DisciplinaDetailSerializer(ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'
        depth = 1

    
class ProfessorSerializer(ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'
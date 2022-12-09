from rest_framework.viewsets import ModelViewSet
from core.models import Aluno, Turma, Disciplina, Professor
from .serializers import (AlunoSerializer, AlunoDetailSerializer, TurmaSerializer,
                          DisciplinaSerializer, DisciplinaDetailSerializer, ProfessorSerializer)


class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    
    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return AlunoDetailSerializer
        return AlunoSerializer


class TurmaViewSet(ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer


class DisciplinaViewSet(ModelViewSet):
    queryset = Disciplina.objects.all()
    #serializer_class = DisciplinaSerializer
    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return DisciplinaDetailSerializer
        return DisciplinaSerializer


class ProfessorViewSet(ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
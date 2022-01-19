from django.db import models
from django.conf import settings



class Course(models.Model):
    nome = models.CharField('Nome',max_length=100)
    slug = models.SlugField('Atalho')
    descricao = models.TextField('Descrição Simples', blank=True)
    about=models.TextField('Sobre o Curso',blank=True)
    data_inicio =  models.DateField('Data de Inicio',null=True , blank=True)
    image =  models.ImageField(upload_to='images',verbose_name='imagem' ,null=True,blank=True)
    created_at = models.DateTimeField('Criado em ' , auto_now=True)
    update_at = models.DateTimeField('Atualizado em ' , auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name='Curso'
        verbose_name_plural='Cursos'
        ordering=['nome']

class Enrollment(models.Model):
    STATUS_CHOICES =(
        (0,'Pendente'),
        (1,'Aprovado'),
        (2,'Cancelado'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL,verbose_name="Usuário",related_name="enrollments",on_delete=models.CASCADE)
    course = models.ForeignKey(Course,verbose_name="Curso",related_name="enrollments",on_delete=models.CASCADE)
    status = models.IntegerField('Situação',choices= STATUS_CHOICES , default=1, blank=True)
    created_at = models.DateTimeField('Criado em ' , auto_now=True)
    update_at = models.DateTimeField('Atualizado em ' , auto_now=True)
    
    class Meta:
        verbose_name="Inscrição"
        verbose_name_plural="Inscrições"
        unique_together=(('user','course'),)

    def active(self):
        self.status = 1
        self.save()



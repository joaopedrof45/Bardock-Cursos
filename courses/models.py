from django.db import models



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





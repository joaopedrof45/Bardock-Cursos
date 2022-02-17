from rest_framework import viewsets, permissions
from accounts.ContasSerializador import ContasSerializer
from accounts.models import User , PasswordReset
 

class UserViewSet(viewsets.ModelViewSet):
  queryset =  User.objects.all()
  serializer_class = ContasSerializer
  permission_classes = [permissions.IsAuthenticated]
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

class CustomeAuth(ObtainAuthToken):
    def post(self,request,*args,**kwargs):
        serailizer=self.serializer_class(data=request.data,context=({'request':request}))
        serailizer.is_valid(raise_exception=True)
        user=serailizer.validated_data['user']
        token,created=    Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,
            'user_id':user.pk,
            'email':user.email
        })
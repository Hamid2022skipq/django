from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *


class ReactView(APIView):
    # Get all user
    def get(self, request):
        id = request.data.get('id')
        print(id)
        if id:
            output=React.objects.get(pk=id)
            return Response({'id': output.id, "employee": output.employee, "department": output.department})
        
        output = [{'ID': output.id, "employee": output.employee, "department": output.department}
                  for output in React.objects.all()]
        return Response(output)
    

    # Create
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message': 'Data received successfully'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'msg': 'Error'},status=status.HTTP_204_NO_CONTENT)
    
    # Delete
    def delete(self, request):
        id = request.data.get('id')
        try:
            record = React.objects.get(pk=int(id))
            record.delete()
        except React.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class updateReact(APIView):
    def get(self, request, id):
        print(id)
        try:
            output = React.objects.get(pk=id)
            return Response({'id': output.id, "employee": output.employee, "department": output.department})
        except React.DoesNotExist:
            return Response({"error": "Record not found"}, status=404)
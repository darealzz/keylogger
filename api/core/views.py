from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


@api_view(['GET'])
def create_session(request, client):
    """
    Creates Session if no session exists.
    If a session already exists for the client, it will join the session.

    returns session ID
    """

    print(client)
    return JsonResponse({'foo': 'asd'})

class LoggerView(APIView):
    #https://simpleisbetterthancomplex.com/tutorial/2018/11/22/how-to-implement-token-authentication-using-django-rest-framework.html

    permission_classes = (IsAuthenticated)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)    

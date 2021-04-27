from django.http.response import JsonResponse, HttpResponse
from django.core import serializers
from .models import Article

# Create your views here.
def article_list(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data)


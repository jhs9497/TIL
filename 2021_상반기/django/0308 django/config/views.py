from django.http import HttpResponse


def index(request):
    return HttpResponse('안녕하세요!!!')


def greeting(request):
    return HttpResponse('반가워요 ㅎㅎ')
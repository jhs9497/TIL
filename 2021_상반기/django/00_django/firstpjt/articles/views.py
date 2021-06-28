from django.shortcuts import render

# Create your views here.
def index(request): # 첫번째 인자는 반드시 request
    return render(request, 'index.html') # render 함수의 첫번째 인자도 반드시 request
                                         # 장고는 templates까지의 경로는 알고 있기 때문에
                                         # 그 다음의 경로인 inde.html을 그대로 넣어주면 됨

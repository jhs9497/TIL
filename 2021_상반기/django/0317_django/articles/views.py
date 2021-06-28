from django.shortcuts import render, redirect

from .models import Article
# from ??? import ??? # Form 사용을 위해 import

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def detail(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


def delete(request, pk):
    article = Article.objects.get(id=pk)

    # article.delete()
    # POST 로 요청 처리
    if request.method == 'POST':
        article.delete()

    return redirect('articles:index')


# 아래에서 부터 주석을 해제 하면서 ??? 를 채워가면 됩니다.


# def new(request):
#     form = ???
#     context = {
#         'form': form
#     }
#     return render(request, 'articles/new.html', context)



# def create(request):
#     # 데이터를 받아 DB에 저장할 때
#     if request.method == ???:
#         form = ???
#         # 유효성 검사
#         if form.???:
#             # DB에 저장
#             article = ???
#             # 디테일 페이지로 이동
#             return redirect(???)
#     # form 을 보여줄 때
#     else:
#         form = ???
    
#     # context의 위치는 어디에? else 안쪽? 바깥쪽?
#         # context = {
#         #     'form': form,
#         # }
#     return render(request, 'articles/new.html', context)




# def update(???):
#     # 데이터를 수정하기 위해 data를 가져온다.
#     ???

#     # 데이터를 DB에 저장 할 때
#     if ???:
#         # 기존 DB에 저장된 데이터의 값을 입력 값으로 변경.
#         form = ArticleForm(???)
#         # 입력 값이 올바른지 유효성 검사
#         if ???:
#             # DB에 저장
#             ???
#             return redirect('articles:detail', article.pk)
    
#     else:
#         # 기존 값을 입력 폼에 넣어준다.
#         form = ArticleForm(???)

#     context = {
#         'form': form,
#         ???
#     }
#     return render(request, 'articles/update.html', context)



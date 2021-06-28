from django.shortcuts import render

# Create your views here.
def index(request):
    # html 파일은 반드시 templates 폴더 안에 위치해야 합니다. 
    articles = [
        {'title': '1번 게시글',
        'content': '1번 게시글 내용'},
        {'title': '2번 게시글',
        'content': '2번 게시글 내용'},
        {'title': '3번 게시글',
        'content': '3번 게시글 내용'},
    ]
    # templates 경로까지는 자동으로 추적 가능하므로 index.html이라고만 적어준다
    return render(request, 'index.html', { 'articles': articles, })

def detail(request, article_id): # urls.py articles에 지정한 변수이름과 같게 article_id
    return render(request, 'detail.html', { 'article_id': article_id})


def write(request):
    '''
    from 태그가 담긴
    게시글 작성 페이지를 사용자에게 응답해줍니다.
    '''
    return render(request, 'write.html')


def save(request):
    '''
    사용자가 작성한 게시글을 받아서 저장합니다.
    '''
    # GET 요청으로 들어온 사용자 입력 정보가 담겨있는 유사 딕셔너리
    title = request.GET.get('title')
    content = request.GET.get('content')
    context = {
        'title' : title,
        'content' : content,
    }
    return render(request, 'save.html', context)
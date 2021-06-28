####  1. form의 모든 각 필드를 테이블 행으로 렌더링받을 때 (a)빈 칸을 채우시오

```html
{% extends 'base.html' %}
  
{% block content %}
    <h1>NEW</h1>
    <form action="{% url 'articles:create' %}" method="POST">
        {% csrf_token %}
        {{ ___(a)___ }}
        <input type="submit">
    </form>
    <hr>
    <a href="{% url 'articles:index' %}">[back]</a>
{% endblock %}

```



#### 2. 앱네임/forms.py에서 create함수를 다음과 같이 코딩하였을 때 문제점을 서술하시오

```python
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST) 
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
        context = {
            'form': form,
        }
        return render(request, 'articles/create.html', context)

```



#### 3. Form과 ModelForm의 차이점에 대해 서술하시오.



#### 4. update함수에서 빈칸(a)를 채우고 그 이유에 대해 설명하시오.

```python
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        # Create a form to edit an existing Article,
        # but use POST data to populate the form.
        form = ArticleForm(request.POST, (___a___))
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        # Creating a form to change an existing article.
        form = ArticleForm(instance=article)
    context = {
        'form': form,
    }
    return render(request, 'articles/update.html', context)

```



#### 5. 데코레이터는 어떤 함수에 기능을 추가하고 싶을 때, 해당 함수를 직접 수정하지 않고 기능을 연장하게 해주는 함수이다. view가 GET과 POST 요청 method만 허용하도록 하려면 def위에 어떤 데코레이터를 추가해야 하는가


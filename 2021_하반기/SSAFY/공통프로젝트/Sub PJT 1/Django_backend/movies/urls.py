from django.urls import path
from . import views


urlpatterns = [
    # 장르, 영화 API서버를 통해 db저장하기
    path('getGenre/', views.getGenre),
    path('getMovie/', views.getMovie),

    # db에 저장된 친구들 serializers통해 불러오기

    # 장르 <-> 가져오기
    path('movie/genre/<int:genre_id>/', views.movie_genre),
    path('movie/genre/', views.all_movie_genre),

    # 전체영화목록 불러오기
    path('movie/', views.movie_list),
    # 개별 영화 하나씩 불러오기
    path('movie/<int:movie_id>/', views.movie_detail),

    # comment 전체 조회 및 추가 
    path('movie/<int:movie_id>/comment/', views.comment_list),
    path('movie/<int:movie_id>/comment/<int:comment_id>/', views.comment_detail),

    # user별로 불러오기
    path('movie/<int:user_id>/comment/user/', views.comment_list_by_user),
]

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Genre, Movie, Comment
import requests
from .serializers import(
    MovieListSerializer,
    MovieSerializer,
    CommentListSerializer,
    CommentSerializer,
    GenreSerializer,
)
from movies import serializers


# Create your views here.
MYKEY = 'fb9a96092cd1259e59917287f35839c8'

def getGenre(request):
    genreURL = f'https://api.themoviedb.org/3/genre/movie/list?api_key={MYKEY}&language=ko-KR'
    allGenre = requests.get(genreURL)
    datas = allGenre.json().get('genres')
    for data in datas:
        Genre.objects.get_or_create(
            id = data.get('id'),
            name = data.get('name'),
        )
    return


def getMovie(request):
    # n을 변수로삼고 for문을 돌려서 충분한 양의 영화정보를 DB에 저장할 수 있도록 한다.
    for n in range(1, 20):
        movieURL = f'https://api.themoviedb.org/3/discover/movie?api_key={MYKEY}&language=ko-KR&page={str(n)}'
        # 스타트캠프 미세먼지 API 참조하며 가져오기,, 
        allMovie = requests.get(movieURL)
        # get 'results' 찾는데 시간이 좀 걸렸음 
        datas = allMovie.json().get('results')
        for data in datas:
            Movie.objects.get_or_create(
                # 원하는 친구들을 뽑아서 원하는 필드에 넣고
                movie_id = data.get('id'),
                title = data.get('original_title'),
                overview = data.get('overview'),
                release_date = data.get('release_date'),
                voteavg = data.get('vote_average'),
                # poster_path  + 하는 부분도 검색해서 알게됨
                poster_path = "https://image.tmdb.org/t/p/original"+ data.get('poster_path'),
            )
        
            # movie와 genre의 id끼리 M:N 모델을 수립하는 과정 
            # genre별 movie를 꺼내와야 하기 때문에 필요한 과정이다.
            # 해당 영화의 genre 저장해주고
            genreItems = data.get('genre_ids')
            # 지금 for문 내에 잡혀있는 movie_id의 정보들 가져온다음
            movie = Movie.objects.get(movie_id = data.get('id'))
            # 하나의 영화에 장르ID가 여러개 있기 때문에 for문을 돌려가며 추가해줘야한다
            for i in genreItems:
                p1 = get_object_or_404(Genre, pk=i)
                # M:N 필드에 추가
                movie.genres.add(p1)
    return


# 장르별로 무비 가져오기
@api_view(['GET'])
def movie_genre(request, genre_id):
    movie_genres = Movie.objects.filter(genres=genre_id)
    serializer = MovieListSerializer(movie_genres, many=True)

    return Response(data=serializer.data)

# 모든 장르 가져오기
@api_view(['GET'])
def all_movie_genre(request):
    genres = Genre.objects.all()
    serializer = GenreSerializer(genres, many=True)
    return Response(data=serializer.data)


@api_view(['GET']) # GET 요청이 올 때
def movie_list(request):
    movies = Movie.objects.all()
    # Movie 모델에 전체 데이터를 가져오고
    serializer = MovieListSerializer(movies, many=True)
    # 시리얼라이즈화 해서 serializer 변수에 저장! 디폴트값이 여러개 데이터는 못가져오니 many=True 꼭 넣어줘야함!
    return Response(data=serializer.data)
    # Response의 data키워드 인자에 serilaizer.data를 저장해서 보여주기


@api_view(['GET'])
def movie_detail(request, movie_id): # movie_id도 가져와서 
    movie = Movie.objects.get(pk=movie_id)
    # movie_id와 같은 pk값을 가진 친구만  movie에 저장하고
    serializer = MovieSerializer(movie)
    # 똑같이 진행하는데 데이터는 1개일테니 many=True 필요없음!
    return Response(data=serializer.data)


# 영화별로 댓글 불러오기
@api_view(['GET', 'POST'])
def comment_list(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    # 개별 movie 가져오고
    if request.method == 'GET':
        # 만약 GET 요청이면 ( 단순 조회면 )
        comment = Comment.objects.filter(comment_movie=movie)
        # review 중에 movie가 movie인 친구를 선별하여
        serializer = CommentListSerializer(comment, many=True)
        # 똑같이 serializer화 하여서 
        return Response(data=serializer.data)
        # 보여주기
    
    elif request.method == 'POST':
        # 만약 POST 요청이면 ( 생성하는거면 )
        serializer = CommentListSerializer(data=request.data)
        # 방금 생성해서 보낸 데이터를 ReviewListSerializer에 담은 후 저장
        if serializer.is_valid(raise_exception=True):
            # 유효성 검사 // raise_exception을 통해 잘못된 요청이 들어왔을 때 자동으로 적절한 응답 보내기
            serializer.save(comment_movie=movie)
            
            # 해당 movie에 저장
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        # 저장하고 잘 저장됐다는 의미에서 201 보내주기


# user별로 댓글 불러오기
@api_view(['GET'])
def comment_list_by_user(request, user_id):
    comment = Comment.objects.filter(comment_user=user_id)
    # review 중에 movie가 movie인 친구를 선별하여
    serializer = CommentListSerializer(comment, many=True)
    # 똑같이 serializer화 하여서 
    return Response(data=serializer.data)
    # 보여주기


@api_view(['GET', 'PUT', 'DELETE'])
def comment_detail(request, movie_id, comment_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    # 개별 무비를 가져오고
    comment = get_object_or_404(Comment, pk=comment_id, comment_movie=movie)
    # 그 무비에 해당하는 리뷰를 가져온다음
    if request.method == 'GET':
        # 요청이 GET이면
        serializer = CommentSerializer(comment)
        # serializer화 하여서 
        return Response(data=serializer.data)
        # 보여주기

    elif request.method == 'PUT':
        # 요청이 PUT이면
        serializer = CommentSerializer(comment, data=request.data, partial=True)
        # data를 현재 요청되는 data로 바꾼 후 저장
        # partial=True -> 전체를 바꾸지 않고 필드 중에 하나만 바꿔도 수정이 되도록
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(data=serializer.data)

    elif request.method == 'DELETE':
        # 요청이 'DELETE'이면
        comment.delete()
        # 삭제하고
        data = {
            'message': '성공적으로 삭제되었습니다!'
        }
        # message 띄워주기
        return Response(data=data, status=status.HTTP_204_NO_CONTENT)
        # HTTP도 No content를 이용한 204로



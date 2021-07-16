from django.db.models import manager
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from accounts import serializers

# Create your views here.
@api_view(['GET','POST'])
def signup(request):
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # Client에서 온 데이터를 받아서
        password = request.data.get('password')
        password_confirmation = request.data.get('password_confirmation')

        # 패스워드 일치 여부 체크
        if password != password_confirmation:
            return Response({'error': '비밀번호가 일치하지 않습니다'}, status=status.HTTP_400_BAD_REQUEST)

        # UserSerializer를 통해 데이터 직렬화
        serializer = UserSerializer(data=request.data)
        
        #3. validation 작업 진행 -> password도 같이 직렬화 진행
        if serializer.is_valid(raise_exception=True): # is_valid통과못할시 자동으로 에러 보여주기
            user = serializer.save()
            #4. 비밀번호 해싱 후 
            user.set_password(request.data.get('password')) # set_password -> django 내장함수 password 암호화
            user.save() # 암호화 후 저장
            # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     print('하이하이')
        #     return Response({'error': '중복된 ID가 있습니다'}, status=status.HTTP_403_FORBIDDEN)
        


@api_view(['POST'])
def userinfo(request):
    username = request.data.get('username')
    print('여기들어옴?')
    users = User.objects.filter(username=username)
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def alluserinfo(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)



        

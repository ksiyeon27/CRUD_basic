from django.shortcuts import render, HttpResponse
from .models import Post
# Create your views here.


def post_list(request):
    # Read(R)
    # 포스트들을 불러와서 리스트 형태로 보여준다
    posts = Post.objects.all()

    ctx = {'posts': posts}  # 딕셔너리 키; html로 넘어가는 스트링. 밸루; 객체개념.
    # 렌더는 입히는 것. 어떤 형태로 보이게 만든다
    return render(request, template_name='posts/list.html', context=ctx)

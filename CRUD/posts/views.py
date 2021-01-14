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


def post_detail(request, post_id):
    # Read(R)
    # 특정 포스트를 불러와서 상세정보를 보여준다

    post = Post.objects.get(id=post_id)
    ctx = {'post': post}

    return render(request, template_name='posts/detail.html', context=ctx)

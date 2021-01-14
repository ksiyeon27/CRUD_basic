from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
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


def create_post(request):
    # Create(C)
    # 포스트를 새로 생성한다
    # request method ==> GET, POST, PUT, DELETE...
    # 제일 많이 쓰는건 겟과 포스트. 주소창에 엔터 => 겟 메소드 접근 방식.
    # 네이버 블로그에서 우리가 글을 작성하고 저장 버튼을 누르는 거 =? 포스트 메소드 접근 방식.
    if request.method == 'POST':
        # 저장하기 눌렀을 때(POST)
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()  # 저장해서 db에 생성.
            # 사실 할당할 필요 없지만 사용할 일 있으려면 저장.
            return redirect('posts:list')
            # redirect는 url중 한 곳으로 보내겠다는 것. 앱네임:url네임
    else:  # 주로 겟방식이 되겠지 #글쓰기 칸을 보여주기
        form = PostForm()  # 장고의 폼을 사용하기
        ctx = {'form': form}

        return render(request, template_name='posts/post_form.html', context=ctx)


def update_post(request, pk):
    # Update
    # 포스트를 수정하는 뷰

    post = get_object_or_404(Post, id=pk)
    # 고칠려고 받아온 특정한 포스트
    # 위에꺼랑 Post.objects.get(id=pk)의 차이 : 404 에러 반환 차이/ 위에꺼를 더 많이씀. 에러 핸들링 위해.

    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()

            return redirect('posts:detail', pk)  # pk대신 post.id도 가능. 왜그런지 생각해보기
    else:
        # 그 특정한 포스트 요놈이야라고 명시! 새 객체가 아니라 원래 있던 인스턴스 불러오는 느낌.
        form = PostForm(instance=post)
        ctx = {'form': form}
        return render(request, 'posts/post_form.html', ctx)


def delete_post(request, pk):
    # Delete
    # 포스트를 삭제하는 뷰

    post = get_object_or_404(Post, pk=pk)

    if request.method == "GET":
        return redirect('posts:detail', post.id)
    elif request.method == "POST":
        post.delete()
        return redirect('posts:list')

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog

# Create your views here.


def home(request):
    blogs = Blog.objects #쿼리셋(객체드르이 목록)
    #블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 3)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    page = request.GET.get('page')
    #request된 페이지를 열어온ㄷ ㅟ return 해 준다
    posts= paginator.get_page(page)
    return render(request, 'home.html', {'blogs':blogs, 'posts':posts, 'nbar':'home', 'bar':'new' })

def detail(request, blog_id):
    details = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'details':details})

def new(request): #new를 띄워주는 함수
    return render(request, 'new.html')

def create(request): #입력받은 내용을 디비에 넣어주는 함수
    blog = Blog()
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.pub_date = timezone.datetime.now()
    blog.save() #쿼리셋 메소드중 하나인데 blog라는 객체를 저장하는 메소드 ex) 객체.delete를 하면 지워짐
    return redirect('/blog/'+str(blog.id))#다 처리하고난 후에 저기로 가라는의미 str을 형변하는 이유는 받는 블로그id는 항상 인트형이지만 url은 항상 문자열이기 때문
#render과 redirect의 차이 리다이렉트는 아예 다른 url을 입력가능하다 ex) 구글
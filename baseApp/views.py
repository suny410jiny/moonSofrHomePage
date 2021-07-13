from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import  HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages

# Create your views here.
# @login_required
from django.views.generic import ListView
from django.views.generic.edit import FormView, CreateView

from baseApp.form import PostForm, CommentForm
from baseApp.models import Post

paginate_by=12
class IndexListView(ListView):
    # timesince = timezone.now() - timedelta(days=3)
    model = Post
    template_name = "baseApp/index.html"
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page', '1')  # 페이지
        post_list = Post.objects.all().order_by('-created_at')
        paginator = Paginator(post_list, 6)  # 페이지당 10개씩 보여주기
        page_obj = paginator.get_page(page)
        context = {'post_list': page_obj}
        return context
index = IndexListView.as_view()

@login_required
def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        formset = PostForm(request.POST, request.FILES)
        if form.is_valid() and formset.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            post.tag_set.add(*post.extract_tag_list())
            messages.success(request, "포스팅을 저장했습니다.")
            return HttpResponseRedirect("/")  # To Do 상세화면으로 이동

    else:
        form = PostForm()
    return render(request, 'baseApp/post_form.html',
                  {'form': form,} )

# class PostListView(LoginRequiredMixin, ListView):
#     model=Post
#     paginate_by = 10
#     template_name = "baseApp/post_list_prod.html"
# post_list = PostListView.as_view()

class PostListViewProd(ListView):
    model = Post
    template_name = "baseApp/post_list_prod.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page', '1')  # 페이지
        post_list = Post.objects.all().filter(Q(postDivision="PD")).order_by('-created_at')
        paginator = Paginator(post_list, 6)  # 페이지당 10개씩 보여주기
        page_obj = paginator.get_page(page)
        context = {'post_list': page_obj, 'post_count': post_list.count(),}
        return context

post_list_prod = PostListViewProd.as_view()

class PostListViewProject(ListView):
    model=Post
    template_name = "baseApp/post_list_projects.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = self.request.GET.get('page', '1')  # 페이지
        post_list = Post.objects.all().filter(Q(postDivision="PJ")).order_by('-created_at')
        paginator = Paginator(post_list, 6)  # 페이지당 10개씩 보여주기
        page_obj = paginator.get_page(page)
        context = {'post_list': page_obj,'post_count':post_list.count(),}
        return context

post_list_project = PostListViewProject.as_view()

def post_detail_prod(request,pk):
    post = get_object_or_404(Post,  pk=pk) # 객체 즉 pk 가 존재 하지 않는 경우 404에러를 내기 위함
    comment_form = CommentForm()
    return render(request,"baseApp/post_detail.html",{
        'post':post,
        'comment_form' : comment_form,
    })

def post_detail_project(request,pk):
    post = get_object_or_404(Post,  pk=pk) # 객체 즉 pk 가 존재 하지 않는 경우 404에러를 내기 위함
    comment_form = CommentForm()
    return render(request,"baseApp/post_detail.html",{
        'post':post,
        'comment_form' : comment_form,
    })
# 함수 기반으로 코딩
#
# def post_list(request):
#     paginate_by = 10
#     fileSet_qs = FileSet.objects.filter(post=OuterRef("pk")).order_by("-id")
#     postDivision = request.GET['division']
#     qs = Post.objects.all().annotate(post_thumnail=Subquery(fileSet_qs.values("fileName")[:1])).filter(Q(postDivision=postDivision))
#     # 검색기능
#     q = request.GET.get('q', '')  # get 방식 없으면 '' 를 반환-''에 다른값을 넣을수 있음
#     if q:
#         qs = qs.filter(title__icontains=q)
#     # 검색기능
#     # photo = FileSet.objects.first().filter(Q(post=Post))
#     # instagram/templates/instagram/post_list_bak.html
#     return render(request, 'baseApp/post_list_bak.html', {
#         'post_list': qs,
#         'q': q,
#         'paginate_by': paginate_by,
#     })
# @login_required
# def post_new(request):
#     if request.method == 'POST':
#         form = PostForm(request.POST)
#         formset = PostForm(request.POST, request.FILES)
#         if form.is_valid() and formset.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.save()
#             post.tag_set.add(*post.extract_tag_list())
#             for file in request.FILES.getlist("file[]"):
#                 fileSet = FileSet.objects.create(post=post, fileName=file)
#                 fileSet.save()
#             messages.success(request, "포스팅을 저장했습니다.")
#             return HttpResponseRedirect("/")  # To Do 상세화면으로 이동
#
#     else:
#         form = PostForm()
#         formset = FileSetForm()
#     return render(request, 'baseApp/post_form.html',
#                   {'form': form, 'formset': formset}, )
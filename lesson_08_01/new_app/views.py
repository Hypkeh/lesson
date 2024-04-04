from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.db.models import Value, F
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, PermissionRequiredMixin
from django.db.transaction import atomic
from django.contrib import messages
from django.core.signing import TimestampSigner

from .models import Post, Author, Category
from .forms import AuthorForm, PostForm, UserRegistrationForm, SearchForm, AuthorFormset


# def login_required_decorator(view):
#     def wrapper(request):
#         if request.user.is_authenticated:
#             return view(request)
#         else:
#             return HttpResponse
#     return wrapper

def author_formset(request):
    if request.method == 'POST':
        formset = AuthorFormset(request.POST)
        if formset.is_valid():
            formset.save()
            return HttpResponse('ok')
    else:
        formset = AuthorFormset()
    messages.add_message(request, messages.ERROR, 'Введите данные об авторах')
    context = {'formset': formset}
    return render(request, 'new_app/author_formset.html', context)


class AuthorDetail(PermissionRequiredMixin, DetailView):
    model = Author
    context_object_name = 'author'
    permission_required = ['new_app.view_author']


class CategoryDetail(DetailView):
    model = Category
    context_object_name = 'category'


def search(request):
    if request.method == 'GET':
        get_data = request.GET
        form = SearchForm(get_data)
        if form.is_valid():
            q = form.cleaned_data['q']
            authors = Author.objects.filter(name__icontains=q).annotate(url_name=Value('author_detail'), obj_name=F('name'))
            posts = Post.objects.filter(title__icontains=q).annotate(url_name=Value('post_detail'), obj_name=F('title'))
            categories = Category.objects.filter(name__icontains=q).annotate(url_name=Value('category_detail'), obj_name=F('name'))
            object_list = list(authors) + list(posts) + list(categories)
            context = {'object_list': object_list}
            return render(request, 'new_app/search_list.html', context)


class UserRegisterView(FormView):
    template_name = 'new_app/author_form.html'
    form_class = UserRegistrationForm

    def post(self, request, *args, **kwargs):
        data = dict(request.POST)
        pass1 = data.pop('password1') # None
        pass2 = data.pop('password2') # None
        form = UserRegistrationForm(request.POST)
        if pass1 != pass2:
            return self.form_invalid(form)
        else:
            if form.is_valid():
                return self.form_valid(form)
            else:
                return self.form_invalid(form)

    def form_valid(self, form):
        return HttpResponse('New user has been created')


class AuthorList(ListView):
    model = Author
    paginate_by = 2

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, 'Все авторы')
        return super().dispatch(request, *args, **kwargs)


class AuthorCreate(CreateView):
    form_class = AuthorForm
    model = Author
    success_url = '/'


class PostList(LoginRequiredMixin, ListView):
    model = Post
    paginate_by = 2
    paginate_orphans = 1


def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 1, orphans=1)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {"object_list": page.object_list, "page_obj": page}
    return render(request, "new_app/post_list.html", context)


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'


class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('post_list')


class PostUpdate(UpdateView):
    model = Post
    fields = '__all__'
    success_url = reverse_lazy('post_list')


class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')
    template_name = 'new_app/post_form.html'


class MainPage(TemplateView):
    template_name = 'new_app/about.html'


def add_record(request):
    category = Category.objects.create(name='test_atomic')
    category = Category.objects.create(name='test_atomic2')
    category = Category.objects.create(name='test_atomic3')
    return HttpResponse('atomic')


def cookie_view(request):
    try:
        cnt = request.get_signed_cookie('counter')
    except KeyError:
        cnt = 0
    cnt = int(cnt) + 1
    response = HttpResponse(cnt)
    response.set_signed_cookie('counter', cnt)
    return response












    # cnt = int(request.COOKIES.get('counter', 0)) + 1
    # response = HttpResponse('COOKIES')
    # import datetime
    # ten_minutes = datetime.datetime.now() + datetime.timedelta(seconds=10)
    # response.set_cookie('counter', cnt, path='cookies/')
    # return response
    # if 'counter' in request.session:
    #     cnt = request.session['counter'] + 1
    # else:
    #     cnt = 1
    # request.session['counter'] = cnt
    # return HttpResponse(request.session['counter'])


from django.shortcuts import render,redirect,get_object_or_404
from .models import Article,Comment,Poll,NewUser
#from .forms import CommentForm,LoginForm,RegisterForm,SetInfoForm,SearchForm
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate,login,logout
from django.http import JsonResponse
from django.views.decorators.cache import cache_page
#import markdown2,urlparse


# Create your views here.
def index(request):
    latest_article_list = Article.objects.query_by_time()
    loginform = LoginForm()
    context = {'latest_article_list':latest_article_list,'loginform':loginform}
    return render(request,'index.html',context)
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from blog.forms import MessageForm
from blog.models import *


def article_list(request):
    articles = Article.objects.all()
    page_number = request.GET.get('page')
    paginator = Paginator(articles, 6)
    object_list = paginator.get_page(page_number)
    return render(request, "blog/articles_list.html", {'articles': object_list})


def article_detail(request, slug):
    articles = get_object_or_404(Article, slug=slug)
    # if request.method == 'POST':
    #     parent_id = request.POST.get('parent_id')
    #     body = request.POST.get('body')
    #     Comment.objects.create(body=body, article=articles, user=request.user, parent_id=parent_id)
    return render(request, "blog/article_details.html", {'articles': articles})




from django.shortcuts import render , HttpResponse
from . import models

# Create your views here.
def articles_list(request):
    articles = models.Article.objects.all().order_by('-date')
    args = {'article':articles}
    return render(request , 'articles/articleslist.html', args)

def articles_detile(request , article_slug):
    # return HttpResponse(article_slug)
    article = models.Article.objects.get(slug = article_slug)
    return render(request , 'articles/articles_detile.html',{'article_detile':article})

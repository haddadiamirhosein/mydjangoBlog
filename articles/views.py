from django.shortcuts import render , HttpResponse ,redirect
from . import models
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.
def articles_list(request):
    articles = models.Article.objects.all().order_by('-date')
    args = {'article':articles}
    return render(request , 'articles/articleslist.html', args)



def articles_detile(request , article_slug):
    # return HttpResponse(article_slug)
    article = models.Article.objects.get(slug = article_slug)
    return render(request , 'articles/articles_detile.html',{'article_detile':article})



@login_required(login_url = "/accounts/login")
def articles_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,request.FILES)
        if form.is_valid:
            instance = form.save(commit = False)
            instance.author = request.user
            instance.save()
            return redirect('articles_urls:list')
    else:
        form = forms.CreateArticle()
    return render(request , 'articles/articles_create.html',{'form':form})

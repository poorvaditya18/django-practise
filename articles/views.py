from django.shortcuts import render
from django.http import HttpResponse
from articles.repository import * 

# Create your views here.
def article_home_view(request,id=None,*args,**kwargs):

    # print(args,kwargs) # output : () {'id': 1}
    print(id)

    # context or data obj
    # data = {"id" : id}

    # get the article with particular id from article db
    article = get_article_by_id(id)

    print("Received article: " + str(article.title))

    # return render(request, "articles/detail.html", data) # frameworks like Django and Flask, the render method is often used to render HTML templates with dynamic data. Here's an example from Django:

    return HttpResponse("Welcome to the Article section")
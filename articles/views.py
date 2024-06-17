from django.shortcuts import render
from django.http import HttpResponse
from articles.repository import * 

# Create your views here.

# article search view -->
def article_search_view(request):
    print("Inside article_search_view...")
    print("GET request body : "+ str(request.GET))
    query_dict = request.GET # this is a dictionary
    query = query_dict.get("q")

    try:
        query = int(query_dict.get("q"))
    except:
        query = None

    article_obj = None
    if query is not None :
        article_obj = Article.objects.get(id=query)
    context = {
        "object":article_obj
    }
    return render(request, "search.html", context=context)


# article detail view --> 
def article_detail_view(request,id=None,*args,**kwargs):

    # print(args,kwargs) # output : () {'id': 1}
    print(id)

    # context or data obj
    # data = {"id" : id}

    # get the article with particular id from article db
    article = get_article_by_id(id)

    print("Received article: " + str(article.title))

    # return render(request, "articles/detail.html", data) # frameworks like Django and Flask, the render method is often used to render HTML templates with dynamic data. Here's an example from Django:

    return HttpResponse("Welcome to the Article section")
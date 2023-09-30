# ----- views ------
'''
Description: To render html web pages. 
'''
import random
from django.http import HttpResponse # you need to return a HttpResponse to HttpRequest

from articles.models import Article
from django.template.loader import render_to_string
# another way to get render templates 
from django.template.loader import get_template

def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response (Response : is according to the developer . We pick to return the response)
    """
    # we can make this more dynamic using Django Templates.

    name = "Poorvaditya"  

    # from Database 
    article_obj = Article.objects.get(id=1)

    my_list = [102,13,342,1331,213]
    
    # getting all the articles that are saved in the db 
    article_list = Article.objects.all()
    print(article_list) # gives the output as  :<QuerySet [<Article: Article object (1)>]>  we can further perform more complex operations on this. Basically this is a object . 

    # my_list_str += f"<li>number is {x}</li>"  Django engine does not allow rendering of html 

    context  = {
        "my_list": article_list,
        "title": article_obj.title,
        "content": article_obj.content,
        "id": article_obj.id,
    }

    # rendering template --
    HTML_STRING = render_to_string("home-view.html", context=context) # this is mostly used 

    # another way using get template
    # template = get_template("home-view.html") # this will return you html page 
    # HTML_STRING= template.render(context=context)

    # django template ----
    # HTML_STRING = """
    # <h1> Titile:  {title} - Content: {content} - ObjectID : {id} </h1>
    # """.format(**context)
    return HttpResponse(HTML_STRING)
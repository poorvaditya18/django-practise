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
    context  = {
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
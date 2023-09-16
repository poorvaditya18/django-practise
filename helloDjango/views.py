# ----- views ------
'''
Description: To render html web pages. 
'''
import random
from django.http import HttpResponse # you need to return a HttpResponse to HttpRequest



def home_view(request):
    """
    Take in a request (Django sends request)
    Return HTML as a response (Response : is according to the developer . We pick to return the response)
    """
    # we can make this more dynamic using Django Templates.

    name = "Poorvaditya"
    number = random.randint(1,6)*100 # you can also do REST API calls here. 
    HTML_STRING = f"""
    <h1> Hello {name} - {number} </h1>
    """
    return HttpResponse(HTML_STRING)
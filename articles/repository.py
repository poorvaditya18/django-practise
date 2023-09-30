from articles.models import Article

# repository layer can interact with your databases to fetch the entities
# just like in Nodejs 
def get_article_by_id(article_id):
    article_obj = Article.objects.get(id=article_id)
    return article_obj
from rest_framework.response import Response
from rest_framework.decorators import api_view
from article.models import Article
from article.serializers import ArticleSerializer

@api_view(['GET', 'POST'])
def index(request):
    if request.method == "GET":
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_vaild():
            serializer.save()
            return Response(serializer.data)
    else:
        print(serializer.error)
        return Response(serializer.error)
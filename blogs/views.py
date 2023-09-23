from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import Post
import json

from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def index(req: HttpRequest):
    if req.method == "GET":
        posts = Post.objects.filter()
        data = [
            {
                "_id": obj._id,
                "title": obj.title,
                "content": obj.content,
                "author": obj.author,
            }
            for obj in posts
        ]
        return JsonResponse(data, safe=False)

    if req.method == "POST":
        received_json_data = json.loads(req.body.decode("utf-8"))

        print(received_json_data)
        title = received_json_data["title"]
        content = received_json_data["content"]
        author = received_json_data["author"]

        post = Post(title=title, content=content, author=author)
        post.save()
        return HttpResponse("blog created succesfully")

    return HttpResponse("a request")

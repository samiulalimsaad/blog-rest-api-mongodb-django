from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse
from .models import Post
import json

from django.views.decorators.csrf import csrf_exempt
import string
import random


# Create your views here.
@csrf_exempt
def index(req: HttpRequest):
    if req.method == "GET":
        posts = Post.objects.all()
        data = [
            {
                "pid": obj.pid if obj.pid else None,
                "title": obj.title,
                "content": obj.content,
                "author": obj.author,
            }
            for obj in posts
        ]
        return JsonResponse(data, safe=False)

    if req.method == "POST":
        received_json_data = json.loads(req.body.decode("utf-8"))

        pid = "".join(random.choices(string.ascii_uppercase + string.digits, k=20))
        print(received_json_data)
        title = received_json_data["title"]
        content = received_json_data["content"]
        author = received_json_data["author"]

        post = Post(pid=pid, title=title, content=content, author=author)
        post.save()
        return HttpResponse("blog created succesfully")

    return HttpResponse("a request")


@csrf_exempt
def single(req: HttpRequest, id):
    print(id)
    if req.method == "GET":
        posts = Post.objects.filter(pid=id)
        data = [
            {
                "pid": obj.pid if obj.pid else None,
                "title": obj.title,
                "content": obj.content,
                "author": obj.author,
            }
            for obj in posts
        ]
        return JsonResponse(data, safe=False)

    if req.method == "PATCH":
        received_json_data = json.loads(req.body.decode("utf-8"))

        post = Post.objects.get(pid=id)
        if post:
            for key in received_json_data:
                setattr(post, key, received_json_data[key])

            post.save()
        return HttpResponse("blog updated succesfully")

    if req.method == "DELETE":
        post = Post.objects.filter(pid=id)
        post.delete()
        return HttpResponse("blog deleted succesfully")

    return HttpResponse("a request")

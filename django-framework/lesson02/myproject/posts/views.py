from django.shortcuts import render


# Create your views here.
def post_lists(request):
    return render(request, "posts/post_list.html")

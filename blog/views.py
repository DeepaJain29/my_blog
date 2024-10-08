from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>hello from blog!</h1>", status=200)

def starting_page(request):
    return render(request, 'blog/index.html')

def posts(request):
    pass

def post_detail(request):
    pass
from django.shortcuts import render

# Create your views here.
def post_list(request):
    #render() display the result on Webpage. arg1:request, 2:html file on display 3:argument send to template
    return render(request, 'blog/post_list.html', {})
from django.shortcuts import render
from photoapp.models import Picture
from django.http  import HttpResponseRedirect

# Create your views here.

def user_page(request):
    if request.method == 'GET': #ask
        pictures = Picture.objects.all()
        return render(request, 'user_page.html', {'pictures': pictures})
    elif request.method == 'POST': #upload
        picture = Picture(
            description = request.POST['description'],
            file = request.FILES['picture']
        )
        picture.save()
        return HttpResponseRedirect('/user')
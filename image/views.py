from django.shortcuts import render,redirect

# Create your views here.

from .models import Image

def index(request):
    if request.method == "POST":
        caption=request.POST['caption']
        img=request.FILES.get("img")
        images=Image(image=img,caption=caption)
        images.save()
        return redirect('/enter')
    return render(request,"index.html", )
def retrieve (request):
    img = Image.objects.all()
    return render(request,"index.html", {"img":img})
   

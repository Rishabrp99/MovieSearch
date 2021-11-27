from django.shortcuts import render
from .models import Data
from django.db.models import Q
# Create your views here.
def index(request):
    if 'q' in request.GET:
        q=request.GET['q']
        multiple_q=Q(Q(movie_name__icontains=q)|Q(actor_name__icontains=q) | Q(actress_name__icontains=q)|Q(director_name__icontains=q)|Q(year__icontains=q))
        data=Data.objects.filter(multiple_q)
        #data=Data.objects.filter(first_name__icontains=q )
    else:
        data=Data.objects.all()
    context={
        'data':data
    }
    return render(request,'dashboard/index.html',context)
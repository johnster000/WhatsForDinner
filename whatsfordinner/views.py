from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect, JsonResponse, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse_lazy, reverse
from django.views.generic import *
from .models import *
from .forms import *
from .utils import *
import requests

def logout_view(request):
    logout(request)
    return render(request, 'logged_out.html')

@login_required(login_url='/accounts/login/')
def home(request):
    return render(request, 'home.html')

#### MODELS ####
@login_required(login_url='/accounts/login/')
def dinners(request):   
    if request.method == 'POST':
        searchinput = request.POST['searchinput']
        if searchinput:
            dinners = Dinner.objects.filter(dish__startswith=searchinput)
        else:
            dinners = Dinner.objects.all()
    else:
        dinners = Dinner.objects.all()
        
    paginator = Paginator(dinners, 25)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'dinners.html',{'page_obj': page_obj})

#### MODEL DETAILS #### 
@login_required(login_url='/accounts/login/')
def DinnerDetailView(request, pk):   
    dinner = Dinner.objects.get(id=pk)
    return render(request, 'whatsfordinner/dinner_detail_view.html',{'dinner':dinner})

#### MODEL UPDATES ####
@login_required(login_url='/accounts/login/')
def DinnerUpdateView(request, pk):
    model = Dinner.objects.get(id=pk)
    form = DinnerForm(request.POST or None,instance=model,request=request)
    if form.is_valid():
        model = form.save()
        model.save()
        success_url = reverse('dinner_detail', kwargs={"pk": model.id})
        return HttpResponseRedirect(success_url)
    return render(request, 'whatsfordinner/dinner_update_form.html', {'form':form})

#### MODEL CREATES ####
@login_required(login_url='/accounts/login/')
def DinnerCreateView(request):
    form = DinnerForm(request.POST or None, request=request)
    if form.is_valid():
        model = form.save()
        model.save()
        success_url = reverse('dinner_detail', kwargs={"pk": model.id})
        return HttpResponseRedirect(success_url)

    return render(request, 'whatsfordinner/dinner_create_form.html', {'form':form})

#### AJAX ####
@login_required(login_url='/accounts/login/')
def ajax_getdinner(request):
    date = request.GET.get('date')
    alldinners = Dinner.objects.all()
    try:
        datesaved = Date.objects.get(Date = date)
        dinner = Dinner.objects.get(pk=datesaved.Dinner_id)
    except Date.DoesNotExist:
        dinner = None
    return render(request, 'ajax_getdinner.html', {'dinner':dinner, 'alldinners':alldinners})

@login_required(login_url='/accounts/login/')
def ajax_getrandomdinner(request):
    
    response = requests.get('https://random-data-api.com/api/food/random_food')
    dinner = response.json()

    return render(request, 'ajax_getselectdinner.html', {'dinner':dinner, 'random':'random'})

@login_required(login_url='/accounts/login/')
def ajax_getselecteddinner(request):
    try:
        dinner = Dinner.objects.get(pk=request.GET.get('dinner_id'))
    except Dinner.DoesNotExist:
        dinner = None
    return render(request, 'ajax_getselectdinner.html', {'dinner':dinner, 'random':'NOTrandom'})

@login_required(login_url='/accounts/login/')
def ajax_getalldinner(request):
    startdate = request.GET.get('start')
    enddate = request.GET.get('end')
    dinnerobjects = Date.objects.filter(Date__lte=enddate, Date__gte=startdate)
    data = []    
    for obj in dinnerobjects:
        d = {} 
        d = {**d, **{'id': obj.Date}}
        d = {**d, **{'title': obj.Dinner.dish}}
        d = {**d, **{'start': obj.Date}}
        d = {**d, **{'allDay': True}}
        data.append(d)
    return JsonResponse(data, safe=False)
    
@login_required(login_url='/accounts/login/')
def ajax_saveselecteddinner(request):
    random = request.GET.get('random')
    dinnerID = request.GET.get('dinnerID')
    dinnerDish = request.GET.get('dinnerDish')
    dinnerDescription = request.GET.get('dinnerDescription')
    dinnerIngredient = request.GET.get('dinnerIngredient')
    dinnerMeasurement = request.GET.get('dinnerMeasurement')
    dinnerdate = request.GET.get('dinnerDate')
    if random == 'random':
        newdinner = Dinner.create()
        newdinner.dish = dinnerDish
        newdinner.description = dinnerDescription
        newdinner.ingredient = dinnerIngredient
        newdinner.mesurement = dinnerMeasurement
        newdinner.save()
        Date.objects.filter(Date=dinnerdate).delete()
        newdate = Date.create(newdinner, dinnerdate)
        newdate.save()
    else:
        dinner = Dinner.objects.get(pk=dinnerID)
        Date.objects.filter(Date=dinnerdate).delete()
        newdate = Date.create(dinner, dinnerdate)
        newdate.save()
    return HttpResponse('Success')


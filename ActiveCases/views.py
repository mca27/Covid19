from django.db.models import Sum
from django.http import JsonResponse, Http404
from django.shortcuts import render
from django.views import generic
from .models import IndiaCases


class IndexView(generic.ListView):
    template_name = 'ActiveCases/index.html'
    context_object_name = 'all_cases'
    total_price = IndiaCases.objects.all().annotate(total=Sum('confirmed_Cases'))

    def get_queryset(self):
        return IndiaCases.objects.all()


def index(request):
    total_cases = IndiaCases.objects.aggregate(Sum('confirmed_Cases'))
    active_cases = IndiaCases.objects.aggregate(Sum('active_cases'))
    recovered = IndiaCases.objects.aggregate(Sum('recovered'))
    deaths = IndiaCases.objects.aggregate(Sum('deaths'))
    all_cases = IndiaCases.objects.all()
    return render(request, 'ActiveCases/index.html', {
        'all_cases': all_cases,
        'total_cases': total_cases,
        'active_cases': active_cases,
        'recovered': recovered,
        'deaths': deaths
    })


class DetailView(generic.DetailView):
    model = IndiaCases
    # cases = IndiaCases.objects.get(pk=id)
    template_name = 'ActiveCases/details.html'


def details(request, case_id):
    try:
        case = IndiaCases.objects.get(pk=case_id)
    except:
        raise Http404("")

    return render(request, 'ActiveCases/details.html', {'case': case})

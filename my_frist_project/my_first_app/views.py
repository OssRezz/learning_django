from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView

# Create your views here.


def my_view(request):
    car_list = [
        {"title": "BMW"},
        {"title": "Manza"},
    ]

    context = {
        "car_list": car_list
    }
    return render(request, "my_firts_app/car_list.html", context)


def my_test_view(request, *args, **kwargs):
    print(args)
    print(kwargs)
    return HttpResponse("")


class CarListView(TemplateView):
    template_name = "my_firts_app/car_list.html"

    def get_context_data(self):
        car_list = [
            {"title": "BMW"},
            {"title": "Manza"},
        ]

        return {
            "car_list": car_list
        }

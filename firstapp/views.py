from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.
class ViewName(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {"name": "Rahul", "age": 21, "Roll": 100}
        print(context)
        return context

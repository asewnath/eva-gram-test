from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.edit import CreateView
from sandbox_app.models import Plot

from .forms import PlotForm


def home(request):
    form = PlotForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        plot_obj = Plot.objects.get(title=form.cleaned_data['plot'])
        div = plot_obj.div
        script = plot_obj.script

        context = {
            'script': plot_obj.script,
            'div': plot_obj.div,
            'graph_title': plot_obj.title,
            'form': form
        }

        return render(request, 'base.html', context)
    else:
        print("invalid")

    return render(request, 'base.html', {'form': form})


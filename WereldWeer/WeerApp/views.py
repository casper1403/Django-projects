from django.shortcuts import render
from django.views.generic import TemplateView
from .data import get_weather_data, get_hourly_forecast
from .models import City
from django.views.generic.list import MultipleObjectMixin
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from bokeh.models import ColumnDataSource
import pandas as pd



def indexView(request):

    return render(request, 'index.html')

def weerView(request):
    ctx = {}
    url_parameter = request.GET.get('city')
    if url_parameter:
        if get_weather_data(url_parameter):
            weather = get_weather_data(url_parameter)
            ctx['temp'] = weather[0]
            ctx['pressure']=weather[1]
            ctx['humidity']=weather[2]
            ctx['sky']=weather[3]
            ctx['wind']=weather[4]
            try:
                ctx['rain'] = weather[5]
            except IndexError:
                None
        else:
            ctx['None'] = "No data for this city"

    if url_parameter:
        foreCast = get_hourly_forecast(url_parameter)
        if isinstance(foreCast, pd.DataFrame):
            source = ColumnDataSource(foreCast)
            plot = figure(title='Temperatuur',plot_width=300 ,plot_height=250,  toolbar_location = None , y_range=(-10, 50))
            plot.line(x='index', y='temp', source=source, line_width=2)
            script, div = components(plot)
            ctx['script1'] = script
            ctx['div1'] = div

    return render(request,'weatherresult.html',context=ctx)

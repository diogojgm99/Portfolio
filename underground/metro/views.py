from django.shortcuts import render
from .models import Line, Station, Stop
from .forms import  StopForm, LineForm, StationForm
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class HomeView(TemplateView):
  template_name = "home.html"

  def get_context_data(self):
    context = super().get_context_data()
    context["lines"] = Line.objects.all()
    context["stations"] = Station.objects.all()
    context["stops"] = Stop.objects.all()
    return context

##########################################
#                  Lines
##########################################
class LinesView(ListView):
  model = Line
  template_name = "routes/lines.html"

class CreateLineView(CreateView):
  model = Line
  form_class = LineForm
  template_name = "routes/add_line.html"

class UpdateLineView(UpdateView):
  model = Line
  form_class = LineForm
  template_name = "routes/update_line.html"

class DeleteLineView(DeleteView):
  model = Line
  template_name = "routes/delete_line.html"

##########################################
#                  Stations
##########################################

class StationsView(ListView):
    model = Station
    template_name = "routes/stations.html"

class CreateStationView(CreateView):
    model = Station
    form_class = StationForm
    template_name = "routes/add_station.html"

class UpdateStationView(UpdateView):
    model = Station
    form_class = StationForm
    template_name = "routes/update_station.html"

class DeleteStationView(DeleteView):
    model = Station
    template_name = "routes/delete_station.html"


##########################################
#                  Stops
##########################################

class StopsView(ListView):
    model = Stop
    template_name = "routes/stops.html"

class CreateStationView(CreateView):
    model = Stop
    form_class = StopForm
    template_name = "routes/add_stop.html"

class UpdateStationView(UpdateView):
    model = Stop
    form_class = StopForm
    template_name = "routes/update_stop.html"

class DeleteStopView(DeleteView):
    model = Stop
    template_name = "routes/delete_stop.html"
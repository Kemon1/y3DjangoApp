from django.shortcuts import render, get_object_or_404
from .models import Issue
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
import requests

def home(request):
    url = 'https://api.openweathermap.org/data/2.5/weather?q={},{}&units=metric&appid={}'
    cities = [('Sheffield', 'UK'), ('London', 'UK'), ('Manchester', 'UK')]
    weather_data = []

    api_key = '0489486cfde84063e28fdde7ac74e8a8'

    for city in cities:
        # Request the API data and convert the JSON to Python data types
        city_weather = requests.get(url.format(city[0], city[1], api_key)).json()
        # Safely create weather dictionary (use .get() for robustness)
        weather = {

            'city': city_weather.get('name', 'N/A') + ', ' + city_weather.get('sys', {}).get('country', 'N/A'),

            'temperature': city_weather.get('main', {}).get('temp', 'N/A'),

            'description': city_weather.get('weather', [{}])[0].get('description', 'No description')
        }
        # Append data for the current city
        weather_data.append(weather)
    return render(request, 'itreporting/home.html', {'title': 'Homepage', 'weather_data': weather_data})
    
def about(request):
    return render(request, 'itreporting/about.html', {'title':'about'})

def contact(request):
    return render(request, 'itreporting/contact.html', {'title':'conact'})    

def report(request):
    daily_report = {'issues': Issue.objects.all(), 'title': 'Issues Reported'}
    return render(request, 'itreporting/report.html', daily_report)

class PostListView(ListView):
    model = Issue
    ordering = ['-date_submitted']
    template_name = 'itreporting/report.html'
    context_object_name = 'issues'
    paginate_by = 5

class UserPostListView(ListView): 
    model = Issue
    template_name = 'itreporting/user_issues.html' 
    context_object_name = 'issues'
    paginate_by = 5


    def get_queryset(self):
        user=get_object_or_404(User, username=self.kwargs.get('username'))
        return Issue.objects.filter(author=user).order_by('-date_submitted')


class PostDetailView(DetailView):
    model = Issue
    template_name = 'itreporting/issue_detail.html'

class PostCreateView(LoginRequiredMixin, CreateView):

    model = Issue
    fields = ['type', 'room', 'urgent', 'details']

    def form_valid(self, form): 

        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Issue
    fields = ['type', 'room', 'details']

    def test_func(self):
        issue = self.get_object()
        return self.request.user == issue.author
    
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Issue
    success_url = '/report'
    
    def test_func(self):
        issue = self.get_object()
        return self.request.user == issue.author



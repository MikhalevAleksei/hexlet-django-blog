from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View


class HomePageView(View):
    def get(self, request):
        # Используем reverse для получения пути по имени маршрута
        return redirect(reverse('article', kwargs={
            'tags': 'python',
            'article_id': 42
        }))

def about(request):
    return render(request, "about.html")

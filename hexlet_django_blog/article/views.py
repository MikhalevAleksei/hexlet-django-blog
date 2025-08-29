from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View


class IndexView(View):
    def get(self, request, tags, article_id) -> HttpResponse:
        return HttpResponse(f"Статья номер {article_id}. Тег {tags}")




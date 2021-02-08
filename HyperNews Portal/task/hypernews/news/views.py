from django.shortcuts import render
from django.views import View
from django.http import Http404, QueryDict
from django.shortcuts import redirect
import datetime
from collections import defaultdict
import json
from hypernews.settings import NEWS_JSON_PATH

with open(NEWS_JSON_PATH, 'r') as f:
    news_list = json.load(f)
    for news in news_list:
        news['created'] = datetime.datetime.strptime(news['created'], '%Y-%m-%d %H:%M:%S')


# Create your views here.
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return redirect("news/")


class NewsContentView(View):
    def get(self, request, link, *args, **kwargs):
        for news in news_list:
            if int(link) == news['link']:
                return render(request, 'news/news_content.html',
                              context={
                                  'title': news['title'],
                                  'created': news['created'],
                                  'text': news['text']
                              })

        raise Http404


class AllNewsView(View):
    def get(self, request, *args, **kwargs):
        query_dict = request.GET
        keyword = query_dict['q'] if 'q' in query_dict else ''

        times = defaultdict()
        for news in news_list:
            if keyword in news['title']:
                times.setdefault(news['created'].date(), []).append(news)

        time_dict = [{'created': key, 'value': value} for key, value in times.items()]

        return render(request, 'news/news_all.html',
                      context={'time_dict': time_dict})


class CreateNewsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'news/news_create.html')

    def post(self, request, *args, **kwargs):
        title = request.POST.get('title')
        text = request.POST.get('text')
        created = datetime.datetime.now()
        news_list.append({'title': title,
                          'text': text,
                          'created': created,
                          'link': len(news_list) + 1})
        return redirect('/news/')

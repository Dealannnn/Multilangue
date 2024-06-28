from django.shortcuts import redirect, render
from django.utils.translation import activate
from django.conf import settings
from .models import Article

def set_language(request):
    if request.method == 'POST':
        lang_code = request.POST.get('language', settings.LANGUAGE_CODE)
        activate(lang_code)
        response = redirect(request.POST.get('next', '/'))
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, lang_code)
        return response

def article_list(request):
    articles = Article.objects.all()
    return render(request, 'main/article_list.html', {'articles': articles})

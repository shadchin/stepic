from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET
from django.core.paginator import Paginator, EmptyPage

from qa.models import Question, Answer

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return paginator, page


@require_GET
def main(request):
    quest = Question.objects.order_by('-added_at')
    paginator, page = paginate(request, quest)
    return render(request, 'qa/template/main.html', {'paginator': paginator, 'page': page, 'questions': page.object_list})


@require_GET
def popular(request):
    quest = Question.objects.order_by('-rating')
    paginator, page = paginate(request, quest)
    return render(request, 'qa/template/popular.html', {'paginator': paginator, 'page': page, 'questions': page.object_list})


@require_GET
def question(request, id):
    quest = get_object_or_404(Question, id=id)
    try:
        answers = Answer.objects.filter(question=quest).all()
    except Answer.DoesNotExist:
        answers = []
    return render(request, 'qa/template/question.html', {'quest': quest, 'answers': answers})

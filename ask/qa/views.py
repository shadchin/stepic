from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_GET, require_POST
from django.core.paginator import Paginator, EmptyPage
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm
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
    quest = Question.objects.order_by('-id')
    paginator, page = paginate(request, quest)
    user = request.user
    return render(request, 'main.html', {'paginator': paginator, 'page': page, 'questions': page.object_list, 'user': user})


@require_GET
def popular(request):
    quest = Question.objects.order_by('-rating')
    paginator, page = paginate(request, quest)
    return render(request, 'popular.html', {'paginator': paginator, 'page': page, 'questions': page.object_list})


def question(request, id):
    quest = get_object_or_404(Question, id=id)
    try:
        answers = Answer.objects.filter(question=quest).all()
    except Answer.DoesNotExist:
        answers = []
    a = Answer(question=quest, author=request.user)
    form = AnswerForm(instance=a)
    return render(request, 'question.html', {'quest': quest, 'answers': answers, 'form': form})


def ask(request):
    if request.method == "POST":
        print(request.POST)
        request.POST['author'] = u'1'
        form = AskForm(request.POST)
        if form.is_valid():
            quest = form.save()
            return HttpResponseRedirect(quest.get_url())
    else:
        user = request.user
        if not user.is_active:
            user = User.objects.get(pk=1)
        quest = Question(author=user)
        form = AskForm(instance=quest)
    return render(request, 'ask.html', {'form': form})


@require_POST
def answer(request):
    form = AnswerForm(request.POST)
    if form.is_valid():
        ans = form.save()
        quest = ans.question
        return HttpResponseRedirect(quest.get_url())


def mylogin(request):
    if request.method == "POST":
        print(request.POST)
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def singup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

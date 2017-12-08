from django.shortcuts import render, HttpResponse, redirect
from firstapp.models import People, Article, Comment
from django.template import Context, Template
from firstapp.forms import CommentForm
# Create your views here.


def first_try(request):
    person = People(name='Spock', job='officer')
    html_string = '''
        <html>
        <head>
            <title>django web app</title>
            <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/semantic-ui/2.2.6/semantic.css">
        </head> 
        <body>
            <div class="ui segment">
                <h1 class="ui center aligned icon header">
                    <i class="hand spock icon"></i>
                    Hello,{{ person.name }}
                </h1>
            </div>
        </body>
    </html>
    '''
    t = Template(html_string)
    c = Context({'person': person})
    web_page = t.render(c)
    return HttpResponse(web_page)


def index(request):
    context = {}
    tagValue = request.GET.get('tag')
    if tagValue:
        article_list = Article.objects.filter(tag=tagValue)
    else:
        article_list = Article.objects.all()
    context['article_list'] = article_list
    index_page = render(request, 'index.html', context)
    return index_page


def detail(request, article_id, error_form=None):
    context = {}
    artical = Article.objects.get(id=article_id)
    best_comment = Comment.objects.filter(best=True, belong_to=artical).first()
    if best_comment:
        context['best_comment'] = best_comment
    context['artical'] = artical
    if error_form is not None:
        context['form'] = error_form
    else:
        context['form'] = CommentForm

    return render(request, 'detail.html', context)


def detail_comment(request, article_id):
    form = CommentForm(request.POST)
    artical = Article.objects.get(id=article_id)
    if form.is_valid():
        name = form.cleaned_data["name"]
        content = form.cleaned_data["content"]

        c = Comment(name=name, content=content, belong_to=artical)
        c.save()
    else:
        return detail(request, article_id, error_form=form)
    return redirect(to='detail', article_id=article_id)

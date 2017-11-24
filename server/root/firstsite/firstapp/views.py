from django.shortcuts import render, HttpResponse
from firstapp.models import People
from firstapp.models import Article
from django.template import Context, Template

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


def detail(request):
    context = {}
    articalId = request.GET.get('id')
    artical = Article.objects.filter(id=articalId).first()
    print (artical)
    context['artical'] = artical
    index_page = render(request, 'detail.html', context)
    return index_page

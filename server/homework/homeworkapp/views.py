from django.shortcuts import render

# Create your views here.


def index(request):
    print ("===" * 30)
    print (request)
    print ("===" * 30)
    print (dir(request))
    print ("===" * 30)
    print (type(request))
    print ("===" * 30)

    context = {'index': 'index'}
    index_page = render(request, 'list.html', context)
    return index_page
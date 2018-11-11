from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,AccessRecord,WebPage,User

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    return render(request, 'first_app/index.html', context=date_dict)


def help(request):
    my_dict_help = {'insert_me':"How can I help you?"}
    return render(request, 'help/index.html', context=my_dict_help)

def users(request):
    users_list = User.objects.order_by('first_name')
    dict_user = {'user_list':users_list}
    return render(request, 'first_app/users.html', context=dict_user)

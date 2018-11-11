from django.shortcuts import render
from django.http import HttpResponse
from first_app.models import Topic,AccessRecord,WebPage,User
from . import forms
from first_app.forms import NewUserForm

# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpages_list}
    context_dict = {'text':'hello world','number':100}
    #return render(request, 'first_app/index.html', context=date_dict, context_dict)
    return render(request, 'first_app/index.html', context_dict)

def signup(request):
    form = NewUserForm()
#defining a post method to a form and saving it to db
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('Error form is invalid')
    return render(request,'first_app/signup.html',{'form':form})

def help(request):
    my_dict_help = {'insert_me':"How can I help you?"}
    return render(request, 'first_app/help.html', context=my_dict_help)

def users(request):
    users_list = User.objects.order_by('first_name')
    dict_user = {'user_list':users_list}
    return render(request, 'first_app/users.html', context=dict_user)

def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
             #DO SOMETHING CODE
            print("validation success!")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])

    return render(request, 'first_app/form_page.html', {'form':form})

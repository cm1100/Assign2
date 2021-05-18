from django.shortcuts import render,redirect,get_object_or_404,reverse
from collections import Counter
from bs4 import BeautifulSoup
import requests
from django.views import View
from .forms import Url_form
from .models import Url_mod
import lxml

# Create your views here.

def freq_count(url):

    common_words=['a', 'in', 'to', 'the', 'of', 'and', 'for', 'by', 'on', 'is', 'i', 'all', 'this', 'with', 'it', 'at', 'from', 'or', 'you', 'as', 'your', 'an', 'are', 'be', 'that', 'do', 'not', 'have', 'one', 'can', 'was', 'if', 'we', 'but', 'what', 'which', 'there', 'when', 'use', 'their', 'they', 'how', 'he', 'were', 'his', 'had', 'each', 'said', 'she', 'word']
    list2 = ['!', '"', '#', '$', '%', '&', "'", '()', '*', '+', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '.']
    html_text = requests.get(url)

    soup = BeautifulSoup(html_text.text,'lxml')

    text=soup.text

    words_list = text.lower().split()



    words_list=[i for i in words_list if i not in common_words]


    c= Counter(words_list)
    return c.most_common(10)


class Url_view(View):
    def get(self,request):
        ctx = {"form":Url_form}
        return render(request,"freq_counter/form.html",ctx)


    def post(self,request):
        form = Url_form(request.POST)

        print("hi1")
        print(request.POST['url'])

        if(Url_mod.objects.filter(url=request.POST['url']).exists()):
            object = Url_mod.objects.filter(url=request.POST['url'])
            print(object[0].url)
            return redirect(reverse("freq_counter:Result_View",args=[object[0].id]))

        if form.is_valid():

            form1=form.save(commit=False)
            print("hi3")
            form1.frequent_words=freq_count(url=request.POST['url'])

            form1.save()

            print("hi2")

            obj = Url_mod.objects.filter(url=form1.url)


            return redirect(reverse("freq_counter:Result_View",args=[obj[0].id]))



        return render(request,"freq_counter/form.html",{"form":form})


class Result_View(View):

    def get(self,request,pk):
        print("hi here")
        obj = Url_mod.objects.filter(id=pk)
        print("object found")
        ctx={"words":obj[0].frequent_words}
        return render(request,"freq_counter/result.html",ctx)

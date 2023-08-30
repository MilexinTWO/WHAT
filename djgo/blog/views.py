
from django.shortcuts import render
import requests


def index(request):
    response = requests.get(
        "https://emma.pixnet.cc/mainpage/blog/categories/hot/28") #28為國內旅遊
    article = response.json()["articles"]#轉換為JSON物件後，存取articles欄位
    # print( article )
    # #print( article.user.display_name)
    # print( article.title )
    # print( article.link)
    # print( article.link)

    return render(request, "index.html", {"articles": article})


def GetImge(request):
    return render(request, "index.html")
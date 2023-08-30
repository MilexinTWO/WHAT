
import requests as rq
#這是爬蟲
response = rq.get(
    "https://emma.pixnet.cc/mainpage/blog/categories/hot/28") #28為國內旅遊
article = response.json()["articles"]#轉換為JSON物件後，存取articles欄位
print( response.json() )
# #print( article.user.display_name)
# print( article.title )
# print( article.link)
# print( article.link)


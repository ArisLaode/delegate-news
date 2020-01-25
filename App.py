
from flask import Flask, render_template
from newsapi import NewsApiClient
 
 
 
 
app = Flask(__name__)
 
 
 
@app.route('/')
def Index():
    newsapi = NewsApiClient(api_key="7cb11b15c84a4ff1af515df4c4dbaf47")
    topheadlines = newsapi.get_top_headlines(sources="al-jazeera-english")
 
 
    articles = topheadlines['articles']
 
    desc = []
    news = []
    img = []
 
 
    for i in range(len(articles)):
        myarticles = articles[i]
 
 
        news.append(myarticles['title'])
        desc.append(myarticles['description'])
        img.append(myarticles['urlToImage'])
 
 
 
    mylist = zip(news, desc, img)
 
 
    return render_template('index.html', context = mylist)
from django.shortcuts import render, redirect, HttpResponse
import oauth2, json

CONSUMER_KEY = 'fdMbhBwFrqSt0DZDfiETByxcg'
CONSUMER_SECRET = 'kbidjppaYuphctB2NfCGlb5Ny4pBjod3heqNknOjg0vrqEKizK'
thomas={}


def oauth_req(url, key, secret, http_method="GET", post_body="", http_headers='None'):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(url, method=http_method, body=post_body, headers=http_headers)
    return content




def home(request):
    popular=[]
    data = {}
    rated_tag = oauth_req('https://api.twitter.com/1.1/trends/place.json?id=23424848',
                          '737865585107828736-wRnlPmoMXvVM2cVcLxeeb4ThgRTdChi',
                          'KNYcATIkEE2UsxkXOTQhi7DXTKXxEEaRswY5IsbGiAgMM')
    tag = json.loads(rated_tag)
    for item in tag:
        temp = (item.get("trends"))
        newtemp = temp[1:7]

    for items in newtemp:
        temp1=items["name"]
        if temp1[0] == '#':
            temp1 = temp1[1:len(temp1)]
        popular.append(temp1)
        thomas['popular']=popular

        # data[items["name"]]=details(items["name"])


    return render(request, 'home.html', {'popular': popular})


def details(hashtag):
    tempdata = []


    rated_tag = oauth_req('https://api.twitter.com/1.1/search/tweets.json?q=%23' + hashtag+'&count=1000',
                          '737865585107828736-wRnlPmoMXvVM2cVcLxeeb4ThgRTdChi',
                          'KNYcATIkEE2UsxkXOTQhi7DXTKXxEEaRswY5IsbGiAgMM')

    #tag = json.loads(rated_tag)
    tag = json.loads(rated_tag)
    temp = tag["statuses"]
    for temp1 in temp:
        text = temp1["text"]
        temp2 = temp1["user"]
        name = temp2["screen_name"]
        tempdata.append({'name': name, 'text': text})

    return tempdata


def check(request, tag_name):
    new=details(tag_name)
    thomas['data']=new
    return render(request,'details.html',thomas)
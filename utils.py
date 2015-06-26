#!/usr/bin/python

from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
import requests
import re

def GoogleSearch(query):
    try:
        allask = requests.get("http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=site:br.answers.yahoo.com %s" % (query)).json()
        if allsk.status_code == 200:
            return(allask)
        else:
            return(False)
    except:
        return(False)


def GetBestAnswer(answerurl):
    htmlsource = urlopen(answerurl).read()
    assoup = BeautifulSoup(htmlsource)
    bestanswer = assoup.find('span', attrs={'class': 'ya-q-full-text'})
    return(bestanswer.text)

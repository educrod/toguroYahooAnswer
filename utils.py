#!/usr/bin/python

import requests
import urllib2
import re


def GoogleSearch(query):
    return(requests.get("http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=site:br.answers.yahoo.com %s" % (query)).json())


def GetBestAnswer(answerurl):
#    htmlsource = urllib2.urlopen("https://br.answers.yahoo.com/question/index?qid=20130314111535AADyGFC").read()
    htmlsource = urllib2.urlopen(answerurl).read()
    t = False

    l = ''
    for line in htmlsource.splitlines():
        if 'Melhor resposta:' in line:
            t = True
            continue

        if t:
            l += line
            if '</span>' in line:
                break

    TAG_RE = re.compile(r'<[^>]+>')
    b = TAG_RE.sub('', l)
    return(b)

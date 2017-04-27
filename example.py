#!/usr/local/bin/python3
# -*- coding: UTF-8 -*-

#pylint: disable = C0111, C0103, C0326, C0301

import sys
import time
import os
# import urllib
# import urllib.request
# import random
from subprocess import call

from pyquery import PyQuery as pq

tmp_head = '''---
title: {title}
tag: {tag}
date: {date}
---
'''

tmp_body = '''## Description

**Difficulty: {difficulty}**

{contents}

<b>题意:</b><br>


## Solution

```python

```

'''

# get url bt problem No.
# user_agents = ['Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20130406 Firefox/23.0',
#         'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:18.0) Gecko/20100101 Firefox/18.0',
#         'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533+ \
#         (KHTML, like Gecko) Element Browser 5.0',
#         'IBM WebExplorer /v0.94', 'Galaxy/1.0 [en] (Mac OS X 10.5.6; U; en)',
#         'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
#         'Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14',
#         'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) \
#         Version/6.0 Mobile/10A5355d Safari/8536.25',
#         'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) \
#         Chrome/28.0.1468.0 Safari/537.36',
#         'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0; TheWorld)']

# proxy_host = '127.0.0.1:1087'
# def search(queryStr):
#     # queryStr = urllib.quote(queryStr)
#     url = queryStr
#     # url = 'http://ip.gs'
#     request = urllib.request.Request(url)
#     request.set_proxy(proxy_host, 'http')
#     index = random.randint(0, 9)
#     user_agent = user_agents[index]
#     request.add_header('User-agent', user_agent)
#     response = urllib.request.urlopen(request)
#     print(response)
#     html = response.read()
#     # results = self.extractSearchResults(html)
#     return html

# search_url = 'https://www.google.com/search?safe=off&q=%22{no}.%22+site%3Aleetcode.com%2F+inurl%3Aleetcode.com%2Fproblems+inanchor%3A%22{no}.%22'
# if sys.argv[1].isdigit():
#     search_url = search_url.format(no=sys.argv[1])
#     rslt = search(search_url)
#     print(rslt.decode('utf-8'))
# else:s
#     url = sys.argv[1]

simple_mode = False
url = sys.argv[1]
tag = ''
if url.startswith('https://') or url.startswith('http://'):
    tmp = tmp_head + tmp_body
    tag = 'algorithm'
else:
    simple_mode = True
    print('Simple Template Mode')
    tmp = tmp_head
    try:
        tag = sys.argv[2]
    except IndexError:
        tag = ''

path_dir = ''

try:
    a2 = sys.argv[2][0]
except IndexError:
    path_dir = './_posts/'
else:
    if a2[0] == 'p':
        path_dir = './_posts/'
    elif a2[0] == 'd':
        path_dir = './_drafts/'
    else:
        path_dir = './_posts/'

full_path = ''
if not simple_mode:
    d = pq(url)

    get_title      = d('.question-title h3').text()
    get_difficulty = d('.question-info li strong').eq(2).text()
    get_filename   = url.lstrip('https://').split('/')[2] + '.md'
    get_contents   = (d('.question-content').html(method='html')
                    .split('<p><a href="/subscribe/">Subscribe</a>')[0].rstrip().rstrip('<div>')
                    .split('<p><b>Credits:</b>')[0].strip())

    tmp = tmp.format(
        title      = get_title,
        tag        = tag,
        difficulty = get_difficulty,
        contents   = get_contents,
        date       = time.strftime("%F %H:%M:%S", time.localtime()))
    full_path = path_dir + get_filename

else:
    tmp = tmp.format(
        title = url,
        tag   = tag,
        date  = time.strftime("%F %H:%M:%S", time.localtime()))
    file_name = '-'.join(url.lower().split(' ')) + '.md'
    full_path = path_dir + file_name

if not os.path.exists(full_path):
    file = open(full_path, 'w')
    file.write(tmp)
    file.close()
    call(['code', full_path])
    print('Show time:\n', full_path)
else:
    print('Pick up from where u left:\n', full_path)
    call(['code', full_path])

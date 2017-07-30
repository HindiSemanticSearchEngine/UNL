# -*- coding: utf-8 -*-

import urllib2
import urllib
import json
import re

def hin_to_eng(word, target_lang = 'en', source_lang = 'auto'):
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0'
    headers = {'User-Agent': user_agent}
    url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=" + source_lang + "&tl=" + target_lang + "&dt=t&q=" + word
    values = {}
    data = urllib.urlencode(values)
    req = urllib2.Request(url, data, headers)
    response = urllib2.urlopen(req)

    data = response.read()
    #data = data.decode('utf-8')
    json_data = json.loads(data)
    final_list = []
    for i in range(0, len(json_data[0])):
        final_list.append(json_data[0][i][0].strip())
    result_string = "".join(final_list)
    #return result_string.encode("utf-8")
    return result_string

#print hin_to_eng('साहसिक')

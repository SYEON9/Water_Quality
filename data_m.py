from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import pandas as pd
import requests, bs4
from lxml import html

"""공공데이터포털의 openAPI를 get방식으로 받아오기 위한 코드."""

"""end_point"""
xmlUrl = 'http://opendata.kwater.or.kr/openapi-data/service/pubd/dam/effluent/damcode/list'


"""API_key 설정"""
My_API_Key = unquote('MYehZKC6rTmhPDYDSal7OnLyf3caTrsWfvoB%2FyIajKuZ42l51tnmlb4Y24db%2Bb2wZC5PR8gGtGxdbWW5s82HPA%3D%3D')


"""prarmeters설정"""
queryParams = '?'+urlencode(
        {
            quote_plus('ServiceKey'):My_API_Key,
            quote_plus('numOfRows'):'16',
            quote_plus('pageNo'):'1'
        }
)

parameters = {'serviceKey':My_API_Key, 'numOfRows':16, 'pageNo':1}


"""xml file 불러오기"""
res = requests.get(xmlUrl, params = parameters)
print(res.url)
print(res.status_code)

response = res.text.encode('utf-8')
xmlobj = bs4.BeatuifulSoup(response, 'lxml-xml')  





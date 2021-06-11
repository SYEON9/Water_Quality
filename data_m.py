from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote
import pandas as pd
import requests, bs4
from lxml import html



"""공공데이터포털의 openAPI를 get방식으로 받아오기 위한 코드. header를 사용해도 서버와 연결되지 않음."""

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
res = requests.get(xmlUrl, 
        params = parameters,
        headers={
                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.272 Whale/2.9.118.16 Safari/537.36',
                 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                 'Accept-Encoding': 'gzip, deflate',
                 'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
                 'Cache-Control': 'max-age=0',
                 'Connection': 'keep-alive',
                 'Host':'opendata.kwater.or.kr',
                 'Upgrade-Insecure-Requests':'1',
                 'Cookie':'GA1.3.2044898359.1615768575; WMONID=jf5V6G2_gOp; JSESSIONID=vERA0hWAfkExxBvGTlUsKfkEO6q056Y1DUsSLsWMqA37YBq1JeUX4jSmuq01135N.komwaso2_servlet_engine1'
             })

print(res.url)
print(res.status_code)

response = res.text.encode('utf-8')
xmlobj = bs4.BeautifulSoup(response, 'lxml-xml')  





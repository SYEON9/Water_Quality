'''make mongodb'''
db.createCollection('local', {
  validator: {
    $jsonSchema: {
      bsonType: 'object',
      title: 'local',
      required: ['name'],
      properties: {
        name: {
          bsonType: 'string'
        },
        purification_plant: {
          bsonType: 'array',
          items: {
            title: 'wide_water_purification_plant',
            required: ['purification', 'date', 'taste', 'smell', 'color', 'pH', 'NTU', 'residual_chlorine'],
            properties: {
              purification: {
                bsonType: 'string'
              },
              date: {
                bsonType: 'string'
              },
              taste: {
                bsonType: 'string'
              },
              smell: {
                bsonType: 'string'
              },
              color: {
                bsonType: 'double'
              },
              pH: {
                bsonType: 'double'
              },
              NTU: {
                bsonType: 'double'
              },
              residual_chlorine: {
                bsonType: 'double'
              }
            }
          }
        },
        multiPurpose_dam: {
          bsonType: 'array',
          items: {
            title: 'multiPurpose_dam',
            required: ['dam', 'month', 'pH', 'DO', 'BOD', 'COD', 'NTU'],
            properties: {
              dam: {
                bsonType: 'string'
              },
              month: {
                bsonType: 'string'
              },
              pH: {
                bsonType: 'double'
              },
              DO: {
                bsonType: 'double'
              },
              BOD: {
                bsonType: 'double'
              },
              COD: {
                bsonType: 'double'
              },
              NTU: {
                bsonType: 'double'
              }
            }
          }
        }
      }
    }
  }
});



'''insert Data'''
db.local.insertMany([
{
	name: "경상북도",
	purification_plant: [
		{purification:"부남정수장", date:"20190618", taste:"적합", smell:"적합", color: 1, pH:7.47 ,NTU:0.040 ,residual_chlorine: 0.82},
		{purification:"부남정수장", date:"20190617", taste:"적합", smell:"적합", color: 0, pH:7.42 ,NTU:0.020 ,residual_chlorine: 0.89},
		{purification:"부남정수장", date:"20190616", taste:"적합", smell:"적합", color: 0, pH:7.47 ,NTU:0.020 ,residual_chlorine: 0.79},
		{purification:"안덕정수장", date:"20190618", taste:"적합", smell:"적합", color: 1, pH:7.43 ,NTU:0.100 ,residual_chlorine: 1.23},
		{purification:"안덕정수장", date:"20190617", taste:"적합", smell:"적합", color: 1, pH:7.44 ,NTU:0.120 ,residual_chlorine: 1.10},
		{purification:"안덕정수장", date:"20190616", taste:"적합", smell:"적합", color: 1, pH:7.45 ,NTU:0.160 ,residual_chlorine: 1.09},
		{purification:"주왕산정수장", date:"20190618", taste:"적합", smell:"적합", color: 1, pH:7.44 ,NTU:0.070 ,residual_chlorine: 0.56},
		{purification:"주왕산정수장", date:"20190617", taste:"적합", smell:"적합", color: 1, pH:7.41 ,NTU:0.090 ,residual_chlorine: 0.69},
		{purification:"주왕산정수장", date:"20190616", taste:"적합", smell:"적합", color: 0, pH:7.49 ,NTU:0.140 ,residual_chlorine: 0.72}

	],
	multiPurpose_dam: [
		{dam:"안동댐", month:"06", pH: 7.0, DO: 10.6, BOD:1.0 ,COD:2.8 ,NTU:0.9 },
		{dam:"안동댐", month:"05", pH: 7.5, DO: 9.6, BOD:1.3 ,COD:2.8 ,NTU:0.3},
		{dam:"안동댐", month:"04", pH: 7.4, DO: 11.0, BOD:1.0 ,COD:2.4 ,NTU:1.6}
	]
},
{
name: "경상남도",
	purification_plant: [
		{purification:"일운정수장", date:"20190618", taste:"적합", smell:"적합", color: 0, pH:7.11 ,NTU:0.057 ,residual_chlorine: 0.66},
		{purification:"일운정수장", date:"20190617", taste:"적합", smell:"적합", color: 0, pH:7.11 ,NTU:0.066 ,residual_chlorine: 0.72},
		{purification:"일운정수장", date:"20190616", taste:"적합", smell:"적합", color: 0, pH:7.11 ,NTU:0.069 ,residual_chlorine: 0.71}
	],
	multiPurpose_dam: [
		{dam:"밀양댐", month:"06", pH: 7.2, DO: 9.5, BOD:0.7 ,COD:0.8 ,NTU:2.8 },
		{dam:"밀양댐", month:"05", pH: 7.0, DO: 9.7, BOD:0.8 ,COD:1.3 ,NTU:3.1},
		{dam:"밀양댐", month:"04", pH: 7.1, DO: 10.7, BOD:0.7 ,COD:1.9 ,NTU:1.1},
		{dam:"남강댐", month:"06", pH: 7.7, DO: 8.5, BOD:0.3 ,COD:4.1 ,NTU:2.3 },
		{dam:"남강댐", month:"05", pH: 7.7, DO: 10.3, BOD:1.6 ,COD:3.0 ,NTU:15.8},
		{dam:"남강댐", month:"04", pH: 8.1, DO: 9.8, BOD:1.4 ,COD:5.3 ,NTU:1.3},
		{dam:"합천댐", month:"06", pH: 9.7, DO: 9.5, BOD:0.7 ,COD:0.8 ,NTU:1.1 },
		{dam:"합천댐", month:"05", pH: 7.4, DO: 10.6, BOD:0.7 ,COD:1.5 ,NTU:1.0},
		{dam:"합천댐", month:"04", pH: 8.0, DO: 10.3, BOD:0.6 ,COD:2.3 ,NTU:0.5}
	]
}
])


'''data request'''
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



'''수질 오염을 판단하는 기준 데이터.  기준값 이상이면 부적합.
'''

df = pd.DataFrame({
    '기준':['taste','smell','color','pH','NTU','residual_chlorine','DO','BOD','COD'],
    '기준값':['무미','무취','5', '5.8~8.5', '0.5', '4', '5', '6', '6']})

print(df)

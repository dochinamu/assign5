import requests
import json

city = "Seoul"
apikey = '841c6403689d7ac9d3f5cbccdd9de554'
lang = 'kr'
api = f"""https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units=metric"""

result = requests.get(api)
data = json.loads(result.text)

print(data['name'] + '의 날씨입니다.')
print('날씨는 ' + str(data['weather'][0]['description']) + '입니다')
print('현재 온도는 '+ str(data['main']['temp']) +'입니다')
print('체감 온도는 '+ str(data['main']['feels_like']) +'입니다')
print('최저 온도는 '+ str(data['main']['temp_min']) +'입니다')
print('최고 온도는 '+ str(data['main']['temp_max']) +'입니다')
print('습도는 '+ str(data['main']['humidity']) +'입니다')
print('기압은 '+ str(data['main']['pressure']) +'입니다')
print('풍향은 '+ str(data['wind']['deg']) +'입니다')
print('풍향은 '+ str(data['wind']['speed']) +'입니다')
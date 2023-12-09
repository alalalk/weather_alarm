import requests
import json

city_name:str = "Seoul" #도시
apiKey:str = "7e6ef85f6b794bbe0f6dbf35a534b694" #내 API키
lang:str = 'En' #언어
units :str= 'metric' #화씨 온도를 섭씨 온도로 변경
api:str = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={apiKey}&lang={lang}&units={units}"

response = requests.get(api)

# JSON 데이터 피싱
data = json.loads(response.text)

#날씨 정보 출력(특정 정보 취합)
print(f'{city_name}의 날씨: {data["weather"][0]["main"]}')
print(f'현재 온도:{data["main"]["temp"]}c')
print(f'체감 온도:{data["main"]["feels_like"]}c')

weather = f'{data["weather"][0]["main"]}'

import time
import winsound

def set_alarm():

    try:

        alarm_time = input("alarm time: ")

        alarm_hour, alarm_minute = map(int, alarm_time.split(':'))

        if weather== 'Clouds' :
                
                if alarm_minute >= 10:
                    alarm_minute -= 10
                else:
                    alarm_hour -= 1
                    alarm_minute += 50
            
        if weather== 'Snow' :
                
                if alarm_minute >= 10:
                    alarm_minute -= 10
                else:
                    alarm_hour -= 1
                    alarm_minute += 50

        while True:

            current_time = time.localtime()
        

            if (current_time.tm_hour == alarm_hour and current_time.tm_min == alarm_minute):

                print("알람 시간입니다!")

                winsound.Beep(1000, 1000)
                winsound.Beep(1000, 1000)
                winsound.Beep(1000, 1000)
                winsound.Beep(1000, 1000)
                winsound.Beep(1000, 1000)# 1초에 한번씩 총 5번  1000Hz의 소리를 내도록 설정

                if weather== 'Clouds' :
                    from twilio.rest import Client
                    account_sid = 'AC84a7744ae3c717391eb8fb7cb5e7c459'
                    auth_token = '9a9ed83cdd3becba58f3456fc34fa449'
                    client = Client(account_sid, auth_token)

                    message = client.messages.create(to="+8201062489035", from_="+12342310641", body="비가 오니 우산을 챙기세요!")

                    print(message.sid)

                if weather== 'Snow' :
                    from twilio.rest import Client
                    account_sid = 'AC84a7744ae3c717391eb8fb7cb5e7c459'
                    auth_token = '9a9ed83cdd3becba58f3456fc34fa449'
                    client = Client(account_sid, auth_token)

                    message = client.messages.create(to="+8201062489035", from_="+12342310641", body="눈이 오니 출근길 조심하세요!")

                    print(message.sid)

                break
                

            time.sleep(1)  # 1초 동안 대기

    except ValueError:

        print("올바른 형식으로 입력하세요 (예: 09:30).")



if __name__ == "__main__":

    set_alarm()

from twilio.rest import Client
import keys
from bs4 import BeautifulSoup
import requests


def sendMessage():
    client = Client(keys.account_sid, keys.auth_token)

    message = client.messages.create(
        body = "Good morning beast! Here is the weather for you today" + getWeatherReport(),
        from_ = keys.twilio_number,
        to = keys.target_number
    )



def getWeatherReport():
    url = "https://weather.com/weather/tenday/l/USPA1575:1:US"

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    temp = soup.find("p",{"class":"myforecast-current-lrg"}).getText(strip=True)
    condition = soup.find("p",{"class":"myforecast-current"}).text

    return(f'{temp} \n {condition}')


sendMessage()
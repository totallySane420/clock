import pyttsx3
import requests
import json
import time

url = ('https://newsapi.org/v2/top-headlines?apikey=2cdf5904a86b4878b247fc5406c2eff1&country=in')

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate + 10)

volume = engine.getProperty('volume')
engine.setProperty('volume', volume-0.60)

sound = engine.getProperty ('voices');
engine.setProperty('voice', 'sound[1].id')


try:
	response = requests.get(url)
except:
	engine.say("can, t access link, plz check you internet ")

news = json.loads(response.text)

# print(news)
count = 0
for new in news['articles']:
    if count >= 2:
        break
    print("##############################################################\n")
    print(str(new['title']), "\n\n")
    engine.say(str(new['title']))
    print('______________________________________________________\n')

    

    print(str(new['description']), "\n\n")
    engine.say(str(new['description']))
    engine.runAndWait()
    print("..............................................................")
    count += 1

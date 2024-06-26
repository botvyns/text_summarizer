import requests

# url where the app is running with indication of the specific endpoint

url = "http://127.0.0.1:8000/summarize"

# `data` contains text to be summarized

data = {"text": """Ukrainian Cossacks were brave warriors who, under the leadership of great commanders, defended the independence of the Ukrainian state for centuries. They were called “free people” and “knights of the Ukrainian steppes” for their bravery, desire for freedom, and immortal courage.

Cossacks can be called “brothers in arms” of Japanese samurai, European knights, and cowboys of the Wild West for their fighting excellence, loyalty, heroism, and short temper.

Who were the Ukrainian Cossacks: definition 
Ukrainian Cossacks were nomads who led a military lifestyle and earned their livelihood through war and crafts (hunting, fishing, later trade, and agriculture). These people took part in military campaigns and were part of the state troops or outside guards of wealthy people. 
Cossacks are an ancient phenomenon. As the Ukrainian professor Mykhailo Hrushevskyi wrote, the first official mention of the Cossacks appeared in 1492, when warriors attacked a Turkish galley near Tiahyn Castle (the Kherson region) and freed the Ukrainians who had been sold into slavery.

In the 16th century, Cossack people united in various military-political groups, the most famous of which was the Zaporizhzhia Host (or Sich), under the leadership of hetmans and kish otamans such as Dmytro “Baida” Vyshnevetskyi and Ivan Sirko, who fought against the invaders. 

In the 17th century, the Cossacks founded their own Cossack state and called it the Cossack Hetmanate or Hetmanshchyna under the leadership of the first Hetman, Bohdan Khmelnytskyi. """}

response = requests.post(url, json=data)

print(response.json())

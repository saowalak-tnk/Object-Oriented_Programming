import requests 


url = f"https://api.chnwt.dev/thai-gold-api/latest"

result = requests.get(url).json()
#print(result)
date = result['response']['date']
update_time = result['response']['update_time']
buy = result['response']['price']['gold']['buy']
sell = result['response']['price']['gold']['sell']

gold_bar_buy = result['response']['price']['gold_bar']['buy']
gold_bar_sell = result['response']['price']['gold_bar']['sell']


print(f"วันที่ : {date}")
print(f"เวลาอัพเดท : {update_time}")
print(f"Gold (Buy): {buy}")
print(f"Gold (Sell) : {sell}")
print(f"Gold Bar (Buy) : {gold_bar_buy}")
print(f"Gold Bar (Sell) : {gold_bar_sell}")

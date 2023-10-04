from bs4 import BeautifulSoup
import requests

url = "https://www.flipkart.com/search?q=samsung+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=samsung+mobiles%7CMobiles&requestId=21804647-c355-4564-ace9-09414e83fc64&as-searchtext=sam&sort=relevance&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.price_range.from%3D20000&p%5B%5D=facets.price_range.to%3D30000&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG"
res = requests.get(url)
log = BeautifulSoup(res.text, "html.parser")
pages = log.find(class_="_2MImiq")
pages = int(str(pages).split("of")[1][1])
data = {}
for page in range(pages):
    url = f"https://www.flipkart.com/search?q=samsung+mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=samsung+mobiles%7CMobiles&requestId=21804647-c355-4564-ace9-09414e83fc64&as-searchtext=sam&sort=relevance&p%5B%5D=facets.rating%255B%255D%3D4%25E2%2598%2585%2B%2526%2Babove&p%5B%5D=facets.price_range.from%3D20000&p%5B%5D=facets.price_range.to%3D30000&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&page={page}"
    res = requests.get(url)
    log = BeautifulSoup(res.text, "html.parser")
    tags = log.find_all(class_="_3pLy-c row")
    for tag in tags:
        name = tag.find(class_="_4rR01T").text
        star = tag.find(class_="_3LWZlK").text
        price = tag.find(class_="_30jeq3 _1_WHN1").text
        data[name] = {"star": star, "price": price}

sorted_items = sorted(data.items(), key=lambda x: x[1]['price'])

for dt in sorted_items:
    print(dt[0])
    print(dt[1]["star"])
    print(dt[1]["price"])
    print()

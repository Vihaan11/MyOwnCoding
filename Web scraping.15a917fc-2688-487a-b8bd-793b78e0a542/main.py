import requests,bs4

base_url = "https://books.toscrape.com/catalogue/page-{}.html"

for pageno in range(1,51):
    myres = requests.get(base_url.format(str(pageno)))
    mysoup = bs4.BeautifulSoup(myres.text,"lxml")
    myproducts = mysoup.select(".product_pod")
    for product in myproducts:
        if len(product.select(".star-rating.Two"))==0:
            continue
        else:
            mytitle = product.select("a")[1]["title"]
            print(mytitle)            
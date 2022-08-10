import requests
from bs4 import BeautifulSoup
#from products.models import Product

#jumia_product_url = "https://www.jumia.com.ng/infinix-32-inch-smart-android-tv-71343628.html"
#konga_product_url = "https://www.konga.com/product/nexus-nexus-43-hd-smart-led-tv-5610823"
#kara_product_url = "https://kara.com.ng/apple-iphone-13pro-max-512gb-rom"
headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36"}

# for jumia
#page = requests.get(url=jumia_product_url, headers=headers) 
#soup = BeautifulSoup(page.content,'lxml')

def jumia(jumia_product_url):

   page = requests.get(url=jumia_product_url, headers=headers) 
   soup = BeautifulSoup(page.content,'lxml')

   jumia_title = soup.find(class_ = "-fs20 -pts -pbxs").get_text().strip()

   jumia_price = soup.find(class_ = "-b -ltr -tal -fs24").get_text().strip()
   #print("For Jumia\n" + jumia_price + "\n" + jumia_title+ "\n")
   return(jumia_price)

#jumia()


#page = requests.get(url=konga_product_url, headers=headers) 
#soup = BeautifulSoup(page.content,'lxml')
# for konga
def konga(konga_product_url):
   
   page = requests.get(url=konga_product_url, headers=headers) 
   soup = BeautifulSoup(page.content,'lxml')

   konga_title = soup.find(class_ = "_24849_2Ymhg").get_text().strip()

   konga_price = soup.find(class_ = "_678e4_e6nqh").get_text().strip()
   #print("For Konga\n" + konga_price + "\n" + konga_title+ "\n")
   return(konga_price)

#konga()

#page = requests.get(url=kara_product_url, headers=headers) 
#soup = BeautifulSoup(page.content,'lxml')
# for konga
def kara(kara_product_url):

   page = requests.get(url=kara_product_url, headers=headers) 
   soup = BeautifulSoup(page.content,'lxml')   
   kara_title = soup.find(class_ = "base").get_text().strip()

   kara_price = soup.find(class_ = "price").get_text().strip()
   #print("For Kara\n" + kara_price + "\n" + kara_title)
   return(kara_price)

#kara()
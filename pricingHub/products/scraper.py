import requests
from bs4 import BeautifulSoup

headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36"}

# Iphones Note: Prices are limited due to what we could find on Kara
jumia_iphone11_64gb = "https://www.jumia.com.ng/apple-refurbished-class-b-apple-iphone-11-64gb-green-88600142.html"
konga_iphone11_64gb = "https://www.konga.com/product/apple-iphone-11-6-4-64gb-rom-4gb-ram-red-5471223"
kara_iphone11_64gb = "https://kara.com.ng/apple-iphone-11-64gb"
jumia_iphone11_128gb = "https://www.jumia.com.ng/iphone-11-6.1-inch-liquid-retina-lcd-4gb-ram-128gb-rom-ios-13-12mp12mp12mp-4g-lte-smartphone-red-apple-mpg1595382.html"
konga_iphone11_128gb = "https://www.konga.com/product/apple-iphone-11-6-1-128gb-rom-4gb-ram-nano-sim-3000mah-5695741"
kara_iphone11_128gb = "https://kara.com.ng/apple-iphone-11-128gb"


jumia_iphone12_mini = "https://www.jumia.com.ng/apple-iphone-12-6.1-inches-5gb-ram-64gb-rom-black-108447672.html"
konga_iphone12_mini = "https://www.konga.com/product/apple-iphone-12-6-1-4gb-ram-2815mah-pacific-blue-5382621"
kara_iphone12_mini = "https://kara.com.ng/apple-iphone-12-mini-purple-64gb-afe-mgqf3aa-a"
jumia_iphone12 = "https://www.jumia.com.ng/iphone-12-6.1-inches-4gb-ram-64gb-rom-12mp-12mp-2815mah-black-apple-mpg1566249.html"
konga_iphone12 = "https://www.konga.com/product/apple-iphone-12-64gb-rom-4gb-ram-6-1-2815mah-red-5246877"
kara_iphone12 = "https://kara.com.ng/apple-iphone-12-black-64gb-afe-mgj53an-a"
jumia_iphone12pro = "https://www.jumia.com.ng/iphone-12-pro-max-128gb-6gb-ram-6.7-inch12mp12mp12mp-pacific-blue-apple-mpg1595396.html"
konga_iphone12pro = "https://www.konga.com/product/apple-iphone-12-pro-6gb-128gb-gold-5171724"
kara_iphone12pro = "https://kara.com.ng/apple-iphone-12pro-gold-128gb-afe-gmm3aa-a"
jumia_iphone12pro_256gb = "https://www.jumia.com.ng/iphone-13-pro-max-6.7-super-retina-xdr-display-6gb-ram-128gb-rom-ios-15-gold-apple-mpg1636720.html"
konga_iphone12pro_256gb = "https://www.konga.com/product/apple-iphone-12-pro-max-256gb-rom-4gb-ram-5033923"
kara_iphone12pro_256gb = "https://kara.com.ng/apple-iphone-12pro-graphite-256gb-afe-mgmp3aa-a"

jumia_iphone13pro_256gb = "https://www.jumia.com.ng/iphone-13-6.1-super-retina-xdr-display-4gb-ram-256gb-rom-ios-15-with-facetime-midnight-black-apple-mpg1625142.html"
konga_iphone13pro_256gb = "https://www.konga.com/product/apple-iphone-13-4gb-256gb-pink-5476826"
kara_iphone13pro_256gb = "https://kara.com.ng/apple-iphone-13pro-256gb"
jumia_iphone13promax_512gb = "https://www.jumia.com.ng/apple-iphone-13-pro-max-6.7-xdr-display-6gb-ram-512gb-romfacetime-125767884.html"
konga_iphone13promax_512gb = "https://www.konga.com/product/apple-iphone-13-pro-max-5g-single-sim-512gb-rom-6gb-ram-6-7-oled-ios-15-4352mah-graphite-5456541"
kara_iphone13promax_512gb = "https://kara.com.ng/apple-iphone-13pro-max-512gb-rom"
jumia_iphone13promax_1tb = "https://www.jumia.com.ng/apple-iphone-13-pro-max-6gb-ram-1tb-rom-gold-139050507.html"
konga_iphone13promax_1tb = "https://www.konga.com/product/apple-iphone-13-pro-max-5g-single-sim-1tb-rom-6gb-ram-6-7-oled-ios-15-4352mah-gold-5456544"
kara_iphone13promax_1tb = "https://kara.com.ng/apple-iphone-13pro-max-1tb-rom"


# for iphone13pro_256gb
page = requests.get(url=jumia_iphone13pro_256gb, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')
def jumiaiphone13pro_256gb():
   jumia_title = soup.find(class_ = "-fs20 -pts -pbxs").get_text().strip()
   jumia_price = soup.find(class_ = "-b -ltr -tal -fs24").get_text().strip()

   print("For Jumia\n" + jumia_price + "\n" + jumia_title+ "\n")

jumiaiphone13pro_256gb()

page = requests.get(url=konga_iphone13pro_256gb, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')
def kongaiphone13pro_256gb():
   konga_title = soup.find(class_ = "_24849_2Ymhg").get_text().strip()
   konga_price = soup.find(class_ = "_678e4_e6nqh").get_text().strip()

   print("For Konga\n" + konga_price + "\n" + konga_title + "\n")

kongaiphone13pro_256gb()

page = requests.get(url=kara_iphone13pro_256gb, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')
def karaiphone13pro_256gb():
   kara_title = soup.find("span", class_ = "base").get_text().strip()
   kara_price = soup.find("span", class_ = "price").get_text().strip()

   print("For Kara\n" + kara_price + "\n" + kara_title + "\n")

karaiphone13pro_256gb()

# for iphone13promax_512gb
page = requests.get(url=jumia_iphone13promax_512gb, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')

def jumia():
   jumia_title = soup.find(class_ = "-fs20 -pts -pbxs").get_text().strip()
   jumia_price = soup.find(class_ = "-b -ltr -tal -fs24").get_text().strip()

   print("For Jumia\n" + jumia_price + "\n" + jumia_title+ "\n")

jumia()


page = requests.get(url=konga_iphone13promax_512gb, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')
def konga():
   konga_title = soup.find(class_ = "_24849_2Ymhg").get_text().strip()
   konga_price = soup.find(class_ = "_678e4_e6nqh").get_text().strip()

   print("For Konga\n" + konga_price + "\n" + konga_title+ "\n")

konga()


page = requests.get(url=kara_iphone13promax_512gb, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')
def kara():
   kara_title = soup.find("span", class_ = "base").get_text().strip()
   kara_price = soup.find("span", class_ = "price").get_text().strip()

   print("For Kara\n" + kara_price + "\n" + kara_title + "\n")

kara()

# for iphone13promax_1tb
page = requests.get(url=jumia_iphone13promax_1tb, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')
def jumiaiphone13promax_1tb():
   jumia_title = soup.find(class_ = "-fs20 -pts -pbxs").get_text().strip()
   jumia_price = soup.find(class_ = "-b -ltr -tal -fs24").get_text().strip()

   print("For Jumia\n" + jumia_price + "\n" + jumia_title+ "\n")

jumiaiphone13promax_1tb()

page = requests.get(url=konga_iphone13promax_1tb, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')
def kongaiphone13promax_1tb():
   konga_title = soup.find(class_ = "_24849_2Ymhg").get_text().strip()
   konga_price = soup.find(class_ = "_678e4_e6nqh").get_text().strip()

   print("For Konga\n" + konga_price + "\n" + konga_title+ "\n")

kongaiphone13promax_1tb()

page = requests.get(url=kara_iphone13promax_1tb, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')
def karaiphone13promax_1tb():
   kara_title = soup.find("span", class_ = "base").get_text().strip()
   kara_price = soup.find("span", class_ = "price").get_text().strip()

   print("For Kara\n" + kara_price + "\n" + kara_title + "\n")

karaiphone13promax_1tb()


# for iphone12_mini
page = requests.get(url=jumia_iphone12_mini, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')
def jumiaiphone12_mini():
   jumia_title = soup.find(class_ = "-fs20 -pts -pbxs").get_text().strip()
   jumia_price = soup.find(class_ = "-b -ltr -tal -fs24").get_text().strip()

   print("For Jumia\n" + jumia_price + "\n" + jumia_title+ "\n")

jumiaiphone12_mini()

page = requests.get(url=konga_iphone12_mini, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')
def kongaiphone12_mini():
   konga_title = soup.find(class_ = "_24849_2Ymhg").get_text().strip()
   konga_price = soup.find(class_ = "_678e4_e6nqh").get_text().strip()

   print("For Konga\n" + konga_price + "\n" + konga_title+ "\n")

kongaiphone12_mini()

page = requests.get(url=kara_iphone12_mini, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')
def karaiphone12_mini():
   kara_title = soup.find("span", class_ = "base").get_text().strip()
   kara_price = soup.find("span", class_ = "price").get_text().strip()

   print("For Kara\n" + kara_price + "\n" + kara_title + "\n")

karaiphone12_mini()


# for iphone12
page = requests.get(url=jumia_iphone12, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')
def jumiaiphone12():
   jumia_title = soup.find(class_ = "-fs20 -pts -pbxs").get_text().strip()
   jumia_price = soup.find(class_ = "-b -ltr -tal -fs24").get_text().strip()

   print("For Jumia\n" + jumia_price + "\n" + jumia_title+ "\n")

jumiaiphone12()

page = requests.get(url=konga_iphone12, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')
def kongaiphone12():
   konga_title = soup.find(class_ = "_24849_2Ymhg").get_text().strip()
   konga_price = soup.find(class_ = "_678e4_e6nqh").get_text().strip()

   print("For Konga\n" + konga_price + "\n" + konga_title+ "\n")

kongaiphone12()

page = requests.get(url=kara_iphone12, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')
def karaiphone12():
   kara_title = soup.find("span", class_ = "base").get_text().strip()
   kara_price = soup.find("span", class_ = "price").get_text().strip()

   print("For Kara\n" + kara_price + "\n" + kara_title + "\n")

karaiphone12()

# for iphone12pro
page = requests.get(url=jumia_iphone12pro, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')

def jumia1():
   jumia_title = soup.find(class_ = "-fs20 -pts -pbxs").get_text().strip()
   jumia_price = soup.find(class_ = "-b -ltr -tal -fs24").get_text().strip()

   print("For Jumia\n" + jumia_price + "\n" + jumia_title+ "\n")

jumia1()

page = requests.get(url=konga_iphone12pro, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')
def konga1():
   konga_title = soup.find(class_ = "_24849_2Ymhg").get_text().strip()
   konga_price = soup.find(class_ = "_678e4_e6nqh").get_text().strip()

   print("For Konga\n" + konga_price + "\n" + konga_title+ "\n")

konga1()

page = requests.get(url=kara_iphone12pro, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')
def kara1():
   kara_title = soup.find("span", class_ = "base").get_text().strip()
   kara_price = soup.find("span", class_ = "price").get_text().strip()
   
   print("For Kara\n" + kara_price + "\n" + kara_title + "\n")

kara1()

# for iphone12pro_256gb
page = requests.get(url=jumia_iphone12pro_256gb, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')

def jumia1_256gb():
   jumia_title = soup.find(class_ = "-fs20 -pts -pbxs").get_text().strip()
   jumia_price = soup.find(class_ = "-b -ltr -tal -fs24").get_text().strip()

   print("For Jumia\n" + jumia_price + "\n" + jumia_title+ "\n")

jumia1_256gb()

page = requests.get(url=konga_iphone12pro_256gb, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')
def konga1_256gb():
   konga_title = soup.find(class_ = "_24849_2Ymhg").get_text().strip()
   konga_price = soup.find(class_ = "_678e4_e6nqh").get_text().strip()

   print("For Konga\n" + konga_price + "\n" + konga_title+ "\n")

konga1_256gb()

page = requests.get(url=kara_iphone12pro_256gb, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')
def kara1_256gb():
   kara_title = soup.find("span", class_ = "base").get_text().strip()
   kara_price = soup.find("span", class_ = "price").get_text().strip()
   
   print("For Kara\n" + kara_price + "\n" + kara_title + "\n")

kara1_256gb()


# for iphone11_64gb
page = requests.get(url=jumia_iphone11_64gb, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')

def jumia2():
   jumia_title = soup.find(class_ = "-fs20 -pts -pbxs").get_text().strip()

   jumia_price = soup.find(class_ = "-b -ltr -tal -fs24").get_text().strip()
   print("For Jumia\n" + jumia_price + "\n" + jumia_title+ "\n")

jumia2()

page = requests.get(url=konga_iphone11_64gb, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')
def konga2():
   
   konga_title = soup.find(class_ = "_24849_2Ymhg").get_text().strip()

   konga_price = soup.find(class_ = "_678e4_e6nqh").get_text().strip()
   print("For Konga\n" + konga_price + "\n" + konga_title+ "\n")

konga2()

page = requests.get(url=kara_iphone11_64gb, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')
def kara2():
   kara_title = soup.find("span", class_ = "base").get_text().strip()
   kara_price = soup.find("span", class_ = "price").get_text().strip()
   
   print("For Kara\n" + kara_price + "\n" + kara_title + "\n")

kara2()

# for iphone11_128gb
page = requests.get(url=jumia_iphone11_128gb, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')
def jumiaiphone11_128gb():
   jumia_title = soup.find(class_ = "-fs20 -pts -pbxs").get_text().strip()
   jumia_price = soup.find(class_ = "-b -ltr -tal -fs24").get_text().strip()

   print("For Jumia\n" + jumia_price + "\n" + jumia_title+ "\n")

jumiaiphone11_128gb()

page = requests.get(url=konga_iphone11_128gb, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')
def kongaiphone11_128gb():
   konga_title = soup.find(class_ = "_24849_2Ymhg").get_text().strip()
   konga_price = soup.find(class_ = "_678e4_e6nqh").get_text().strip()

   print("For Konga\n" + konga_price + "\n" + konga_title+ "\n")

kongaiphone11_128gb()

page = requests.get(url=kara_iphone11_128gb, headers=headers) 
soup = BeautifulSoup(page.content,'lxml')
def karaiphone11_128gb():
   kara_title = soup.find("span", class_ = "base").get_text().strip()
   kara_price = soup.find("span", class_ = "price").get_text().strip()

   print("For Kara\n" + kara_price + "\n" + kara_title + "\n")

karaiphone11_128gb()
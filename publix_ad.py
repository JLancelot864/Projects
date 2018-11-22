import bs4 as bs
import urllib.request


##you may want to try ""add favorite_sale_items = print favorite sale items

item = input("What sale item are you looking for?")
    


##also needs to print what it is on sale for 
def data():
    for num in range(1,5):
        sauce = urllib.request.urlopen('http://weeklyad.publix.com/PublixAccessibility/BrowseByPage?PromotionID=137850&PromotionViewMode=1&StoreID=2500176&PageNumber='+str(num) +"&BreadCrumb=Weekly+Ad&SneakPeek=N").read()
        soup = bs.BeautifulSoup(sauce, 'lxml')


        for div in soup.find_all('div', class_="positionGridTileImage excludeFromMobile"):
            img = div.find('img', alt=True)
            sale_item = img['alt']
            print(sale_item)

#this is supposed to 
            
   
######        if item in sale_item:
######            print('this item is not on sale')
######        
######        else:
######            print('on sale')
######        

data()
  

##add sale type to true line +sale_type




##    if item != sale_item
##    print ('This item is not on sale!, try again next week!')

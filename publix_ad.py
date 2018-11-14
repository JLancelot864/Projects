import bs4 as bs
import urllib.request


sauce = urllib.request.urlopen('http://weeklyad.publix.com/PublixAccessibility/BrowseByPage?PromotionID=137850&PromotionViewMode=1&StoreID=2500176&PageNumber=3&BreadCrumb=Weekly+Ad&SneakPeek=N').read()
soup = bs.BeautifulSoup(sauce, 'lxml')

print(soup)

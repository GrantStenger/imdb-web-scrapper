import requests, bs4
response = requests.get('http://www.imdb.com/user/ur53580546/ratings?sort=your_rating,desc&ratingFilter=0&mode=detail&ref_=undefined&lastPosition=0#void')
soup = bs4.BeautifulSoup(response.text)
for i in range(25):
	print(soup.find_all("h3", class_="lister-item-header")[i].select('a')[0].getText())

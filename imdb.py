import requests
import time
import csv
import re
from random import randint
from bs4 import BeautifulSoup

pages=110
headers = {"Accept-Language": "en-US, en;q=0.5"}  #accept only US language or other english lang
count=0
results=[[0 for x in range(0,6)]for y in range(0,50*pages)]	#store results here
for i in range(1,pages+1):

	#url="http://www.imdb.com/search/title?release_date=%d&sort=num_votes,desc&page=1" % (i+2006)
	url="https://www.imdb.com/search/title?title_type=feature&release_date=1990-01-01,&user_rating=5.0,10.0&runtime=85,&sort=num_votes,desc&page=%d" % (i)
	response=requests.get(url,headers=headers)
	if response.status_code!=200:
		print("Response wasnt OK,Termination!")
		break
	time.sleep(randint(2,5))
	
	print(i)
	soup=BeautifulSoup(response.text,'html.parser')
	#extracat useful html data using BeautifulSoup
	for tag in soup.find_all("div",class_ ='lister-item mode-advanced'):
		
		rating_div=tag.find("div",class_="ratings-bar")
		runtime=tag.find("p",class_="text-muted")
		num_votes=tag.find("p",class_="sort-num_votes-visible")
		real_runtime=runtime.find("span",class_="runtime")
		
		results[count][0]=str(tag.h3.contents[3].string.strip())		#title
		results[count][1]=int(re.sub("[^0-9]", "",tag.h3.contents[5].string.strip()))		#year
		results[count][2]=float(rating_div.contents[1].contents[3].string.strip())*10*9		#IMDb rating
		has_metascore=rating_div.find("div",class_="inline-block ratings-metascore")
		if has_metascore:
			results[count][2]+=float(rating_div.contents[5].contents[1].string.strip())		#Metascore
		else:
			results[count][2]+=results[count][2]/9
		results[count][3]=re.sub("[^0-9]", "",real_runtime.string.strip())		#Runtime
		genre=runtime.find("span",class_="genre")
		gen=str(genre.string.strip())
		#if gen.find("Music")>=0:
		#	results[count][2]-=7
		#elif gen.find("Animation")>=0:
		#	results[count][2]-=5
		results[count][4]=str(genre.string.strip())		#Genres
		results[count][5]=int(num_votes.contents[3].string.replace(',','').strip())	#Votes
		
		
		results[count][2]=results[count][2]/10		#total score
		count+=1
		
		
	

with open("movies.csv",'w',newline='') as csvfile:
	wr=csv.writer(csvfile,quoting=csv.QUOTE_NONNUMERIC)
	wr.writerows(results)


#print(results)


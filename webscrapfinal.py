from bs4 import BeautifulSoup
import urllib2

url="http://www.imdb.com/chart/top"
page=urllib2.urlopen(url) #Response of the the 'url'

soup = BeautifulSoup(page.read()) #Beautifulsoup parses the contents of the page
table1=soup.find('table',attrs={'class':'chart full-width'}) #Finds a specific table with attribute `results`
table_body=table1.find('tbody')

rows=table_body.findAll('tr') #Finds specific table rows

target = open('Movies.txt','w');#Opens a file with rights 'write'
target.truncate()
i=0;
for row in rows:
	if i==10: #To obtain first 10 rows
		break;
	row_data=row.find('td','titleColumn') # Finds specific table data
	title=row_data.find('a') #Finds the title of the movie
	print title.text	#to obtain the name of the movie

	synopsis=title['href'] #hyperlink to the synopsis page

	url1="http://imdb.com"
	url1=url1+synopsis   #Hyperlink

	pagesynopsis=urllib2.urlopen(url1) #Open the url to the synopsis
	soup1=BeautifulSoup(pagesynopsis.read()) #Parses the response of the url
	#To extract the desired content from the page
	divbody=soup1.find("body",class_="fixed")  
	divdesign=divbody.find("div",class_="redesign")
	divpage=divdesign.find("div",class_="pagecontent")
	divflat=divpage.find("div",class_="flatland")
	divmain=divflat.find('div',id="main_bottom")
	divcontent=divpage.find('div',id="titleStoryLine")
	divcontent1=divcontent.find("div",class_="inline canwrap")
	description=divcontent1.find('p').text
		
	#writes in the file
	target.write("Title: ") 
	target.write(title.text)
	target.write("\n")
	target.write("Synopsis: ")
	target.write(description)
	target.write("\n")
	target.write("***")
	target.write("\n\n")
	
	i=i+1; #counter


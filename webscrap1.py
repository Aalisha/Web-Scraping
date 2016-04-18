from bs4 import BeautifulSoup
import urllib2

url="http://www.imdb.com/search/title?year=2015,2015&title_type=feature&sort=moviemeter,asc"
page=urllib2.urlopen(url) #Response of the the 'url'

soup = BeautifulSoup(page.read()) #Beautifulsoup parses the contents of the page
table=soup.find('table',attrs={'class':'results'}) #Finds a specific table with attribute `results`

rows=table.findAll('tr',attrs={'class':'even detailed','class':'odd detailed'}) #Finds specific table rows

target = open('Movies.txt','w');#Opens a file with rights 'write'
target.truncate()
i=0;
for row in rows:
	if i==10: #To obtain first 10 rows
		break;
	row_data=row.find('td','title') # Finds specific table data
	title=row_data.find('a') #Finds the title of the movie
	synopsis=row_data.find('span',attrs={'class':'outline'}) #Finds the class with the synopsis of the movie
	target.write("Title: ") #Writes in the file
	target.write(title.text)
	target.write("\n")
	target.write("Synopsis: ")
	target.write(synopsis.text)
	target.write("\n")
	target.write("***")
	target.write("\n\n")
	i=i+1; #counter

	


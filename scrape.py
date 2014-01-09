import urllib2
from bs4 import BeautifulSoup

#create and open a (comme separated) file called data.txt 
f = open('get-data.csv', 'w')


#Iterate through the projects 
for p in range (1, 1000):
	
	#Open the website
	print "Retrieving entry " + str(p) + " from visualcomplexity..." 
	url = "http://www.visualcomplexity.com/vc/project_details.cfm?id=" + str(p) + "&index=" + str(p) + "&domain="
	page = urllib2.urlopen(url)

	#Get titles from page
	soup = BeautifulSoup(page)
	titles = soup.findAll(attrs={"class":"ProjectTitle"})
	#Format and print
	for t in titles:
		titleText = ''.join(t.findAll(text=True))
    	titleData = titleText.strip()
	print "Title: " + titleData

	#Get section/ProjectDomains from page
	grp = soup.findAll(attrs={"class":"DomainInProject"})
	#Format and print
	for g in grp:
		groupText = ''.join(g.findAll(text=True))
		groupData = groupText.strip()
	print "Section: " + groupData + '\n'

	#Format data list

	#write data to file
	f.write(str(p) + "," + titleData + "," + groupData + '\n')

#Close the file
f.close()



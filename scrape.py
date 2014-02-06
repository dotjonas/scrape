import urllib2
from bs4 import BeautifulSoup

#Create and open a new .csv file 
f = open('get-data.csv', 'w')


#Iterate through the projects 
for p in range (1, 1000):
	
	#Open the website
	print "Retrieving entry " + str(p) + " from visualcomplexity..." 
	url = "http://www.visualcomplexity.com/vc/project_details.cfm?id=" + str(p) + "&index=" + str(p) + "&domain="
	page = urllib2.urlopen(url)
	soup = BeautifulSoup(page)

	#Get titles from page
	titles = soup.findAll(attrs={"class":"ProjectTitle"})
	
	#Format and print titles
	for t in titles:
		titleText = ''.join(t.findAll(text=True))
    	titleData = titleText.strip()
	print "Title: " + titleData

	#Get section/ProjectDomains from page
	grp = soup.findAll(attrs={"class":"DomainInProject"})
	
	#Format and print groups
	for g in grp:
		groupText = ''.join(g.findAll(text=True))
		groupData = groupText.strip()
	print "Section: " + groupData

	#Get year for each project
	year = soup.findAll(attrs={"class":"bodytext"})
	
	for y in year:
		bodyText = ''.join(y.findAll(text=True))
		
		if len(bodyText) == 4:
			yearText = ''.join(y.findAll(text=True))
			yearData = yearText.strip()
			print "Year: " + yearData + '\n' + "Done!" + '\n'

	
	#Add data to list of documents for LSA


	#write data to .csv file
	f.write(str(p) + "," + titleData + "," + groupData + "," + yearData + '\n')

#Close the file
f.close()



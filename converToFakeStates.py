'''

This converts avian flu data from csv to geojson

'''
import csv

#doing it with string for now, should use json ojbect instead
jsonString = "{\"states\":["

with open('flu_with_location.csv', 'rU') as csvfile:
	fluereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	reader = csv.DictReader(csvfile)
	for row in reader:
		jsonString = jsonString + "{\"state\": \"" + row['State'] + "\","
		jsonString = jsonString + "\"avian_indiator\":true},"
		
	   
	    
jsonString = jsonString + "]}"


geoJsonPage = open("avian_flu_fake.geojson", "w")
geoJsonPage.write(jsonString)
geoJsonPage.close()

         
    
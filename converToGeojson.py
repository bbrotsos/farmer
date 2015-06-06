'''

This converts avian flu data from csv to geojson

'''
import csv

#doing it with string for now, should use json ojbect instead
jsonString = "{\"features\":["

with open('flu_with_location.csv', 'rU') as csvfile:
	fluereader = csv.reader(csvfile, delimiter=' ', quotechar='|')
	reader = csv.DictReader(csvfile)
	for row in reader:
		
	    print (row['County'])
	    jsonString = jsonString + "{\"type\": \"Feature\", \"geometry\":{\"type\":\"Point\",\"coordinates\":[" + row['LATITUDE'] + "," + row['LONGITUDE'] + "]},"
	    
	    jsonString = jsonString + "\"properties\": { \"name\": \"" + row['County'] +"\"}},"
	    
jsonString = jsonString + "]}"


geoJsonPage = open("avian_flu.geojson", "w")
geoJsonPage.write(jsonString)
geoJsonPage.close()

         
    
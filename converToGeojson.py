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
		
	    print (row['flock_size'])
	    jsonString = jsonString + "{\"type\": \"Feature\", \"geometry\":{\"type\":\"Point\",\"coordinates\":[" + row['LATITUDE'] + "," + row['LONGITUDE'] + "]},"
	    
	    jsonString = jsonString + "\"properties\": { \"name\": \"" + row['flock_size'] + "\","
	    if (row['flock_size']== "pending"): 
			jsonString = jsonString + "\"flock_size\":0,"
	    else:
	    	jsonString = jsonString + "\"flock_size\":" + row['flock_size'] + ","
	    jsonString = jsonString + "\"flyway\":\"" + row['Flyway'] + "\","
	    jsonString = jsonString + "\"species\":\"" + row['Species'] + "\","
	    jsonString = jsonString + "\"subtype\":\"" + row['subtype'] + "\","
	    jsonString = jsonString + "\"confirmation_date\":\"" + row['confirmation_date'] + "\""
	    jsonString = jsonString + "}},"
	    
jsonString = jsonString + "]}"


geoJsonPage = open("avian_flu.geojson", "w")
geoJsonPage.write(jsonString)
geoJsonPage.close()

         
    
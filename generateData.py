#!/usr/bin/env python

import math
import subprocess

###
# Produce a series of regular points in WGS84 to cover the whole BNG
###

###
# Spherical Law of Cosines
# http://www.movable-type.co.uk/scripts/latlong.html
###
def calculateDistance(lon1, lat1, lon2, lat2):
	latr1 = math.radians(lat1)
	latr2 = math.radians(lat2)
	diffLon = math.radians(lon2-lon1)
	R = 6371000;
	return math.acos(math.sin(latr1) * math.sin(latr2) + math.cos(latr1) * math.cos(latr2) * math.cos(diffLon) ) * R;

# These are the false origin of the British National Grid, converted to decimal degrees
falseoriginLat = 49 + (45/60) + (58/3600)
falseoriginLon = -1 * (7 + (33/60) + (23/3600))
bngWidth = 700000
bngHeight = 1300000

### GB Settings ###
# START_LAT = falseoriginLat
# START_LON = falseoriginLon
# WIDTH = bngWidth
# HEIGHT = bngHeight
# INCREMENT = 0.5 # THE INCREMENT (GRID RESOLUTION) IN DEGREES

### STORNOWAY SETTINGS ###
START_LAT = 58.21030268118494
START_LON = -6.3855332104069475
WIDTH = 100
HEIGHT = 100
INCREMENT = 0.0001 # THE INCREMENT (GRID RESOLUTION) IN DEGREES

# Init values
currLon = START_LON
currLat = START_LAT

# open a file
f = open('grid.csv', 'w')

# print header and false origin
f.write("id,longitude,latitude\n")

# id counter
n = 1

# Build a grid of values
while(calculateDistance(START_LON, START_LAT, currLon, START_LAT) < WIDTH):
	while(calculateDistance(START_LON, START_LAT, START_LON, currLat) < HEIGHT):
	
		# write coordinates to file
		f.write(`n` + "," + `currLon` + "," + `currLat` + "\n")
		
		# increment Y
		currLat += INCREMENT
		
		# increment id
		n += 1
		
	# increment X
	currLon += INCREMENT
	
	# reset Y
	currLat = START_LAT

# free up the file
f.close()
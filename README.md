# OSTN02-Script

This bash script quickly draws an illustration of the differences between coordinates after transforming them using 3-Parameter, 7-Parameter and OSTN02 transformations between WGS84 and OSGB36.

It draws a grid of poionts in WGS84 Latitude and Longitude, transforms them using all three types of trabnsformation, and then draws them using Mapnik so that you can see the difference.

To run, use:
`bash ./transformation.sh`

For more information, and some examples, see the blog post [here](https://geographicalinformation.science/2015/11/09/transforming-between-osgb36-and-wgs84-using-ostn02/).

Requirements:
* Python 2.7
* OGR2OGR
* Mapnik
* Nik2Img.py

###TODO:
Make it more user friendly so that users don't have to edit multiple files to set parameters

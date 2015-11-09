# OSTN02-Script

This bash script quickly draws an illustration of the differences between coordinates after transforming them using 3-Parameter, 7-Parameter and OSTN02 transformations between WGS84 and OSGB36.

It draws a grid of poionts in WGS84 Latitude and Longitude, transforms them using all three types of trabnsformation, and then draws them using Mapnik. They points are rendered using a CYM Multiplication composite operation:
![CYM Legend](https://jonnyhuckblog.files.wordpress.com/2015/11/point.png)

Here is an example 100m square from Stornoway, Isle of Lewis (Where differences between them are high):
![Stornoway Example](https://jonnyhuckblog.files.wordpress.com/2015/11/gb2.png)

To run, use:
`bash ./transformation.sh`

For more information, see the blog post [here](https://jonnyhuckblog.wordpress.com/2015/11/09/transforming-between-osgb36-and-wgs84-using-ostn02/).

Requirements:
* Python 2.7
* OGR2OGR
* Mapnik
* Nik2Img.py

##TODO:
Make it more user friendly so that users don't have to edit multiple files to set parameters

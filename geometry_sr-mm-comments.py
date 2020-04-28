"""
Shadrock Comment - put good comment headers here. Add the necessary information, such as:
What inputs does this code take? What is the output (e.g. a new file, a value, etc)

Output: Total length of all river segments.
"""

import arcpy    #imports arcpy library
from arcpy import env
env.workspace = "C:\Users\MMasitha\Downloads\Lab4_working_with_geometries\Lab4_working_with_geometries\Data_Lab4_working_geometries"  #Sets up workspace environment
fc = "rivers.shp" #Specifies river shape file as the variable of interest
cursor = arcpy.da.SearchCursor(fc, ["SHAPE@LENGTH"])
length = 0


for row in cursor:          #Creates a "for" loop for details on river length
    length = length + row[0]                                             # Sums up lengths of the river
    units = arcpy.Describe(fc).spatialReference.linearUnitName          #Specifies the unit of length
    print str(length) + " " + units     #Displaying the total length of river segments in metres. This is a float data type for river polylines

#The output from this is 256937.409437 meters 

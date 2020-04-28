"""This script gives co-ordinates for each individual point data"""
import arcpy    #Imports arcpy library
from arcpy import env
env.workspace = "C:\Users\MMasitha\Downloads\Lab4_working_with_geometries\Lab4_working_with_geometries\Data_Lab4_working_geometries"   #Sets up workspace environment
fc = "dams.shp"         #Specifies dam shape file as the variable of interest
cursor = arcpy.da.SearchCursor(fc, ["SHAPE@XY"]) #"for" loop to reiterate through the rows to extract field values of interest.
length = 0
for row in cursor:
    x,y = row[0]
    print ("{0}, {1}".format(x,y))    #This displays the co-ordinates of point features of the dam polygons.

# Output here:
"""
852911.336075, 2220578.93538
792026.89767, 2310863.76822
784830.427658, 2315171.53882
741687.458878, 2321601.76549
702480.327773, 2340545.89511
623387.057118, 2361903.92116
623695.640648, 2366334.33243
605189.090984, 2369713.27767
607428.403551, 2371200.1893
598227.039352, 2377783.5839
605311.561749, 2377828.1123
600279.281455, 2381117.02117
600424.5035, 2385911.05609
448531.157196, 2422948.79249
448699.851908, 2423689.86222
444571.703829, 2424622.48102
449058.132475, 2425902.48822
445617.791672, 2428493.00554
438054.0539, 2429993.01392
458892.662963, 2435094.24857
429678.478408, 2443134.25808
462354.502917, 2445966.35229
461503.007988, 2447816.94401
"""

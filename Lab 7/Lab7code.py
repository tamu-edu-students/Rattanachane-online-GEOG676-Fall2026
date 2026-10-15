import arcpy

#assign bands
source = r"C:\Rattanachane-online-GEOG676-Fall2026\Rattanachane-online-GEOG676-Fall2026\Lab 7"
band1 = arcpy.sa.Raster(source + r"\B1.TIF") #blue
band2 = arcpy.sa.Raster(source + r"\B2.TIF") #green
band3 = arcpy.sa.Raster(source + r"\B3.TIF") #red
band4 = arcpy.sa.Raster(source + r"\B4.TIF") #NIR
combined = arcpy.CompositeBands_management([band1, band2, band3, band4], source + r"\output_combined.tif")

#HillShade
azimuth = 315
altitude = 45  
shadows = 'NO_SHADOWS'
z_factor = 1
arcpy.ddd.HillShade(source + r"\DEM.tif", source + r"\output_hillshade.tif", azimuth, altitude, shadows, z_factor)

#Slope
output_measurement = "DEGREE"
arcpy.ddd.Slope(source + r"\DEM.tif", source + r"\output_slope.tif", output_measurement, z_factor)
print("success!")
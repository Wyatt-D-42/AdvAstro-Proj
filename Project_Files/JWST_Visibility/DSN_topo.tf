\begintext

PCK kernel for the topocentric coordinate transform for the Deep Space
Network (DSN) stations.

This kernel must be loaded to perform to return state vectors in the
local topocentric frame.

The topocentric frame defines the z axis as the normal outward at the
station site, the x axis points at local north (geographic) with the
y axis completing the right handed frame.  Positive azimuth is measured
counter clockwise from the x axis.



Antenna position data obtained from

     http://dsnra.jpl.nasa.gov/Antennas.html

values taken from Geodetic coordinate table listed below.


             Geodetic coordinates of DSN antennas 
			    						in
				ITRF93 reference frame at epoch 1993.0

         latitude             longitude            height
         deg min sec         deg  min sec           (m)
Parkes  -32  59  54.25297    148  15  48.64683    0415.529
DSS 12   35  17  59.77577    243  11  40.24697    0962.875
DSS 13   35  14  49.79375    243  12  19.95732    1071.227
DSS 14   35  25  33.24518    243   6  37.66967    1002.114
DSS 15   35  25  18.67390    243   6  46.10495    0973.945
DSS 16   35  20  29.54391    243   7  34.86823    0944.711
DSS 17   35  20  31.83778    243   7  35.38803    0937.650
DSS 23   35  20  22.38335    243   7  37.70043    0946.086
DSS 24   35  20  23.61555    243   7  30.74842    0952.156
DSS 25   35  20  15.40450    243   7  28.69836    0960.862
DSS 26   35  20  08.48213    243   7  37.14557    0970.159
DSS 27   35  14  17.78052    243  13  24.06569    1053.203
DSS 28   35  14  17.78136    243  13  15.99911    1065.382
DSS 33  -35  24  01.76138    148  58  59.12204    0684.839
DSS 34  -35  23  54.53605    148  58  55.06377    0661.078
DSS 42  -35  24  02.44494    148  58  52.55396    0675.356
DSS 43  -35  24   8.74388    148  58  52.55394    0689.608
DSS 45  -35  23  54.46400    148  58  39.65992    0675.086
DSS 46  -35  24  18.05462    148  58  59.08571    0677.551
DSS 53   40  25  38.48040    355  45  01.24312    0827.487
DSS 54   40  25  27.75530    355  44  48.99946    0823.927
DSS 61   40  25  43.45508    355  45  03.51113    0841.159
DSS 63   40  25  52.34908    355  45   7.16030    0865.544
DSS 65   40  25  37.86055    355  44  54.88622    0834.539
DSS 66   40  25  47.98902    355  44  54.71175    0855.268

Parkes is assigned to DSS-05

The equatorial radius and flattening factor for the ITRF93
reference ellipsoid are

     radius      = 6378.1363
     flattening  = 1.0/298.257


The use of this kernel requires the use of a high precision
earth model kernel. 

Please note that all rotations mean the rotation of the coordinate
frames about an axis and not of the vectors.

The rotation defined in this file describes a rotation from
an initial frame defined as

x - along the line of zero longitude intersecting the equator
z - along the spin axis
y - completing the right hand coordinate frame

to the topocentric frame defined as

z - normal to the surface at the site
x - local north
y - local west

This is a 3-2-3 rotation with defined angles as the negative of the site
longitude, the negative of the site colatitude, 180 degrees.

Another useful rotation is from the initial frame to a topocentric 
frame defined as

x - normal to the surface at the site
z - local north
y - local east

This is also a 3-2-3 rotation with defined angles as the negative of the
site longitude, the positive site colatitude, 0 degrees.


Ed Wright Aug 7, 1997
ewright@spice.jpl.nasa.gov
1-818-354-0371



\begindata

   TKFRAME_EARTH_FIXED_RELATIVE = 'ITRF93'
   TKFRAME_EARTH_FIXED_SPEC     = 'MATRIX'
   TKFRAME_EARTH_FIXED_MATRIX   = ( 1   0   0
                                    0   1   0
                                    0   0   1 )



   FRAME_DSS-05_TOPO            =  1399005
   FRAME_1399005_NAME           = 'DSS-05_TOPO'
   FRAME_1399005_CLASS          =  4
   FRAME_1399005_CLASS_ID       =  1399005
   FRAME_1399005_CENTER         =   399005

   OBJECT_399005_FRAME          = 'DSS-05_TOPO'

   TKFRAME_DSS-05_TOPO_RELATIVE = 'EARTH_FIXED'
   TKFRAME_DSS-05_TOPO_SPEC     = 'ANGLES'
   TKFRAME_DSS-05_TOPO_UNITS    = 'DEGREES'
   TKFRAME_DSS-05_TOPO_AXES     = ( 3, 2, 3 )
   TKFRAME_DSS-05_TOPO_ANGLES   = ( -148.2635130083333,
                                    -122.9984036027778,
                                      180.0        )



   FRAME_DSS-12_TOPO            =  1399012
   FRAME_1399012_NAME           = 'DSS-12_TOPO'
   FRAME_1399012_CLASS          =  4
   FRAME_1399012_CLASS_ID       =  1399012
   FRAME_1399012_CENTER         =   399012

   OBJECT_399012_FRAME          = 'DSS-12_TOPO'

   TKFRAME_DSS-12_TOPO_RELATIVE = 'EARTH_FIXED'
   TKFRAME_DSS-12_TOPO_SPEC     = 'ANGLES'
   TKFRAME_DSS-12_TOPO_UNITS    = 'DEGREES'
   TKFRAME_DSS-12_TOPO_AXES     = ( 3, 2, 3 )
   TKFRAME_DSS-12_TOPO_ANGLES   = ( -243.1945130472222,
                                    -54.70006228611111,
                                      180.0        )



   FRAME_DSS-13_TOPO            =  1399013
   FRAME_1399013_NAME           = 'DSS-13_TOPO'
   FRAME_1399013_CLASS          =  4
   FRAME_1399013_CLASS_ID       =  1399013
   FRAME_1399013_CENTER         =   399013

   OBJECT_399013_FRAME          = 'DSS-13_TOPO'

   TKFRAME_DSS-13_TOPO_RELATIVE = 'EARTH_FIXED'
   TKFRAME_DSS-13_TOPO_SPEC     = 'ANGLES'
   TKFRAME_DSS-13_TOPO_UNITS    = 'DEGREES'
   TKFRAME_DSS-13_TOPO_AXES     = ( 3, 2, 3 )
   TKFRAME_DSS-13_TOPO_ANGLES   = ( -243.2055437000000,
                                    -54.75283506944445,
                                      180.0        )



   FRAME_DSS-14_TOPO            =  1399014
   FRAME_1399014_NAME           = 'DSS-14_TOPO'
   FRAME_1399014_CLASS          =  4
   FRAME_1399014_CLASS_ID       =  1399014
   FRAME_1399014_CENTER         =   399014

   OBJECT_399014_FRAME          = 'DSS-14_TOPO'

   TKFRAME_DSS-14_TOPO_RELATIVE = 'EARTH_FIXED'
   TKFRAME_DSS-14_TOPO_SPEC     = 'ANGLES'
   TKFRAME_DSS-14_TOPO_UNITS    = 'DEGREES'
   TKFRAME_DSS-14_TOPO_AXES     = ( 3, 2, 3 )
   TKFRAME_DSS-14_TOPO_ANGLES   = ( -243.1104637972222,
                                    -54.57409856111111,
                                      180.0        )



   FRAME_DSS-15_TOPO            =  1399015
   FRAME_1399015_NAME           = 'DSS-15_TOPO'
   FRAME_1399015_CLASS          =  4
   FRAME_1399015_CLASS_ID       =  1399015
   FRAME_1399015_CENTER         =   399015

   OBJECT_399015_FRAME          = 'DSS-15_TOPO'

   TKFRAME_DSS-15_TOPO_RELATIVE = 'EARTH_FIXED'
   TKFRAME_DSS-15_TOPO_SPEC     = 'ANGLES'
   TKFRAME_DSS-15_TOPO_UNITS    = 'DEGREES'
   TKFRAME_DSS-15_TOPO_AXES     = ( 3, 2, 3 )
   TKFRAME_DSS-15_TOPO_ANGLES   = ( -243.1128069305555,
                                    -54.57814613888889,
                                      180.0        )



   FRAME_DSS-16_TOPO            =  1399016
   FRAME_1399016_NAME           = 'DSS-16_TOPO'
   FRAME_1399016_CLASS          =  4
   FRAME_1399016_CLASS_ID       =  1399016
   FRAME_1399016_CENTER         =   399016

   OBJECT_399016_FRAME          = 'DSS-16_TOPO'

   TKFRAME_DSS-16_TOPO_RELATIVE = 'EARTH_FIXED'
   TKFRAME_DSS-16_TOPO_SPEC     = 'ANGLES'
   TKFRAME_DSS-16_TOPO_UNITS    = 'DEGREES'
   TKFRAME_DSS-16_TOPO_AXES     = ( 3, 2, 3 )
   TKFRAME_DSS-16_TOPO_ANGLES   = ( -243.1263522861111,
                                    -54.65846002499999,
                                     180.0             )



   FRAME_DSS-17_TOPO            =  1399017
   FRAME_1399017_NAME           = 'DSS-17_TOPO'
   FRAME_1399017_CLASS          =  4
   FRAME_1399017_CLASS_ID       =  1399017
   FRAME_1399017_CENTER         =   399017

   OBJECT_399017_FRAME          = 'DSS-17_TOPO'

   TKFRAME_DSS-17_TOPO_RELATIVE = 'EARTH_FIXED'
   TKFRAME_DSS-17_TOPO_SPEC     = 'ANGLES'
   TKFRAME_DSS-17_TOPO_UNITS    = 'DEGREES'
   TKFRAME_DSS-17_TOPO_AXES     = ( 3, 2, 3 )
   TKFRAME_DSS-17_TOPO_ANGLES   = ( -243.12649667500000,
                                     -54.65782283888888,
                                      180.0             )



   FRAME_DSS-23_TOPO            =  1399023
   FRAME_1399023_NAME           = 'DSS-23_TOPO'
   FRAME_1399023_CLASS          =  4
   FRAME_1399023_CLASS_ID       =  1399023
   FRAME_1399023_CENTER         =   399023

   OBJECT_399023_FRAME                = 'DSS-23_TOPO'

   TKFRAME_DSS-23_TOPO_RELATIVE = 'EARTH_FIXED'
   TKFRAME_DSS-23_TOPO_SPEC     = 'ANGLES'
   TKFRAME_DSS-23_TOPO_UNITS    = 'DEGREES'
   TKFRAME_DSS-23_TOPO_AXES     = ( 3, 2, 3 )
   TKFRAME_DSS-23_TOPO_ANGLES   = ( -243.1271390083333,
                                    -54.66044906944444,
                                     180.0        )



   FRAME_DSS-24_TOPO            =  1399024
   FRAME_1399024_NAME           = 'DSS-24_TOPO'
   FRAME_1399024_CLASS          =  4
   FRAME_1399024_CLASS_ID       =  1399024
   FRAME_1399024_CENTER         =   399024

   OBJECT_399024_FRAME          = 'DSS-24_TOPO'

   TKFRAME_DSS-24_TOPO_RELATIVE = 'EARTH_FIXED'
   TKFRAME_DSS-24_TOPO_SPEC     = 'ANGLES'
   TKFRAME_DSS-24_TOPO_UNITS    = 'DEGREES'
   TKFRAME_DSS-24_TOPO_AXES     = ( 3, 2, 3 )
   TKFRAME_DSS-24_TOPO_ANGLES   = ( -243.1252078944445,
                                    -54.66010679166667,
                                     180.0        )



   FRAME_DSS-25_TOPO            =  1399025
   FRAME_1399025_NAME           = 'DSS-25_TOPO'
   FRAME_1399025_CLASS          =  4
   FRAME_1399025_CLASS_ID       =  1399025
   FRAME_1399025_CENTER         =   399025

   OBJECT_399025_FRAME          = 'DSS-25_TOPO'

   TKFRAME_DSS-25_TOPO_RELATIVE = 'EARTH_FIXED'
   TKFRAME_DSS-25_TOPO_SPEC     = 'ANGLES'
   TKFRAME_DSS-25_TOPO_UNITS    = 'DEGREES'
   TKFRAME_DSS-25_TOPO_AXES     = ( 3, 2, 3 )
   TKFRAME_DSS-25_TOPO_ANGLES   = ( -243.1246384333333,
                                    -54.66238763888889,
                                     180.0        )



   FRAME_DSS-26_TOPO            =  1399026
   FRAME_1399026_NAME           = 'DSS-26_TOPO'
   FRAME_1399026_CLASS          =  4
   FRAME_1399026_CLASS_ID       =  1399026
   FRAME_1399026_CENTER         =   399026

   OBJECT_399026_FRAME          = 'DSS-26_TOPO'

   TKFRAME_DSS-26_TOPO_RELATIVE = 'EARTH_FIXED'
   TKFRAME_DSS-26_TOPO_SPEC     = 'ANGLES'
   TKFRAME_DSS-26_TOPO_UNITS    = 'DEGREES'
   TKFRAME_DSS-26_TOPO_AXES     = ( 3, 2, 3 )
   TKFRAME_DSS-26_TOPO_ANGLES   = ( -243.1269848805556,
                                    -54.66431051944444,
                                     180.0        )



   FRAME_DSS-27_TOPO            =  1399027
   FRAME_1399027_NAME           = 'DSS-27_TOPO'
   FRAME_1399027_CLASS          =  4
   FRAME_1399027_CLASS_ID       =  1399027
   FRAME_1399027_CENTER         =   399027

   OBJECT_399027_FRAME          = 'DSS-27_TOPO'

   TKFRAME_DSS-27_TOPO_RELATIVE = 'EARTH_FIXED'
   TKFRAME_DSS-27_TOPO_SPEC     = 'ANGLES'
   TKFRAME_DSS-27_TOPO_UNITS    = 'DEGREES'
   TKFRAME_DSS-27_TOPO_AXES     = ( 3, 2, 3 )
   TKFRAME_DSS-27_TOPO_ANGLES   = ( -243.2233515805556,
                                    -54.76172763333333,
                                     180.0             )



   FRAME_DSS-28_TOPO            =  1399028
   FRAME_1399028_NAME           = 'DSS-28_TOPO'
   FRAME_1399028_CLASS          =  4
   FRAME_1399028_CLASS_ID       =  1399028
   FRAME_1399028_CENTER         =   399028

   OBJECT_399028_FRAME          = 'DSS-28_TOPO'

   TKFRAME_DSS-28_TOPO_RELATIVE = 'EARTH_FIXED'
   TKFRAME_DSS-28_TOPO_SPEC     = 'ANGLES'
   TKFRAME_DSS-28_TOPO_UNITS    = 'DEGREES'
   TKFRAME_DSS-28_TOPO_AXES     = ( 3, 2, 3 )
   TKFRAME_DSS-28_TOPO_ANGLES   = ( -243.2211108638889,
                                    -54.76172740000000,
                                     180.0             )



   FRAME_DSS-33_TOPO            =  1399033
   FRAME_1399033_NAME           = 'DSS-33_TOPO'
   FRAME_1399033_CLASS          =  4
   FRAME_1399033_CLASS_ID       =  1399033
   FRAME_1399033_CENTER         =   399033

   OBJECT_399033_FRAME          = 'DSS-33_TOPO'

   TKFRAME_DSS-33_TOPO_RELATIVE = 'EARTH_FIXED'
   TKFRAME_DSS-33_TOPO_SPEC     = 'ANGLES'
   TKFRAME_DSS-33_TOPO_UNITS    = 'DEGREES'
   TKFRAME_DSS-33_TOPO_AXES     = ( 3, 2, 3 )
   TKFRAME_DSS-33_TOPO_ANGLES   = ( -148.9830894555556,
                                    -125.4004892722222,
                                     180.0             )



   FRAME_DSS-34_TOPO            =  1399034
   FRAME_1399034_NAME           = 'DSS-34_TOPO'
   FRAME_1399034_CLASS          =  4
   FRAME_1399034_CLASS_ID       =  1399034
   FRAME_1399034_CENTER         =   399034

   OBJECT_399034_FRAME          = 'DSS-34_TOPO'

   TKFRAME_DSS-34_TOPO_RELATIVE = 'EARTH_FIXED'
   TKFRAME_DSS-34_TOPO_SPEC     = 'ANGLES'
   TKFRAME_DSS-34_TOPO_UNITS    = 'DEGREES'
   TKFRAME_DSS-34_TOPO_AXES     = ( 3, 2, 3 )
   TKFRAME_DSS-34_TOPO_ANGLES   = ( -148.9819621583333,
                                    -125.3984822361111,
                                      180.0        )



   FRAME_DSS-42_TOPO            =  1399042
   FRAME_1399042_NAME           = 'DSS-42_TOPO'
   FRAME_1399042_CLASS          =  4
   FRAME_1399042_CLASS_ID       =  1399042
   FRAME_1399042_CENTER         =   399042

   OBJECT_399042_FRAME          = 'DSS-42_TOPO'

   TKFRAME_DSS-42_TOPO_RELATIVE = 'EARTH_FIXED'
   TKFRAME_DSS-42_TOPO_SPEC     = 'ANGLES'
   TKFRAME_DSS-42_TOPO_UNITS    = 'DEGREES'
   TKFRAME_DSS-42_TOPO_AXES     = ( 3, 2, 3 )
   TKFRAME_DSS-42_TOPO_ANGLES   = ( -148.9812649888889,
                                    -125.4006791500000,
                                      180.0        )



   FRAME_DSS-43_TOPO            =  1399043
   FRAME_1399043_NAME           = 'DSS-43_TOPO'
   FRAME_1399043_CLASS          =  4
   FRAME_1399043_CLASS_ID       =  1399043
   FRAME_1399043_CENTER         =   399043

   OBJECT_399043_FRAME          = 'DSS-43_TOPO'

   TKFRAME_DSS-43_TOPO_RELATIVE = 'EARTH_FIXED'
   TKFRAME_DSS-43_TOPO_SPEC     = 'ANGLES'
   TKFRAME_DSS-43_TOPO_UNITS    = 'DEGREES'
   TKFRAME_DSS-43_TOPO_AXES     = ( 3, 2, 3 )
   TKFRAME_DSS-43_TOPO_ANGLES   = ( -148.9812649833334,
                                    -125.4024288555555,
                                      180.0        )



   FRAME_DSS-45_TOPO            =  1399045
   FRAME_1399045_NAME           = 'DSS-45_TOPO'
   FRAME_1399045_CLASS          =  4
   FRAME_1399045_CLASS_ID       =  1399045
   FRAME_1399045_CENTER         =   399045

   OBJECT_399045_FRAME          = 'DSS-45_TOPO'

   TKFRAME_DSS-45_TOPO_RELATIVE = 'EARTH_FIXED'
   TKFRAME_DSS-45_TOPO_SPEC     = 'ANGLES'
   TKFRAME_DSS-45_TOPO_UNITS    = 'DEGREES'
   TKFRAME_DSS-45_TOPO_AXES     = ( 3, 2, 3 )
   TKFRAME_DSS-45_TOPO_ANGLES   = ( -148.9776833111111,
                                    -125.3984622222222,
                                      180.0        )



   FRAME_DSS-46_TOPO            =  1399046
   FRAME_1399046_NAME           = 'DSS-46_TOPO'
   FRAME_1399046_CLASS          =  4
   FRAME_1399046_CLASS_ID       =  1399046
   FRAME_1399046_CENTER         =   399046

   OBJECT_399046_FRAME          = 'DSS-46_TOPO'

   TKFRAME_DSS-46_TOPO_RELATIVE = 'EARTH_FIXED'
   TKFRAME_DSS-46_TOPO_SPEC     = 'ANGLES'
   TKFRAME_DSS-46_TOPO_UNITS    = 'DEGREES'
   TKFRAME_DSS-46_TOPO_AXES     = ( 3, 2, 3 )
   TKFRAME_DSS-46_TOPO_ANGLES   = ( -148.9830793638889,
                                    -125.4050151722222,
                                      180.0        )



   FRAME_DSS-53_TOPO            =  1399053
   FRAME_1399053_NAME           = 'DSS-53_TOPO'
   FRAME_1399053_CLASS          =  4
   FRAME_1399053_CLASS_ID       =  1399053
   FRAME_1399053_CENTER         =   399053

   OBJECT_399053_FRAME          = 'DSS-53_TOPO'

   TKFRAME_DSS-53_TOPO_RELATIVE = 'EARTH_FIXED'
   TKFRAME_DSS-53_TOPO_SPEC     = 'ANGLES'
   TKFRAME_DSS-53_TOPO_UNITS    = 'DEGREES'
   TKFRAME_DSS-53_TOPO_AXES     = ( 3, 2, 3 )
   TKFRAME_DSS-53_TOPO_ANGLES   = ( -355.7503453111111,
                                    -49.57264433333334,
                                      180.0        )



   FRAME_DSS-54_TOPO            =  1399054
   FRAME_1399054_NAME           = 'DSS-54_TOPO'
   FRAME_1399054_CLASS          =  4
   FRAME_1399054_CLASS_ID       =  1399054
   FRAME_1399054_CENTER         =   399054

   OBJECT_399054_FRAME          = 'DSS-54_TOPO'

   TKFRAME_DSS-54_TOPO_RELATIVE = 'EARTH_FIXED'
   TKFRAME_DSS-54_TOPO_SPEC     = 'ANGLES'
   TKFRAME_DSS-54_TOPO_UNITS    = 'DEGREES'
   TKFRAME_DSS-54_TOPO_AXES     = ( 3, 2, 3 )
   TKFRAME_DSS-54_TOPO_ANGLES   = ( -355.7469442944445,
                                    -49.57562352777778,
                                     180.0             )



   FRAME_DSS-61_TOPO            =  1399061
   FRAME_1399061_NAME           = 'DSS-61_TOPO'
   FRAME_1399061_CLASS          =  4
   FRAME_1399061_CLASS_ID       =  1399061
   FRAME_1399061_CENTER         =   399061

   OBJECT_399061_FRAME          = 'DSS-61_TOPO'

   TKFRAME_DSS-61_TOPO_RELATIVE = 'EARTH_FIXED'
   TKFRAME_DSS-61_TOPO_SPEC     = 'ANGLES'
   TKFRAME_DSS-61_TOPO_UNITS    = 'DEGREES'
   TKFRAME_DSS-61_TOPO_AXES     = ( 3, 2, 3 )
   TKFRAME_DSS-61_TOPO_ANGLES   = ( -355.7509753138889,
                                    -49.57126247777778,
                                     180.0             )



   FRAME_DSS-63_TOPO            =  1399063
   FRAME_1399063_NAME           = 'DSS-63_TOPO'
   FRAME_1399063_CLASS          =  4
   FRAME_1399063_CLASS_ID       =  1399063
   FRAME_1399063_CENTER         =   399063

   OBJECT_399063_FRAME          = 'DSS-63_TOPO'

   TKFRAME_DSS-63_TOPO_RELATIVE = 'EARTH_FIXED'
   TKFRAME_DSS-63_TOPO_SPEC     = 'ANGLES'
   TKFRAME_DSS-63_TOPO_UNITS    = 'DEGREES'
   TKFRAME_DSS-63_TOPO_AXES     = ( 3, 2, 3 )
   TKFRAME_DSS-63_TOPO_ANGLES   = ( -355.751988972222,
                                    -49.5687919222222,
                                     180.0            )



   FRAME_DSS-65_TOPO            =  1399065
   FRAME_1399065_NAME           = 'DSS-65_TOPO'
   FRAME_1399065_CLASS          =  4
   FRAME_1399065_CLASS_ID       =  1399065
   FRAME_1399065_CENTER         =   399065

   OBJECT_399065_FRAME          = 'DSS-65_TOPO'

   TKFRAME_DSS-65_TOPO_RELATIVE = 'EARTH_FIXED'
   TKFRAME_DSS-65_TOPO_SPEC     = 'ANGLES'
   TKFRAME_DSS-65_TOPO_UNITS    = 'DEGREES'
   TKFRAME_DSS-65_TOPO_AXES     = ( 3, 2, 3 )
   TKFRAME_DSS-65_TOPO_ANGLES   = ( -355.7485795055556,
                                    -49.57281651388889,
                                     180.0             )



   FRAME_DSS-66_TOPO            =  1399066
   FRAME_1399066_NAME           = 'DSS-66_TOPO'
   FRAME_1399066_CLASS          =  4
   FRAME_1399066_CLASS_ID       =  1399066
   FRAME_1399066_CENTER         =   399066

   OBJECT_399066_FRAME          = 'DSS-66_TOPO'

   TKFRAME_DSS-66_TOPO_RELATIVE = 'EARTH_FIXED'
   TKFRAME_DSS-66_TOPO_SPEC     = 'ANGLES'
   TKFRAME_DSS-66_TOPO_UNITS    = 'DEGREES'
   TKFRAME_DSS-66_TOPO_AXES     = ( 3, 2, 3 )
   TKFRAME_DSS-66_TOPO_ANGLES   = ( -355.7485310416667,
                                    -49.57000305000000,
                                      180.0            )


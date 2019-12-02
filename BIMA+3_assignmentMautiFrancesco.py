#AssignmentBIMA+3(1.0)

# PointNumbers

n = int(input("enter number of points"))

# Coordinates. 
# The last point (n + 1) equals the first point 
x  =  [ ] 
y  =  [ ]

for  i  in  range ( n ): 
    line = input(f"pont {i+1} (eg. x y)")
    words = line.split()

   
    x.append (float(words[0]))
    y.append (float(words[1]))

    
x.append(x[0])
y.append(y[0])
#Area formula 
Ax  =  0.0 
for  i  in  range ( n ): 
    Ax  =  Ax  +  ( x [ i + 1 ]  +  x [ i ])  *  ( y [ i + 1 ]  -  y [ i ])

Ax  =  0.5  *  Ax

# Print
print ("Ax ", Ax) 


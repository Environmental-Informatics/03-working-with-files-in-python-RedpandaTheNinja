# Author : Kevin Lee
# assignment 3
# Target file : 2008Male00006.txt
# /Users/taesuplee/onepur/class/ABE651/hw/assignment-03

# open file as directed from the book
fin = open( "2008Male00006.txt" , "r" )
header = fin.readline().split( "," )


fileline = fin.readlines()
status = fileline[-1]
fileline = fileline[:-1]
fin.close()

# create data list
data = [ 0 ] * (len( fileline ))
#yes
line: int
for line in range( len( fileline[ 1:15 ] ) ):
    data[ line ] = fileline[ line ].split( "," )
    data[ line ][ 0 ] = int( data[ line ][ 0 ] )
    data[ line ][ 3 ] = int( data[ line ][ 3 ] )
    data[ line ][ 4:6 ] = map( float , data[ line ][ 4:6 ] )
    data[ line ][ 8:15 ] = map( float , data[ line ][ 8:15 ] )
# print(data)
# creating dictionary empty
dic_fin = dict()

data.pop( -1 )
dic_fin = {header[ i ]: [ row[ i ] for row in data ] for i in range( len( header ) )}
import math
import numpy as np


def mean(g):
    mean = np.sum( g ) / len( g )
    return mean


def sum(h):
    sum = np.cumsum( h )
    return ( sum )


def distance(X , Y):
    dist = [0]
    for i in range( len( X ) - 1 ):
        dist.append( np.sqrt( (X[ i ] - X[ i+1 ]) ** 2 + (Y[ i ] - Y[ i+1 ]) ** 2 ) )

    dist = sum(dist)
    return dist

info = fileline[-1].strip().split(",")
dic_fin.update( {'Distance': distance( dic_fin[ ' X' ] , dic_fin[ ' Y' ] )} )
coon_dis = dic_fin['Distance'][-1]
mean_energy=mean( dic_fin[ 'Energy Level' ] )
mean_x =mean( dic_fin[ ' X' ])
mean_y = mean( dic_fin[ ' Y' ] )
fout = open('Georges_life.txt', 'w')
print(dic_fin)
fout.write ('Raccoon name: George \n' )             # Writing header
fout.write ('Average location: X %f, Y %f \n' %(mean_x , mean_y))
fout.write ('Distance traveled: %.2f \n' %coon_dis)
fout.write ('Average energy level: %.2f  \n' %mean_energy)
fout.write ('Raccoon end state: %s \n\n' %status)


# Writing select content
header = ['Date', 'X', 'Y', 'Asleep Flag', 'Behavior Mode', 'Distance Traveled']
fout.write ('%s \t %s \t %s \t %s \t %s \t %s \n'%(header[0], header[1], header[2], header[3], header[4], header[5]))

for i in range(len(dic_fin['Year'])):
    fout.write ('%s \t %f \t %f \t %s \t %s \t %.2f \n'%(dic_fin['Day'][i],dic_fin[' X'][i],dic_fin[' Y'][i],dic_fin[' Asleep'][i],dic_fin['Behavior Mode'][i],dic_fin['Distance'][i]))

fout.close()
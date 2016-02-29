from __future__ import division
from numpy import *

def calculateProbability(x, mean, stdev):
	exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
	return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent

def ClassProbabilities(x,M)
	P = []
	for i in arange(0,6):
		P.append(calculateProbability(x,M[i,0],M[i,1]))
	P = P/sum(P)
	return (P)	
	
def EulerVer3(I):
	E = 0
	# Calculation of Euler characteristic by definition
	for i in arange(1,img.size[1]):
		for j in arange(1,img.size[0]):
			V = I[i,j] or I[i,j-1] or I[i-1,j-1] or I[i-1,j]
			R1 = I[i,j] or I[i,j-1]
			R2 = I[i,j] or I[i-1,j]
			E += V + (-1)*R1 + (-1)*R2
	E += sum(I)			
	return E
	
M = zeros((6,2))

M[0,0] = 
M[0,1] =

M[1,0] = -6282.79487179
M[1,1] = 728.876943625

M[2,0] = 
M[2,1] =

M[3,0] = 
M[3,1] =

M[4,0] = 
M[4,1] =

M[5,0] = 
M[5,1] =

#load image
img = Image.open('D:\\Pattern recognition\\Small texture\\cushion1\\BW\\image{0:03d}.png'.format(i))
rgb = array(img)
I = rgb[:,:]]

#Calculate Euler characteristics
x = EulerVer3(I)

#Classify
P = ClassProbabilities(x,M)

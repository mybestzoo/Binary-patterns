from __future__ import division
from numpy import *
from PIL import Image, ImageDraw

def calculateProbability(x, mean, stdev):
	exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
	return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent

def ClassProbabilities(x,M):
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

M[0,0] = -5228.28205128
M[0,1] = 426.361285869

M[1,0] = -6282.79487179
M[1,1] = 728.876943625

M[2,0] = -9883.66666667
M[2,1] = 1078.52594879

M[3,0] = -10230.1794872
M[3,1] = 844.530513538

M[4,0] = -3593.84615385
M[4,1] = 423.303524397

M[5,0] = -10442.8974359
M[5,1] = 829.914632461

#load image
img = Image.open('D:\\Pattern recognition\\Small texture\\canvas1\\BW\\image001.png')
rgb = array(img)
I = rgb[:,:]

#Calculate Euler characteristics
x = EulerVer3(I)

#Classify
P = ClassProbabilities(x,M)

print P, max(P)

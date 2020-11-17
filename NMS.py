'''
Input: A list of Proposal boxes B (Location of points like - [[x1,y1,S1], [x2,y2,S2], [x3,y3,S3]]) where S is corresponding
confidence scores, N is overlap threshold, and h = length of Box in horizontal direction(x-direction), v = lenth of box
in vertical direction(y-direction). 
Output: A list of filtered proposals D.
'''
def NMS(B, N, h, v):
	def fun(x):
		return x[2]

	B1 = sorted(B, key = fun, reverse=True)
	D = list()
	
	i = 0
	k1 = len(B1)

	while i<k1:
		a = B1[0]
		D.append(a)
		B1.remove(B1[0])
		k1 -= 1
		j = 0
		print('D = ',D)
#		print('i = ',i)
		while j < k1:
#			print('B1=',B1)
			if abs(D[-1][0] - B1[j][0]) < h and abs(D[-1][1] - B1[j][1]) < v:

				print('i,j = ',i,j)
				print('D = ',D)
				print('B1 = ',B1)
				I = abs((h - abs(D[-1][0]-B1[j][0]))*(v - abs(B1[j][1] - D[-1][1])))
				U = 2*h*v - I
				IoU = I/U
				print('IoU = ',IoU)
				if IoU >= N:
					B1.remove(B1[j])
					k1 -= 1
#					print('k1 = ',k1)
				else:
					j += 1
			else:
				j+=1
	return D

#B = [[0,0,0.5], [1,1,0.8], [10,10,0.3],[5,5,0.2]]
#print(NMS(B,0.1,2,2))


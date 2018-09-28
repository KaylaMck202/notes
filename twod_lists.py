#a = [[1,2,3],
#     [4,5,6],
#     [7,8,9]]
#
#b= a[0]
#
#a[0][1] =7
#
#b[2] = 9
#print(a)

a = [[1,2,3],
     [4,5,6]]


#def print_rdlist(lst):
#    for i in range(len(a)):
#        for j in range(len(a[i])):
#            print(a[i][j],end=' ')
#        print()
##print(len(a))

#for i in range(len(a)):
#    for j in range(len(a[i])):
#        print(a[i][j],end=' ')
#    print()

### Another way to traverse
#for row in a:
#    for element in row:
#        print(element, end=' ')
#    print()

### Add all elements in 2d list
#sum= 0
#for i in range(len(a)):
#    for j in range(len(a[i])):
#        sum += a[i][j]
#print(sum)

###second way to add
#sum=0
#for row in a:
#    for element in row:
#        sum += element
#print(sum)

#for i in range(len(a)):
#    for j in range(len(a[i])):
#        a[i][j] += 1
        
#print_2dlist(a)

##creating 2d list
#x= [[0] *5]*8 DOES NOT WORK!!!
#x[0][0]=100

##to make an m x n list
#m= 5
#n=8
#x= [[0]*n for i in range(m)]
##x[0][0]=100
#print(x)

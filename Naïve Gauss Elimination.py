#input


n = int(input("Enter number for n*n matrix: "))
a=[[] for i in range(n)]
b=[]
x=[]

for i in range(n):
    a[i] = [float(x) for x in input("Enter "+str(n)+" value: ").split()] 
    b.append(float(input("Enter C value col"+str(i+1)+" : ")))
    x.append('x'+str(i+1))
#Show mattrix

def mertixnow(a,b,x):
    print()
    for i in range(n):
        A=a[i]
        B=b[i]
        X=x[i]
        
        for ad in A:
            print("%.3f"%ad,end = " ")

         
        if(not(isinstance(X, str))):
            print(" ","%.3f"%float(X)," ","%.3f"%float(B))
        else:
            print(" ",X," ","%.3f"%float(B))
    print()
    
mertixnow(a,b,x)


#Forward Elimation
print("Forward Elimation")

for k in range(0,n-1):
    for i in range(k+1,n):
        print("********************************************ROW************************************")
        print(a[i][k],"/",a[k][k])
        factor = a[i][k]/a[k][k]
        print("Factor:",factor)
        print()
        
        for j in range(k,n):
          print(a[i][j]," - ",factor," * ",a[k][j],end=" = ") 
          a[i][j] = a[i][j]-(factor*a[k][j])
          print(a[i][j])
        b[i] = b[i]-( factor*b[k] )
       
        mertixnow(a,b,x)


x[n-1]=b[n-1]/a[n-1][n-1]
print()
#back Elimation
print("back Elimation")
for i in range(n-1,-1,-1):
    print("********************************************ROW************************************")
    Sum=0.0
    for j in range(i+1,n):
        Sum = Sum + a[i][j]*x[j]
    x[i]=(b[i]-Sum)/a[i][i]
    
    mertixnow(a,b,x)
print("Ans")
for i in range(len(x)):
    print("x"+str(i+1),"= %.3f"%x[i])

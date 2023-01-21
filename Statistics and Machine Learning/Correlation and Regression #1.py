# https://www.hackerrank.com/challenges/correlation-and-regression-lines-6/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT

n=10
x=[]
y=[]
x=[15, 12, 8, 8, 7, 7, 7, 6, 5, 3]
y=[10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
#print(x)
#print(y)

def mean(a):
    mean=sum(a)/n
    return mean
#print(mean(x))

def sigma(a):
    sods=0
    for i in range(n):
        sods=sods+(float(a[i]-mean(a))**2)
    sd=(sods/n)**(1/2)
    return sd
#print(sigma(x))

def pearson(a, b):
       
    cov=0
    for i in range(n):
        cov=cov + (a[i]-mean(a))*(b[i]-mean(b))*1/n
    #print(cov)
    
    pearson_coef=cov/(sigma(a)*sigma(b))
    return pearson_coef

print(round(pearson(x,y),3))

beta= pearson(x,y)*sigma(y)/sigma(x)
#print(round(beta,3))

epsilon=mean(y)-beta*mean(x)
#print(epsilon)

def predict(b,e,x):
    y_hat=e+b*x
    print(format(y_hat,".1f"))

#predict(beta, epsilon, 10)

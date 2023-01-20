#https://www.hackerrank.com/challenges/predicting-house-prices/problem?isFullScreen=true

# Enter your code here. Read input from STDIN. Print output to STDOUT
from sklearn import linear_model

m,n=map(int,input().split())
#print(m)
#print(n)

x_arr = []
y_arr = []
for i in range(n):
    x_n_y = input().split()      
    x_arr.append([float(x_n_y[j]) for j in range(m)])
    y_arr.append(float(x_n_y[-1]))
#print(x_arr)
#print(y_arr)

lm = linear_model.LinearRegression()
lm.fit(x_arr, y_arr)
epsilon = lm.intercept_
beta = lm.coef_
#print(epsilon)
#print(beta)

def predict(b, e, pred):
    for i in range(len(pred)):
        y_hat=e
        for j in range(m):
            y_hat=y_hat+b[j]*pred[i][j]
        print(format(y_hat, '.2f'))
    #print(len(pred))
    

q=int(input())
q_arr = []
for i in range(q):
    q_n_y = input().split()      
    q_arr.append([float(q_n_y[j]) for j in range(m)])
#print(q_arr)

predict(beta, epsilon, q_arr)


#Importing the modules require for the contour plots
from numpy import *
from matplotlib import pyplot
#I have used raw_input to customise the output and i have discovered when varying between entering known and unknown gradient
#that the unknown gradient outputs a value error so i have used try and except to read the data if it is known or unknown
#If a error occurs,the try and except will identify it and use the appropriate code. The rest is just reading the data
# and converting to the appropriate format

filename=raw_input("What is the name of the file we are trying to read?  ")
#filename="quadratic.opt"

try:
    infile = open(filename,"r")
    N= int(infile.readline())
    function = infile.readline()
    gradient = infile.readline()
    gradient0 , gradient1 = gradient.split(" ")
    initialx= infile.readline().split(" ")
    ix0=float(initialx[0]) ; ix1=float(initialx[1])
    Tol= float(infile.readline())
    kmax = int(infile.readline())
    infile.close()
    x=[ix0,ix1]
    
except ValueError:
    infile = open(filename,"r")
    N= int(infile.readline())
    function = infile.readline()
    gradient = infile.readline().strip()
    initialx= infile.readline().split(" ")
    ix0=float(initialx[0]) ; ix1=float(initialx[1])
    Tol= float(infile.readline())
    kmax = int(infile.readline())
    infile.close()
    x=[ix0,ix1]

#Here we define our function f(x) using the eval command as it reads the text
def f(x):
    return  eval(function)
#We take the specific case if the gradient is unknown use the finite differences methods to calculate the partial derivatives at x0 and x1
#Because we used a list for the x values, we have to extract each element in the list and make a new list for the new things as f
#requires the input to be in a list of len 2
if gradient == "unknown":
    def pdx0(x):
        epi=[10**-6,0]
        xplusepi=[]
        xminusepi=[]
        for i in range(len(x)):
            xplusepi.append(x[i]+epi[i])
            xminusepi.append(x[i]-epi[i])
        return  (f(xplusepi)-f(xminusepi))/(2*epi[0])
    def pdx1(x):
        epi=[0,10**-6]
        xplusepi=[]
        xminusepi=[]
        for i in range(len(x)):
            xplusepi.append(x[i]+epi[i])
            xminusepi.append(x[i]-epi[i])
        return  (f(xplusepi)-f(xminusepi))/(2*epi[1])
#If the gradient isnt unknown and is known by default, then we simply use the gradient provided from the text file
else:
    def pdx0(x):
        return eval(gradient0)
    def pdx1(x):
        return eval(gradient1)

# k is the number of iterations and it is 0 when no programme has been run
k=0
#gk is the directional derivative as shown by the task
gk= [pdx0(x),pdx1(x)]
modgk = (pdx0(x)**2 + pdx1(x)**2)**0.5
#Finding s:  F(s) is a function that maps the output of the new x values and uses it to find a small value to find a new value of s
#The method we have used to solve s was given to us in the task. We define F(s) for the output and use the
def F(s):
    sgk=[]
    l=[]
    for i in range(len(x)):
        sgk.append(s*gk[i])
    for i in range(len(x)):
        l.append(x[i]-sgk[i])
    return f(l)
#e is a small arbirtary number. Any number can be used here.
e=0.1
def find_s(e):
    n=2
    while F(n*e)<F((n-1)*e):
        n+=1
    return (n-1)*e
#Here we are creating the list the X values are stored in and we enter the first value for x
xvalues=[]
xvalues.append(x)
#This is the main algorithm here. Because i used a list, i need to extract then multiply every member of the list for each calculation
#I then update the value of x and update the gk and mod gk as a result and repeat the algortihm
#sgk and l are just 2 blank lists i used to temporally use the values. The x values are stored in xvalues using the list append commands
while (k<kmax and modgk>Tol):
    s=find_s(e)
    sgk=[]
    l=[]
    for i in range(len(x)):
        sgk.append(s*gk[i])
    for i in range(len(x)):
        l.append(x[i]-sgk[i])
    k+=1
    x=l
    gk= [pdx0(x),pdx1(x)]
    modgk = (pdx0(x)**2 + pdx1(x)**2)**0.5
    xvalues.append(x)

#The final results using the algorithm and are presented nicely using print specifications
print("The minima is at (%f,%f)  with the number of iterations being %d") %(x[0],x[1],k)
if modgk < Tol:
    print ("The tolerance has been met and the final value for |gk| is %f ") %modgk
if k>kmax:
    print ("The algortihm has failed as the maximum number of iterations has been reached")
print("Next time, please consider using https://www.wolframalpha.com/ for a better solution.")

# This is the section for the countour plots, length is just the 2|xfinal-xinitia| and the linspace just produces a linearly spaced vector
# of the values so we can produce a plot for the values
length=((x[0]-ix0)**2 + (x[1]-ix1)**2)**0.5
xlist = linspace(x[0]-length, x[0]+length, 100)
ylist = linspace(x[1]-length, x[1]+length, 100)
X, Y = meshgrid(xlist, ylist)
Z = f([X,Y])

#Seting up the graph with the title and labeling the axes and it plots the lines

pyplot.figure()
cp = pyplot.contour(X, Y, Z)
pyplot.clabel(cp, inline=True, fontsize=10)
pyplot.title('Contour Plot')
pyplot.xlabel('x')
pyplot.ylabel('y')
pyplot.show()

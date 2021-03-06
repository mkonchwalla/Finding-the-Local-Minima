# Finding-the-Local-Minima

This project is a project for the UCL Mathematics Methods 2 Module 
Please see the PDF file




Project 3: Finding minima of a nonlinear function 1 The problem
In many applications both in applied sciences and in industry an important
problem is that of finding local or global maxima or minima of nonlinear
functions of several variables. The problem of finding a local minimum may
N ! N
bewritten:givenf:R 7!Rfindx2R suchthat,forsome✏0>0,
! ! ! ! N !  f(x)f(x + y), forall y 2R suchthat|y|✏0.
Such a point is known as a critical point as we have seen in the course. Provided f(·) is smooth enough, it is characterised by the fact that the
!  !  !  ! 
gradient of f vanishes at x , r f ( x ) = 0 and that the Hessian evaluated
at this point is positive defininite.
The algorithm that we will use to find approximate local minim=a is
known as the steepest descent algorithm and is an iterative procedure that
!  N
starts from some initial guess x 0 2 R and then creates a sequence of
! 
updates, x k created by “moving” in the direction in which f decreases ! 
the most, the direction of “steepest descent”. Given x 0, a tolerance TOL and some upper limit on the number of iterations, maxit we can write the algorithm for minimisation, at iteration k, as follows
!  !  ! 
1. Compute gk =rf(xk).
! 
2. If | g k| <TOL or k >maxit: return xk, |gk| and k and claim success if
! 
| g k | <TOL and failure if k >maxit.
 ! ! 
3. Consider the one dimensional function f (s) = f (xk   s g k ).
 ̃ ̃
4. Pick an sk > 0 such that f(sk) < f(0). Since we know that the
! 
gradient points in the direction of largest increase of f , we see that  !  ! ! 
f(xk) > f(xk   s g k) for some s > 0, small enough.
5. Update the point:
!  !  !  x k+1 = x k   sk g k
6. Increase the iteration counter, k, by one, k+=1, and repeat from point 1.
Observe that the choice of sk is not specified above and left to your imag- ination. The procedure of finding the minimum of this one dimensional
1
 ̃
minimisation problem is known as a“line search”. A naive (and expensive) waytofindanacceptablesk istofixasmallvalueof✏>0,setn=1and then loop (if we identify f ̃ with F ).
while (F(n*epsilon) <F((n-1)*epsilon)):
  n+=1
s_k = (n-1)*epsilon
2 The project
The aim of the project is to write a program that uses the above presented algorithm to find the minimum of a given function.
2.1
1. 2.
3.
4.
2.2
Program structure
Open a file filename.opt for reading. ReadthedataN,astringcontainingthefunctionf,astringgradient
that contains either the N components of the gradient of f or the string
!  N
’unknown’. Then read the initial guess x 0 2 R , the parameters TOL
and finally maxit.
An example of the file (quadratic.opt) reads:
2
x[0]**2-1.5*x[0]*x[1]+x[1]**2 - x[0]-x[1]
2*x[0]-1.5*x[1]-1 2*x[1]-1.5*x[0]-1
-2.0 3.0
0.001
2000
Then use the above algorithm to find a (local) minimum of the function
f, starting from the initial guess x 0. Computation and output
The program should execute the algorithm taking into account the di↵erent data given in the following way
• If gradient != ’unknown’
then execute the above algoritm using the provided gradient. Store all the intermediate points xk in a list.
2
! 

3
!  ! ⇤
2| x 0   x |. Choose the parameters for the plot command so that it
!  ⇤ is easy to see that there is a local minimum in x .
What to submit for the assessment
•
• •
If gradient == ’unknown’
execute the above algoritm, but this time approximate the components of the gradient using finite di↵erences:
!  !  !  !  @f (x) ⇡ f( x + ✏ )   f( x   ✏ )
@xi 2✏
where ✏ isavectorwithelements✏k =0.fork6=iand✏i =1.e 6.
Store all the intermediate points xk in a list.
Return whether or not the tolerance has been met and how many iterations that have been used. Also return the size of the gradient for the last iteration.
  ! 
If N = 2, produce contourplots of the function f in a square, centered !  ⇤ !  ⇤
in x , where x is the approximate local minimum, and with side
You should submit the following items in a zipped folder:
• A .pdf document with details on the members of the group, names and student numbers. Here you may also give some information on the project, such as if you have implemented some particular line search algorithm or some of the extensions below have been considered.
• A well commented code that produces the expected output as outlined in the discussion above.
• The output of the program run using the following three input files (available on the moodle page):
– quadratic.opt
– quartic.opt
– quartic_unknow.opt
• Include both text and graphical output (graphics can be saved using the buttons on the bottom of the Figure window).

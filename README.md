# Regpack: A lightweight linear regression library. 
by Jamie McElhiney. 



## Features

### Matrix Multiplication

#### Divide and Conquer

Alternative matrix multipliation where we can derive our Strassen Algorithm from. 

#### Strassen

<img src="https://upload.wikimedia.org/wikipedia/commons/2/2e/Strassen_algorithm.svg" height=100>

Efficient matrix multiplication.

#### Textbook Matrix Multiplication


<img src="/images/mmt.png"
     alt="Markdown Monster icon"
     height=200 >

### Matrix Inversion


<img src="/images/gauss.png"
     height=200 >

#### Gauss-Jordan Elimination
Gauss-Jordan elimination is our initially selected algorithm for solving systems of linear equations. We have created several intuitive methods to emulate sequential operations done by hand. 

#### Ordinary Least-Squares

Introductory machine learning model with linear regression. We will primarily be using our textbook matrix multiplication method and of course our gaussian inversion method. The underlying methodology of OLS is to set up a system of linear equations using a given design matrix (or data set), and solving for the coefficients that minimize the Sum of the Squared Residuals (SSR).  
<img src="/images/solq.svg"
     height=200 >\n
<img src="/images/beta.svg"
     height=200 >


### Determinant

#### Laplace's formula

<img src="/images/laplace.png"
     height=200 >




## Sources
- https://en.wikipedia.org/wiki/Ordinary_least_squares
- https://en.wikipedia.org/wiki/Gaussian_elimination
- https://en.wikipedia.org/wiki/Tikhonov_regularization
- https://en.wikipedia.org/wiki/Strassen_algorithm
- https://en.wikipedia.org/wiki/Determinant#Levi-Civita_symbol
- https://www.math.uwaterloo.ca/~hwolkowi/matrixcookbook.pdf
- http://statweb.stanford.edu/~owen/courses/305-1314/Rudyregularization.pdf
- https://web.stanford.edu/~mrosenfe/soc_meth_proj3/matrix_OLS_NYU_notes.pdf

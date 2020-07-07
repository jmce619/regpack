
from utils import matrix

class ols:
    
    def __init__(self):
       
        pass
    
    def fit(self,x,y,use_constant=False):

        
        X=matrix(x)

        if use_constant==True:
            X=X.add_constant()


        Xt=X.transpose()
        y=matrix(y)
        
        self.beta_vector=Xt.m_mult(X).gauss_inv().m_mult(Xt).m_mult(y)
        
        self.constant=self.beta_vector[0][0]
        self.coefficients=matrix(self.beta_vector[1:])
        
    def predict(self,x):
        
        X=matrix(x)
        return X.m_mult(self.beta_vector)

    def mae_(self,x,y):


        X=matrix(x)
        y=matrix(y)

        sum1=0
        for n,i in enumerate(y.m_sub(X.m_mult(self.beta_vector))):
            if i[0]<0:
                i[0]=i[0]*(-1)
                sum1+=i[0]
            else:
                sum1+=i[0]
        
        return sum1/n+1

    def mse_(self,x,y):

        X=matrix(x)
        y=matrix(y)

        sum1=0
        for n,i in enumerate(y.m_sub(X.m_mult(self.beta_vector))):
            sum1+=i[0]**2
        
        return sum1/n+1




class ridge:

    def __init__(self):

        pass

    def fit(self,x,y):

        X=matrix(x)
        y=matrix(y)

        Xt=X.transpose()

        p1=Xt.m_mult(X).gauss_inv()
        p2=Xt.m_mult(X)
        print(p1,p2)

        self.alpha=p1.m_sub(p2)
        #self.alpha=Xt.mmult(X).msubb()





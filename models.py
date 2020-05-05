
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
        
        self.beta_vector=Xt.mmult(X).gauss_inv().mmult(Xt).mmult(y)
        
        self.constant=self.beta_vector[0]
        self.coefficients=self.beta_vector[1:]
        
    def predict(self,x):
        
        X=matrix(x)
        return X.mmult(self.coefficients).madd(self.constant)


class ridge:

    def __init__(self):

        pass





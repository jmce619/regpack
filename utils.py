class matrix:
    
    def __init__(self,x):
        
        for i in x:
            assert len(i)==len(x[0]),"columns differ in length"
        self.x=x
        self.row=len(x)
        self.column=len(x[0])

        
    def __repr__(self):
        
        x1=''
        for i in range(self.row):
            x2=''
            for j in range(self.column):
                x2+=str(self[i][j])+','
            x1+='|'+x2+'|\n'
        return x1  
    
    def __setitem__(self, index1, value):
        
        self.x[index1] = value

    def __getitem__(self,i):
        
        return self.x[i]
        
    
    def empty(self):
        
        return matrix(([[0]*self.column]*self.row))

    def identity(self):

        x1=[]
        for i in range(self.row):
            x2=[0]*self.column
            x2[i]=1
            x1.append(x2)
        return matrix(x1)
    

    def set_gauss(self):
        
        x1=[]
        for i in range(self.row):
            x2=[0]*self.column
            x2[i]=1
            x1.append(self.x[i]+x2)
            
        return matrix(x1)
        
    
     
    def sort_zeros(self):
        
        list1=[]
        for i,row in enumerate(self):
            count_lead=0
            for j,column in enumerate(row):
                if column==0:
                    count_lead+=1
                else:
                    break
                    
            list1.append([count_lead,self.x[i]])
        list1.sort(key=lambda x: x[0])
        for i,item in enumerate(list1):
            self.x[i]=item[1]
        return matrix(self.x)
         

    def scale(self):
        
        for i in range(self.row):
            for j in range(self.column):
                
                if self.x[i][j]!=0:
                    scalar=self.x[i][j]
                    for k in range(j,self.column):
                        self.x[i][k]=self.x[i][k]/scalar
                    break
                        
                else:
                    continue
                    
                 
        return matrix(self.x)
                    
                                    
    def row_reduce(self):
            
        n=1
        for i in range(self.row):
            a=self.x[i][i]
            for j in range(n,self.row):
                b=self.x[j][i]
                c=float(b/a)
                
                if b==0:
                    pass
                else:
                
                    for k in range(n-1,self.column):
                                                   
                        self.x[j][k]=self.x[j][k]-c*self.x[i][k]
               
              
            n+=1
              
        return matrix(self.x)                    
           
    

    def echelon_form(self):
        m=1
        for i in range(self.row-1):
            n=1
            
            for j in range(m,self.row):
                b=self.x[i][j]

                
                for k in range(n,self.column):
                    
                    self.x[i][k]=self.x[i][k]-b*self.x[j][k]
                n+=1
            m+=1
                
                
        return matrix(self.x)   
    
    def take_inv(self):
        
        for i,row in enumerate(self):
            self[i]=row[int(self.column/2):self.column]
        self.column=int(self.column/2)
        
        return matrix(self.x)

    def madd(self,x):
        assert self.column==x.column
        assert self.row==x.row

        x1=[]
        for i,row in enumerate(self):
            x2=[]
            for j,row in enumerate(x):
                x2.append(self[i][j]+x[i][j])
            x1.append(x2)
        return matrix(x1)

    
       
    def mmult(self,x):
        
        assert self.column==x.row

        x1=[]
        x2=x.transpose()
        
        for i,row in enumerate(self):
            x3=[]
            
            for j,column in enumerate(x2):
                sum1=0
                for k in range(self.column):
                    sum1+=self[i][k]*x2[j][k]
                x3.append(sum1)
            x1.append(x3)

        return matrix(x1)
                
    def transpose(self):

        x1=[]
        for i in range(self.column):
            x2=[]
            for j in range(self.row):
               
                x2.append(self.x[j][i])
            x1.append(x2)

        return matrix(x1)
    
    
    def gauss_inv(self):
        
        return self.set_gauss().row_reduce().scale().echelon_form().take_inv()
    
    def add_constant(self):
        
        x1=[]
        for i in range(self.row):
            x2=[1]
            for j in range(self.column):
                x2.append(self.x[i][j])
            
          
            x1.append(x2)
            
        return matrix(x1)
        
        






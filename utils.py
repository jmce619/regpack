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

    def to_list(self):

        x1=[]
        for i in range(self.row):
            x2=[]
            for j in range(self.column):
                x2.append(self[i][j])
            x1.append(x2)
        return x1 

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
            if a==0:
                pass
            else:
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

    def m_add(self,x):

        assert self.column==x.column
        assert self.row==x.row

        x1=[]
        for i,row in enumerate(self):
            x2=[]
            for j,row in enumerate(x):
                x2.append(self[i][j]+x[i][j])
            x1.append(x2)
        return matrix(x1)

    def m_sub(self,x):

        assert self.column==x.column
        assert self.row==x.row

        x1=[]
        for i in range(self.row):
            x2=[]
            for j in range(self.column):
                x2.append(self[i][j]-x[i][j])
            x1.append(x2)
        return matrix(x1)
    
       
    def m_mult(self,x):
        
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

    def m_mult1(self,x):
        
        assert self.column==x.row

        x1=[]
        
        for i,row in enumerate(self):
            x3=[]
            
            for j,column in enumerate(x2):
                sum1=0
                for k in range(self.column):
                    sum1+=self[i][k]*x3[k][i]
                x3.append(sum1)
            x1.append(x3)



        return matrix(x1)


    def div_conq1(self,x):

        ring1={}
        x3=[[0]*self.row]*x.column

        for k in range(int(self.column/2)):
            for i in range(0,self.row-1,2):
                x2=matrix(([[0]*2]*2))
                for j in range(0,self.column-1,2):

                    ring1[f'a{i}_{j}']=matrix([[self.x[i][j],self.x[i][j+1]],[self.x[i+1][j],self.x[i+1][j+1]]])
                    ring1[f'b{j}_{i}']=matrix([[x[i][i],x[i][i+1]],[x[i+1][i],x[i+1][i+1]]])
                    x2=x2.m_add(ring1[f'a{i}_{j}'].m_mult(ring1[f'b{j}_{i}']))

                x3[k*2][i]=x2[0][0]
                x3[k*2+1][i]=x2[1][0]
                x3[k*2][i+1]=x2[0][1]
                x3[k*2+1][i+1]=x2[1][1]


        return matrix(x3)

    def div_conq2(self,x):

        a11=[[0]*int(self.row/2)]*int(self.column/2)
        a12=[[0]*int(self.row/2)]*int(self.column/2)
        a21=[[0]*int(self.row/2)]*int(self.column/2)
        a22=[[0]*int(self.row/2)]*int(self.column/2)

        b11=[[0]*int(self.row/2)]*int(self.column/2)
        b12=[[0]*int(self.row/2)]*int(self.column/2)
        b21=[[0]*int(self.row/2)]*int(self.column/2)
        b22=[[0]*int(self.row/2)]*int(self.column/2)



        for i in range(self.row):
            for j in range(self.column):

                if i<self.row/2 and j<self.column/2:
                    a11[i][j]=self.x[i][j]
                    b11[i][j]=x[i][j]

                elif i<self.row/2 and j>=self.column/2:
                    a12[i][j-int(self.column/2)]=self.x[i][j]
                    b12[i][j-int(self.column/2)]=x[i][j]

                elif i>=self.row/2 and j<self.column/2:
                    a21[i-int(self.row/2)][j]=self.x[i][j]
                    b21[i-int(self.row/2)][j]=x[i][j]

                else:
                    print(i,j)
                    a22[i-int(self.row/2)][j-int(self.column/2)]=self.x[i][j]
                    b22[i-int(self.row/2)][j-int(self.column/2)]=x[i][j]

        c11=matrix(a11).m_mult(matrix(b11)).m_add(matrix(a12).m_mult(matrix(b21)))
        c12=matrix(a11).m_mult(matrix(b12)).m_add(matrix(a12).m_mult(matrix(b22)))
        c21=matrix(a21).m_mult(matrix(b11)).m_add(matrix(a22).m_mult(matrix(b21)))
        c22=matrix(a21).m_mult(matrix(b12)).m_add(matrix(a22).m_mult(matrix(b22)))

        
        x3=[]

        for i in range(self.row):
            if i<self.row/2:
                x3.append(c11[i]+c12[i])
            else:
                x3.append(c21[i-int(self.row/2)]+c22[i-int(self.row/2)])

        return matrix(x3)



    def strassen(self,x):

        a11=[[0]*int(self.row/2)]*int(self.column/2)
        a12=[[0]*int(self.row/2)]*int(self.column/2)
        a21=[[0]*int(self.row/2)]*int(self.column/2)
        a22=[[0]*int(self.row/2)]*int(self.column/2)

        b11=[[0]*int(self.row/2)]*int(self.column/2)
        b12=[[0]*int(self.row/2)]*int(self.column/2)
        b21=[[0]*int(self.row/2)]*int(self.column/2)
        b22=[[0]*int(self.row/2)]*int(self.column/2)



        for i in range(self.row):
            for j in range(self.column):

                if i<self.row/2 and j<self.column/2:
                    a11[i][j]=self.x[i][j]
                    b11[i][j]=x[i][j]

                elif i<self.row/2 and j>=self.column/2:
                    a12[i][j-int(self.column/2)]=self.x[i][j]
                    b12[i][j-int(self.column/2)]=x[i][j]

                elif i>=self.row/2 and j<self.column/2:
                    a21[i-int(self.row/2)][j]=self.x[i][j]
                    b21[i-int(self.row/2)][j]=x[i][j]

                else:
                    print(i,j)
                    a22[i-int(self.row/2)][j-int(self.column/2)]=self.x[i][j]
                    b22[i-int(self.row/2)][j-int(self.column/2)]=x[i][j]
        print(a11,a12,a21,a22,b11,b12,b21,b22)

        m1=(matrix(a11).m_add(matrix(a22))).m_mult((matrix(b11)).m_add(matrix(b22)))
        m2=(matrix(a21).m_add(matrix(a22))).m_mult((matrix(b11)))
        m3=matrix(a11).m_mult((matrix(b11)).m_sub(matrix(b22)))
        m4=matrix(a22).m_mult((matrix(b21)).m_sub(matrix(b11)))
        m5=(matrix(a11).m_add(matrix(a12))).m_mult((matrix(b22)))
        m6=(matrix(a21).m_sub(matrix(a11))).m_mult((matrix(b11)).m_add(matrix(b12)))
        m7=(matrix(a12).m_sub(matrix(a22))).m_mult((matrix(b21)).m_add(matrix(b22)))
        
        c11=m1.m_add(m4).m_sub(m5).m_add(m7)
        c12=m3.m_add(m5)
        c21=m2.m_add(m4)
        c22=m1.m_sub(m2).m_add(m3).m_add(m6)
       
        x3=[]

        for i in range(self.row):
            if i<self.row/2:
                x3.append(c11[i]+c12[i])
            else:
                x3.append(c21[i-int(self.row/2)]+c22[i-int(self.row/2)])

        return matrix(x3)


    def madd_constant(self,x):

        for i in range(self.row):
            for j in range(self.column):
                self.x[i][j]+=x
        return matrix(self.x)
                
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

    def svd(self):

        ata=self.x.transpose().m_mult(self.x)

        return ata

    # def rc_del(self,m,n):

    #     x1=[]
    #     for i in range(self.row):
    #         for j in range(self.column):
    #             if i==m or j==n:
    #                 pass
    #             else:
    #                 x2.append(self.x[i][j])
    #         x1.append(x2)

    #     return x1

    def rc_del2(self,m,n):

        return matrix([[self.x[i][j] for j in range(self.column) if j!= n] for i in range(self.row) if i!=m])

    def calc_det1(self,sum1=0):
        if self.column==2 and self.row==2:
            # print(sum1)
            return get_det1(self.x)
            
        else:
            _i=0
            for i in range(self.row):
                for j in range(self.column):
                    # print(sum1)
                    # print(i,j)
                    
                    sum1+=((-1)**(_i+j+2))*self.x[i][j]*self.rc_del2(i,j).calc_det1()
                    print(sum1)


        return sum1

def get_det1(matrix):

    return float((matrix[0][0]*matrix[1][1]- matrix[0][1]*matrix[1][0])) 



        
        






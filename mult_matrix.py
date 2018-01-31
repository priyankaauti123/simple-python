r1=input("Enter row1:=")
c1=input("Enter col1:=")
r2=input("Enter row2:=")
c2=input("Enter col2:=")


mat1=[[input()for i in range(c1)]for j in range(r1)]
mat2=[[input()for i in range(c2)]for j in range(r2)]
print mat1
print mat2


def mult_mat(mat1,mat2,r1,r2,c1,c2):
    mat3=[[0 for i in range(c2)]for j in range(r1)]
    if c1==r2:
        for i in range(r1):
            j=0
            k=0
            val=0
            while(k<c2):
                if j==r2:
                    #print mat3
                    mat3[i][k]=val
                    k+=1
                    j=0
                    val1=0
                else:
                    print mat1[i][j],mat2[j][k]
                    val+=mat1[i][j]*mat2[j][k]
                    j+=1
        print mat3
    else:
        print "not equal"

mult_mat(mat1,mat2,r1,r2,c1,c2)






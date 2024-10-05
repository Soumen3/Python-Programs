def matrix_sum():
    r1,c1=int(input('Enter the row and column of first matrix:\n')),int(input())
    r2,c2=int(input('Enter the row and column of second matrix:\n')),int(input())
    
    if r1==r2 and c1==c2:
        print('Enter the first matrix value row wise:\n')
        mat1=[]
        for i in range(r1):
            arr=[]
            for j in range(c1):
                arr.append(int(input()))
            mat1.append(arr)

        print('Enter the second matrix value row wise:\n')
        mat2=[]
        for i in range(r2):
            arr=[]
            for j in range(c2):
                arr.append(int(input()))
            mat2.append(arr)

        mat_re=[]
        for i in range(r1):
            arr=[]
            for j in range(c1):
                arr.append( mat1[i][j] + mat2[i][j])
            mat_re.append(arr)
             

        print('The result matrix is:\n')
        for i in range(r1):
            for j in range(c1):
                print(mat_re[i][j],end=' ')
            print()

        
    else:
        print('Row column should be same for both matrix')


def matrix_product():
    r1,c1=int(input('Enter the row and column of first matrix:\n')),int(input())
    r2,c2=int(input('Enter the row and column of second matrix:\n')),int(input())

    if c1==r2:
        # input first matrix
        print('Enter the first matrix value row wise:\n')
        mat1=[]
        for i in range(r1):
            arr=[]
            for j in range(c1):
                arr.append(int(input()))
            mat1.append(arr)

        #inout second matrix
        print('Enter the second matrix value row wise:\n')
        mat2=[]
        for i in range(r2):
            arr=[]
            for j in range(c2):
                arr.append(int(input()))
            mat2.append(arr)

            
        # calculate the result
        re=[]
        
        for i in range(r1):
            arr=[]
            
            for j in range(c2):
                s=0
                for k in range(c1):
                    s=s+mat1[i][k] * mat2[k][j]
                arr.append(s)
            re.append(arr)

        #printing the result matrix
        
        print('The result matrix is:\n')
        for i in range(r1):
            for j in range(c2):
                print(re[i][j],end=' ')
            print()           

        

    else:
        print('multiplication is not possible in this matrix format')

        

choice=int (input('1 for sum of matrices\n2 for product of matrices\n'))

match choice:
    case 1:
        matrix_sum()
    case 2:
        matrix_product()
    case _ :
        print('invalid choice!')

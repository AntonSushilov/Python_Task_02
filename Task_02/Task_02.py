def main():
    with open("input_1.txt", "r") as file1:
        a = file1.readlines()
    a = [[int(n) for n in x.split()] for x in a]
    print(a)
    #####
    with open("input_2.txt", "r") as file2:
        b = file2.readlines()
    b = [[int(n) for n in x.split()] for x in b]
    print(b)
    #####
    ox = []
        
    
    ox = func(a,b,ox)
    if ox!= None:
        print("Ok", ox)
    else:
        print("False")

    file1.close()
    file2.close()

def func(a,b,ox):
    result = False
    for i in range(len(a)):
        for j in range(len(a[i])):
            if a[i][j] == b[0][0]:            
                for k in range(len(b)):
                    for n in range(len(b[k])):
                        if a[i+k][j+n]==b[k][n]:
                            ox = [i,j]
                            result = True
                        else:
                            result = False
                            break
    if result:
        return ox
 
main()
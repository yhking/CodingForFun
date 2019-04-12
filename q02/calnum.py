

for n in range(1000,10000,1):
    str_n = list(str(n))
    op = ('*','') ## + - / 能组成的最大值是999+9=1008，因此其他组合连四位数都凑不齐，因此直接去掉+ - /
    for i in op:
        for j in op:
            for k in op:
                if i == "" and j == "" and k == "":
                    continue
                if j == "" and str_n[1] == "0":
                    str_n[1] = ""
                if k == "" and str_n[2] == "0":
                    str_n[2] = ""   
                
                if eval(str_n[0]+i+str_n[1]+j+str_n[2]+k+str_n[3]) == int(str(n)[::-1]):
                    print(str_n[0]+i+str_n[1]+j+str_n[2]+k+str_n[3]+'='+str(n)[::-1])
                else:
                    str_n = list(str(n)) #还原
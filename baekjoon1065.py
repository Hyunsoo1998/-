def hansoo(G):
    hansoo_cnt=0
    for i in range(1,G+1):
        G_list=list(map(int,str(i)))
        if i<100:
            hansoo_cnt+=1
        elif G_list[0]-G_list[1]== G_list[1]-G_list[2]:
            hansoo_cnt+=1
    return hansoo_cnt

N=int(input())
print(hansoo(N))
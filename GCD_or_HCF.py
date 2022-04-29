N,M=map(int,input().split())
while(N!=M):
    if(N>M):
        N=N-M
    else:
        M=M-N
print(N)        
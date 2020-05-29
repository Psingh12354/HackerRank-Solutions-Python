n=int(input())
for i in range(n):
    S=str(input())
    c=0
    for i in S:
        if(i.isupper()):
            c+=1
    if(c>1):
        d=0
        for j in S:
            if(j.isdigit()):
                d+=1
        if(d>2):
            if(S.isalnum()):
                if(len(S)==10):
                    m=0
                    for k in S:
                        for h in S:
                            if(k==h):
                                m+=1
                    if(m==10):
                        print('Valid')
                    else:
                        print('Invalid')
                else:
                    print('Invalid')
        else:        
            print('Invalid')
    else:        
        print('Invalid')

                

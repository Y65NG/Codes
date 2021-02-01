from functools import reduce
print(list(filter(None,map(lambda y:y*reduce(lambda x,y:x*y!=0, map(lambda x,y=y:y%x,range(2,int(pow(y,0.5)+1))),1),range(2,100000)))))


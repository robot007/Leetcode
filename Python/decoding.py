# from https://www.youtube.com/watch?v=qli-JCrSwuk&list=PLaRrM3Te30Pis5BIrekQH4WhMc5IQrlHy
# 

## Try 1: failed
# tried to find out all the possible combinations, than count the numbers. This is more difficult
# class Tree():
#     end_leaf = set()
#     def __init__(self, root):
#         self.root= root;
#         self.left=None;
#         self.right=None;
#     def add_left(self, left):
#         self.left = Tree(left)
#         self.left


# class Decode():
#     dic=None
#     def __init__(self):
#         letter='abcdedfhijklmnopqrstuvwxyz'
#         dic={}
#         for cnt in range(26):
#             dic[str(cnt+1)]=letter[cnt]
#         self.dic = dic

#     def decode(self, instr):
#         for ix in range(len(instr)-1):
#             s1 = instr[ix]
#             s2 = instr[ix:ix+1]
        
instr = '1234'

## solution 1
letter='abcdedfhijklmnopqrstuvwxyz' # dont need this 
dic={}
for cnt in range(26):
    dic[str(cnt+1)]=letter[cnt]
print(dic)
def num_decode(instr, pt):
    if len(instr)-pt > 2:
        s1=instr[pt]
        s2=instr[pt:pt+1]
        n = num_decode(instr, pt+1)
        if s1 in dic.keys():
            n=n+1
        if s2 in dic.keys():
            n=n+1
    else: # stopping condition
        s1=instr[pt]
        s2=instr[pt+1]
        s3=instr[pt:pt+1]
        ## branch 1: check if both s1 and s2 exists
        n=0 
        if s1 in dic.keys() and s2 in dic.keys():
            n=n+1
        ## branch 2: singal digit number always has a letter? NOT for 0!
        # n=1 # 
        if s3 in dic.keys():
            n+n+1
    return n

n = num_decode(instr, 0)
print(n)

## solution 2

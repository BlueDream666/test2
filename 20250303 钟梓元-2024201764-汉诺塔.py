'''
用Python编写求解汉诺塔问题的移动函数
思想：使用move(n,a,c)完成小操作：从a到c
使用hanoi(n,a,b,c)完成大操作：a经过b走到c
hanoi则包括：hanoi(n-1,a,c,b),move(n,a,c),hanoi(n-1,b,a,c)
用来完成：将n-1个上层塔搬到中间，把a->c，再将n-1个塔搬到右边
'''

count=0

def move(n,a,c):
    global count#一定要global!要不然记不了数
    count+=1
    print("[step {0}] move plate {1} from {2} to {3}\n".format(count,n,a,c),end="")

def hanoi(n, a='A', b='B', c='C'):
    if n==1:
        move(n,a,c)
    else:
        hanoi(n-1,a,c,b)
        move(n,a,c)
        hanoi(n-1,b,a,c)
        #用来完成：将n-1个上层塔搬到中间，把a->c，再将n-1个塔搬到右边

try:
    n=int(input("请输入要移动的层数"))
except:
    n=int(input("输入错误！请输入要移动的层数"))

hanoi(n,a='A', b='B', c='C')
print("一共花了{}步".format(count))

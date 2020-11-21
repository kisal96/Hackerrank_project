
a=[[1,4,5],[2,3,6],[5,6,7]]
n=len(a)

count=len(a)

while n>0:
  for i in range(n):
   m = len(a[i])
   if not i==n-1:
    for j in range(m):
      if j==n-1:
        while not a[i][n-1]==0:
            a[i][n-1]-=1
            a[n-1][n-1]+=1
  n=n-1
print(a)

if __name__ == '__main__':


      q = int(input())

      for q_itr in range(q):
          n = int(input())

          container = []

          for _ in range(n):
              container.append(list(map(int, input().rstrip().split())))



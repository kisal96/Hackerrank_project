keyboards = [3,1,9,5]
drives = [5,2,8,4,5,7,9]
suma = 0
buma = 0
h=[]
g=[]


b = int(input())
mink = min(keyboards)
minb = min(drives)
maxk = max(keyboards)
maxb = max(drives)

m = mink + minb

if m > b:
    print('-1')

else:
    for i in keyboards:

            if suma < maxb + i:
              suma = maxb + i
              if suma <= b:

                h.append(i)
              else:
                  suma=0
            else:
                pass

    for j in drives:
        if buma <= b:

            if buma < maxk + j:
                buma = maxk + j
                if buma <= b:

                 g.append(j)
                else:
                  buma=0
            else:
                pass
        else:
            pass
    if maxb + max(h) >= maxk + max(g):
        print(maxb + max(h))

    else:
        print(maxk + max(g))
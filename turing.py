
info = open("infor.txt","w")
myinfo = input("write your value \n")
info.write(myinfo)
info.close()
info = open("infor.txt","r")
leng = len(myinfo)
i=0
pos = 1
p = "q0"
print(leng)

sp = "0"+info.read()+"0"


def insert( p ,v, sp):
   i=0
   spn = ""
   for i in range(len(sp)):

       if i == p :
          spn = spn + v
       else   :
          spn = spn + sp[i]
       i=i+1
   return spn
def putit(sp,pos,p):
   spt = ""
   i=0
   for i in range(len(sp)):
       if i == pos :
           spt = spt + "(" + p +")"
       spt = spt+sp[i]
       i=i+1
   return spt




while p != "qf" :
    inst = open("instra.txt", "r")
    for x in inst :
        if x[0:2] == p :


            if x[3] == sp[pos] :

                   if x[5] == "0" :
                    sp = insert(pos,"0",sp)
                    p = x[7:9]

                    break

                   if x[5] == "1" :
                    sp = insert(pos,"1",sp)
                    p = x[7:9]

                    break

                   if x[5] == "*" :
                    sp = insert(pos,"*",sp)
                    p = x[7:9]


                    break
                   if x[5] == "r":
                      pos = pos + 1

                      p = x[7:9]

                      break


                   if x[5] == "l":
                       pos = pos -1

                       p = x[7:9]

                       break

    inst.close()
    spt1 = putit(sp,pos,p)
    print(spt1[1:(len(spt1)-1)])
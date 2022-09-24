f  =   open("Shafin")
Contain = f.read()
print(Contain)

#koto tuku jaiga read korbo

contain = f.read(12)
print(contain)


#Binary nite chaile
f=open("Shafin", "rb" )
con = f.read()
print(con)


#line by line nite chaile

f=open("Shafin ")
conn=f.read()
for line in conn :
    print(line)


#sob file ke list akare chaile

f=open("Shafin")
connn=f.readline()
print(conn)

#vector

a<-c(1:9)
a
length(a)
print(class(a))
colors<-c('red','blue','yellow',NA)
names(colors)<-c('c1','c2','c3','c4')
colors
sortcol<-sort(colors,decreasing = TRUE)
sortcol

which(is.na(colors))

print(class(colors))

b<-seq(1,34,by=0.5)
b

rm(b)  #delete vector


mean(a,trim = 0,na.rm = FALSE)

B<-c(3,5,6,7,8,9)
median(B,na.rm = FALSE)

#list

l1<-list('ab','bs',1,2,TRUE,c(9:12))
l1

list2<-list(c('red','blue','black'),matrix(c(3:15),nrow=2),list('java','py','c++'))

names(list2)<-c('colors','matrix','language')
list2

print(list2$language[2])

l1<-list(1,2,3,4,5,6)
l3<-list(1,2,3,4,5,6)
listmerge<-c(l1,l3)
listmerge             #list merge

c<-unlist(l1)
c

#matrix
rownames = c("r1","r2","r3")
colnames = c("c1","c2","c3")
m1<-matrix(c(1:9),nrow = 3, byrow = TRUE,dimnames=list(rownames,colnames))
m1

m3<-t(m1)
m3

m2<-apply(m1, 1,sum)
m2

#dataframe
df1<-data.frame(
  empid=(1:3),
  empname = c("kk","pk","ak"),
  empsal=c(200,200,300),
  stringsAsFactors = FALSE
)

print(df1)
str(df1)

print(df1[1:2])

df1$dept<-c("it","ec","ce")
df1

df3<-cbind(df1,age=c(45,67,67))
df3
print(summary(df3))

df4<-rbind(df1,df3)
df4




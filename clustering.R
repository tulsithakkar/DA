#Clustering in R
attendance <- c(80,50,90,95,80,40,50)

print(attendance)

grade <- c(7,4,8,7,8,5,4)

---------------------------
  
  print(grade)

df <- data.frame(attendance,grade)

print(df)

kmm <- kmeans(df,3)

print(kmm)

summary(kmm)

---------------------
  
kmm $cluster

install.packages("fpc")
library(fpc)

plotcluster(df,kmm$cluster)

----------------------
  
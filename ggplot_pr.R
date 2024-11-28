install.packages("ggplot2")
library(ggplot2) 

car_data <- data.frame( 
  
  model = c("Toyota", "Honda", "Ford", "BMW", "Audi"), 
  
  mpg = c(30, 35, 25, 20, 18), 
  
  hp = c(120, 150, 200, 250, 280) 
  
) 

print(car_data) 

ggplot(data = car_data, aes(x = hp, y = mpg)) + 
  
  geom_point(color = "blue", size = 3) +           # Scatter plot points 
  
  geom_smooth(method = "lm", se = FALSE, color = "red") +  # Add a regression line 
  
  labs(title = "Relationship between Horsepower and MPG", 
       
       x = "Horsepower (hp)", 
       
       y = "Miles Per Gallon (mpg)") + 
  
  theme_minimal() 



#simple scatter plot on iris data

df_iris <- data.frame(iris) 
df_iris

ggplot(df_iris, aes(x = Sepal.Length, y = Sepal.Width, color = Species)) +
  geom_point() +
  labs(title = "Sepal Length vs Sepal Width", x = "Sepal Length", y = "Sepal Width") + theme_minimal()

#bar graph on studnet data 
#Student Example: 
  
sdata <- data.frame(sname = c("Jaimin", "Sachin", "Virat"), savg = c(33, 22, 55), scity = c("Bvn", "Srt", "Bmm")) 

ggplot(sdata, aes(x = sname, y = savg, fill = scity)) + geom_bar(stat = "identity") + labs(title = "Average Scores by Player", x = "Player Name", y = "Average Score") + theme_minimal() 

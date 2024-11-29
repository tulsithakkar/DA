data =[]
ni= int(input("enter the number of value: "))
for i in range(ni):
    k = int(input("enter value: "))
    data.append(k)


min_value = min(data)
max_value = max(data)

new_min = int(input("enter new min value: "))
new_max = int(input("enter new max value: "))

max_min_normalized_data =[]

for value in data:
    normalized_value = ((value - min_value) / (max_value -min_value)) * (new_max - new_min) + new_min
    max_min_normalized_data.append(normalized_value)

print("original_data : ",data)
print("normalized data: ",max_min_normalized_data)

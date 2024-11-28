#binning by mean & boundary

data=[]
ni = int(input("how many items you want: "))
for i in range(ni):
    k = int(input("enter value: "))
    data.append(k)

data.sort()

bin_size = int(input("ente bins sizes: "))
bins=[]
i=0
binned_by_mean_data=[]
binned_by_boundary=[]

while i < len(data):
    bin_values = data[i:i + bin_size]
    bins.append(bin_values)
    mean_value = sum(bin_values) / len(bin_values)
    for value in bin_values:
        binned_by_mean_data.append(mean_value)
    i += bin_size

i=0
for bin_values in bins:
    min_value = min(bin_values)
    max_value = max(bin_values)
    for value in bin_values:
        if abs(value - min_value) < abs(value - max_value):
            binned_by_boundary.append(min_value)
        else :
            binned_by_boundary.append(max_value)



print("\n original data: ", data)
print("\nbins ",)

for idx,bin_values in enumerate(bins,1):
    print(f"bins{idx} : {bin_values}")

print("\n mean: ", binned_by_mean_data)
print("\n boundary: ", binned_by_boundary)



    



            












        

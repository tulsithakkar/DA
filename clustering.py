#clustering

data =[]
ni =int(input("how many data you want: "))
for i in range(ni):
    k = int(input("enetr data: "))
    data.append(k)

k = int(input("enter number of cluster you want: "))

clusters =[]

cluster_size = len(data) // k
extra = len(data) % k

start =0

for i in range(k):
    end = start + cluster_size + (1 if i < extra else 0)
    clusters.append(data[start:end])
    start = end

print("original data : ",data)
print("clusters: ")

for cluster in clusters:
    print(f"cluster {clusters.index(cluster) +1} : {cluster}")






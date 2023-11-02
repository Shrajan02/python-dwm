import matplotlib.pyplot as plot

data =[]
data = list(map(int, input("Enter the data set = ").split()))

#HISTOGRAM
plot.figure(figsize=(8,5))  #box 
plot.hist(data, bins = 10, edgecolor='k' , alpha =0.7) #main histogram
plot.title("Histogram")
plot.xlabel("Value")
plot.ylabel("Frequency")
plot.grid(True) #adding grid lines to the graph

plot.show()


#SCATTER PLOT

x = list(range(1,len(data) + 1))

plot.figure(figsize=(8,5))
plot.scatter(x,data, c ='b',marker='o',label='Data Points') #main scatterplot
plot.title("Scatter Plot:")
plot.xlabel("Index")
plot.ylabel("Value")
plot.grid(True)

plot.legend()
plot.show()








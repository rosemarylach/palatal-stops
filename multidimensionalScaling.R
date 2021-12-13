dist_data <- read.csv(file="vietnamese.csv", header=TRUE, encoding = "UTF-8")
rownames(dist_data) = dist_data[,1]
dist_data = dist_data[,-1]
dist_data = as.matrix(dist_data)
library(MASS)
mds_data = isoMDS(dist_data, k=2)
plot(mds_data$points[,1],mds_data$points[,2], type='n', main="Vietnamese Multidimensional Scaling")
text(mds_data$points, label=dimnames(mds_data$points)[[1]])
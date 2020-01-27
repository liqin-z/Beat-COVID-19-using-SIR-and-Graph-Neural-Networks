library(rjson)
library(jsonlite)

data<-jsonlite::stream_in(file("data.json"),pagesize = 100)
data$area
data[data$area=="湖北武汉" | data$area=='湖北', ]
data[data$area=="海南",]


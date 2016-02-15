library(ggplot2)
library(ggmap)

lon <- weatherNorthEastUS$lon
lat <- weatherNorthEastUS$lat
temp <- weatherNorthEastUS$temp
wind_chill <- weatherNorthEastUS$wind_chill

## map of New England with temperature of cities
myMap <- get_map(location="New England",
                 source="google", maptype="terrain", crop=FALSE, zoom = 6)

ggmap(myMap)+
  geom_point(aes(x = lon, y = lat, size = temp, color = wind_chill), data = weatherNorthEastUS,
             alpha = .7) + scale_colour_gradient(low = "blue") + labs(title = "Wind Chill Temperature around New England (Celsius)") + xlab("Longitude") + ylab("Latitude")

## histogram of wind_chill
m <- ggplot(weatherNorthEastUS, aes(x=wind_chill))
m + geom_histogram(aes(fill = ..count..)) +
  scale_fill_gradient("Count", low = "azure")


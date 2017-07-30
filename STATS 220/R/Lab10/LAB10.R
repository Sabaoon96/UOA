# Sabaoon Raza Khan - STATS220 - LAB10

# Q1
  pat2015 <- read.csv("patronage-2015.csv")
  pat2015
  
# Q2
  busTotal <- pat2015$BusTotal
  ferry <- pat2015$Ferry
  bigBus <- busTotal[1:nrow(pat2015)]/ferry[1:nrow(pat2015)] > 10
  bigBus
  
# Q3
  bigMonths <- pat2015[pat2015$BusTotal/pat2015$Ferry > 10, c(3,7)]
  bigMonths
  
# Q4
  years <- 2005:2016
  filenames <- paste("patronage-", years, ".csv", sep="")
  for (file in filenames) {
    data <- read.csv(file)
    count <- 0
    for (i in 1:nrow(data)) {
      if (data$BusTotal[i]/data$Ferry[i] > 10){
        count <- count + 1
      } else {
        count <- count + 0
      }
    }
    cat(file, "contains", count, "months in which bus patronage was more than 10 times Ferry patronage", "\n")
  }
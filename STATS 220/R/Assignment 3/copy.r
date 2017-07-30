# STATS 220 - A3 - Sabaoon Raza Khan (skha787)

# Q1
	july2014 <- read.csv("burglaries201407.csv")
	head(july2014)
	
# Q2
	july2014max <- max(july2014$Count, na.rm=TRUE)
	july2014max

# Q3
	years <- c(rep(2014, 6), rep(2015, 12))
	years
	
# Q4
	first <- c(rep(0:1, each=3), rep(0, 9), rep(1, 3))
	second <- c(7:9, 0:2, 1:9, 0:2)
	months <- paste(first, second, sep="")
	months
	
# Q5
	filenames <- paste("burglaries", years, months, ".csv", sep="")
	filenames
	
# Q6
	overallMax <- 0
	for (item in filenames) {
		content <- read.csv(item)
		fileMax <- max(content$Count, na.rm=TRUE)
		overallMax <- max(overallMax, fileMax, na.rm=TRUE)
	}
	overallMax
	
# Q7
	# Part(i)
	rows <- (july2014$AreaUnit == "Glendowie")
	july2014glendowie <- july2014[rows, ]
	head(july2014glendowie)
	# Part (ii)
	dim(july2014glendowie)
	
# Q8
	glendowieMax <- 0
	for (item in filenames) {
		content <- read.csv(item)
		fileMax <- max(content[content$AreaUnit == "Glendowie", "Count"], na.rm=TRUE)
		glendowieMax <- max(glendowieMax, fileMax, na.rm=TRUE)
	}
	glendowieMax
	
# Q9 
	glendowieTotal <- 0
	for (item in filenames) {
		content <- read.csv(item)
		fileSum <- sum(content[content$AreaUnit == "Glendowie", "Count"], na.rm=TRUE)
		glendowieTotal <- glendowieTotal + fileSum
	}
	glendowieTotal
	
	
	
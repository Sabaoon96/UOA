# Sabaoon Raza Khan - skha787 

# Q1 (Years from 2005 to 2016)
	year <- 2005:2016
	year
	
# Q2 (Creating filename format)
	filenames <- paste("patronage-", year, ".csv", sep="")
	filenames
	
# Q3 (Reading the first file)
	file1 <- read.csv("patronage-2005.csv", row.names=1)
	file1
	
# Q4 (Finding max value in file)
	max1 <- max(file1$Total)
	max1
	
# Q5 (Finding maximum value across all files)
	overallMax <- 0
	for (i in filenames) {
		item <- read.csv(i)
		fileMax <- max(item$Total)
		overallMax <- max(overallMax, fileMax) 
	}
	overallMax
	
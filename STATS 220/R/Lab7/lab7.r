# Reads the csv file (Q1)
	patronage <- read.csv("D:/University\ of\ Auckland/STATS\ 220/patronage-2015.csv", row.names = 1)
	
# Finds the maximum value in the file (Q2)	
	maxPatronage <- max(patronage)

# Calculates sumBus (Q3)
	totalBus <- patronage$BusTotal
	sumBus <- sum(totalBus)

# Calculates sumBusByAddition (Q4.i)
	rapidBus <- patronage$BusRapid
	otherBus <- patronage$BusOther
	sumBusByAddition <- sum(rapidBus, otherBus)

# Calculates sumBusBySubtraction (Q4.ii)
	totalsum <- sum(patronage$Total)
	trainsum <- sum(patronage$Train)
	ferrysum <- sum(patronage$Ferry)
	sumBusBySubtraction <- totalsum - (trainsum + ferrysum)


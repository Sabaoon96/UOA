# Sabaoon Raza Khan (skha787) | LAB 09

# Q1
  pat2005 <- read.csv("patronage-2005.csv")
  pat2005
  
# Q2
  pat2005total <- pat2005[, 2]
  pat2005total
  
# Q3
  monthChange <- NULL
  julyTotal <- pat2005[1,2]
  augustTotal <- pat2005[2,2]
  if (augustTotal > julyTotal) {
    monthChange <- "increased"
  } else {
    monthChange <- "decreased"
  }
  monthChange
  
# Q4
  monthChange <- NULL
  newTotal <- julyTotal
  x <- 1
  for (value in pat2005[2:6,2]) {
    if (value > newTotal) {
      monthChange <- "increased"
    } else {
      monthChange <- "decreased"
    }
    newTotal <- value
    cat("The patronage in", as.character(pat2005[2:6, 1])[x], monthChange ,"to",value ,"\n")
    x = x + 1
  } 
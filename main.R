library(data.table)
library(ggplot2)
library(dplyr)
library(purrr)

teams      <- fread("data/teams.csv")
conference <- fread("data/conference.csv")
tslots     <- fread("data/ncaatourneyslots.csv")
tseeds     <- fread("data/ncaatourneyseeds.csv")
tresults   <- fread("data/ncaatourneyresult.csv")
season     <- fread("data/regularseasonresults.csv")


teamdf <- inner_join(teams, conference) %>% 
  select(., -Season) %>% 
  unique()
  
df <- reduce(list(teams,conference, tseeds), inner_join)

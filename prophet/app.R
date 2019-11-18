# App

# Libraries
library(prophet)
library(dplyr)
library(tibble)

# Sources
source("utils.R")

main <- function(plot = FALSE, data = FALSE) {
  
  if(!plot && !data || plot && data) {print("Warning - Input one desired outcome: Plot or Data")}
  
  if(!plot && data ) {return(run_forecast_with(x = formatted_data(), data.plot = 'Data'))}
  
  if(plot && !data ) {return(run_forecast_with(x = formatted_data(), data.plot = 'Plot'))}

  
}


main(F, F)

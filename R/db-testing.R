library(someDBlibrary)
library(tidyverse)

timer <- function(fn, ...) {
  start.time <- Sys.time()
  fn(...)
  end.time <- Sys.time()
  dur <- end.time - start.time
  return(dur)
}

check_exists_db_sflake <- function (schema, table){

  error_msg <- paste("Unable to verify that table:", table,
                     "exists in schema:", schema)
  query.string <- "SELECT EXISTS(SELECT * FROM INFORMATION_SCHEMA.TABLES 
                   WHERE table_name = 'TABLE_SUB' AND table_schema = 'SCHEMA_SUB')" %>%
                    gsub("SCHEMA_SUB", toupper(schema), .) %>% 
                    gsub("TABLE_SUB", toupper(table), .)
                                                    
  exists_df <- tryCatch(expr = some_query_call_to_snowflake_db(schema, table),
                        error = function(e){error_msg return(FALSE)})
  return(exists_df[[1]])
}


check_exists_db <- function (schema, table){
  error_msg <- paste("Unable to verify that table:", table,
                     "exists in schema:", schema)
  query.string <- "SELECT EXISTS(SELECT * FROM INFORMATION_SCHEMA.TABLES 
                   WHERE table_name = 'TABLE_SUB' AND table_schema = 'SCHEMA_SUB')" %>%
                    gsub("SCHEMA_SUB", toupper(schema), .) %>% 
                    gsub("TABLE_SUB", toupper(table), .) 
                                                    
  exists_df <- tryCatch(expr = some_query_call_to_pg_db(schema, table),
                        error = function(e){error_msg return(FALSE)}))
  return(exists_df[[1]])
}


test_queries <- function(n) {
  sftest_ <- vector("numeric", n)
  pgtest_ <- vector("numeric", n)
  for(i in seq(n)){
    # I don't know how to call multiple functions and their respective arguments so I have to hard put these :c
    flog.info(paste('now running snowflake test query on data_science.ops_metros number :', i))
    sftest_[i] <- timer(check_exists_db_sflake, schema, table)
    flog.info(paste('now running pg number:', i))
    pgtest_[i] <- timer(check_exists_db, schema,table)
  }
  # garbage collect it
  rm(i,n)

  snowflake_mean <- mean(sftest_)
  postgres_mean  <- mean(pgtest_)

  # get local env vars
  env <- ls()
  # call output of previous vars
  sapply(env, function(x){eval(as.name(x))})
}

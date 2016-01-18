# ==============================================================================#
#-- Project Name: Recurrence Plots : redis update agent
#-- Task : To set the ticker name and threshold value given by user in redis
#-- Version : 1.0
#-- Date : 2015:12:08
#-- Author : Neeraj Komuravalli
# ==============================================================================#

#----------------
#Get Env Variable
#----------------

mripPath = Sys.getenv("MRIP_HOME")
if(mripPath == "") mripPath = getwd()

#---------------
# Load libraries
#---------------

library(futile.logger)
library(rredis)
library(rjson)
#-------------
# Setup logger
#-------------

flog.appender(appender.file(paste(mripPath,"/MINTlogs/UIevent.log",sep="")))
flog.info("UI event agent started")

#---------------
# Connect Redis
#---------------

redisConnect(host = "172.25.1.35", port = 6379, password = NULL, returnRef = FALSE, nodelay = TRUE)

#---------------------------------
# Updates threshold value in redis
#---------------------------------

set_threshold <- function(threshold_value){
  	#threshold in redis database will be replaced by threshold_value given by user
    flog.info(ticker_value)  
    threshold <- gsub(" ","", threshold)
    threshold_value = paste0("$", threshold_value, collapse =NULL)
  	redisSet("threshold", threshold_value, NX = FALSE)
  	flog.info("Threshold value is updated")
}

#---------------------------------
# Updates ticker name in redis
#---------------------------------

 set_ticker <- function(ticker_value){
   	#ticker_req in redis database will be replaced by threshold_value given by user
    flog.info(ticker_value)
    ticker_value <- gsub(" ","",ticker_value)
   	ticker_value = paste0("$", ticker_value, collapse =NULL)
   	redisSet("ticker_req", ticker_value, NX = FALSE)
   	flog.info("Ticker name is updated")
 }
 
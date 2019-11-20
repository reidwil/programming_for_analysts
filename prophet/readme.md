# A Timeseries Forecast in R


`library(fbprophet)`
## A few iterations

I wanted to take a right-out-the-box approach to show a sample timeseries forecast and a few iterations.

**The first iteration:**

    
    > m <- prophet(df)                                     # Call the model
    > future <- make_future_dataframe(m, periods = 365)    # Future df with 365 days
    > forecast <- predict(m, future)                       # Predict future df with model
    >
    > plot(m, forecast)
    
![Initial Plot](https://github.com/reidwil/programming_for_analysts/blob/master/prophet/plot.png)


#--------------------------------

This is a very excellent forecast right out of the box on this set of dummy data.
I did notice the points of data were lending to a more multiplicative method: 

`Data = (Seasonal Effect) x (Trend) x (Noise)`

So I decided to adjust the way the model calculated its decomposition components 

**The second iteration:**


    > m <- prophet(df, seasonality.mode = 'multiplicative')   # Call the model - declare multiplicative method
    > future <- make_future_dataframe(m, periods = 365)       # Future df with 365 days
    > forecast <- predict(m, future)                          # Predict future df with model
    >
    > plot(m, forecast)
    
![Multiplicative - 4 sin fourier](https://github.com/reidwil/programming_for_analysts/blob/master/prophet/multiplicative_fourier_4.png)

--------------------------------

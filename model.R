## Load deSolve package
library(deSolve)
Total=1.4e9
PERIOD=19
#c(beta = 1.06, gamma = 0.85)

## Create an SIR function
sir <- function(time, state, parameters) {
  
  with(as.list(c(state, parameters)), {
    
    dS <- -beta * S * I
    dI <-  beta * S * I - gamma * I
    dR <-                 gamma * I
    
    return(list(c(dS, dI, dR)))
  })
}

### Set parameters
## Proportion in each compartment: Susceptible 0.999999, Infected 0.000001, Recovered 0
init       <- c(S = 1-41/1400000000, I = 41/1400000000, R = 0.0)
## beta: infection parameter; gamma: recovery parameter
parameters <- c(beta = 1.0, gamma = 0.785)
## Time frame
times      <- seq(0, PERIOD, by = 1)
## Solve using ode (General Solver for Ordinary Differential Equations)
out <- ode(y = init, times = times, func = sir, parms = parameters)
## change to data frame
out <- as.data.frame(out)
## Delete time variable
out$time <- NULL
# Show data
## Plot
par(mfrow=c(1,3))
# matplot(x = times, y = out, type = "l",
#         xlab = "Time", ylab = "Susceptible and Recovered", main = "SIR Model",
#         lwd = 1, lty = 1, bty = "l", col = 2:4)
plot(x = times, y = out$S, type = 'l', xlab = "Time", ylab = "Susceptible and Recovered", main="S(t)")
plot(x = times, y = out$I, type = 'l', xlab = "Time", ylab = "Susceptible and Recovered", main="I(t)")
plot(x = times, y = out$R, type = 'l', xlab = "Time", ylab = "Susceptible and Recovered", main="R(t)")

## Add legend
legend(0, 0.7, c("Susceptible", "Infected", "Recovered"), pch = 1, col = 2:4, bty = "n")

final=out*Total
final=cbind(Time=seq(1.13,1.32,0.01),final,Total=Total-final$S)
final[seq(1,19,1),]

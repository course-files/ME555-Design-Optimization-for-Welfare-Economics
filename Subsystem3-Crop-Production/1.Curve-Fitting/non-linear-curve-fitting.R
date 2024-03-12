# **********************************************************************
# Non-Linear Curve Fitting ----
#
# Course Code: ME555
# Course Name: Design Optimization
# University of Michigan
# Semester Duration: 10th Jan 2024 to 29th April 2024
#
## Purpose ----
# To model the underlying trends in the data to understand relationships.
# It implements the Levenberg-Marquardt (LM) method.
# **********************************************************************

# Imports ----
## minpack.lm ----
if (require("minpack.lm")) {
  require("minpack.lm")
} else {
  install.packages("minpack.lm", dependencies = TRUE,
                   repos = "https://cloud.r-project.org")
}

# Dataset ----
# URL of the dataset
url <- "https://raw.githubusercontent.com/course-files/ME555-Design-Optimization-for-Welfare-Economics/main/Datasets/siaya.csv" # nolint

# Load the dataset from the URL
data <- read.csv(url)

# Small-Scale farmers only: data <- data[1:1000, ]

# Medium-Scale farmers only: data <- data[1001:2000,]

# Large-Scale farmers only:
data <- data[2001:3000, ]


# Check the first few rows of the dataset
head(data)

# Set the Initialization and Bounds ----
start_vector <- c(alpha = 1, beta = 1, gamma = 1, theta = 1, tau = 1,
                  kappa = 1, epsilon = 1)
lower_bounds <- c(alpha = -1000, beta = -1000, gamma = -1000, theta = -1000,
                  tau = -1000, kappa = -1000, epsilon = -1000)
upper_bounds <- c(alpha = 1000, beta = 1000, gamma = 1000, theta = 1000,
                  tau = 1000, kappa = 1000, epsilon = 1000)

# Fit the Non-Linear Model using the Levenberg-Marquardt (LM) Method ----
model <- nlsLM(mal ~ (alpha * (r ^ -1.0) - beta * ((sin(cw / tw)) * (ce)) +
                        (qs_stddev) ^ gamma + theta * (qd) ^ -1.0 +
                        tau * ((sin(qs / ts)) - qd) -
                        kappa * (tal ^ -1) + epsilon),
               data = data,
               start = start_vector,
               lower = lower_bounds,
               upper = upper_bounds)

# View the Summary of the Model Fit (the parameters) ----
summary(model)

# Plot the Residuals ----
plot(residuals(model), type = "p",
     main = "Residuals of the Model for Large-Scale Farmers",
     xlab = "Fitted Values", ylab = "Residuals")
abline(h = 0, col = "red")


# Print the Evaluation Metrics ----
predictions <- predict(model)

# Calculate RMSE
rmse <- sqrt(mean((data$mal - predictions)^2))
print(sprintf("RMSE = %.2f", rmse))

# Calculate R Squared
# Total Sum of Squares (variation in the data)
sst <- sum((data$mal - mean(data$mal))^2)

# Sum of Squared Residuals (unexplained variation)
ssr <- sum(residuals(model)^2)

# R-squared
r_squared <- 1 - (ssr / sst)
print(sprintf("R Squared = %.2f", r_squared))


# Calculate MAE
# Assuming 'predictions' contains the predicted values from your model
# and 'y' contains the observed values

# Calculate MAE
mae <- mean(abs(data$mal - predictions))
print(sprintf("Mean Absolute Error (MAE) = %.2f", mae))

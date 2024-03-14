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

## caret ----
if (require("caret")) {
  require("caret")
} else {
  install.packages("caret", dependencies = TRUE,
                   repos = "https://cloud.r-project.org")
}

# Dataset ----
# URL of the dataset
url <- "https://raw.githubusercontent.com/course-files/ME555-Design-Optimization-for-Welfare-Economics/main/Datasets/siaya.csv" # nolint

# Load the dataset from the URL
data <- read.csv(url)

# Small-Scale farmers only: data <- data[1:3000, ]

# Medium-Scale farmers only: data <- data[3001:7000,]

# Large-Scale farmers only: data <- data[7001:10000, ]

# Check the first few rows of the dataset
head(data)

## Split the dataset ----
# Define an 80:10:10 train:test:validate data split of the dataset.
# That is, 80% of the original data will be used to train the model,
# 10% of the original data will be used to test the model and
# 10% of the original data will be used to validate the model.

train_index <- createDataPartition(data$i,
                                   p = 0.8,
                                   list = FALSE)
train <- data[train_index, ]
test_validate <- data[-train_index, ]

train_index <- createDataPartition(test_validate$i,
                                   p = 0.5,
                                   list = FALSE)
test <- test_validate[train_index, ]
validate <- test_validate[-train_index, ]

# Set the Initialization and Bounds ----
start_vector <- c(alpha = 1, beta = 1, gamma = 1, theta = 1, tau = 1,
                  kappa = 1, epsilon = 1)
lower_bounds <- c(alpha = -10, beta = -10, gamma = -10, theta = -10,
                  tau = -10, kappa = -10, epsilon = -10)
upper_bounds <- c(alpha = 10, beta = 10, gamma = 10, theta = 10,
                  tau = 10, kappa = 10, epsilon = 1000)

# Fit the Non-Linear Model using the Levenberg-Marquardt (LM) Method ----
model <- nlsLM(mal ~ (alpha * (r ^ -1.0) - beta * ((sin(cw / tw)) * (ce)) +
                        gamma * (qs_stddev) + theta * (qd) ^ -1.0 +
                        tau * ((sin(qs / ts)) - qd) -
                        kappa * (tal ^ -1) + epsilon),
               data = train,
               start = start_vector,
               lower = lower_bounds,
               upper = upper_bounds)

# View the Summary of the Model Fit (the parameters) ----
summary(model)

# Plot the Residuals ----
plot(residuals(model), type = "p",
     main = "Residuals of the Model",
     xlab = "Fitted Values", ylab = "Residuals")
abline(h = 1, col = "red")


# Print the Evaluation Metrics ----
# Notes on R_Squared in Engineering, Physics, and Economics
# A “good” R_Squared value depends heavily on the context of the research,
# the domain, and the specific application. In fields where data can be highly
# controlled and variables are well-understood, such as physics or engineering,
# a high R_Squared value close to 1 might be expected for a good model.

# In contrast, in fields dealing with complex systems or human behaviour, such
# as social sciences or economics, a lower R_Squared might still be considered
# acceptable. In these fields, phenomena are influenced by many factors, some of
# which are difficult to measure or include in the model, leading to lower
# R_Squared values.

# General guidelines:
## •	R_Squared > 0.9: The model explains most of the variability of the response
#     data around its mean, which is typically considered excellent in many
#     applications.
## •	0.7 ≤ R_Squared ≤ 0.9: The model explains a substantial amount of
#     variability, considered good in many fields.
## •	0.5 < R_Squared ≤0.7: The model explains a moderate amount of variability,
#     which can be acceptable depending on the domain.
## •	R_Squared ≤0.5: The model does not explain much variability in the
#     response; its predictive capability can be considered weak.

# However, a model can have a high R_Squared value but might still fail at
# predictive tasks, especially if it is overfitting the training data.
# Conversely, a model with a lower R_Squared value might be more generalizable
# or useful in practice.

predictions <- predict(model, test[, -10])

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

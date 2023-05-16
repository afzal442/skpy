# sktime interface entities

Sktime is a Python library that specializes in time series analysis and forecasting. It provides a wide range of tools and functionalities for working with time series data. One of the key components of sktime is its collection of time series estimators.

In sktime, an estimator is an object that is capable of learning from data and making predictions. Estimators in sktime are specifically designed for time series data, taking into account the temporal dependencies and patterns present in the data.

Sktime provides various types of estimators, including both traditional machine learning algorithms adapted for time series and specialized algorithms designed specifically for time series analysis

Sktime estimators follow the scikit-learn API, which means they have a consistent interface and can be used interchangeably with other scikit-learn-compatible estimators. This makes it easy to incorporate sktime estimators into existing machine learning pipelines and workflows.

To use a sktime estimator, you typically create an instance of the estimator class, fit it to your training data, and then use it to make predictions on new, unseen data. Sktime also provides utilities for data preprocessing, feature extraction, and evaluation of time series models.

Here are some practical examples of using sktime estimators with Python code:

```python
from sktime.datasets import load_airline
from sktime.forecasting.arima import ARIMA
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Load the airline passenger dataset
y = load_airline()

# Create an ARIMA model for time series forecasting
arima = ARIMA(order=(1, 1, 1))

# Split the data into training and testing sets
train_size = int(len(y) * 0.8)
train, test = y[:train_size], y[train_size:]

# Fit the ARIMA model to the training data
arima.fit(train)

# Predict the future values
y_pred = arima.predict(fh=[len(test)])

# Calculate the root mean squared error (RMSE)
rmse = mean_squared_error(test, y_pred, squared=False)
print("RMSE:", rmse)

# Plot the actual values and the predictions
plt.plot(range(len(y)), y, label="Actual")
plt.plot(range(train_size, len(y)), y_pred, label="Predicted")
plt.legend()
plt.show()
```
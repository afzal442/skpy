# Here's an example of how you can use the get_params and set_params methods in sktime:

from sktime.datasets import load_airline
from sktime.datasets import load_basic_motions
from sktime.classification.distance_based import KNeighborsTimeSeriesClassifier
from sktime.forecasting.arima import AutoARIMA

# load the airline dataset
y = load_airline()

# create an instance of AutoARIMA with default parameters
arima = AutoARIMA()

# get the current parameter values
params = arima.get_params()
print(params)
# output: {'d': None, 'error_action': 'warn', 'max_order': 5, 'max_p': 5, 'max_q': 5, 'method': 'lbfgs', 'out_of_sample_size': 0, 'scoring': 'mse', 'scoring_args': None, 'seasonal': True, 'solver': 'lbfgs', 'start_order': None, 'suppress_warnings': False, 'trend': None, 'with_intercept': True}

# change a parameter value
arima.set_params(max_order=3)

# confirm the parameter change
params = arima.get_params()
print(params)
# output: {'d': None, 'error_action': 'warn', 'max_order': 3, 'max_p': 5, 'max_q': 5, 'method': 'lbfgs', 'out_of_sample_size': 0, 'scoring': 'mse', 'scoring_args': None, 'seasonal': True, 'solver': 'lbfgs', 'start_order': None, 'suppress_warnings': False, 'trend': None, 'with_intercept': True}

# Load the basic motions dataset
X, y = load_basic_motions(return_X_y=True)

# Create a KNN classifier for time series classification
knn = KNeighborsTimeSeriesClassifier(n_neighbors=3, metric="dtw")

# Get the current parameters of the KNN classifier
params = knn.get_params()
print("Current parameters:", params)

# Update the number of neighbors using set_params
knn.set_params(n_neighbors=5)

# Get the updated parameters
updated_params = knn.get_params()
print("Updated parameters:", updated_params)

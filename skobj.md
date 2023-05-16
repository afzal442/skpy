Objects: In sktime, an "object" refers to an instance of an estimator or any other class within the library. For example, when you create a KNeighborsTimeSeriesClassifier or ARIMA model in sktime, you are creating objects of these respective classes.

Constructor: The constructor is a special method that is called when creating a new object. In sktime, the constructor is responsible for initializing the object and setting its initial state. For instance, when you create a KNeighborsTimeSeriesClassifier, you use its constructor to set parameters such as the number of neighbors.

get_params/set_params: These methods are commonly used in sktime (and scikit-learn in general) to get and set the parameters of an estimator. The get_params method returns a dictionary of the estimator's parameters and their current values, while set_params allows you to update the parameters of an estimator. This is useful for inspecting or modifying the configuration of an estimator.

Tags: Tags in sktime refer to labels or metadata associated with an estimator. They provide additional information about the estimator's characteristics or behavior. For example, an estimator might be tagged as supporting "univariate" or "multivariate" time series, or it might be tagged as suitable for "classification" or "forecasting" tasks. Tags can be used to filter and select specific estimators based on their capabilities.

Configs: Configs in sktime refer to the configuration options or settings that can be used to customize the behavior of an estimator. These options can control various aspects of the estimator, such as the algorithm used, the hyperparameters, or preprocessing steps. Configurations allow you to fine-tune the behavior of an estimator according to your specific needs.

repr: In Python, the repr method is used to define a string representation of an object. In sktime, many estimators have a well-defined repr method that provides a concise and informative string representation of the estimator's configuration. This is useful for displaying the estimator's settings in a human-readable format.

Pretty-printing: Pretty-printing refers to the process of formatting complex data structures, such as objects or dictionaries, in a visually appealing and easy-to-read manner. Sktime provides utilities for pretty-printing its objects, including estimators, which helps in understanding their structure and configuration when working with large or complex models.

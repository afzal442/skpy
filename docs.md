Time Series Classification: Let's say you have a dataset of wearable sensor data collected from individuals performing different physical activities (e.g., walking, running, sitting). You can use sktime's k-nearest neighbors (KNN) classifier, specifically designed for time series, to classify the activities based on the sensor readings.

Time Series Regression: Suppose you have historical sales data for a product and want to forecast future sales. You can use sktime's autoregressive integrated moving average (ARIMA) model to capture the temporal dependencies and predict the future sales figures.

Time Series Forecasting: Imagine you have a dataset containing historical stock prices and you want to predict future price movements. Sktime offers various forecasting algorithms, such as exponential smoothing (ETS) or seasonal decomposition of time series (STL), which can help you generate accurate predictions.

Anomaly Detection: Consider a scenario where you have sensor data from a manufacturing process, and you want to identify anomalous patterns that could indicate equipment malfunction. Sktime provides outlier detection methods, such as time series forest (TSF), which can help you detect abnormal time series patterns in real-time.

Time Series Clustering: Let's say you have a dataset of multivariate time series representing the electrical power consumption of different households. You can use sktime's clustering algorithms, like k-means for time series (KMeansTimeSeries) or time series k-Shape (KShape), to group similar households based on their consumption patterns.

These are just a few examples of the practical applications of sktime estimators. Sktime's extensive library provides a wide range of estimators and tools for various time series analysis tasks, enabling you to explore and analyze your time-dependent data effectively.

### Let's go through each point and explain them in the context of sktime:

Estimators: In sktime, an "estimator" refers to a specific algorithm or model used for time series analysis or forecasting. It is an object that implements the learning algorithm and is capable of fitting itself to the data and making predictions. Sktime provides a wide range of estimators, including classifiers, regressors, and forecasters, each tailored to specific time series tasks.

Fitting and is_fitted: Fitting an estimator refers to the process of training the model using the available data. In sktime, you can fit an estimator to your training data using the fit method. For example, you can fit a KNeighborsTimeSeriesClassifier to a set of labeled time series to train it on the provided data.

The is_fitted method in sktime is used to check if an estimator has been fitted or trained. It returns a boolean value indicating whether the estimator has been fitted to data or not. This can be useful to verify if an estimator has been trained before making predictions.

get_fitted_params: The get_fitted_params method in sktime allows you to retrieve the parameters or attributes of an estimator after it has been fitted to data. It returns a dictionary of the fitted parameters or attributes, providing insights into the learned model's internal state. This can be helpful for inspecting the learned model and extracting useful information.

Show atomic, composition simple, composition pipeline: Sktime supports different ways of constructing models and pipelines for time series analysis.

Atomic Estimators: Atomic estimators in sktime are standalone models that can be used individually. For example, you can use a KNeighborsTimeSeriesClassifier as a standalone model without any composition or combination with other estimators.

Composition (Simple): Composition in sktime refers to combining multiple estimators in a simple manner, such as stacking or ensembling. For example, you can create an ensemble of multiple KNeighborsTimeSeriesClassifier models using sktime's composition methods.

Composition (Pipeline): Composition pipelines in sktime allow you to chain multiple processing steps, such as feature extraction and model fitting, into a single pipeline. This enables a streamlined workflow for time series analysis. For instance, you can create a pipeline that applies feature extraction techniques, followed by a KNeighborsTimeSeriesClassifier to classify time series.

By leveraging these different composition methods, sktime provides flexibility and modularity in constructing time series models and pipelines, allowing you to build complex analysis workflows while keeping the code clean and organized.
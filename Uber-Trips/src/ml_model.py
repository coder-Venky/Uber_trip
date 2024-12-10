import math
from statistics import mean
import random

class SimpleFarePredictionModel:
    def __init__(self):
        self.coefficients = None
    
    def prepare_features(self, features):
        """Convert feature dictionary to list of lists."""
        X = [[
            f['hour'],
            f['day_of_week'],
            f['month'],
            f['is_weekend'],
            f['distance']
        ] for f in features]
        
        y = [f['fare'] for f in features]
        return X, y
    
    def split_data(self, X, y, test_size=0.2):
        """Simple train-test split."""
        data = list(zip(X, y))
        random.shuffle(data)
        split_idx = int(len(data) * (1 - test_size))
        train_data = data[:split_idx]
        test_data = data[split_idx:]
        
        X_train, y_train = zip(*train_data)
        X_test, y_test = zip(*test_data)
        return list(X_train), list(X_test), list(y_train), list(y_test)
    
    def train(self, features):
        """Train a simple linear regression model."""
        X, y = self.prepare_features(features)
        X_train, X_test, y_train, y_test = self.split_data(X, y)
        
        # Calculate average fare per mile
        distances = [x[4] for x in X_train]  # distance is the 5th feature
        fares = y_train
        self.coefficients = sum(fares) / sum(distances)
        
        # Evaluate model
        y_pred = [self.predict_single(x) for x in X_test]
        mse = sum((pred - actual) ** 2 for pred, actual in zip(y_pred, y_test)) / len(y_test)
        
        # Calculate R² score
        y_mean = mean(y_test)
        ss_tot = sum((y - y_mean) ** 2 for y in y_test)
        ss_res = sum((y_pred - y_test) ** 2 for y_pred, y_test in zip(y_pred, y_test))
        r2 = 1 - (ss_res / ss_tot if ss_tot != 0 else 0)
        
        return {
            'mse': mse,
            'rmse': math.sqrt(mse),
            'r2_score': r2
        }
    
    def predict_single(self, features):
        """Predict fare based on distance and average fare per mile."""
        return features[4] * self.coefficients  # distance * fare_per_mile
    
    def predict(self, feature):
        """Predict fare for a single trip."""
        features = [
            feature['hour'],
            feature['day_of_week'],
            feature['month'],
            feature['is_weekend'],
            feature['distance']
        ]
        return self.predict_single(features)
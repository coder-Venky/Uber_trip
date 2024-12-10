from datetime import datetime

def extract_time_features(trips):
    """Extract time-based features from trip data."""
    features = []
    for trip in trips:
        pickup_time = trip['pickup_datetime']
        feature = {
            'hour': pickup_time.hour,
            'day_of_week': pickup_time.weekday(),
            'month': pickup_time.month,
            'is_weekend': 1 if pickup_time.weekday() >= 5 else 0,
            'distance': trip['distance'],
            'fare': trip['fare']
        }
        features.append(feature)
    return features

def calculate_trip_duration(trip):
    """Calculate trip duration in minutes."""
    duration = trip['dropoff_datetime'] - trip['pickup_datetime']
    return duration.total_seconds() / 60

def normalize_features(features):
    """Normalize numerical features to [0,1] range."""
    normalized = []
    max_vals = {
        'distance': max(f['distance'] for f in features),
        'fare': max(f['fare'] for f in features)
    }
    
    for feature in features:
        normalized_feature = feature.copy()
        normalized_feature['distance'] = feature['distance'] / max_vals['distance']
        normalized_feature['fare'] = feature['fare'] / max_vals['fare']
        normalized.append(normalized_feature)
    
    return normalized
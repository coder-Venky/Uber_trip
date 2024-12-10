from data_loader import load_uber_data
from data_preprocessor import extract_time_features, normalize_features
from analysis import calculate_basic_stats, analyze_peak_hours, analyze_weekday_patterns
from ml_model import SimpleFarePredictionModel

def main():
    # Load data
    print("Loading Uber trip data...")
    trips = load_uber_data('uber_trips.csv')
    
    if not trips:
        print("Failed to load data. Exiting...")
        return
    
    # Basic analysis
    print("\nCalculating basic statistics...")
    stats = calculate_basic_stats(trips)
    print(f"Total trips: {stats['total_trips']}")
    print(f"Total revenue: ${stats['total_revenue']}")
    print(f"Average distance: {stats['average_distance']} miles")
    print(f"Average fare: ${stats['average_fare']}")
    
    # Peak hour analysis
    print("\nAnalyzing peak hours...")
    peak_analysis = analyze_peak_hours(trips)
    print(f"Peak hour: {peak_analysis['peak_hour']}:00")
    print(f"Number of trips during peak hour: {peak_analysis['trips_at_peak']}")
    
    # Weekday pattern analysis
    print("\nAnalyzing weekday patterns...")
    weekday_analysis = analyze_weekday_patterns(trips)
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    for day, trips_count, revenue in zip(days, 
                                       weekday_analysis['trips_by_day'],
                                       weekday_analysis['revenue_by_day']):
        print(f"{day}: {trips_count} trips, ${revenue} revenue")
    
    # Simple Machine Learning
    print("\nTraining simple fare prediction model...")
    features = extract_time_features(trips)
    normalized_features = normalize_features(features)
    
    model = SimpleFarePredictionModel()
    metrics = model.train(normalized_features)
    
    print("\nModel Performance:")
    print(f"Root Mean Square Error: ${metrics['rmse']:.2f}")
    print(f"R² Score: {metrics['r2_score']:.3f}")
    
    # Example prediction
    sample_feature = {
        'hour': 14,
        'day_of_week': 2,
        'month': 6,
        'is_weekend': 0,
        'distance': 5.0
    }
    
    predicted_fare = model.predict(sample_feature)
    print(f"\nSample Prediction:")
    print(f"Predicted fare for a {sample_feature['distance']} mile trip: ${predicted_fare:.2f}")

if __name__ == "__main__":
    main()
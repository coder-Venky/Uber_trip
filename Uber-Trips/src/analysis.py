def calculate_basic_stats(trips):
    """Calculate basic statistics from trip data."""
    total_trips = len(trips)
    total_revenue = sum(trip['fare'] for trip in trips)
    avg_distance = sum(trip['distance'] for trip in trips) / total_trips
    
    stats = {
        'total_trips': total_trips,
        'total_revenue': round(total_revenue, 2),
        'average_distance': round(avg_distance, 2),
        'average_fare': round(total_revenue / total_trips, 2)
    }
    
    return stats

def analyze_peak_hours(trips):
    """Analyze peak hours based on trip frequency."""
    hour_counts = [0] * 24
    for trip in trips:
        hour = trip['pickup_datetime'].hour
        hour_counts[hour] += 1
    
    peak_hour = hour_counts.index(max(hour_counts))
    return {
        'peak_hour': peak_hour,
        'trips_at_peak': hour_counts[peak_hour],
        'hourly_distribution': hour_counts
    }

def analyze_weekday_patterns(trips):
    """Analyze trip patterns by day of the week."""
    weekday_counts = [0] * 7
    weekday_revenue = [0] * 7
    
    for trip in trips:
        day = trip['pickup_datetime'].weekday()
        weekday_counts[day] += 1
        weekday_revenue[day] += trip['fare']
    
    return {
        'trips_by_day': weekday_counts,
        'revenue_by_day': [round(rev, 2) for rev in weekday_revenue]
    }
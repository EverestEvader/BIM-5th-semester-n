class Time:
    def __init__(self, hours, minutes, seconds):
        """Initialize Time object with hours, minutes and seconds"""
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self._normalize()
    
    def _normalize(self):
        """Convert excess seconds to minutes and excess minutes to hours"""
        # Convert excess seconds to minutes
        extra_minutes, self.seconds = divmod(self.seconds, 60)
        self.minutes += extra_minutes
        
        # Convert excess minutes to hours
        extra_hours, self.minutes = divmod(self.minutes, 60)
        self.hours += extra_hours
    
    def __add__(self, other):
        """Overload the + operator to add two Time objects"""
        if not isinstance(other, Time):
            raise TypeError("Can only add Time object to another Time object")
            
        total_seconds = (
            (self.hours + other.hours) * 3600 +
            (self.minutes + other.minutes) * 60 +
            (self.seconds + other.seconds)
        )
        
        # Convert total seconds back to hours, minutes, seconds
        hours, remainder = divmod(total_seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        return Time(hours, minutes, seconds)
    
    def __str__(self):
        """Return string representation of Time object"""
        return f"{int(self.hours)}:{int(self.minutes):02d}:{int(self.seconds):02d}"

# Example usage
if __name__ == "__main__":
    # Create two time objects
    time1 = Time(1, 20, 40)
    time2 = Time(2, 50, 30)
    
    # Add them using the overloaded + operator
    time3 = time1 + time2
    
    # Display results
    print(f"Time 1: {time1}")
    print(f"Time 2: {time2}")
    print(f"Sum   : {time3}")

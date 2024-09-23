'''One cause for speeding is the desire to shorten the time spent traveling. Create a program
 that calculates the amount of time saved if you are traveling with an average speed that is 
 above the speed-limit as compared to traveling with an average speed exactly at the speed-limit.
 As the user for the average speed in miles per hour, speed limit in miles per hour and 
 distance travelled in miles. THE TIME SAVED SHOULD BE REPORTED IN MINUTES. Create a screenshot
 of output where your average speed is 80 mph, speed limit is 60 mph and distance travelled is 
 100 miles. Your answer should indicate that you saved 25 minutes, '''

#Ask user for average speed, speed limit, and distance traveled
average_speed = float(input("What is your average speed in miles per hour? "))
speed_limit = float(input("What is the speed limit in miles per hour? "))
distance_traveled = float(input("How many miles were driven? "))

# Find how long it takes when driving the speed limit
speedlimit_time = distance_traveled / speed_limit

# If driving faster than the speed limit: calculate how long it takes, and the amount of time saved
if average_speed > speed_limit: 
    speeding_time = distance_traveled / average_speed
    time_saved = int((speedlimit_time - speeding_time) * 60)
    print(f'You saved {time_saved} minutes.')

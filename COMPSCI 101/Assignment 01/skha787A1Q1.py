"""
Sabaoon Raza Khan - skha787
ID Number: 983957824

Calculates the elapsed time (in hours, minutes and seconds), given a start and end time.
"""

start = "06:55:55"
end = "07:04:57"

#Converts start time into seconds
start_hours_in_seconds = int(start[0:2]) * 3600 
start_minutes_in_seconds = int(start[3:5]) * 60
start_seconds = int(start[6:8]) 

#Converts end time into seconds
end_hours_in_seconds = int(end[0:2]) * 3600
end_minutes_in_seconds = int(end[3:5]) * 60
end_seconds = int(end[6:8])

start_time = int(start_hours_in_seconds) + int(start_minutes_in_seconds) + int(start_seconds)
end_time = int(end_hours_in_seconds) + int(end_minutes_in_seconds) + int(end_seconds)

elapsed_time_in_seconds = end_time - start_time #Elapsed time in seconds
elapsed_time_in_hours = elapsed_time_in_seconds / 3600 #Elapsed time in hours

elapsed_hours = int(elapsed_time_in_hours // 1) #Elapsed hours value

minutes = (float(elapsed_time_in_hours) - float(elapsed_hours)) * 60
elapsed_minutes = int(minutes // 1) #Elapsed minutes value

elapsed_seconds = round((minutes - elapsed_minutes) * 60) #Elapsed seconds value

#Converting time units into strings
elapsed_hours = str(elapsed_hours)
elapsed_minutes = str(elapsed_minutes)
elapsed_seconds = str(elapsed_seconds)

#Adding a "0" before the time units
elapsed_hours = "0" * (2 - len(elapsed_hours)) + elapsed_hours
elapsed_minutes = "0" * (2 - len(elapsed_minutes)) + elapsed_minutes
elapsed_seconds = "0" * (2 - len(elapsed_seconds)) + elapsed_seconds

print("Start time: ", start, "  End time: ", end)
print("Total time elapsed:  ", elapsed_hours, ":", elapsed_minutes, ":", elapsed_seconds, sep = "")


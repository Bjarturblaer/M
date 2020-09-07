#project Voyager 1
daysafter = int(input("Number of days after 9/25/09: "))
#miles
miles_hour = 38241
distance_miles = 16637000000
distance_miles_from_sun = distance_miles+(daysafter*(miles_hour*24))

#km
distance_km_from_sun = distance_miles_from_sun*1.609344
rounded_km = round(distance_km_from_sun)

#AU
distance_au_from_sun = distance_miles_from_sun/92955887.6
rounded_au = round(distance_au_from_sun)

print("Miles from the sun:",(distance_miles_from_sun))
print("Kilometers from the sun:",(rounded_km))
print("AU from the sun:",(rounded_au))







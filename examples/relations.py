import db, assign_values
from User import User
from Country import Country

# Create a country
country = Country()
country.__primary__ = 'Canada'
country.save()

# Get user object.
user = User('alex')

# Create a relation in user.
user.has_relation('visited_countries', 'countries')

# Assign a country to user.
user.visited_countries.append(country.__primary__)
user.save()
print "User visited countries: ", user.visited_countries

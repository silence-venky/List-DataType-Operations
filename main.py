#Create a new list containing the names of 5 different cities
cities = ["New York", "London", "Tokyo", "Paris", "Sydney"]
#Use indexing to access and print the name of the city at the middle index of the list
print(cities[len(cities) // 2])
#Use slicing to extract a subset of cities from the list (e.g., the first 3 cities) and print the result
print(cities[:3])
#Sort the list of cities in ascending order and print the result
cities.sort()
print(cities)
#Append a new city to the end of the list and print the updated list
cities.append("Berlin")
print(cities)
#Remove the first city from the list and print the updated list
cities.pop(0)
print(cities)
#Write a function that takes a list of cities as input and returns the length of the list
def get_city_count(city_list):
    return len(city_list)

print(get_city_count(cities))
#Test the function with the list of cities created in the first task and print the result
print(get_city_count(["New York", "London", "Tokyo", "Paris", "Sydney"]))

import random


#1

'''cities list'''
cities: list[str] =  [ "Tokyo", "New York", "Paris", "London", "Sydney", "Dubai", "Shanghai"]

'''sort by city name length'''
print(sorted(cities, key=lambda city: len(city)))

'''sort by number of words in city words'''
print(sorted(cities, key=lambda city: len(city.split())))

'''by city last letter in name'''
print(sorted(cities, key=lambda city: city[-1]))

'''opposit reading'''
print(sorted(cities, key=lambda city: city[::-1]))

'''letter a appeard'''
print(sorted(cities, key=lambda city: city.lower().count('a')))


# list of cities with distance and continents
cities_with_data = [
    ["Tokyo", 5760, "Asia"],
    ["New York", 5690, "North America"],
    ["Paris", 2050, "Europe"],
    ["London", 2240, "Europe"],
    ["Sydney", 8780, "Australia"],
    ["Dubai", 1300, "Asia"],
    ["Shanghai", 4920, "Asia"]]

'''sort by distanse to israel'''
print(sorted(cities_with_data, key=lambda city: city[1]))

'''sprt from shortest lo longer distance to israel'''
print(sorted(cities_with_data, key=lambda city: city[1], reverse=True))

'''sort by continent name'''
print(sorted(cities_with_data, key=lambda city: city[2]))

'''sort by continent name and then by distance'''
print(sorted(cities_with_data, key=lambda city: (city[2], city[1])))










#2 list of 50 random numbers
numbers = [random.randint(1, 100) for _ in range(50)]

'''sort by rise'''
print(sorted(numbers))

'''sory by average distance'''
average = sum(numbers) / len(numbers)
print(sorted(numbers, key=lambda x: abs(x - average)))


#3 verbal

''' טקסט נתון'''
text = """This chocolate cake is rich, moist, and full of delicious chocolate flavor.
To make the cake, you will need chocolate, flour, sugar, eggs, and butter.
After baking the chocolate cake, let the cake cool before adding the chocolate frosting."""

# a.
'''word count'''
words = text.lower().replace('.', '').replace(',', '').split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word, 0) + 1
print(word_count)
most_common_word = max(word_count, key=word_count.get)
print(f"The most common word is '{most_common_word}' with {word_count[most_common_word]} occurrences.")

# b.
'''letter count'''
letter_count = {}
for letter in text.lower():
    if letter.isalpha():
        letter_count[letter] = letter_count.get(letter, 0) + 1
print(letter_count)
least_common_letter = min(letter_count, key=letter_count.get)
print(f"The least common letter is '{least_common_letter}' with {letter_count[least_common_letter]} occurrences.")

#4 numeric dictionary
'''creating a dictionary for number between 1- 20 that are powered bi 3'''
cube_dict = {num: num**3 for num in range(1, 21)}
print(cube_dict)

'''input number from the user'''
user_input = int(input("Enter a number: "))
if user_input in cube_dict:
    print(f"The cube of {user_input} is {cube_dict[user_input]}")
else:
    print("Not exist")







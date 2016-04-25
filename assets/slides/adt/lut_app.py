from lut import *

phone_book_data = [
    ("Christine Strauch", "510-842-9235"),
    ("Frances Catal Buloan", "932-567-3241"),
    ("Jack Chow", "617-547-0923"),
    ("Joy De Rosario", "310-912-6483"),
    ("Casey Casem", "415-432-9292"),
    ("Lydia Lu", "707-341-1254")]

print("Phone book")
phone_book = lut_with_bindings(phone_book_data)
lut_print(phone_book)

print("Jack Chows's Number: ", lut_get(phone_book, "Jack Chow"))

print("Area codes")
area_codes = lut_map_values(phone_book, lambda x:x[0:3])
lut_print(area_codes)

new_phone_book = lut_update(phone_book, "Jack Chow", "805-962-0936")
print("Jack change: ", lut_get(phone_book, "Jack Chow"), lut_get(new_phone_book, "Jack Chow"))

print("Sort by number")
print(lut_sorted(new_phone_book, lambda k,v:v))

print("Fuzzy get")
def name_dist(name1, name2):
    count = max(len(name1),len(name2)) - min(len(name1),len(name2))
    for i in range(min(len(name1), len(name2))):
        if (name1[i] != name2[i]):
            count += 1 
    return count

print("Jack's Number: ", lut_fuzzy_get(phone_book, "Jack", name_dist))

friend_data = [
    ("Christine Strauch", "Jack Chow"),
    ("Christine Strauch", "Lydia Lu"),
    ("Jack Chow", "Christine Strauch"),
    ("Casey Casem", "Christine Strauch"),
    ("Casey Casem", "Jack Chow"),
    ("Casey Casem", "Frances Catal Buloan"),
    ("Casey Casem", "Joy De Rosario"),
    ("Casey Casem", "Casey Casem"),
    ("Frances Catal Buloan", "Jack Chow"),
    ("Jack Chow", "Frances Catal Buloan"),
    ("Joy De Rosario", "Lydia Lu"),
    ("Joy De Lydia", "Jack Chow")
    ]

def make_friends(friends):
    friend_lut = lut()
    for (friender, friendee) in friends:
        old_friends = lut_get(friend_lut, friender)
        new_friends = old_friends + [friendee] if old_friends is not None else [friendee]
        friend_lut = lut_update(friend_lut, friender, new_friends)
    return friend_lut

friends = make_friends(friend_data)
lut_print(friends)

def friend_phones(person, phone_lut, friend_lut):
    return [(friend, lut_get(phone_lut, friend)) for friend in lut_get(friend_lut, person)]

print(friend_phones("Casey Casem", phone_book, friends))



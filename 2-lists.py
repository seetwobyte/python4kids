# list use [] like a Box


grocery_list = ["juice", "tomatoes", "potatoes", "bananas"]

print("first Item", grocery_list[0])


grocery_list[0] = "green juice"

print("first item",grocery_list[0])

# pick items in the list #


# combine the list  #


other_events = ["cut lawn ", "pick up kids", "car wash"]

to_do_list = [other_events, grocery_list]

print(to_do_list)


print((to_do_list[1][2]))

# add to the list s=using the .append comand #


grocery_list.append("lemons")
print(to_do_list)

grocery_list.insert(1, "pickle")
print(to_do_list)


grocery_list.sort()
grocery_list.reverse()
del grocery_list[4]
print(to_do_list)

print(len(to_do_list))
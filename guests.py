guests = ["Robert", "Anna", "Sofia", "Joe"]

print(guests)
print()
print(f"{guests[0]}, you are invited for dinner")
print(f"{guests[1]}, you are invited for dinner")
print(f"{guests[2]}, you are invited for dinner")
print(f"{guests[3]}, you are invited for dinner")
print()

guests[1] = "Tom"
print()

guests.insert(0, "Tim")
guests.insert(2, "Zoe")
guests.append("Luna")

cancelled_guest = guests.pop()
print(f"Sorry {cancelled_guest}, no place for you")

cancelled_guest = guests.pop()
print(f"Sorry {cancelled_guest}, no place for you")

cancelled_guest = guests.pop()
print(f"Sorry {cancelled_guest}, no place for you")

cancelled_guest = guests.pop()
print(f"Sorry {cancelled_guest}, no place for you")

cancelled_guest = guests.pop()
print(f"Sorry {cancelled_guest}, no place for you")

del guests[0]
del guests[0]

print(guests)



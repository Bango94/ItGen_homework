floors = 9
entrances = 4
flats: int = 4
flat = int(input("flat number="))

entr = (flat - 1) // (floors * flats) + 1
floor = (flat - 1) // flats - (entr - 1) * floors + 1
floor_number = (flat - 1) % flats + 1


print((1 <= flat <=flats * floors * entrances) and (flat,entr,floor, floor_number) or "error")
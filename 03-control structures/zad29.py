washing_product = str(input("What u washin?"))
rinse = True
spin = False

if washing_product == "jacket":
    washing_time = 40
elif washing_product == "underwear":
    washing_time = 70
elif washing_product == "shoes":
    washing_time = 20
else:
    print("Invalid washing product")

if rinse:
    washing_time += 15

if spin:
    washing_time += 9

print("Total washing time:", washing_time, "minutes")
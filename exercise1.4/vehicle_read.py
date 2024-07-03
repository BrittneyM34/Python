import pickle

with open('vehicledetail.bin', 'rb') as my_file:
    vehicle = pickle.load(my_file)

print("Vehicle details - ")
print("Name: " + vehicle['brand'] + " " + vehicle['model'])
print("Color: " +vehicle['color'])
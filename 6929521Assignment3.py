#https://github.com/Eronasey/Data-Structures..git
# list of available cars with their corresponding prices 
cars= {
"Tesla" :900000,
"Toyota Camry" :40000,
"Toyota Rav4" :50000,
"Toyota Corolla" :5500,
"SUV" :80000,
"Grand Tourer" :75000,
"Mercedes Benz":95000,
"Honda Civic":80080,
"Bentley":90000,
"Ferrari":100000,
"Lamborghini":150000,
"Alfa Romeo":80000,
"Chevrolet Corvette":115000,
"Lincoln":90000,
"Bugatti Veyron":400000,
"Jaguar":500000,
"BMW":185000,
"Porsche":320000,
"Hyundai Venue":195000,
"Hyundai SantaFe":100000,
"Ford Mustang":600000,
"Jeep":445000,
"Volvo":508000,
"Cadillac":87000,
"Ford Explorer":780000,
"Kia Sonet":800000,
"Maruti Baleno":700090,
"Honda City":678900,
"Pagani Huayra":900000,
"Rimac Nevera":1000000
}
#get user input for car name
carName=input("Enter carName:")
if carName in cars:
    print("available")
    #if carName is availble, get its price
    carPrice= cars[carName]
    print(f"The price of {carName} is ${carPrice}.")
else:
    print(f"sorry, {carName} is not availabe.")
    
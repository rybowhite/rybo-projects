##currently only doing kg/lbs and lbs/kg conversions, but can easily be expanded to include more units
kg_weight = float(input("Enter weight in kg: "))
lbs_weight = float(input("Enter weight in lbs: ")) 
conversion = input("Enter the conversion you want to perform 1/2(kg to lbs, lbs to kg): ")
if conversion == "1":
    result = round(kg_weight * 2.20462, 2)
elif conversion == "2":    
    result = round(lbs_weight / 2.20462, 2)
else:    print("Invalid conversion")
print(f"The result is: {result}")
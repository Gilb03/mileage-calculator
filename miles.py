print("How many kilometers did you drive today?")
kms = input()
miles = float(kms)/1.60934
miles = round(miles, 2)
print(f"Your {kms} km ride is equal to {miles} miles")


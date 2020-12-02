bill = input("How high is your bill? ")
bill = bill.replace("$","")
bill = float(bill)

tip10 = bill * 0.1
tip15 = bill * 0.15
tip20 = bill * 0.2

print(f"Tip 10% and give ${round(bill + tip10)} which includes a tip of ${round(tip10)}.")
print(f"Tip 15% and give ${bill + tip15} which includes a tip of ${tip15}.")
print(f"Tip 20% and give ${bill + tip20} which includes a tip of ${tip20}.")

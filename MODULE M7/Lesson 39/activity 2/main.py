weight = 45
height = 1.5

bmi = weight / (height * height)

print("BMI is", bmi)

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
else:
    print("Overweight")

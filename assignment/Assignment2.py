gravity_earth = 9.81
gravity_moon = 1.62

mass = float(input("Enter the value of the mass in kg:"))

weight_earth = mass * gravity_earth
weight_moon = mass * gravity_moon

print(f"The weight on Earth is {weight_earth:.2f} N")
print(f"The weight on Moon js {weight_moon:.2f}")
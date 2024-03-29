"""
Python: Calculate your Body Mass Index (BMI)

Note:
    1. if name in ['a', 'b', 'c']:
    2. round(x, ndigits)
    3. def: return
"""
def standard(BMI):
    if BMI <= 18.5:
        return 'Underweight'
    elif 18.5 < BMI <= 25:
        return 'Normal weight'
    elif 25 < BMI <= 29.9:
        return 'Overweight'
    else:
        return 'Obesity'

while True:
    system = input('Do you use metric (cm/kg) or imperial(in/lbs) measures? ')
    if system in ['imperial', 'in', 'inch', 'lbs']:      
        height = input('Your height(inch): ')
        weight = input('Your weight(lbs): ')
        BMI_fl = float(weight) * 703 / float(height) ** 2
        BMI = round(BMI_fl, 2)
        print('Your BMI is', BMI, ':', standard(BMI))
        break
    elif system in ['metric', 'cm', 'm', 'kg', 'g']:
        height = input('Your height(cm): ')
        weight = input('Your weight(kg): ')
        BMI_fl = float(weight) / (float(height) / 100) ** 2
        BMI = round(BMI_fl, 2)
        print('Your BMI is', BMI, ':', standard(BMI))
        break
    else:
        print('Please enter the correct system.')
        continue

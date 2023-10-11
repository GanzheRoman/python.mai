def bmi_info(height, *args):
    bmi = (sum([*args])/len([*args]) / (height**2 / 100)) * 100 
    print(f'Your BMI: {bmi:.1f}')
    if bmi < 18.5:
        print('It can be classificate as Underweight')
        print('Risk for your health is Minimal')
    elif 18.5 <= bmi <= 24.9:
        print('It can be classificate as Normal')
        print('Risk for your health is Minimal')
    elif 25 <= bmi <= 29.9:
        print('It can be classificate as Overweight')
        print('Risk for your health is Increased')
    elif 30 <= bmi <= 34.9:
        print('It can be classificate as Obese')
        print('Risk for your health is High')
    elif 35 <= bmi <= 39.9:
        print('It can be classificate as Severely Obese')
        print('Risk for your health is Very High')
    else:
        print('It can be classificate as Mordibly Obese')
        print('Risk for your health is Extremely High')

bmi_info(155,49,1,20)
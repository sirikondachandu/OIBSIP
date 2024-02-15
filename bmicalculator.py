def calculate_bmi(weight,height):
    bmi=weight/(height*height)
    return bmi
def BMI_Category(bmi):
    if bmi<18.5:
        return "Underweight"
    elif bmi>=18.5 and bmi<24.9:
        return "Normal"
    elif bmi>24.9 and bmi<29.9:
        return "Underweight"
    else:
        return "Obesity"
def main():
    try:
        weight=float(input("Enter your weight in kilograms: "))
        height=float(input("Enter Your height in meters: "))

        if weight <=0 and height<=0:
            print("Invalid input! Weight and height must be greater than Zero.")
        else:
            bmi=calculate_bmi(weight,height)
            category=BMI_Category(bmi)
            print(f"Your BMI is:{bmi:.2f}")
            print("Category:",category)
    except ValueError:
        print("Invalid input! Weight and Height must be numeric values.")
if __name__=="__main__":
    main()


        


















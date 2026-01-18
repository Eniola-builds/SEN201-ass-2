# SEN ASSIGNMENT: Temperature Converter

def main():
    # NOMENCLATURE: 'celsius_input' matches our SDLC Design
    celsius_input = float(input("Enter temperature in Celsius: "))
    
    # Formula: (C * 9/5) + 32
    # NOMENCLATURE: 'fahrenheit_result' matches our SDLC Design
    fahrenheit_result = (celsius_input * 9/5) + 32
    
    print(f"{celsius_input} degrees Celsius is {fahrenheit_result} degrees Fahrenheit.")

if __name__ == "__main__":
    main()
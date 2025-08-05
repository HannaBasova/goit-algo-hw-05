
import re


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями 27.45 і 324.00 доларів."


'''
a function that parses text, identifies all float numbers
 and returns them as a generator.
'''
def generator_numbers(text: str)-> list:
    #looking for all float numbers in text
    matches = re.findall(r'\b\d+[.]\d+\b', text)
    for match in matches:
        yield float(match)


'''
The function which takes a generator as an argument when called
and uses a generator to calculate the total sum of 
numbers  
'''
def sum_profit(text: str, generator_numbers)->float:
    #calculate sum of numbers
    total = 0
    for profit in generator_numbers(text):
        total += profit
    return total



total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")
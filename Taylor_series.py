import math


def convert_degree_to_radiant(degree):
   
   # для того щоб конвертувати кут у градусах у
   # радіани
   # слід скласти пропорцію виду
   # 180  degree 
   #   π  x
   # Виходячи з цього x = (π * degree)/180

   converter = (math.pi * degree) / 180

   return converter 


def sin (degree , n = 20):

  # Для того щоб обрахувати синус чи косинус
  # використовується ряд Тейлора 
  # чи Маклорена

  x = convert_degree_to_radiant(degree)
  
  result = 0
  
  
  for i in range(0, n + 1):
     first_part_of_formula = ((-1)**i) * (x ** 
  ((2 * i) + 1))
    
     second_part_of_formula = math.factorial((2 *     i) + 1)
     
     result  += (first_part_of_formula / 
  second_part_of_formula) 
  
    
  return result  


def cos(degree , n = 30):
   
   x = convert_degree_to_radiant(degree)

   result = 0
  
  
   for i in range(0, n + 1):
     first_part_of_formula = x ** (2 * i)
    
     second_part_of_formula = math.factorial(2 *     i)
     
     result += ((-1) ** i) * (first_part_of_formula / 
  second_part_of_formula) 
  
   return result 
  
  
def exp(x, n = 20):

   # Розрахунок за рядом Тейлора e^x
   
   result = 0
   
   for i in range(0, n):
      
      first_part_of_formula = x ** i
      second_part_of_formula = math.factorial(i)
      
      result += (first_part_of_formula / second_part_of_formula)
   
   return result 



if __name__ == '__main__':
   print(f"convert :  {convert_degree_to_radiant(45)}")
   print()
   print(f"sin : {sin(45)}")
   print()
   print(f"Значення яке видає вбудованна функція синусу : {math.sin(convert_degree_to_radiant(45))}")
   print()
   print(f"cos : {cos(45)}")
   print()
   print(f"Значення яке видає вбудованна функція косинусу : {math.cos(convert_degree_to_radiant(45))}")
   print()
   print(f"exp : {exp(5)}")
   print()
   print(f"Значення яке видає функція ееспоненти у степені  : {math.exp(5)}")

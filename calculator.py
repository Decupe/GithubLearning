count = 0
num_list = []
calculator = ('addition', 'subtraction', 'multiplication', 'division', 'average')
selection = input("Choose an operation: ").lower()

if selection == 'addition':
    nums_to_add = int(input('How many numbers do you want to add?: '))
    while count < nums_to_add:
        num = int(input('Enter a number: '))
        num_list.append(num)
        count += 1
        
    result = num_list[0]
    for n in num_list[1:]:
        result += n
        
    print(f"Result of addition = {result}")


elif selection == 'subtraction':
      nums_to_subtract = int(input('How many numbers do you want to subtract?: '))
      while count < nums_to_subtract:
        num = int(input('Enter a number: '))
        num_list.append(num)
        count += 1        
          

      result = num_list[0]
      for n in num_list[1:]:
        result -= n

      print(f"Result of subtraction = {result}")
import sys

def ordinalify(num, last=None):
    if last is not None and num == last:
        return "last"
    match num:
        case 1:
            return "1st"
        case 2:
            return "2nd"
        case 3:
            return "3rd"
        case _:
            return str(num)+"th"
        

numbers = []
while len(numbers) < 6:
    try:
        numbers.append(int(input(f"Enter the {ordinalify(len(numbers)+1, 6)} number: ")))
    except KeyboardInterrupt:
        print("\nSIGINT termination. Bye.")
        sys.exit(130) # unixy convention for processes terminated by ^C
    except:
        print("Please enter a valid number.")


num_to_find = numbers.pop()
nt = "n't"
print(f'{num_to_find}', f'is{nt if num_to_find not in numbers else ""} in', \
      ",".join([str(n) for n in numbers]))
    

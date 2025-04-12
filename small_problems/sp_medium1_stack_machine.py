
def minilang(program):
    print(program)
    stack = []
    register = 0
    instructions = program.split()
    for instruction in instructions:
        match instruction:
            case 'PRINT':
                print(register)
            case 'PUSH':
                stack.append(register)
            case 'POP':
                register = stack.pop()
            case 'ADD':
                register = register + stack.pop()
            case 'SUB':
                register = register - stack.pop()
            case 'MULT':
                register = register * stack.pop()
            case 'DIV':
                register = register // stack.pop()
            case 'REMAINDER':
                register = register % stack.pop()
            #case _ if instruction.isdigit():
            case _:
                register = int(instruction)
            #case _:
            #    print("ERROR: Unrecognized instruction: ", instruction)


minilang('PRINT')
# 0

minilang('5 PUSH 3 MULT PRINT')
# 15

minilang('5 PRINT PUSH 3 PRINT ADD PRINT')
# 5
# 3
# 8

minilang('5 PUSH POP PRINT')
# 5

minilang('3 PUSH 4 PUSH 5 PUSH PRINT ADD PRINT POP PRINT ADD PRINT')
# 5
# 10
# 4
# 7

minilang('3 PUSH PUSH 7 DIV MULT PRINT')
# 6

minilang('4 PUSH PUSH 7 REMAINDER MULT PRINT')
# 12

minilang('-3 PUSH 5 SUB PRINT')
# 8

minilang('6 PUSH')
# (nothing is printed)

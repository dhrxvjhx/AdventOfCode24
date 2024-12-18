def run_three_bit_computer(initial_a, initial_b, initial_c, program):
    # Initialize registers
    registers = {
        'A': initial_a,
        'B': initial_b,
        'C': initial_c
    }
    
    # Output will collect values from 'out' instructions
    output = []
    
    # Instruction pointer starts at 0
    ip = 0
    
    while ip < len(program):
        # Read opcode and operand
        opcode = program[ip]
        operand = program[ip + 1] if ip + 1 < len(program) else None
        
        # Instruction handling
        if opcode == 0:  # adv: divide A by 2^operand
            operand_value = 2 ** operand if operand < 4 else 2 ** registers[['A', 'B', 'C'][operand - 4]]
            registers['A'] = registers['A'] // operand_value
        
        elif opcode == 1:  # bxl: XOR B with literal operand
            registers['B'] ^= operand
        
        elif opcode == 2:  # bst: set B to operand modulo 8
            registers['B'] = operand % 8
        
        elif opcode == 3:  # jnz: jump if A is not zero
            if registers['A'] != 0:
                ip = operand
                continue  # Skip normal instruction pointer increment
        
        elif opcode == 4:  # bxc: XOR B with C
            registers['B'] ^= registers['C']
        
        elif opcode == 5:  # out: output operand modulo 8
            output.append(operand % 8)
        
        elif opcode == 6:  # bdv: divide A by 2^operand, store in B
            operand_value = 2 ** operand if operand < 4 else 2 ** registers[['A', 'B', 'C'][operand - 4]]
            registers['B'] = registers['A'] // operand_value
        
        elif opcode == 7:  # cdv: divide A by 2^operand, store in C
            operand_value = 2 ** operand if operand < 4 else 2 ** registers[['A', 'B', 'C'][operand - 4]]
            registers['C'] = registers['A'] // operand_value
        
        # Move instruction pointer
        ip += 2
    
    return ','.join(map(str, output))

# Main script
def main():
    with open("input.txt") as f:
        # Read initial register values
        initial_a = int(f.readline().split(': ')[1])
        initial_b = int(f.readline().split(': ')[1])
        initial_c = int(f.readline().split(': ')[1])
        
        # Read program
        program_line = f.readline().split(': ')[1]
        program = [int(x) for x in program_line.split(',')]
    
    # Run the computer simulation
    result = run_three_bit_computer(initial_a, initial_b, initial_c, program)
    print(result)

if __name__ == '__main__':
    main()
def print_formatted(number):
    # your code goes here
    width_len = len(bin(number)[2:])
    
    for i in range(n):
        a_decimal = str(i+1)
        b_octal = oct(i+1)[2:]
        c_hex = hex(i+1)[2:].upper()
        d_binary = bin(i+1)[2:].rjust(width_len)
        print(a_decimal.rjust(width_len), b_octal.rjust(width_len), c_hex.rjust(width_len), d_binary.rjust(width_len))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
    

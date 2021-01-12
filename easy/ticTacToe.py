
input_symbols = list(input("Enter cells: "))
print("-" * len(input_symbols))
for i in range(0,8,3):
    print(f"| {input_symbols[i]} {input_symbols[i + 1]} {input_symbols[i + 2]} |")
print("-" * len(input_symbols))


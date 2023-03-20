nl = []

while True:
    n = input("Enter a number: ")
    if n == "done":
        break
    try:
        n = float(n)
    except ValueError:
        print("Invalid input")
        continue
    nl.append(n)

if nl:
    print("Maximum: ", max(nl))
    print("Minimum: ", min(nl))
else:
    print("Invalid input")
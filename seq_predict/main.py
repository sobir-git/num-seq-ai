""" Command line interface """

from seq_predict.search import findNext


run = True
print("""
Hi,
Enter some numbers and I will try to predict the next number.
The numbers should be seperated by space.
Example:
    input: 1 4 9
    output: 1, 4, 9 --> 16

""")


while True:

    seq = input("Enter a sequence: ")
    try:
        seq = map(int, seq.split())
    except Exception:
        print("Invalid input (see the example).")
        continue

    result = findNext(seq)
    print(result.log_tree.to_string())

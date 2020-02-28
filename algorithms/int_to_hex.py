"""
int_to_hex.py
~~~~~~~~~~~~~
Convert an integer to its hex representation.
"""

def int_to_hex(n):
    mapping = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

    _result = []
    while n > 0:
        look_up = n - 1
        print(look_up)
        if look_up == 0:
            return _result.append(mapping[look_up])

        divided = n / 16

        left = str(divided).split(".")[0]
        right = str(divided).split(".")[-1]

        _result.append(left)

        n = int(float(right) * 16)



if __name__ == "__main__":
    # for i in range(32):
    print(int_to_hex(32))

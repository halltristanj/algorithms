"""
int_to_hex.py
~~~~~~~~~~~~~
Convert an integer to its hex representation.
"""

def int_to_hex(n):
    mapping = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]

    _result = []
    while n >= 0:
        if n == 0:
            _result.append(mapping[n])
            return "".join(_result)
        elif n <= 16:
            _result.append(mapping[n - 1])
            return ''.join(_result)

        divided = n / 16

        left = str(divided).split(".")[0]
        right = str(divided).split(".")[-1]

        _result.append(mapping[int(left)])

        print(n, left, right)

        n = int(float(f".{right}") * 16)

    return ''.join(_result)



if __name__ == "__main__":
    for i in range(32):
        print(int_to_hex(i))

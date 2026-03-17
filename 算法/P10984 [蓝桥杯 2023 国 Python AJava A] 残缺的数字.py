SEGMENTS = [
    0b1111110,
    0b0110000,
    0b1101101,
    0b1111001,
    0b0110011,
    0b1011011,
    0b1011111,
    0b1110000,
    0b1111111,
    0b1111011,
]

BROKEN = [
    0b0000011,
    0b1001011,
    0b0000001,
    0b0100001,
    0b0101011,
    0b0110110,
    0b1111111,
    0b0010110,
    0b0101001,
    0b0010110,
    0b1011100,
    0b0100110,
    0b1010000,
    0b0010011,
    0b0001111,
    0b0101101,
    0b0110101,
    0b1101010,
]

def solve():
    result = 1
    for broken_code in BROKEN:
        count = 0
        for seg in SEGMENTS:
            if (broken_code & seg) == broken_code:
                count += 1
        result *= count
    print(result)
solve()
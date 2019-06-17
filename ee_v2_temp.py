from matplotlib import pyplot as plt

start = [
    (0.5, 0),
    (0.5, 1)
]

one = [
    (0.25, 0),
    (0.75, 1)
]

zero = [
    (0.75, 0),
    (0.25, 1)
]

alphabet = {
    0: zero,
    1: one,
    -1: start,
}


def draw(bin_arr):
    x = []
    y = []
    accu = 0
    for n in bin_arr:
        t = alphabet[n]
        for i in t:
            x.append(accu)
            y.append(i[1])
            accu += i[0]
            x.append(accu)
            y.append(i[1])
    plt.plot(x, y)
    plt.show()


def to_dec(bin_arr, big_endian=False):
    d = 0
    if big_endian:
        bin_arr.reverse()
    for i in range(len(bin_arr)):
        d += bin_arr[i] * pow(2, i)
    return d


def get_temp(val):
    return val / (pow(2, 16) - 1) * (150 + 50) - 50


if __name__ == '__main__':
    z1 = [-1, 0, 0, 0, 0, 0, 0, 1, 1, 0]
    z2 = [-1, 0, 0, 1, 0, 1, 0, 1, 0, 1]
    draw(
        z1 + z2
    )
    print(get_temp(to_dec(z1[1:-1] + z2[1:-1])))

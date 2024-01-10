def main():
    with open("input_1.txt", "r") as file1:
        a = file1.readlines()
    a = [[int(n) for n in x.split()] for x in a]
    print(a)
    #####
    with open("input_2.txt", "r") as file2:
        b = file2.readlines()
    b = [[int(n) for n in x.split()] for x in b]
    print(b)
    #####
    ox = {}

    ox = func(a, b, ox)
    if ox is not None:
        print("Ok", ox)
    else:
        print("False")


def func(a, b, ox):
    result = False
    for i, el_b in enumerate(b):
        for j, el_a in enumerate(a):
            for n in range(len(el_a)):
                check = True

                if el_b[0] == el_a[n]:
                    for m in range(1, len(el_b)):
                        if not el_b[m] == el_a[n+m]:
                            check = False
                            ox[i] = None
                            break

                    if check:
                        ox[i] = [j, n]
    return ox


if __name__ == '__main__':
    main()

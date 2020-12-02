# These solutions are not efficient

def part1():
    with open("../input", 'r') as fh:
        all_lines = fh.readlines()
        for o in all_lines:
            for i in all_lines:
                if (int(o) + int(i)) == 2020:
                    print(int(o), int(i))
                    print(int(o) * int(i))
                    return


def part2():
    with open("../input", 'r') as fh:
        all_lines = fh.readlines()
        for o in all_lines:
            for i in all_lines:
                for ii in all_lines:
                    if (int(o) + int(i) + int(ii)) == 2020:
                        print(int(o), int(i), int(ii))
                        print(int(o) * int(i) * int(ii))
                        return


if __name__ == "__main__":
    part1()
    part2()

import calc
import cProfile

profile = cProfile.Profile()
profile.enable()

# sum of all x
def sum(list_numbers):
    total = 0
    for number in list_numbers:
        total = calc.add(total, int(number))
    return total


# (sum of all x / N)
def div_2(list_numbers):
    return sum(list_numbers) / len(list_numbers)


def std(list_numbers):
    a = 0
    for number in list_numbers:
        a = calc.add(a, calc.exp(int(number), 2))

    b = calc.mult(len(list_numbers), calc.exp(div_2(list_numbers), 2))
    s = calc.root(calc.div(calc.sub(a, b), calc.sub(len(list_numbers), 1)), 2)
    return s


if __name__ == "__main__":
    string_input = input()
    num_list = string_input.replace("\t", " ").replace("\n", " ").split(" ")
    deviation = std(num_list)
    print(deviation)

profile.disable()
profile.print_stats(sort='time')
profile.dump_stats("profiling.prof")

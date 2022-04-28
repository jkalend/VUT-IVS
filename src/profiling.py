import cProfile
import calc
import sys

numbers = sys.stdin.read().rstrip().split()

profile = cProfile.Profile()
profile.enable()

sum = 0
sum_x = 0
for num in numbers:
    sum = calc.eval_str(f"{str(sum)} + {num}")
    sum_x = calc.eval_str(f"{num}^2 + {str(sum_x)}")

sum = calc.eval_str(f"({str(sum)}/{len(numbers)})^2 * {len(numbers)}")

print(calc.eval_str(f"√((1/({len(numbers)} - 1)) * ({str(sum_x)} - {str(sum)}))"))


profile.disable()
profile.print_stats(sort='time')
profile.dump_stats("profiling.prof")

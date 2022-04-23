import sys
from src import calc
import cProfile

### Help message
print("Enter numbers. Ctrl+D to continue.")

### global variables ###
x=sys.stdin.readlines()
N=len(x)

profile = cProfile.Profile()
profile.enable()

def avrg(): 
    # average of input numbers  

    def div_1():
        # 1/N
        global N
        div = calc(1.0) / calc(N)
        return div

    def add_1():
        # sum of input numbers
        global x
        sum=0
        for i in range(len(x)):
            x[i]=x[i].replace('\n','')
            sum = calc(sum) + calc(x[i])
        return sum 

    def mult_1(a,b):
        m = a * b
        return m

    average = mult_1(div_1(), add_1())
    return average

av = avrg()
def rootino():
    def div_2():
        # 1/(N-1)
        global N
        div = calc(1.0) / (calc(N) - calc(1))
        return div

    def brackets():
        def add_2():
            # sum of input numbers^2
            global x
            sum=0
            for i in range(len(x)):
                x[i]=x[i].replace('\n','')
                sum = calc(sum) + (calc(x[i]), calc(2))
            return sum 

        def mult_2():
            # N * x^2
            global N, av
            m = calc(N) * (av,  calc(2))
            return m

        def sub(a,b):
            s = a - b
            return s
        
        brac = sub(add_2(), mult_2())
        return brac

    def mult_3(a,b):
        m = a * b
        return m
    
    multRes = mult_3(div_2(),brackets())
    root = multRes.root()
    return root
avrg()
rootino()
profile.disable()
profile.print_stats(sort='time')
profile.dump_stats("profiling_calc.prof")

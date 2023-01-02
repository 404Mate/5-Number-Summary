import numpy as np
import statistics

def main():
    # Loops adding to the list until an empty string is sent
    var = 0
    list = []
    # TODO Backspace option
    while True:
        var = input("\nAdd a number to the list, press enter to end\n")
        if var != "":
            var = int(var)
            list.append(int(var))
            print(list)
        else:
            break
    list.sort()
    print(list)
    # decides between midpoint and higher/lower depending on the list being even/odd
    if len(list) % 2 == 0:
        evenOdd = "midpoint"
        evenOdd1 = "midpoint"
    else:
        evenOdd = "higher"
        evenOdd1 = "lower"
    
    # Math section
    min = np.min(list)
    Q1 = np.percentile(list, 25, method = evenOdd1)
    median = np.percentile(list, 50, method = 'midpoint')
    Q3 = np.percentile(list, 75, method = evenOdd)
    max = np.max(list)
    IQR = Q3 - Q1
    mean = np.mean(list)
    mode = statistics.mode(list)
    
    # Prints results from math section in a easy to read format
    print(f"""\nYour five number summary is:
    Min: {min}
    Q1: {Q1}
    Median: {median}
    Q3: {Q3}
    Max: {max}
    IQR: {IQR}
    Mean: {mean}
    Mode: {mode}""")

if __name__ == "__main__":
    main()




#---------------------------
#  made by 404Mate with <3  
#---------------------------

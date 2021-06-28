class Myclass:
    def __init__(self):
        pass

    def gugudan(self):
        for i in range(2,10):
            print(f"{i}단", end="           ")
        print()
        for i in range(1,10):
            for j in range(2,10):
                print("{} * {} = {:2}".format(j, i, i*j),end="    ")
            print()


    def odd_even(self):
        while True:
            num = int(input("plz, input number(0:close) :  "))
            if num == 0:
                break
            elif num%2 == 0:
                print("Even ! ")
            else:
                print("Odd !")

    def sequence(self):
        print("1-2+3-4 .. -98+99-100 의 값을 구하라", end="")
        num = 0
        for i in range(1,101,2):
            num +=i
        for i in range(2,101,2):
            num -=i
        
        print(" :", num)


if __name__ == "__main__":
    mc = Myclass()
    mc.gugudan()

    print()
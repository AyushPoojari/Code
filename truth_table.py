def truth_table(exp,input = 2):
    print(exp)
    exp = exp.lower()
    exp = exp.replace("and","&")
    exp = exp.replace("or","|")
    exp = exp.replace("xor","^")
    exp = exp.replace("not","~")
    if (input == 2):
        print("------")
        print("A" + "|" + "B" + "|" + "X")
        print("------")
        for a in range(0,2):
            for b in range(0,2):
                x = eval(exp)
                print(str(a) + "|" + str(b) + "|" + str(x))
                print("------")

    elif(input == 3):
        print("------")
        print("A" + "|" + "B" + "|" + "C" + "|" + "X")
        print("------")
        for a in range(0,2):
            for b in range(0,2):
                for c in range(0,2):
                    x = eval(exp)
                    print(str(a) + "|" + str(b) + "|" + str(c) + "|" + str(x))
                    print("------")
    elif(input == 4):
        print(1)
    else:
        print("Error")



exp = "(A and B) or C"
truth_table(exp,3)
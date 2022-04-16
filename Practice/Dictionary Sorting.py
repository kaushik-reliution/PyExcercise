def dictionary():
    keyval = {}

    keyval[6] = 56
    keyval[5] = 60
    keyval[3] = 50
    keyval[4] = 55
    keyval[2] = 60
    keyval[1] = 58
    print("Before sorting\n",keyval.values())
    print("After Sorting")
    for i in sorted(keyval):
        print(i,keyval[i])

def main():
    dictionary()
if __name__ == "__main__":
    main()



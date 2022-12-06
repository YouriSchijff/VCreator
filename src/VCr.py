import sys

def gen(type,major,minor,patch):
    s = major+"."+minor+"."+patch
    match type:
        case "a": print(s+"-a.1")
        case "b": print(s+"-b.2")
        case "pr": print("pre-"+s)
        case "r": print(s)
        case "x": print(s+"-ex.4")
        case _: print("Invalid type: use (i, a, b, pr, r, rc, x or rx)")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Use `vers` or `help`")
        exit(0)
    if sys.argv[1] == "vers":
        if len(sys.argv) == 2:
            print("Select a type (i, a, b, pr, r, rc, x or rx)")
            exit(0)
        if len(sys.argv) == 3:
            print("Fill in major argument")
            exit(0)
        if sys.argv[2] == "i":
            if len(sys.argv) == 4:
                try:
                    int(sys.argv[3])
                    print("Indev-" + sys.argv[3])
                    exit(0)
                except:
                    print("Only Integers are used for major")
                    exit(0)
            else:
                print("Too many arguments!")
                exit(0)
        if len(sys.argv) > 7:
            print("Too many arguments!")
            exit(0)
        if len(sys.argv) == 7 and sys.argv[2] == "rx":
            # 1.0.0a
            try:
                int(sys.argv[3])
                int(sys.argv[4])
                int(sys.argv[5])
                print(sys.argv[3]+"."+sys.argv[4]+"."+sys.argv[5]+sys.argv[6])
                exit(0)
            except:
                    print("Only Integers are used for major, minor and/or patch")
                    exit(0)
        if len(sys.argv) == 6:
            try:
                int(sys.argv[3])
                int(sys.argv[4])
                int(sys.argv[5])
            except:
                    print("Only Integers are used for major, minor and/or patch")
                    exit(0)
            gen(sys.argv[2],sys.argv[3],sys.argv[4],sys.argv[5])
    
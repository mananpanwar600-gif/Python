while True:
    try:
        a = int(input("Enter a : "))
        b = int(input("Enter b : "))
        x = a/b
        print(x)

    except Exception as e:
        print(e)
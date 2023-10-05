#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    toprint = dir(hidden_4)

    for name in toprint:
        if name == "__":
            print(toprint)
            break

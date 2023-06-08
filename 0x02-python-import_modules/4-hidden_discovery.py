#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4
    
    words = dir(hidden_4)
    for i in words:
        if i[:2] != "__":
            print(i)

quese = list()

def enqueu(x):
    global quese
    quese.append(x)

def dequeu():
    global quese
    if is_empty():
        return
    return quese.pop(0)

def is_empty():
    global quese
    return len(quese) == 0


if __name__ == "__main__":
    enqueu(6)
    enqueu(99)
    print(dequeu())
    print(dequeu())

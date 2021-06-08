# Q. Given a str revers it uses recursion

"ABCD" "to" "DCBA"

def reverse (str):
    if str == "":
        return ""

    rev = str[-1]+reverse(str[:-1])
    return rev

if __name__=="__main__":
    
    print(reverse("ABCD"))        
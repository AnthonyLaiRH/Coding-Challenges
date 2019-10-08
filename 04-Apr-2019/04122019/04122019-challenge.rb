# Implement division of 2 postive integers, without using divsion, multiplication, or modulus operators

def main()
    puts (specialDivide(24,5))
end

def specialDivide(n,m)
    i = 0;
    until (n - m) < 0
        n = (n - m)
        i+=1
    end

    return i
end

main()
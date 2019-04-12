#Given the function rand7() whihc returns a random int from 1 to 7, implement rand5 only using rand7()

def main()
    puts(rand5().to_s)
end

def rand5()
    return ((rand7()*5)/7)
end    

def rand7 ()
    n = rand(1..7)
    puts ("n=" + n.to_s)
    return n
end

main()
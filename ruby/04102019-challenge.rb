#!/usr/bin/env ruby

#Given a string of brackets, write a function to return the number of brackets to remove
# so that every bracket is closed
def main()
    s = "()()()((("
    n = neededToCloseAll(s)
    p(n)
end
    
def neededToCloseAll(s)
    open = 0
    close = 0
    arr = s.split("")
    arr.each do |character|
        if character == "("
            open += 1
            
        elsif character == ")"
            close += 1            
        end
    end

    if (open > close)
        return (open - close)
    elsif (open < close)
        return (close - open)
    else
        return 0
        
    end

end

main()
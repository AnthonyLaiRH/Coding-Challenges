def main(){
    str = "Hello World"
    print(readN(7, str))
}

def readN(n,str){
    result = ""

    for i in 0..n-1 do
        if i < length(str)
            result = result + str[i..i+1]
        else
            return result
}
ones =["","one","two","three","four","five","six","seven","eight","nine",
       "ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen",
      "seventeen","eighteen","nineteen"]
tens =["","","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]

def numLettersForNum(n):
    if n < 20:
        return len(ones[n])
    else:
        sum=0
        s=str(n)
        
        if int(s[-2])==1:
            sum+=len(ones[int(s[-2::])])
        else:
            sum+=len(tens[int(s[-2])])+len(ones[int(s[-1])])
            
        if n>=100 and n<1000:
            sum+=len(ones[int(s[-3])])+len("hundred")

            if n%100!=0:
                sum+=len("and")
            
        if n==1000:
            sum+=len("one")+len("thousand")

        return sum
        

print sum([numLettersForNum(i) for i in range(1,1001)])

        

text="I completely agree with you"
#Tip: to split text into words, use the split() function. Sample result:
#Text: I completely agree with you
#No. of letters in words: [1,10,5,4,3]
sum = list(map(lambda text:len(text),text.split()))
print(sum)

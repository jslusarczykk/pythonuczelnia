import sys
facebook = (input("Does your influencer use facebook?: "))
twitter = (input("Does your influencer use twitter?: "))
instagram = (input("Does your influencer use instagram?: "))


if(facebook and twitter=="yes"):
    print("A person can be a good influencer!")
    sys.exit()
if(facebook and instagram=="yes"):
    print("A person can be a good influencer!")
    sys.exit()
if(instagram and twitter=="yes"):
    print("A person can be a good influencer!")
    sys.exit()

def f(x):
    x=list(x) #[1,0,2,7]
    sum=0
    for i in range(len(x)):
        if(x.count(x[i])>1):
            sum+=int(x[i])
    return sum

#    def test_p7(self):
#        import p7
#        self.assertEqual(p7.f(1027),0)
#        self.assertEqual(p7.f(4444),16)
#        self.assertEqual(p7.f(22777),25)
#        self.assertEqual(p7.f(230335),9)
#        self.assertEqual(p7.f(513553007),21)
#        self.assertEqual(p7.f(112345),2)
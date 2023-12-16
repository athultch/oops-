class father :    

    def feature1(self):
        print("first feature")


class son ():           

    def feature2(self):
        print("seconde feature")


class son2(son,father):

     def feature3(self):
        print("therd feature")


mom =son2()
mom.feature1()
mom.feature2()
mom.feature3()
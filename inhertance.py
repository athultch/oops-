#single level inheritance


class father :                 #parent class  or super class
    def feature1(self):
        print("first feature")

    def feature2(self):
        print("seconde feature")


class son (father):            #child class   or  sub class
    def feature3(self):
        print("therd feature")

    def feature4(self):
        print("fourth feature")

mom =son()

mom.feature1()
mom.feature2()
mom.feature3()
mom.feature4()
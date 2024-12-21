print("WELCOME CVR BANK")

class Bank:
    acb = 10000

    def validate(self):
        i=3
        while i>0:
            pin = (input("ENTER YOUR ENTER PIN NUMBER"))
            pinps = "1234"
            if (pin == pinps):
                print("you have entered correct pin")
                i=0
                self.options()
            else:
                i=i-1
                print("wrong pin retry")



    def options(self):
        print("1.depoist \n 2.withdraw \n 3.balance enq \n 0.exit\n choose the option")
        opt = input("ENTER THE OPTION NUMBER")
        match opt:
            case "1":
                self.depoist()
                obj.options()
            case "2":
                self.withdraw()
                obj.options()
            case "3":
                self.balanceenq()
                obj.options()




    def depoist(self):

        depo=int(input("enter depoist amt"))
        if depo>=100 & (depo%100)==0:
            self.acb = self.acb + depo
            print(f"avl balance{self.acb}")
        else:
            print("minimum depoist is less than 100 or not a multiple of 100")
        if depo>50000 :
            print("min depoist is 50000")

    def withdraw(self):
        wtd=int(input("enter withdrawl amount"))
        if wtd%100==0:
            if wtd >= 100 and wtd < obj.acb and wtd < 20000:
                self.acb = self.acb - wtd
                if self.acb < 500:
                    print("need to maintain 500 bank bal")

                else:
                    print(f"after withdrawl ur amount {self.acb}")


            else:
                print("our withdrawl amount is not multple or more than aval balance or less than 100")
        else:
            print("is not multliple of 100")


    def balanceenq(self):
        print(f"your available balance is{self.acb}")





obj=Bank()
obj.validate()
from random import Random


class Atm(object):
    def __init__(self,totalamount,takingmoney,depositingmoney):
        self.totalamount = totalamount
        self.takingmoney = takingmoney
        self.depositingmoney = depositingmoney


    def showtotalamount(self):
        print("Please fill your password")

    def thankyou(self):
        print("Thank you for trusting us.We are always here to help you.Here is your list.")



card1 = Atm("Total Money-4000","Taking-2000","Depositing-5000")
card2 = Atm("Total Money-5000","Taking-1000","Depositing-6000")

card1.showtotalamount()
print("sfdghy")
card1.thankyou()
print(card1.totalamount,card1.takingmoney,card1.depositingmoney)
card2.showtotalamount()
print("dgyssi")
card2.thankyou()
print(card2.totalamount,card2.takingmoney,card2.depositingmoney)

        
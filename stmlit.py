import streamlit as st
st.title("Bank Application")
class Bank:
    acb = 10000

    def validate(self):
        i=3
        while i>0:
            pin = st.number_input("Enter the pin number:")
            if st.button("verify pin"):
                if pin == 1234:
                    i=0
                    st.html("""
                    <h1>1.Depoist</h1>
                    <h1>2.Withdraw</h1>
                    <h1>3.Balance enq</h1>
                    <h1>4.Exit</h1>
                    """)
                else:
                    st.warning("wrong pin")
                self.options()
            else:
                i=i-1
                st.warning("wrong pin retry")
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
    def balance_enquiry(self):
        print(f"your available balance is{self.acb}")

    def deposit(self):
        depo = st.number_input("enter depoist amt")
        if depo >= 100 & (depo % 100) == 0:
            self.acb = self.acb + depo
            st.write(f"avl balance :{self.acb}")
        else:
            st.warning("minimum depoist is less than 100 or not a multiple of 100")
        if depo > 50000:
            st.warning("min depoist is 50000")

    def options(self):

        while True:
            st.write("Choose an option")
            option = st.selectbox(
                "Select an option:",
                options=["Deposit", "Withdraw", "Balance Enquiry", "Exit"]
            )

            if option == "Deposit":
                self.deposit()
            elif option == "Withdraw":
                self.withdraw()
            elif option == "Balance Enquiry":
                self.balance_enquiry()
            elif option == "Exit":
                st.write("Thank you for using our service!")
                break
            else:
                st.write("Invalid option. Please try again.")




obj=Bank()
obj.validate()

















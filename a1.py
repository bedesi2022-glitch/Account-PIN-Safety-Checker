class AccountPIN:
    __PrivateVar = 7773;
    def __privMeth(self):
        print("I am inside class AccountPIN")
    def hello(self):
        print("Priate Variable Value:",AccountPIN.__PrivateVar)
foo = AccountPIN
foo.hello()
foo.__privMeth
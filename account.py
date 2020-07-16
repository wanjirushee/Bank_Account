#python 3.7.1

class BankAccount:
  bank="Co - operative"
  
  def __init__(self,first_name,last_name):
      self.first_name=first_name
      self.last_name=last_name
      self.balance=0
    
   
  def account_name(self):
      name="{} account for {} {} ". format(self.bank,self.first_name,self.last_name)
      return name
      
  def deposit(self, amount):
        self.balance +=amount
        print("You have deposited {} to your account".format(amount))   
  
  def get_balance(self):
        return("The balance for {} is {}".format(self.account_name(),self.balance))
        
  def withdraw(self, amount):
    self.balance -=amount
    print("You have withdrawn {} "" dollars from your account". format (amount))
  
  def deposit_update(self,amount):
    self.balance += amount
    if amount> 0:
      print("You have deposited {} to your account".format(amount))
    else:
      print("you have insufficient funds ".format(amount))
   
  def withdraw_update(self,amount):
    self.balance -= amount
    if amount> 0:
      print("You have withdrawn {}ksh from your account".format(amount))
    else:
      print("Sorry! we cannot complete this transaction.you account balance is insufficient"
.format(amount))
  
  
  
acc1=BankAccount("Jeff", "Bezos")
acc2=BankAccount("mark","zuckerberg")
acc3=BankAccount("Starr","winner")


acc1.deposit (1000)
acc2.deposit (5000)
acc3.deposit(4000)

print(acc1.account_name())
print(acc2.account_name())
print(acc3.account_name())



print(acc2.get_balance())
print(acc1.get_balance())
print (acc3.get_balance())



acc1.withdraw(3000)
acc2.withdraw(8000)
acc3.withdraw(20000)


acc1.deposit_update(1000)
acc2.deposit_update(2000)
acc3.deposit_update(20000)
acc1.withdraw_update(0)
acc2.withdraw_update(2000)

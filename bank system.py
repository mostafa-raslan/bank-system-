
class BankAccount:
    def __init__(self, name, balance=0): #constructor
        self.name = name
        self.balance = balance#هنا بحظ الرصيد

    def deposit(self, amount):#اضافه فلوس الحساب ديى داله اسمها بوزيت
        self.balance += amount#amount المبلغ اللي انا هضيفه وفي الاخر الداله كلها بتطلع لي الفلوس كلها
        print("Deposit successful!")

    def withdraw(self, amount):#دي داله السحب ي
        if amount > self.balance:#لو المبلغ المسحوب اكبر من الرصيد يطبع الرصيد غير كافي
            print("Insufficient balance!")
        else:
            self.balance -= amount#هنا بطرح المبلغ من الرصيد القديم  هيطبع العمليه ناجحه
            print("Withdrawal successful!")

    def show_balance(self):#دي داله عرض الرصيد
        print("Current balance:", self.balance)


name = input("Enter account holder name: ")#دخل الاسم هنا 
account = BankAccount(name)#بستخدم الكلالس دي في اننا نعمل حساب بنكي

while True: # البرنامج يفضل شغال لحد ما المستخدم يحلص
    print("\n1.Deposit")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4.Exit")

    choice = input("Choose an option: ") # اكنب رقم من اللي فوق دول

    if choice == "1":
        amount = float(input("Enter deposit amount: "))#بحط الرقم ممكن يكون عشري
        account.deposit(amount)

    elif choice == "2":
        amount = float(input("Enter withdraw amount: "))#بحط الرقم ممكن يكون عشري#يدخل المبلغ ويسحب
        account.withdraw(amount)

    elif choice == "3":
        account.show_balance() # يعرض الرصيد

    elif choice == "4":
        print("Thank you !")
        break

    else:
        print("Invalid choice!") #لو رقم غير موجود

# %%




# #16.11.2023 Exam Q


# class Client:
#     def __init__(self,name,tel,balance):
#         self.name = name
#         self.tel = tel
#         self.balance = balance
#         self.payments = []
        
#     def  deduct(self,date,amount):
#         self.balance -= amount
#         self.payments.append([date,amount])
        
#     def show_balance(self):
#         print(self.balance)
        
#     def show_payments(self):
#         for date ,amount in self.payments:
#             print(f'{date},{amount}')
        
#     def show_payments_between_interval(self, start, end):
#         for date , amount in self.payments:
#             if start < date < end:
#                 print(date,amount)

# client1 = Client("Bek", "0777665544", 10000)

# client1.deduct("2023-10-07", 2000)
# client1.deduct("2023-10-08", 1500)
# client1.deduct("2023-10-10", 3000)
# print("*"*10,'Balaence',"*"*10)
# print("Client Balance:")
# client1.show_balance()

# print("\nAll Payments:")
# client1.show_payments()

# print("\nPayments Between 2023-10-07 and 2023-10-09:")
# client1.show_payments_between_interval("2023-10-07", "2023-10-09")



        
        

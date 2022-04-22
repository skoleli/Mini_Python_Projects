import functions
import time


start_time = time.time()

temp =time.time()
functions.Word_Order_Frequency_One_Book('book_1.txt', 1, 'output1.txt')
print("First function running duration = {}".format(time.time()-temp))

temp =time.time()
functions.Word_Order_Frequency_One_Book('book_2.txt', 1, 'output2.txt')
print("Second function running duration = {}".format(time.time()-temp))

temp =time.time()
functions.Word_Order_Frequency_One_Book('book_3.txt', 2, 'output3.txt')
print("Thirds function running duration = {}".format(time.time()-temp))

temp =time.time()
functions.Word_Order_Frequency_Two_Books ('book_4.txt', 'book_5.txt', 1, 'output4.txt')
print("Forth function running duration = {}".format(time.time()-temp))

temp =time.time()
functions.Word_Order_Frequency_Two_Books ('book_5.txt', 'book_6.txt', 2, 'output5.txt')
print("Fifth function running duration = {}".format(time.time()-temp))

    

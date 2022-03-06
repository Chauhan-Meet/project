try:
    import mysql.connector as sq
    p=sq.connect(host="localhost",user="root",password="",database="library")
    if p.is_connected()==False:
        print("Error..")
    else:
        myc=p.cursor()
except:
    print("ERROR")
def Add_book():
    Bid=int(input("Enter book id:"))
    book=input("Enter book name:")
    au=input("Enter Author name:")
    pr=float(input("Enter price:"))
    copies=int(input("Enter number of copies:"))
    qr="INSERT INTO book VALUES({},'{}','{}',{},{},{})".format(Bid,book,au,pr,copies,copies)
    myc.execute(qr)
    p.commit()
    print("Book was added successfully")
def Edit_book():
    Id=int(input("Enter book id:"))
    qry="SELECT* FROM book WHERE Bookid={}".format(Id)
    myc.execute(qry)
    
while True:
    print("="*80)
    print("\t\t\t-------LIBRARY MANAGEMENT-------")
    print("="*80)
    print("\t\t\t\tChoose an action:\n\t\t\t\t1.Book details.\n\t\t\t\t2.Member details.\n\
           \t\t\t3.Issue or return a book.\n\t\t\t\t4.Information.\n\t\t\t\t5.EXIT")
    a=int(input())
    if a==1:
        while True:
            print("\t\t\t\tChoose an action:\n\t\t\t\t1.Add book.\n\t\t\t\t2.Edit book details.\n\
        \t\t\t3.Delete a book.\n\t\t\t\t4.Search for a book.\n\t\t\t\t5.Back to main menu")
            ch=int(input())
            if ch==1:
                Add_book()
            elif ch==2:
                Edit_book()
            elif ch==3:
                print("3")
            elif ch==4:
                print("4")
            elif ch==5:
                break
    elif a==2:
        while True:
            print("\t\t\t\tChoose an action:\n\t\t\t\t1.Add member.\n\t\t\t\t2.Edit member details\
    .\n\t\t\t\t3.Delete a member.\n\t\t\t\t4.Search for a member.\n\t\t\t\t5.Back to main menu")
            c=int(input())
            if c==1:
                print("1")
            elif c==2:
                print("2")
            elif c==3:
                print("3")
            elif c==4:
                print("4")
            elif c==5:
                break
    elif a==3:
        while True:
            print("\t\t\t\tChoose an action:\n\t\t\t\t1.Issue book.\n\t\t\t\t2.Return book.\n\
            \t\t\t3.Back to main menu")
            h=int(input())
            if h==1:
                print("1")
            elif h==2:
                print("2")
            elif h==3:
                break
    elif a==4:
        while True:
            print("\t\t\t\tChoose an action:\n\t\t\t\t1.Related to Book .\n\t\t\t\t2.Related \
   Member\n\t\t\t\t3.Issue details.\n\t\t\t\t4.Return details.\n\t\t\t\t5.Back to main menu.")
            x=int(input())
            if x==1:
                print("1")
            elif x==2:
                print("2")
            elif x==3:
                print("3")
            elif x==4:
                print("4")
            elif x==5:
                break
    elif a==5:
        break
    
  

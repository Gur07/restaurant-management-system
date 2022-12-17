# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
import tkinter as tk
import random
import pymysql
from datetime import date
from tkinter import messagebox
dicprice = {'item1': 100, 'item2': 100, 'item3': 100, 'item4': 100, 'item5': 100, 'item6': 100, 'item7': 100, 'item8': 100}

#Sql passcode window
intropage=tk.Tk()
intropage.title('startup')
intropage.geometry('600x200')
intropage.resizable(0,0)


def disable_event():
    exit()


intropage.protocol('WM_DELETE_WINDOW', disable_event)
cur=None
db=None
psw1=None
# global variables for cursor and db


def conn():
    try:
        global cur
        global db
        global psw1
        db=pymysql.connect(host='localhost',user='root',password=psw.get())
        print('connected')
        cur=db.cursor()
        try:
            cur.execute('use restaurant;')
            print('data base present.')
            psw1=psw.get()  #assigning value to global psw1
            intropage.destroy()
        except:
            cur.execute('create database restaurant;')
            cur.execute('use restaurant;')
            cur.execute('create table ctd(name varchar(30),phno char(10),order_id varchar(15) primary key,mode_of_payment char(4),tax varchar(5),amount int,date_of_order date);')
            cur.execute('create table employee(empno int,ename varchar(20) primary key,designation varchar(20),hiredate date,salary int,department varchar(15));')
            cur.execute('create table order_details(order_id varchar(15) primary key,no_of_items int,item1 int,item2 int,item3 int,item4 int,item5 int,item6 int,item7 int,item8 int);')
            print('database/tables created')

            psw1 = psw.get()
            intropage.destroy()

    except:
        print('Wrong passcode')
        exit()


la=tk.Label(intropage,text='Enter Password(MYSQL):')
la.pack()
psw=tk.Entry()
psw.pack()
confirmb=tk.Button(text='confirm',command=conn)
confirmb.pack()
intropage.mainloop()

def t():
    window_takeorder = tk.Tk()
    window_takeorder.title('Take order')
    window_takeorder.geometry('800x500')
    window_takeorder.resizable(None, None)
    window_takeorder.focus()
    l = []
    dic = {'item1': 0, 'item2': 0, 'item3': 0, 'item4': 0, 'item5': 0, 'item6': 0, 'item7': 0, 'item8': 0}


    def add_dict(n):
        dic[n] += 1


    def add_item(n):
        if n == 1:
            add_dict('item1')
        elif n == 2:
            add_dict('item2')
        elif n == 3:
            add_dict('item3')
        elif n == 4:
            add_dict('item4')
        elif n == 5:
            add_dict('item5')
        elif n == 6:
            add_dict('item6')
        elif n == 7:
            add_dict('item7')
        elif n == 8:
            add_dict('item8')

    it1 = tk.Button(window_takeorder, text='item1', bg='purple', fg='white', font='100', height=3, width=15,
                    command=lambda: add_item(1))
    it1.place(relx=0.2, rely=0.2, anchor='center')

    it2 = tk.Button(window_takeorder, text='item2', bg='purple', fg='white', font='100', height=3, width=15,
                    command=lambda: add_item(2))
    it2.place(relx=0.4, rely=0.2, anchor='center')

    it3 = tk.Button(window_takeorder, text='item3', bg='purple', fg='white', font='100', height=3, width=15,
                    command=lambda: add_item(3))
    it3.place(relx=0.6, rely=0.2, anchor='center')

    it4 = tk.Button(window_takeorder, text='item4', bg='purple', fg='white', font='100', height=3, width=15,
                    command=lambda: add_item(4))
    it4.place(relx=0.8, rely=0.2, anchor='center')

    it5 = tk.Button(window_takeorder, text='item5', bg='purple', fg='white', font='100', height=3, width=15,
                    command=lambda: add_item(5))
    it5.place(relx=0.2, rely=0.4, anchor='center')

    it6 = tk.Button(window_takeorder, text='item6', bg='purple', fg='white', font='100', height=3, width=15,
                    command=lambda: add_item(6))
    it6.place(relx=0.4, rely=0.4, anchor='center')

    it7 = tk.Button(window_takeorder, text='item7', bg='purple', fg='white', font='100', height=3, width=15,
                    command=lambda: add_item(7))
    it7.place(relx=0.6, rely=0.4, anchor='center')

    it8 = tk.Button(window_takeorder, text='item8', bg='purple', fg='white', font='100', height=3, width=15,
                    command=lambda: add_item(8))
    it8.place(relx=0.8, rely=0.4, anchor='center')

    def done_command():
        l.append(enter_name.get())
        l.append(enter_phno.get())
        a = 0
        # total amount
        for item in dic.items():
            x = item[0]
            y = item[1]
            s = dicprice[x]
            a = a + (y * s)
        l.append(str(a))

        window_takeorder.destroy()
        window_confirm = tk.Tk()
        window_confirm.title('confirmation')
        window_confirm.resizable(True, True)
        window_confirm.geometry('300x300')

        label1 = tk.Label(window_confirm, text='select payment option-', font=('arial', 13))
        label1.place(relx=0.2,rely=0.2)

        def conf():

            orderidno = random.randint(0, 9999)

            l.append(str(orderidno))
            window_confirm.destroy()

            # SQL connectivity

            l.append('18')                 # tax

            l.append(date.today() )        # date

            total_items=0
            for i in dic:                  # total items
                total_items+=dic[i]
            list_of_items=list(dic.values())
            try:
                query = '''insert into ctd values('{}','{}','{}','{}','{}','{}','{}',{})'''.format(l[0], l[1], l[4], l[3], l[5], l[2],l[6],a+(0.18*a))
                cur.execute(query + ';')
                db.commit()

            except Exception as e:
                print(e)
            try:
                query2 = '''insert into order_details values('{}',{},{},{},{},{},{},{},{},{})'''.format(l[4],
                                                                                                        total_items,
                list_of_items[0],list_of_items[1],list_of_items[2],list_of_items[3],list_of_items[4],list_of_items[5],
                                                                                    list_of_items[6],list_of_items[7])
                cur.execute(query2+';')
                db.commit()

            except Exception as e:
                print(e)

            messagebox.showinfo('Thanks','Thanks for choosing us.\nOrder id:{}'.format(l[4]))



        def chb1():
            l.append('CASH')
            conf()

        def chb2():
            l.append('CARD')
            conf()

        chbox1 = tk.Checkbutton(window_confirm, text='CASH', onvalue='1', offvalue='0', font=('arial', 10),
                                command=chb1,
                                )
        chbox1.place(relx=0.4,rely=0.3)
        chbox2 = tk.Checkbutton(window_confirm, text='CARD', onvalue='1', offvalue='0', font=('arial', 10),
                                command=chb2,
                                )
        chbox2.place(relx=0.4,rely=0.4)
        amountdisplay=tk.Label(window_confirm,text='total amount= {}'.format(a+(0.18*a)),font=('arial,25'),fg='red')
        amountdisplay.place(relx=0.2,rely=0.1)




    done = tk.Button(window_takeorder, text='Done', fg='black', font=('Arial', 15), height=1, width=5,
                     command=done_command,state='disabled')
    done.place(relx=0.9, rely=0.6, anchor='center')

    labal_name = tk.Label(window_takeorder, text='Enter name :', font=('arial', 15))
    labal_name.place(relx=0.2, rely=0.6, anchor='e')

    enter_name = tk.Entry(window_takeorder, font=15, width=15, fg='red')
    enter_name.place(relx=0.3, rely=0.6, anchor='center')

    labal_no = tk.Label(window_takeorder, text='Contact no. :', font=('arial', 15))
    labal_no.place(relx=0.2, rely=0.7, anchor='e')

    def valinumber():
        if enter_phno.get().isdigit() and len(enter_phno.get())==10:
            done.config(state='active')
            enter_phno.config(state='disabled')
            return True
        else:
            enter_phno.delete(0, tk.END)
            return False

    enter_phno = tk.Entry(window_takeorder, font=15, width=15, fg='red', validatecommand=valinumber,
                          validate='focusout')
    enter_phno.place(relx=0.3, rely=0.7, anchor='center')

    window_takeorder.mainloop()


def c():

    windowemp = tk.Tk()
    windowemp.title('Add employee')
    windowemp.geometry('400x450')
    windowemp.resizable(None,None)

    def butentry():


        try:
            query='''insert into employee values('{}','{}','{}',{},'{}')'''.format(namentry.get(),desientry.get(),hirentry.get(),salentry.get(),depentry.get())
            cur.execute(query+';')
            db.commit()
        except Exception as e:
            p=tk.Label(windowemp,text='employee name already present\nDETAILS UPDATED',font=20,fg='red')
            p.place(rely=0.8,relx=0.2)

            cur.execute('''update employee set salary ={},hiredate='{}',designation='{}',department='{}' where 
                ename='{}';'''.format(salentry.get(),hirentry.get(),desientry.get(),depentry.get(),namentry.get()))
            db.commit()


        namentry.delete(0, tk.END)
        desientry.delete(0, tk.END)
        hirentry.delete(0, tk.END)
        salentry.delete(0, tk.END)
        depentry.delete(0, tk.END)

    l = tk.Label(windowemp, text='Name:', font=20)
    l.grid(column=1, row=1, ipadx=10, ipady=10, sticky=tk.W)
    namentry = tk.Entry(windowemp)
    namentry.grid(column=2, row=1, ipadx=10, ipady=5, sticky=tk.W, padx=10, pady=10)
    l2 = tk.Label(windowemp, text='Designation:', font=20)
    l2.grid(column=1, row=2, ipadx=10, ipady=10, sticky=tk.W)
    desientry = tk.Entry(windowemp)
    desientry.grid(column=2, row=2, ipadx=10, ipady=5, sticky=tk.W, padx=10, pady=10)
    hiredate = tk.Label(windowemp, text='Hire Date(YYYY-MM-DD)', font=20)
    hiredate.grid(column=1, row=3, ipadx=10, ipady=10, sticky=tk.W)

    def validate1():
        if len(hirentry.get())==10 and hirentry.get()[4]=='-' and hirentry.get()[7]=='-':
            hirentry.config(fg='green')
            butentrywindowemp.config(state='active')
            return True
        else:
            hirentry.config(fg='red')
            butentrywindowemp.config(state='disabled')
            return False

    hirentry = tk.Entry(windowemp,validatecommand=validate1,validate='focusout')
    hirentry.grid(column=2, row=3, ipadx=10, ipady=5, sticky=tk.W, padx=10, pady=10)

    salary = tk.Label(windowemp, text='Salary', font=20)
    salary.grid(column=1, row=4, ipadx=10, ipady=10, sticky=tk.W)
    department = tk.Label(windowemp, text='Department', font=20)
    department.grid(column=1, row=5, ipadx=10, ipady=10, sticky=tk.W)

    salentry = tk.Entry(windowemp)
    salentry.grid(column=2, row=4, ipadx=10, ipady=5, sticky=tk.W, padx=10, pady=10)
    depentry = tk.Entry(windowemp)
    depentry.grid(column=2, row=5, ipadx=10, ipady=5, sticky=tk.W, padx=10, pady=10)

    butentrywindowemp = tk.Button(windowemp, text='ADD Employee', command=butentry)
    butentrywindowemp.grid(column=2, row=11, ipadx=10, ipady=5, sticky=tk.W, padx=10, pady=10)

    def b():
        windowemp.destroy()

    backbutton = tk.Button(windowemp, text='Back', command=b)
    backbutton.grid(column=3, row=12)


    windowemp.mainloop()


def s():

    window_search=tk.Tk()
    window_search.title('search employee')
    window_search.geometry('800x350')
    window_search.resizable(None,None)
    name_search=tk.Label(window_search,text='enter name :',font='30')
    name_search.place(relx=0.8,rely=0.12)
    en1=tk.Entry(window_search)
    en1.place(rely=0.2,relx=0.8)

    def sea():
        try:
            query = '''select * from employee where ename = '{}'; '''.format(en1.get())
            x = cur.execute(query)
            f = cur.fetchall()
            if x > 0:
                print('record found', f)
                for i in f :

                    l3 = tk.Label(window_search, text='Name:', font=20)
                    l3.grid(column=1, row=1, ipadx=10, ipady=10, sticky=tk.W)
                    namentry = tk.Label(window_search, text='{}'.format(i[0]))
                    namentry.grid(column=2, row=1, ipadx=10, ipady=5, sticky=tk.W, padx=10, pady=10)
                    l2 = tk.Label(window_search, text='Designation:', font=20)
                    l2.grid(column=1, row=2, ipadx=10, ipady=10, sticky=tk.W)
                    desientry = tk.Label(window_search, text='{}'.format(i[1]))
                    desientry.grid(column=2, row=2, ipadx=10, ipady=5, sticky=tk.W, padx=10, pady=10)
                    hiredate = tk.Label(window_search, text='Date(YYYY-MM-DD)', font=20)
                    hiredate.grid(column=1, row=3, ipadx=10, ipady=10, sticky=tk.W)
                    hirentry = tk.Label(window_search, text='{}'.format(i[2]))
                    hirentry.grid(column=2, row=3, ipadx=10, ipady=5, sticky=tk.W, padx=10, pady=10)

                    salary = tk.Label(window_search, text='Salary', font=20)
                    salary.grid(column=1, row=4, ipadx=10, ipady=10, sticky=tk.W)
                    department = tk.Label(window_search, text='Department', font=20)
                    department.grid(column=1, row=5, ipadx=10, ipady=10, sticky=tk.W)

                    salentry = tk.Label(window_search, text='{}'.format(i[3]))
                    salentry.grid(column=2, row=4, ipadx=10, ipady=5, sticky=tk.W, padx=10, pady=10)
                    depentry = tk.Label(window_search, text='{}'.format(i[4]))
                    depentry.grid(column=2, row=5, ipadx=10, ipady=5, sticky=tk.W, padx=10, pady=10)


            else:
                print('not found')
        except Exception as e:
            print(e)

    searchbutton=tk.Button(window_search,text='search',command=sea)
    searchbutton.place(rely=0.3,relx=0.9,anchor=tk.E)



    window_search.mainloop()


def sd():
    window_searchdesignation = tk.Tk()
    window_searchdesignation.title('search employee')
    window_searchdesignation.geometry('800x200')
    window_searchdesignation.resizable(0,1)
    name_search = tk.Label(window_searchdesignation, text='enter designation :',font='30')
    name_search.pack()
    en1 = tk.Entry(window_searchdesignation)
    en1.pack()
    def sea():
        try:
            query = '''select * from employee where designation = '{}'; '''.format(en1.get())
            x = cur.execute(query)
            f = cur.fetchall()
            if x > 0:
                print('record found', f)
                for i in f :

                    lt=[i[0],i[1],str(i[2]),i[3],i[4]]
                    label=tk.Label(window_searchdesignation,text='{}'.format(lt),font=25)
                    label.pack()


            else:
                print('not found')
        except Exception as e:
            print(e)

    searchbutton = tk.Button(window_searchdesignation, text='search', command=sea)
    searchbutton.pack()

    window_searchdesignation.mainloop()


def st():
    window = tk.Tk()
    window.title('My Window')
    window.geometry('500x300')

    def extstat(n):

        cur.execute('select count(name),sum(total),sum(amount)*0.25 from ctd;')
        db.commit()
        f = cur.fetchall()

        d = {0: 'item1', 1: 'item2', 2: 'item3', 3: 'item4', 4: 'item5', 5: 'item6', 6: 'item7', 7: 'item8'}
        cur.execute('select sum(item1),sum(item2),sum(item3),sum(item4),sum(item5),sum(item6),sum(item7),sum(item8)'
                    'from order_details;')
        f1 = cur.fetchall()
        i = f1[0]
        m = 0
        for j in i:
            if j > m:
                m = j
            else:
                pass

        z = i.index(m)
        cur.execute('select sum(salary),count(ename) from employee;')
        f2 = cur.fetchall()
        cur.execute('select mode_of_payment,count(mode_of_payment) from ctd group by mode_of_payment;')
        f3 = cur.fetchall()
        cc=dict(f3)
        cashnum=cc['CASH']
        cardnum=cc['CARD']

        cur.execute('select sum(no_of_items),count(no_of_items) from order_details;')
        f4=cur.fetchall()


        return (f[0][0],
                f[0][1],
                f[0][2],
                d[z], m,
                f2[0][0],
                f2[0][1],cashnum,cardnum,f4[0][0],f4[0][1])

    q=extstat(psw1)

    e1 = tk.Label(window,text='enter code:',font=('Arial', 14))
    e2 = tk.Entry(window, show='*', font=('Arial', 14))
    e1.pack()
    e2.pack()
    def check():
        if e2.get()=='000':
            window.destroy()

            windowstat = tk.Tk()
            windowstat.title('Statistics')
            windowstat.geometry('400x500')
            windowstat.resizable(None, None)

            tnot = tk.Label(windowstat, text='Total number of orders taken:', font=20)
            tnot.grid(column=1, row=2, ipadx=10, ipady=10, sticky=tk.W)

            ans1 = tk.Label(windowstat,text='{}'.format(q[0]),font=20)
            ans1.grid(column=2, row=2, ipadx=10, ipady=5, sticky=tk.W, padx=10, pady=10)

            tr = tk.Label(windowstat, text='total revenue:', font=20)
            tr.grid(column=1, row=3, ipadx=10, ipady=10, sticky=tk.W)

            ans2 = tk.Label(windowstat,text='{}'.format(q[1]),font=20)
            ans2.grid(column=2, row=3, ipadx=10, ipady=5, sticky=tk.W, padx=10, pady=10)

            pxs = tk.Label(windowstat, text='Profit(excluding salary):', font=20)
            pxs.grid(column=1, row=4, ipadx=10, ipady=10, sticky=tk.W)

            ans3 = tk.Label(windowstat,text='{}'.format(q[2]),font=20)
            ans3.grid(column=2, row=4, ipadx=10, ipady=5, sticky=tk.W, padx=10, pady=10)

            msi = tk.Label(windowstat, text='Most sold item:', font=20)
            msi.grid(column=1, row=5, ipadx=10, ipady=10, sticky=tk.W)

            ans4 = tk.Label(windowstat,text='{}'.format(q[3]),font=20)
            ans4.grid(column=2, row=5, ipadx=10, ipady=5, sticky=tk.W, padx=10, pady=10)

            cs = tk.Label(windowstat, text='Combined salary\nno. of employees', font=20)
            cs.grid(column=1, row=6, ipadx=10, ipady=10, sticky=tk.W)

            ans5 = tk.Label(windowstat, text='{}\n{}'.format(q[5],q[6]),font=20)
            ans5.grid(column=2, row=6, ipadx=10, ipady=5, sticky=tk.W, padx=10, pady=10)

            avgodv = tk.Label(windowstat, text='Average order value', font=20)
            avgodv.grid(column=1, row=7, ipadx=10, ipady=10, sticky=tk.W)

            ans6 = tk.Label(windowstat, text='{}'.format(q[1]/q[0]),font=20)
            ans6.grid(column=2, row=7, ipadx=10, ipady=5, sticky=tk.W, padx=10, pady=10)

            cor = tk.Label(windowstat, text='Cash orders\nCard orders', font=20)
            cor.grid(column=1, row=8, ipadx=10, ipady=10, sticky=tk.W)

            ans7 = tk.Label(windowstat, text='{}\n{}'.format(q[7],q[8]),font=20)
            ans7.grid(column=2, row=8, ipadx=10, ipady=5, sticky=tk.W, padx=10, pady=10)

            aoi = tk.Label(windowstat, text='Average order items', font=20)
            aoi.grid(column=1, row=9, ipadx=10, ipady=10, sticky=tk.W)

            ans8 = tk.Label(windowstat, text='{}'.format(q[9]/q[10]),font=20)
            ans8.grid(column=2, row=9, ipadx=10, ipady=5, sticky=tk.W, padx=10, pady=10)



            windowstat.mainloop()


        else:
            wl=tk.Label(window,text='wrong code')
            wl.pack()
    show_det=tk.Button(window,text='verify',command=check)
    show_det.pack()


    window.mainloop()

def sr():
    window_record = tk.Tk()
    window_record.title('search order')
    window_record.geometry('800x400')
    window_record.resizable(0, 0)
    name_search = tk.Label(window_record, text='enter order id:', font='30')
    name_search.place(relx=0.8, rely=0.15)
    en1 = tk.Entry(window_record)
    en1.place(rely=0.2, relx=0.8)

    def search_rec():
        q='''select name,phno,mode_of_payment,date_of_order,total,no_of_items from ctd,order_details 
        where ctd.order_id=order_details.order_id and ctd.order_id='{}'; '''.format(en1.get())

        x = cur.execute(q)
        f = cur.fetchall()
        if x > 0:
            print('record found', f)
            for i in f:


                tnot = tk.Label(window_record, text='Name of recipient:', font=20)
                tnot.grid(column=1, row=2, ipadx=10, ipady=10, sticky=tk.W)

                ans1 = tk.Label(window_record, text='{}'.format(i[0]))
                ans1.grid(column=2, row=2, ipadx=10, ipady=5, sticky=tk.W, padx=10, pady=10)

                tr = tk.Label(window_record, text='Phone number:', font=20)
                tr.grid(column=1, row=3, ipadx=10, ipady=10, sticky=tk.W)

                ans2 = tk.Label(window_record, text='{}'.format(i[1]))
                ans2.grid(column=2, row=3, ipadx=10, ipady=5, sticky=tk.W, padx=10, pady=10)

                pxs = tk.Label(window_record, text='Mode of payment:', font=20)
                pxs.grid(column=1, row=4, ipadx=10, ipady=10, sticky=tk.W)

                ans3 = tk.Label(window_record, text='{}'.format(i[2]))
                ans3.grid(column=2, row=4, ipadx=10, ipady=5, sticky=tk.W, padx=10, pady=10)

                msi = tk.Label(window_record, text='Date:', font=20)
                msi.grid(column=1, row=5, ipadx=10, ipady=10, sticky=tk.W)

                ans4 = tk.Label(window_record, text='{}'.format(i[3]))
                ans4.grid(column=2, row=5, ipadx=10, ipady=5, sticky=tk.W, padx=10, pady=10)

                cs = tk.Label(window_record, text='Bill amount', font=20)
                cs.grid(column=1, row=6, ipadx=10, ipady=10, sticky=tk.W)

                ans5 = tk.Label(window_record, text='{}'.format(i[4]))
                ans5.grid(column=2, row=6, ipadx=10, ipady=5, sticky=tk.W, padx=10, pady=10)

                np = tk.Label(window_record, text='No. of items:', font=20)
                np.grid(column=1, row=7, ipadx=10, ipady=10, sticky=tk.W)

                ans6 = tk.Label(window_record, text='{}'.format(i[5]))
                ans6.grid(column=2, row=7, ipadx=10, ipady=5, sticky=tk.W, padx=10, pady=10)





    searchbutton = tk.Button(window_record, text='search', command=search_rec)
    searchbutton.place(rely=0.3, relx=0.9, anchor=tk.E)


first_window = tk.Tk()     # first window / starting window
first_window.title("Restaurant")
first_window.geometry('1000x500')
first_window.resizable(0, 0)

first_window.columnconfigure(1, weight=1)
first_window.columnconfigure(2, weight=1)
first_window.columnconfigure(3, weight=1)

first_window.rowconfigure(1, weight=1)
first_window.rowconfigure(2, weight=1)
first_window.rowconfigure(3, weight=1)


take_order_button = tk.Button(first_window, text='TAKE ORDER',bg='orange',height=5,width=35,borderwidth=3, command=t)
take_order_button.grid(column=2,row=2)
change_price = tk.Button(first_window, text='ADD EMPLOYEE DETAILS / UPDATE',bg='purple',fg='white',height=5,width=35,borderwidth=3, command=c)
change_price.grid(column=3,row=1)
search_emp_work = tk.Button(first_window, text='SEARCH EMPLOYEE\nby designation',bg='purple',fg='white',height=5,width=35,borderwidth=3, command=sd)
search_emp_work.grid(column=1,row=1)
search_emp = tk.Button(first_window, text='SEARCH EMPLOYEE\nby name',bg='purple',fg='white',height=5,width=35,borderwidth=3,command=s)
search_emp.grid(column=1,row=3)
statb = tk.Button(first_window, text='RESTAURANT stats',bg='purple',fg='white',height=5,width=35,borderwidth=3, command=st)
statb.grid(column=3,row=3)
searchbill = tk.Button(first_window, text='SEARCH record', bg='purple',  fg='white', height=5, width=35, borderwidth=3, command=sr)
searchbill.grid(column=2,row=3)

first_window.mainloop()

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
import pickle
import random
import pymysql
from datetime import date
from tkinter import messagebox


def t():
    window_takeorder = tk.Tk()
    window_takeorder.title('Take order')
    window_takeorder.geometry('800x500')
    window_takeorder.resizable(None, None)
    window_takeorder.focus()
    l = []
    dic = {'item1': 0, 'item2': 0, 'item3': 0, 'item4': 0, 'item5': 0, 'item6': 0, 'item7': 0, 'item8': 0}
    dicprice = {'item1': 10, 'item2': 10, 'item3': 10, 'item4': 10, 'item5': 10, 'item6': 10, 'item7': 10, 'item8': 10}

    def add_dict(n):
        dic[n] += 1


    def add_item(n):
        if n == 1:
            print('item 1 added')
            add_dict('item1')
        elif n == 2:
            print('item 2 added')
            add_dict('item2')
        elif n == 3:
            print('item 3 added')
            add_dict('item3')
        elif n == 4:
            print('item 4 added')
            add_dict('item4')
        elif n == 5:
            print('item 5 added')
            add_dict('item5')
        elif n == 6:
            print('item 6 added')
            add_dict('item6')
        elif n == 7:
            print('item 7 added')
            add_dict('item7')
        elif n == 8:
            print('item 8 added')
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
        a = 0  # total amount
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

            orderidno = random.randint(0, 9999999)
            f = open('e:\\computer science 12 files\\project XII\\2nd test\\orderids.dat', 'ab+')
            c = 0
            try:
                while True:
                    h = pickle.load(f)
                    if orderidno == h:
                        orderidno = random.randint(0, 9999999)
                        c = 1
            except:
                f.close()
            if c == 0:
                f = open('e:\\computer science 12 files\\project XII\\2nd test\\orderids.dat', 'ab+')
                pickle.dump(str(orderidno), f)
                f.close()
            l.append(str(orderidno))
            window_confirm.destroy()


            # SQL connectivity


            db = pymysql.connect(host='localhost', user='root', password='123st.gur', db='restaurant')
            print('connected successfully')
            cur = db.cursor()
            l.append('18')                 # tax

            l.append(date.today() )        # date
            print('l=', l)
            print('dic=',dic)
            total_items=0
            for i in dic:                  # total items
                total_items+=dic[i]
            list_of_items=list(dic.values())
            try:
                query = '''insert into ctd values('{}','{}','{}','{}','{}','{}','{}')'''.format(l[0], l[1], l[4], l[3], l[5], l[2],l[6])
                cur.execute(query + ';')
                db.commit()
                print('row inserted')
            except Exception as e:
                print(e)
            try:
                query2 = '''insert into order_details values('{}',{},{},{},{},{},{},{},{},{})'''.format(l[4],
                                                                                                        total_items,
                list_of_items[0],list_of_items[1],list_of_items[2],list_of_items[3],list_of_items[4],list_of_items[5],
                                                                                    list_of_items[6],list_of_items[7])
                cur.execute(query2+';')
                db.commit()
                print('order details added')
            except Exception as e:
                print(e)

            messagebox.showinfo('Thanks','Thanks for choosing us.')



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
        amountdisplay.place(relx=0.4,rely=0.1)



        '''con_button = tk.Button(window_confirm, text='confirm', command=conf)
        con_button.grid(row=4, column=2)'''

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
            db = pymysql.connect(host='localhost', user='root', password='123st.gur', db='restaurant')
            print('connected successfully')
            cur = db.cursor()
        except Exception as e:
            print(e)
        try:
            query='''insert into employee values({},'{}','{}','{}',{},'{}')'''.format(1,namentry.get(),desientry.get(),hirentry.get(),salentry.get(),depentry.get())
            cur.execute(query+';')
            db.commit()
        except Exception as e:
            p=tk.Label(windowemp,text='employee name already present',font=20,fg='red')
            p.place(rely=0.8,relx=0.2)
            print(e)

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
    hiredate = tk.Label(windowemp, text='Date(YYYY-MM-DD)', font=20)
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
    window_search.geometry('800x500')
    window_search.resizable(None,None)
    name_search=tk.Label(window_search,text='enter name :',font='30')
    name_search.place(relx=0.8,rely=0.15)
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
                    print('{}\t{}\t{}\t{}\t{}\t{}'.format(i[0],i[1],i[2],i[3],i[4],i[5]))


            else:
                print('not found')
        except Exception as e:
            print(e)

    searchbutton=tk.Button(window_search,text='search',command=sea)
    searchbutton.place(rely=0.3,relx=0.9,anchor=tk.E)
    try:
        db = pymysql.connect(host='localhost', user='root', password='123st.gur', db='restaurant')
        print('connected successfully')
        cur = db.cursor()
    except Exception as e:
        print(e)


    window_search.mainloop()


def sd():
    window_searchdesignation = tk.Tk()
    window_searchdesignation.title('search employee')
    window_searchdesignation.geometry('800x500')
    window_searchdesignation.resizable(None, None)
    name_search = tk.Label(window_searchdesignation, text='enter designation :',font='30')
    name_search.place(relx=0.8,rely=0.15)
    en1 = tk.Entry(window_searchdesignation)
    en1.place(rely=0.2,relx=0.8)
    def sea():
        try:
            query = '''select * from employee where designation = '{}'; '''.format(en1.get())
            x = cur.execute(query)
            f = cur.fetchall()
            if x > 0:
                print('record found', f)
                for i in f :
                    print('{}\t{}\t{}\t{}\t{}\t{}'.format(i[0],i[1],i[2],i[3],i[4],i[5]))


            else:
                print('not found')
        except Exception as e:
            print(e)
    try:
        db = pymysql.connect(host='localhost', user='root', password='123st.gur', db='restaurant')
        print('connected successfully')
        cur = db.cursor()
    except Exception as e:
        print(e)

    searchbutton = tk.Button(window_searchdesignation, text='search', command=sea)
    searchbutton.place(rely=0.3, relx=0.9, anchor=tk.E)

    window_searchdesignation.mainloop()


def st():
    window = tk.Tk()
    window.title('My Window')
    window.geometry('500x300')

    e1 = tk.Label(window,text='enter code:',font=('Arial', 14))
    e2 = tk.Entry(window, show='*', font=('Arial', 14))
    e1.pack()
    e2.pack()
    def check():
        if e2.get()=='000':



        else:
            wl=tk.Label(window,text='wrong code')
            wl.pack()
    show_det=tk.Button(window,text='verify',command=check)
    show_det.pack()

    window.mainloop()


first_window = tk.Tk()     # first window / starting window
first_window.title('rasoi')
first_window.geometry('1550x800')
first_window.resizable(None, None)

take_order_button = tk.Button(first_window, text='TAKE ORDER', command=t)
take_order_button.pack()
change_price = tk.Button(first_window, text='ADD EMPLOYEE DETAILS', command=c)
change_price.pack()
search_emp_work = tk.Button(first_window, text='SEARCH EMPLOYEE\nby designation', command=sd)
search_emp_work.pack()
search_emp = tk.Button(first_window, text='SEARCH EMPLOYEE\nby name', command=s)
search_emp.pack()
statb = tk.Button(first_window, text='Restaurant stats', command=st)
statb.pack()

first_window.mainloop()

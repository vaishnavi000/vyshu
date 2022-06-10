from tkinter import *
import pandas as pd
root=Tk()
root.geometry("900x500")
root.config(bg="lightgrey")
def printtext():
    global e
    global s
    global t
    global u
    global l
    global h
    df=pd.read_csv("E:/python project/Mobile Recommendation System/mobile recommendation system")
    df['RAMGB']=df['RAMGB'].map(str)
    df['ROMGB']=df['ROMGB'].map(str)
    df['price']=df['price'].map(str)
    df['Battery power']=df['Battery power'].map(str)
    df['generation']=df['generation'].map(str)
    df['frontcam']=df['frontcam'].map(str)
    df['primarycam']=df['primarycam'].map(str)
    string1= e.get()
    string2= s.get()
    string3= t.get()
    string4= u.get()
    string5= l.get()
    string6= h.get()
    string7= i.get()
    ##combinations
    if(string1==''):
        ac=df.loc[(df['RAMGB']==string2)&(df['ROMGB']==string3)&(df['Battery power']==string4)&(df['generation']==string5)&(df['frontcam']==string6)&(df['primarycam']==string7)]
        ab=Label(root, text=ac)
        ab.grid(row=11, column=1, sticky='e',padx=10, pady=20)
    elif(string2==''):
        ac=df.loc[(df['company']==string1)&(df['ROMGB']==string3)&(df['Battery power']==string4)&(df['generation']==string5)&(df['frontcam']==string6)&(df['primarycam']==string7)]
        ab=Label(root, text=ac)
        ab.grid(row=11, column=1, sticky='e',padx=10, pady=10)
    elif(string3==''):
        ac=df.loc[(df['company']==string1)&(df['RAMGB']==string2)&(df['Battery power']==string4)&(df['generation']==string5)&(df['frontcam']==string6)&(df['primarycam']==string7)]
        ab=Label(root, text=ac)
        ab.grid(row=11, column=1, sticky='e',padx=10, pady=10)
    elif(string4==''):
        ac=df.loc[(df['company']==string1)&(df['RAMGB']==string2)&(df['ROMGB']==string3)&(df['generation']==string5)&(df['frontcam']==string6)&(df['primarycam']==string7)]
        ab=Label(root, text=ac)
        ab.grid(row=11, column=1, sticky='e',padx=10, pady=20)
    elif(string5==''):
        ac=df.loc[(df['company']==string1)&(df['RAMGB']==string2)&(df['ROMGB']==string3)&(df['Battery power']==string4)&(df['frontcam']==string6)&(df['primarycam']==string7)]
        ab=Label(root, text=ac)
        ab.grid(row=11, column=1, sticky='e',padx=10, pady=20)
    elif(string6==''):
        ac=df.loc[(df['company']==string1)&(df['RAMGB']==string2)&(df['ROMGB']==string3)&(df['Battery power']==string4)&(df['generation']==string5)&(df['primarycam']==string7)]
        ab=Label(root, text=ac)
        ab.grid(row=11, column=1, sticky='e',padx=10, pady=20)
    elif(string7==''):
        ac=df.loc[(df['company']==string1)&(df['RAMGB']==string2)&(df['ROMGB']==string3)&(df['Battery power']==string4)&(df['generation']==string5)&(df['frontcam']==string6)]
        ab=Label(root, text=ac)
        ab.grid(row=11, column=1, sticky='e',padx=10, pady=20)

    else:
        ac=df.loc[(df['company']==string1)&(df['RAMGB']==string2)&(df['ROMGB']==string3)&(df['Battery power']==string4)&(df['generation']==string5)&(df['frontcam']==string6)&(df['primarycam']==string7)]
        ab=Label(root, text=ac)
        ab.grid(row=11, column=1, sticky='e',padx=10, pady=10)
        
Title=Label(root,text="Mobile recommendation",font=('Arial 20 bold'), bg="black",fg="white")
Title.grid(row=1, column=1, pady=20, columnspan=2)
root.title("a")
#company entry
comp=Label(root,text="Enter the company name:",font=('Forte 20 bold'), bg="lightgrey",fg="black")
comp.grid(row=2,column=0 ,sticky='w')
e=Entry(root)
e.grid(row=2, column=1, sticky='e', padx=10, pady=10)
en=Label(root, text="eg:realme, oppo, Mi, Apple, sony, nokia, samsung")
en.grid(row=2, column=2, padx=10, pady=10)
e.focus_set()
#RAM
ram=Label(root,text="Enter the RAM in GB:",font=('Forte 20 bold'), bg="lightgrey",fg="black")
ram.grid(row=3,column=0 ,sticky='w')
s=Entry(root)
s.grid(row=3, column=1, sticky='e', padx=10, pady=10)
sn=Label(root, text="eg:4,6,8 in GB") 
sn.grid(row=3, column=2)
s.focus_set
#ROM
rom=Label(root,text="Enter the ROM in GB:",font=('Forte 20 bold'), bg="lightgrey",fg="black")
rom.grid(row=4,column=0 ,sticky='w')
t=Entry(root)
t.grid(row=4, column=1, sticky='e',padx=10, pady=10)
tn=Label(root, text="eg:32,64,128 in GB")
tn.grid(row=4, column=2)
t.focus_set
#Battery power
bat=Label(root,text="Enter the battery power in mah:",font=('Forte 20 bold'), bg="lightgrey",fg="black")
bat.grid(row=5,column=0 ,sticky='w')
u=Entry(root)
u.grid(row=5, column=1, sticky='e',padx=10, pady=10)
un=Label(root, text="eg:2000, 2500, 3000, 35000, 4000, 45000, 5000 in Mah")
un.grid(row=5, column=2)
u.focus_set
#generation
gen=Label(root,text="Enter the generation:",font=('Forte 20 bold'), bg="lightgrey",fg="black")
gen.grid(row=6,column=0 ,sticky='w')
l=Entry(root)
l.grid(row=6, column=1, sticky='e',padx=10, pady=10)
ln=Label(root, text="eg:3G, 4G, 5G ")
ln.grid(row=6, column=2)
l.focus_set
#frontcam
front=Label(root,text="Enter the frontcam pixel:",font=('Forte 20 bold'), bg="lightgrey",fg="black")
front.grid(row=7,column=0 ,sticky='w')
h=Entry(root)
h.grid(row=7, column=1, sticky='e',padx=10, pady=10)
hn=Label(root, text="eg:15,20,25,35,45,50 in mega pixel")
hn.grid(row=7, column=2)
h.focus_set
#primary
primary=Label(root,text="Enter the primarycam pixel:",font=('Forte 20 bold'), bg="lightgrey",fg="black")
primary.grid(row=8,column=0 ,sticky='w')
i=Entry(root)
i.grid(row=8, column=1, sticky='e',padx=10, pady=10)
ins=Label(root, text="eg:15,20,25,35,45,50 in mega pixel")
ins.grid(row=8, column=2)
i.focus_set
#Note
note=Label(root,text="NOTE: User must enter minimum 6 specifications to get desired output")
note.grid(row=9, column=1, padx=10, pady=10)
#button
Result_button=Button(root, text="Result", font=('Arial 15 bold'), height=1, width=10, bg="lightgrey", command=printtext)
Result_button.grid(row=10,column=1 , sticky='e')

root.mainloop()

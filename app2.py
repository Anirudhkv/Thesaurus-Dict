import mysql.connector
from difflib import get_close_matches
con=mysql.connector.connect(
user="ardit700_student",
password="ardit700_student",
host="108.167.140.122",
database="ardit700_pm1database"
)

def translate(w):
  l=[]  
  w=w.lower()
  cursor=con.cursor()
  q1=cursor.execute("SELECT Expression FROM Dictionary")
  r1=cursor.fetchall()
  for i in r1:
      l.append(i[0])
  if w in l:
      q2=cursor.execute("SELECT * FROM Dictionary WHERE Expression='%s'"%w)
      r2=cursor.fetchall()
      for r in r2:
       print(r[1])
  elif len(get_close_matches(w,l))>0:
        while(1):
 
         c=str(input("Did you mean %s instead?Y/N " % get_close_matches(w,l)[0]))
         if c=="Y" or c=="y":
            q3=cursor.execute("SELECT * FROM Dictionary WHERE Expression='%s'"%get_close_matches(w,l)[0])
            r3=cursor.fetchall()
            for r in r3:
              print(r[1])


            break
         elif c=="N" or c=="n":
            print("Please check the word again")  
            break   
         else:
             print("Invalid choice")  


  else:
         print("Not found")
          
while(1):        
 a=str(input('Enter the word :'))
 translate(a)
 ch=str(input("Do you want to continue(Y/N): "))
 if ch=="N" or ch=="n":
     break
 elif ch=="Y" or ch=="y":
     continue
 else:
     print("Invalid choice")     
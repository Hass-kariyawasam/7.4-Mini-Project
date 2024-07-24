x = []
fast = input("Countunu this Project (Y/N) : ")

if fast == "Y" :
    Run = fast
    
    while Run == "Y" :
        Run = input("Add anthor Number (Y/N) : ")
        y = int(input("Input your Number : "))  
        x.append(y) 
        Min ,Max = x[0],x[0]
        total = 0
        for i in x :
          total += i
          if i > Max :
             Max = i
          else :
             continue
    
          if i < Min :
             Min = i
          else :
             continue
    print(x)    
    print("Total",total)      
    print("Avg",total/len(x))  
    print("Max",Max)  
    print("Min",Min)
    
else :
    print("program end.")
    print("program end.")
   print("program end.")

                                          


    

    



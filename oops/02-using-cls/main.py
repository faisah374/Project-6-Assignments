class Counter:
     count= 0
     def __init__(self):
         Counter.count += 1
         
     @classmethod
     def show_count(cls):
             print(f"Count of  obj is: {cls.count}")

obj1 = Counter()
obj2 = Counter() 
obj3 = Counter() 
Counter.show_count()


       
           
      

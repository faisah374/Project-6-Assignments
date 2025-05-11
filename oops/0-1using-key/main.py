class Student():
      def __init__(self,name,marks):
        self.name= name
        self.marks= marks
      def display(self):
       print(f"{self.name} gets {self.marks} marks")
            
if __name__=="__main__":
      student1=Student("faisal", 75)
      student1.display()


     
           
   
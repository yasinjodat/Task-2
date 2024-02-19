class StudentsInMLOPs:
    students=[]
    def __init__(self) -> None:
        self.student=[]
        self.className=[]
    def enrollstudents(self,student,ClassName):
        self.student.append(student)
        self.className.append(ClassName)
    def dropStudents(self,studentId,ClassID):
        for i in range(len(self.student,)):
            if self.student[i] == studentId and self.className[i]==ClassID:
                temp=i
        print(len(self.className))
        self.students[temp].drop()
        self.className[temp].drop()
    def getTotalStrength(self):
        return len(self.student)
    def getClassName(self):
        return self.className
    


                
            
        
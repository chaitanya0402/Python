class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def get_number_of_marks(self):
        return len(self.marks)
    def Sum_of_marks(self):
        return sum(self.marks)
s1=student ("Chaitanya",[70,80,90])
s2=student.get_number_of_marks(s1)
s3=student.Sum_of_marks(s1)
print(f"""student[
       number_of_marks-{s2}
       sum-{s3}]""")



from pprint import pprint

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print ("Не студент второй, обидно")
            return
        if self.average_rate(self.grades) > other.average_rate(other.grades):
            print (f'Студент {self.name} {self.surname} круче \
чем студент {other.name} {other.surname} на \
{self.average_rate(self.grades) - other.average_rate(other.grades)}')
        else:
            print (f'Студент {other.name} {other.surname} круче \
чем студент {self.name} {self.surname} на \
{other.average_rate(other.grades) - self.average_rate(self.grades)}')
            
    def add_course_student(self,add_course):
        ''' Add course in learning'''
        if add_course in self.courses_in_progress:
            print ("Данный курс уже есть")
        else:
            self.courses_in_progress.append(add_course)
            print (f'Курс {add_course} добавлен')
                
    def rate_who (self, who, course, grade):
        """Function billing rate lecturer and student"""
        if (isinstance (who, Lecturer) and course in who.courses_attached) or (isinstance(who, Student) and course in who.courses_in_progress):
         if course in who.grades:
             who.grades[course] += [grade]
         else:
             who.grades[course] = [grade]
        else:
            return 'Лектор не читает данный курс или студент не учиться на данном курсе'   
    
    def average_rate(self, average_rate_grades, key = 0):
        ''' Function average counting rate
        key == 0 -  work standart, all course
        key = key_course - work one course'''
        if key == 0:
            summa = 0
            count_rate = 0
            values_list = list(average_rate_grades.values())
            if len(values_list) == 0:
                return 'Division by 0'
            for i1 in range  (0,len(values_list)):
                for i2 in range(0,len(values_list[i1])):
                    summa += (values_list[i1][i2])
                    count_rate += 1
            return float(summa/count_rate)
        elif key in average_rate_grades:
           summa = 0
           count_rate = 0
           values_list = average_rate_grades[key]
           for i1 in range  (0,len(values_list)):
                summa += (values_list[i1])
                count_rate += 1
           return float(summa/count_rate)
        else:
            return 'Error, Call == 1 or Key_course' 
    
    def output_list(self, output_list):
        str =''
        for i1 in output_list:
            str += i1 + ' '
        return str
             
    def __str__(self):
      res = f'\nИмя: {self.name}\nФамилия: {self.surname}\n\
Средние оценки за ДЗ: {round(self.average_rate(self.grades), 2)}\n\
Курсы в процессе изучения: {self.output_list(self.courses_in_progress)}\n\
Оконченные курсы: {self.output_list(self.finished_courses)}'
      return res 
    
    
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    def add_course_mentor(self,add_course):
        if add_course in self.courses_attached:
            print ("Данный курс уже есть")
        else:
            self.courses_attached.append(add_course)
            print (f'Курс {add_course} добавлен')
        

   
class Lecturer (Mentor, Student):
    def __init__(self, name, surname):
        super().__init__(name,surname)
        self.grades = {}
    def __str__(self):
      res = f'\nИмя: {self.name}\nФамилия: {self.surname}\n\
Средние оценки за лекции: {round(self.average_rate(self.grades), 2)}'
      return res 
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print ("Не лекторы второй, обидно")
            return
        if self.average_rate(self.grades) > other.average_rate(other.grades):
            print (f'Лектор {self.name} {self.surname} круче читает лекции\
чем лектор {other.name} {other.surname} на \
{self.average_rate(self.grades) - other.average_rate(other.grades)}')
        else:
            print (f'Лектор {other.name} {other.surname} круче читает лекции\
чем лектор {self.name} {self.surname} на \
{other.average_rate(other.grades) - self.average_rate(self.grades)}')
  
class Reviewer (Mentor, Student):
    def __str__(self):
      res = f'\nИмя: {self.name}\nФамилия: {self.surname}'
      return res     

def average_rate_course(who_list, course):
    var_average_rate_course = 0
    count = 0
    for i1 in range(0, len(who_list)):
        var_average_rate_course += who_list[i1].average_rate(who_list[i1].grades, course)
        count += 1
    return round (float (var_average_rate_course/count), 2)    

if __name__ == '__main__':
   student1 = Student('N1','N2','m')
   student2= Student('Girl1','Girl2','w')
   student1.courses_in_progress += ['PHP']
   student1.courses_in_progress += ['PHP_PHP']
   student1.courses_in_progress += ['PHP_PHP_PHP']
   student2.courses_in_progress += ['PHP']
   student2.courses_in_progress += ['PHP_PHP']
   student2.courses_in_progress += ['Python']
   student1.finished_courses += ['Python']
   student2.finished_courses += ['PHP_PHP_PHP']
   student2.finished_courses += ['Prolog']
   reviewer1 = Reviewer('Test1','Test2')
   reviewer1.rate_who(student1, 'PHP', 10)
   reviewer1.rate_who(student1, 'PHP', 8)
   reviewer1.rate_who(student1, 'PHP', 7)
   reviewer1.rate_who(student1, 'PHP_PHP', 10)
   reviewer1.rate_who(student1, 'PHP_PHP', 8)
   reviewer1.rate_who(student2, 'PHP', 15)
   reviewer1.rate_who(student2, 'PHP', 11)
   reviewer1.rate_who(student1, 'PHP', 9)
   reviewer1.rate_who(student2, 'PHP_PHP', 20)
   reviewer1.rate_who(student2, 'PHP_PHP', 28)
   reviewer1.rate_who(student2, 'PHP_PHP', 27) 
   reviewer1.rate_who(student1, 'PHP_PHP', 7) 
   lec1 = Lecturer ('Lec_1_1','Lec_1_2')
   lec2 = Lecturer('LEC_2_1','LEC_2_2')
   lec1.add_course_mentor('PHP')
   lec2.add_course_mentor('PHP')
   student1.rate_who(lec1, 'PHP', 9)
   student2.rate_who(lec1, 'PHP', 15)
   student1.rate_who(lec2, 'PHP', 29)
   student2.rate_who(lec2, 'PHP', 25)
   print(student1)
   print(student2)
   print(lec1)
   print(lec2)
   print(reviewer1)
   reviewer1.add_course_mentor('PHP')
   reviewer1.add_course_mentor('PHP')
   lec1.add_course_mentor('Prolog')
   print(reviewer1)
   average_st1=student1.average_rate(student1.grades, 'PHP')
   average_st2=student2.average_rate(student2.grades, 'PHP')
   average_lec1=lec1.average_rate(lec1.grades, "PHP")
   average_lec2=lec2.average_rate(lec2.grades, "PHP")
   print (average_st1)
   print (average_st2)
   print (average_lec1)
   print (average_lec2)
   list_student = []
   list_student.append(student1)
   list_student.append(student2)
   list_lec = []
   list_lec.append(lec1)
   list_lec.append(lec2)
   print(average_rate_course(list_student,"PHP"))
   print(f'Средняя оценка лекторов за курс PHP: {average_rate_course(list_lec,"PHP")}')
   print(f'Средняя оценка студентов за курс PHP: {average_rate_course(list_student,"PHP")}')
   print (lec1 < lec2) 
   print (student1 < student2)  
   
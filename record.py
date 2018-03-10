# Sample static data

command_list = {'my': {'grades':'Retrieve your current course grades', 'study':'Retrieve your Study details',
            'review':'Have a practice review before your actual exam', 'mates':'Retrieve your classmates details',
            'dates':'Retrieve your upcoming important deadlines'}, 'bot':{'help':'list all the commands available'}}


grade_list = ({'IT Systems':{'Workshop': '85', 'Project': '90', 'Presentation': '80', 'Exam': '92'}},
               {'Data Handling': {'Project 1': '80', 'Project 2': '86', 'Task 1': '91', 'Task 2': '90', 'Exam': '82'}},
               {'Professional Practice': {'Workshop': '85', 'Project': '84', 'Task': '90', 'Exam': '92'}},
               {'Programming Principles': {'Workshop': '83', 'Project': '80', 'Task 1': '83', 'Task 2': '90', 'Exam': '92'}},
               {'Computer Servicing': {'Workshop': '92', 'Project': '85', 'Presentation': '89', 'Exam': '83'}},
               {'Operating Systems': {'Project': '86', 'Task': '90', 'Exam': '88'}},
               {'Networking': {'Workshop': '80', 'Project': '85', 'Exam': '77'}},
               {'System Administration': {'Task': '81', 'Presentation': '75', 'Exam': '83'}})

date_list = ({'IT Systems':{'Workshop': '18 Apr 2018 0900H', 'Project': '18 Apr 2018', 'Presentation': '18 Apr 2018 0900H', 'Exam': '18 Apr 2018 0900H'}},
               {'Data Handling': {'Project 1': '18 Apr 2018', 'Project 2': '18 Apr 2018','Exam': '18 Apr 2018 0900H'}},
               {'Professional Practice': {'Workshop': '18 Apr 2018 0900H', 'Project': '18 Apr 2018', 'Exam': '18 Apr 2018 0900H'}},
               {'Programming Principles': {'Workshop': '18 Apr 2018 0900H', 'Project': '18 Apr 2018', 'Exam': '18 Apr 2018 0900H'}},
               {'Computer Servicing': {'Workshop': '18 Apr 2018 0900H', 'Project': '18 Apr 2018', 'Presentation': '18 Apr 2018 0900H', 'Exam': '18 Apr 2018 0900H'}},
               {'Operating Systems': {'Project': '18 Apr 2018','Exam': '18 Apr 2018 0900H'}},
               {'Networking': {'Workshop': '18 Apr 2018 0900H', 'Project': '18 Apr 2018', 'Exam': '18 Apr 2018 0900H'}},
               {'System Administration': {'Presentation': '18 Apr 2018 0900H', 'Exam': '18 Apr 2018 0900H'}})

period_list = ({'IT Systems': '29 Jan 2018  -  12 Feb 2018'},
               {'Data Handling': '29 Jan 2018  -  12 Feb 2018'},
               {'Professional Practice': '29 Jan 2018  -  12 Feb 2018'},
               {'Programming Principles': '29 Jan 2018  -  12 Feb 2018'},
               {'Computer Servicing': '29 Jan 2018  -  12 Feb 2018'},
               {'Operating Systems': '29 Jan 2018  -  12 Feb 2018'},
               {'Networking': '29 Jan 2018  -  12 Feb 2018'},
               {'System Administration': '29 Jan 2018  -  12 Feb 2018'})

student_list = ({'Tom Sawyer' : {'House':'Gryffindor','Study':'Computer Science', 'Email':'tom@gryffindor.com','Club': 'Book Club'}},
                {'Huckleberry Finn': {'House':'Slytherin','Study':'Information Technology','Email':'huckleberry@slytherin.com','Club': 'Music Club'}},
                {'Hannibal Lecter': {'House':'Hufflepuff','Study':'Computer Science', 'Email':'hannibal@hufflepuff.com','Club': 'Sports Club'}},
                {'Scarlett O\'Hara': {'House':'Ravenclaw ','Study':'Network Engineering','Email':'scarlett@ravenclaw.com', 'Club': 'Book Club'} },
                {'Jay Gatsby': {'House':'Gryffindor','Study':'Information Technology', 'Email':'jay@gryffindor.com', 'Club': 'Sports Club'} })

inst_date_list = ({'February 2018':{'14 Feb 0900H': {'Workshop': 'Build a Desktop PC'}, '21 Feb 1400H': {'Presentation':'Network Security'}, '27 Feb 1500H': {'Workshop':'Build a Desktop PC'}}},
                {'March 2018': {'03 Mar 0800H': {'Workshop': 'Build a Desktop PC'}, '18 Mar 1300H': {'Presentation':'Network Security'}}},
               {'April 2018': {'21 Feb 1400H': {'Presentation':'Network Security'}, '10 Apr 1000H': {'Workshop': 'Build a Desktop PC'}}})


Q1 = 'You are creating a custom Distance class. You want to ease the conversion from your Distance class to a double. What should you add? \n' \
     'A. Nothing; this is already possible. \n' \
     'B. An implicit cast operator. \n' \
     'C. An explicit cast operator. \n' \
     'D. A static Parse method.'
Q1E = 'A. Incorrect: A conversion between a custom class and a value type does not exist by default. \n' \
      'B. Correct: Adding an implicit operator will enable users of your class to convert between Distance and double without any extra work. \n' \
      'C: Incorrect: Although adding an explicit cast operator will enable users of the class to convert from Distance to double, they will still need to explicitly cast it. \n' \
      'D: Incorrect: A Parse method is used when converting a string to a type. It doesn\'t add conversions from your type to another type. \n'

Q2 = 'You are creating a new collection type and you want to make sure the elements in it can be easily accessed. What should you add to the type? \n' \
     'A. Constructor \n' \
     'B. Indexer property \n' \
     'C. Generic type parameter \n' \
     'D. Static property'
Q2E = 'A: Incorrect: A constructor is used to create an instance of a new type \n' \
      'B. Correct: An indexer property enables the user of the type to easily access a type that represents an array-like collection. \n' \
      'C. Incorrect: Making the type generic enables you to store multiple different types inside your collection. \n' \
      'D. Incorrect: A static property cannot access the instance data of the collection.\n'

Q3 = 'You are creating a generic class that should work only with reference types. Which type constraint should you add? \n' \
     'A: where T: class \n' \
     'B. where T: struct \n' \
     'C. where T: new() \n' \
     'D. where T: IDisposable'

Q3E = 'A. Correct: Constraining your generic type parameter to class allows the class to be used only with reference type. \n' \
      'B. Incorrect: This will constrain the class to be used with a value type, not a reference type \n' \
      'C. Incorrect: This will constrain the class to be used with a type that has an empty default constructor. It can be both a value and a reference type. \n' \
      'D. Incorrect: This constrain the class to be used with a type that implements the IDisposable interface. \n'




question_list = ({'Q1' : { 'Question': Q1, 'B':Q1E }},
                {'Q2' : { 'Question': Q2, 'B':Q2E }},
                {'Q3' : { 'Question': Q3, 'A':Q3E }})
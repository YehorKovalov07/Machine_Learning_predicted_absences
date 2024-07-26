import pandas as pd 

from sklearn.tree import DecisionTreeClassifier

Data = pd.read_csv('Student_performance_data _.csv')

x = Data.drop(columns=['Ethnicity', 'ParentalEducation', 'Tutoring','Extracurricular','GPA','GradeClass','Absences','StudentID'])

y = Data['Absences']

model = DecisionTreeClassifier()

model.fit(x,y)

try:

    Age = int(input('Enter your age: '))
    
    gender = int(input('Enter your gender(0 for female, 1 for male): '))

    StudyTimeWeekly = int(input('Enter your study time(Weekly): '))
    
    ParentalSupport = int(input('Enter your parental support(0-4): '))

    music = int(input('Enter your music involvement(0 or 1): '))
    
    sports = int(input('Enter your sports involvement(0 or 1): '))

    Volunteering= int(input("Enter your volunteering involvement(0 or 1): "))

except ValueError:
    print('Incorrect values! Please enter numerical values only.')
 

Result = model.predict([[Age,gender,StudyTimeWeekly,ParentalSupport,music,sports,Volunteering]])

print('Your predicted absences: ',Result)

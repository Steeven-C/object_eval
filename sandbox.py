from etudiant import Student
from note import Test

test = [Test(12),Test(11)]
student = Student("Toto")

print(f'{student.name} as une moyenne de {test._mean} en chimie')



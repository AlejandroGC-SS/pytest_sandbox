import pytest
from source.school import Classroom, Teacher, Student, TooManyStudents

@pytest.fixture
def mcgonagall():
  return Teacher("Minerva McGonagall")

@pytest.fixture
def students():
  # 9/10 students list
  students_list = [
    "Harry Potter",
    "Hermione Granger",
    "Ron Weasly",
    "Drako Malfoy",
    "Alejandro Garcia",
    "Evil Harry Potter",
    "Evil Hermione Granger",
    "Evil Ron Weasly",
    "Evil Drako Malfoy"
  ]
  return [Student(name) for name in students_list]

@pytest.fixture
def transfiguration_class(mcgonagall, students):
  return Classroom(mcgonagall, students, "Transfiguration")


def test_add_student(transfiguration_class: Classroom):
  new_student = "Luis Quijada"
  transfiguration_class.add_student(new_student)
  assert new_student in transfiguration_class.students


def test_too_many_students(transfiguration_class: Classroom):
  tenth_student = "Luis Quijada"
  eleventh_student = "Luis Davilla"
  with pytest.raises(TooManyStudents):
    transfiguration_class.add_student(tenth_student)
    transfiguration_class.add_student(eleventh_student)


@pytest.mark.parametrize("student_name", [ "Ron Weasly","Drako Malfoy"])
def test_remove_student(transfiguration_class: Classroom, student_name):
  transfiguration_class.remove_student(student_name)
  for student in transfiguration_class.students:
    assert student.name != student_name


def test_change_teacher(transfiguration_class: Classroom):
  new_teacher = "Alejandra"
  transfiguration_class.change_teacher(new_teacher)
  assert transfiguration_class.teacher == new_teacher



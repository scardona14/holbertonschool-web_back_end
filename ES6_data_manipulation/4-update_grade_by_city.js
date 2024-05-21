function updateStudentGradeByCity(students, city, grade) {
  if (!Array.isArray(students)) {
    return [];
  }

  const result = students.filter((student) => student.location === city);

  result.forEach((student) => {
    grade.forEach((newGrade) => {
      if (student.id === newGrade.studentId) {
        student.grade = newGrade.grade;
      }
    });
  });

  return result;
}

export default updateStudentGradeByCity;

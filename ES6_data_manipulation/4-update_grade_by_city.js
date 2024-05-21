function updateStudentGradeByCity(students, city, grade) {
  if (!Array.isArray(students)) {
    return [];
  }
  if (!Array.isArray(grade)) {
    return [];
  }

  const studentsByCity = students.filter((student) => student.location === city);

    const updatedStudents = studentsByCity.map((student) => {
        const gradeFilter = grade.filter((gradeStudent) => gradeStudent.studentId === student.id);

        let grade;

        if (gradeFilter[0]) {
            grade = gradeFilter[0].grade;
        } else {
            grade = 'N/A';
        }

        return {
            ...student,
            grade
        };
    }
    );

    return updatedStudents;
}

export default updateStudentGradeByCity;

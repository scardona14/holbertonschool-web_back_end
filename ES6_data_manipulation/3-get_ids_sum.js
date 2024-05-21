function getStudentIdsSum(students) {
  if (!Array.isArray(students)) {
    return [];
  }

  const reducer = (accumulator, student) => accumulator + student.id;

  const sum = students.reduce(reducer, 0);

  return sum;
}

export default getStudentIdsSum;

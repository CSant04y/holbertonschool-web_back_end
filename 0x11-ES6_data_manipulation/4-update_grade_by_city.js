const updateStudentGradeByCity = (listOfStudents, city, newGrades) => {
  const ret = listOfStudents.filter((student) => student.location === city)
    .map((item) => {
      const newObj = item;
      console.log(newObj);
      const newStudent = newGrades.find((student) => student.studentId === item.id);

      if (newStudent) newObj.grade = newStudent.grade;
      else newObj.grade = 'N/A';

      return newObj;
    });
  return ret;
};
export default updateStudentGradeByCity;

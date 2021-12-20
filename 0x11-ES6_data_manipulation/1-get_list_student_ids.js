const getListStudentIds = (studentList) => ((Array.isArray(studentList) && studentList)
  ? studentList.map((item) => item.id) : []);

export default getListStudentIds;

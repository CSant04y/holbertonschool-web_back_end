const getStudentIdsSum = (student) => student.reduce((item, num) => item + num.id, 0);

export default getStudentIdsSum;

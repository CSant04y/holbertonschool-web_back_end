const getStudentsByLocation = (student, city) => student.filter((item) => (item.location === city));

export default getStudentsByLocation;

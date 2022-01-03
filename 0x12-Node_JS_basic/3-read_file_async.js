const fs = require('fs');

async function countStudents(path) {
  let data;
  const dataView = {};
  const fields = {};
  try {
    data = await fs.promises.readFile(path, 'utf-8');
    // data = fs.readFileSync(path);
  } catch (err) {
    console.log(err);
    throw new Error('Cannot load the database');
  }
  // console.log(data);

  data = data.toString().split('\n');
  data = data.filter((element) => element.length > 0);
  data.shift();

  data.forEach((element) => {
    if (element.length > 0) {
      const row = element.split(',');
      if (row[3] in fields) {
        fields[row[3]].push(row[0]);
      } else {
        fields[row[3]] = [row[0]];
      }
    }
  });
  console.log(fields);
  dataView.numberOfStudents = `Number of students: ${data.length}`;
  dataView.studentFields = [];
  for (const field in fields) {
    if (field) {
      const list = fields[field];

      dataView.studentFields.push(`Number of students in ${field}: ${list.length}. List: ${list.toString().replace(/,/g, ', ')}`);
    }
  }
  console.log(dataView);
  return dataView;
}

module.exports = countStudents;

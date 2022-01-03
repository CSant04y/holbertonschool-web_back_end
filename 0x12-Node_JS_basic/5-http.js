const http = require('http');
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

const hostname = '127.0.0.1';
const port = '1245';

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') res.end('Hello Holberton School!');

  if (req.url === '/students') {
    res.write('This is the list of our students\n');
    console.log(`This is process.argv[2]: ${process.argv[2]}, This is type: ${typeof process.argv[2]}`);
    countStudents(process.argv[2]).then((dataView) => {
      console.log(dataView);
      res.write([`${dataView.numberOfStudents}`].concat(dataView.studentFields).join('\n'));
      res.end();
    }).catch((error) => {
      res.end(error.message);
    });
  }
});

app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});

module.exports = app;

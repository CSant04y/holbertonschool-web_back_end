export default function createIteratorObject(report) {
  let result = [];
  for (const item of Object.values(report.allEmployees)) {
    result = [...result, ...item];
  }
  return result;
}

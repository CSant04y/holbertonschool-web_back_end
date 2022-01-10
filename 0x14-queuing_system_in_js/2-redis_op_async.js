import { createClient } from 'redis';
const { promisify } = require('util');

const client = createClient();
const getSchoolVal = promisify(client.get).bind(client);
// This is a simple connection to a reddis client

(async () => {
  // Handles if connection is errored out
  client.on('error', (err) => console.log('Redis client not connected to the server: ', err));
  // Handles if connection works between server and client
  client.on('ready', () => console.log('Redis client connected to the server'));

  await client.connect();
})();

function setNewSchool(schoolName, value) {
  const setkey = client.set(schoolName, value, (reply) => reply);
  setkey.then((res) => {
    console.log(`Reply: ${res}`);
  });
}

async function displaySchoolValue(schoolName) {
  const value = await getSchoolVal(schoolName);
  console.log(value);
  // value.then((res) => console.log(res));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

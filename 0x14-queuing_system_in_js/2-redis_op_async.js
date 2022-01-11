import { createClient } from 'redis';

const { promisify } = require('util');

const client = createClient();
const getSchoolVal = promisify(client.get).bind(client);

client
  .on('error', (err) => console.log('Redis client not connected to the server: ', err))
  .on('connect', () => console.log('Redis client connected to the server'));

async function setNewSchool(schoolName, value) {
  const setkey = await client.set(schoolName, value, (reply) => reply);
  console.log(`Reply: ${setkey}`);
}

async function displaySchoolValue(schoolName) {
  const value = await getSchoolVal(schoolName);
  console.log(value);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

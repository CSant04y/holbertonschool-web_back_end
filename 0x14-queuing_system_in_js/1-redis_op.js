import { createClient } from 'redis';

// This is a simple connection to a reddis client
const client = createClient();
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

function displaySchoolValue(schoolName) {
  const value = client.get(schoolName, (reply) => reply);
  value.then((res) => console.log(res));
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');

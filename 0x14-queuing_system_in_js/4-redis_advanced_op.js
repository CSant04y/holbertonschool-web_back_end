import redis, { createClient } from 'redis';

const client = createClient();

const cities = {
  Portland: '50',
  Seattle: '80',
  'New York': '20',
  Bogota: '20',
  Cali: '40',
  Paris: '2',
};

const keys = Object.keys(cities);

for (let i = 0; i < keys.length; i += 1) {
  client.hset('HolbertonSchools', keys[i], cities[keys[i]], redis.print);
}

client.hgetall('HolbertonSchools', (err, res) => {
  if (err) throw Error('Could not retrive value');
  console.log(res);
});

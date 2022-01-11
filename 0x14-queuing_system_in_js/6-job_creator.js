const kue = require('kue');

const queue = kue.createQueue();
const jobData = {
  phoneNumber: '000-000-0000',
  message: 'Hello world',
};

const queueName = 'push_notification_code';

const job = queue.create(queueName, jobData).save((err) => {
  if (!err) console.log(`Notification job created: ${job.id}`);
});

job.on('complete', () => console.log('Notification job completed'));

job.on('failed', () => console.log('Notification job failed'));

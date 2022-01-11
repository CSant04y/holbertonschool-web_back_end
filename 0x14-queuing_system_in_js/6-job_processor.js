const kue = require('kue');

const queue = kue.createQueue();
const jobData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
};

const queueName = 'push_notification_code';

const sendNotification = (phoneNumber, message) => {
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
};

const job = queue.create(queueName, jobData).save((err) => {
  sendNotification(jobData.phoneNumber, jobData.message);
});

job.on('complete', () => console.log('Notification job completed'));

job.on('failed', () => console.log('Notificaiton job failed'));

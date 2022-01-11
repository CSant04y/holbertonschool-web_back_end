const kue = require('kue');

const blacklistedNum = ['4153518780', '4153518781'];
const queue = kue.createQueue();

function sendNotification(phoneNumber, message, job, done) {
  const total = 100;
  job.progress(0, total);
  if (blacklistedNum.includes(phoneNumber)) {
    done(Error(`Phone number ${phoneNumber} is blacklisted`));
    return;
  }
  job.progress(50, total);
  console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
  done();
}

const queueName = 'push_notification_code_2';

queue.process(queueName, 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});

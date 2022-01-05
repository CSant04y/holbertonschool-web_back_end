const Utils = require('./utils.js');
const sendPaymentRequestToApi = (totalAmount, totalShipping) => {
    let total = 0;
    total = Utils.calculateNumber("SUM", totalAmount, totalShipping);
    console.log(`The total is: ${total}`);
}

module.exports = sendPaymentRequestToApi;

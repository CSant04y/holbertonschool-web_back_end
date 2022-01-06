const expect = require('chai').expect;
const getPaymentTokenFromAPI = require('./6-payment_token-0');

describe("getPaymentTokenFromAPI function", () => {
  it("testing async function with promise", (done) => {
    getPaymentTokenFromAPI(true)
      .then((res) => {
          expect(res).to.eql({ data: 'Successful response from the API' })
      });
      done();
  });
})

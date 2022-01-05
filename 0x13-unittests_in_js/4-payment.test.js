const sinon = require("sinon");
const expect = require("chai").expect
const sendPaymentRequestToApi = require('./3-payment.js');
const Utils = require('./utils.js');


describe("sendPaymentRequestToApi", function () {

    const logSpy = sinon.spy(console, 'log');
    
    it("Tests Utils function", () => {
      const utilStub = sinon.stub(Utils, "calculateNumber");
      utilStub.withArgs('SUM', 100, 20).returns(10);
      sendPaymentRequestToApi(100, 20);
      expect(logSpy.calledOnce).to.be.true;
      expect(logSpy.calledWith('The total is: 10')).to.be.true;
      utilStub.restore()
      logSpy.restore();
    });

  });

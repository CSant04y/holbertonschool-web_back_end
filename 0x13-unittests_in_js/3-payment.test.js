const sinon = require("sinon");
const expect = require("chai").expect
const sendPaymentRequestToApi = require('./3-payment.js');
const Utils = require('./utils.js');


describe("sendPaymentRequestToApi", function () {

    const utilSpy = sinon.spy(Utils, "calculateNumber");

    it("Tests Utils function", () => {
      sendPaymentRequestToApi(100, 50);
      expect(utilSpy.calledOnce).to.be.true;
      expect(utilSpy.calledWith("SUM", 100, 50)).to.be.true;
      utilSpy.restore()
    });

  });

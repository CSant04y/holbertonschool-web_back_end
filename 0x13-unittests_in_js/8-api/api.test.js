const expect = require('chai').expect;
const request = require('request');
const { spy } = require('sinon');

const header = {
    hostname: '127.0.0.1',
    port: 7865,
    method: 'GET',
}

describe ("index page", function() {
    spy(console, 'log');

    it("status code", () => {
        request('http://localhost:7865', (err, response, body) => {
            console.log(response.statusCode);
            expect(console.log.calledWith(200)).to.be.true;
        })
    });

    it('body return', () => {
        request('http://localhost:7865', (err, response, body) => {
            console.log(body);
            expect(console.log.calledWith('Welcome to the payment system')).to.be.true;
        });
    });

    it('get', () => {
        request('http://localhost:7865', (err, response, body) => {
            console.log(response.request.method);
            expect(console.log.calledWith('GET')).to.be.true;
        });
    });

});

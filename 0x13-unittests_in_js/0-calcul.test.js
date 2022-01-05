const assert = require("assert");
const calculateNumber = require("./0-calcul.js");

describe("calculateNumber", function () {
  it("Calculates postive numbers", function () {
    assert.strictEqual(calculateNumber(5.2, 1.8), 7);
    assert.strictEqual(calculateNumber(5.21, 2.89), 8);
    assert.strictEqual(calculateNumber(7.1, 2.5), 10);
  })
  it("returns sum of negative integers", function () {
    assert.strictEqual(calculateNumber(-2.5, -6.2), -8);
    assert.strictEqual(calculateNumber(-50.1, -10.8), -61);
    assert.strictEqual(calculateNumber(3.85, -10.2), -6);
    assert.strictEqual(calculateNumber(-10, 10), 0);
  });

  it("Calculates sum of zero number", function() {
    assert.strictEqual(calculateNumber(0, 0), 0);
    assert.strictEqual(calculateNumber(100.6736, 0), 101);
    assert.strictEqual(calculateNumber(0, 50.1234), 50);
  });
});
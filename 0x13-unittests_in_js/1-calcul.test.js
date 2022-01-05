const assert = require("assert");
const calculateNumber = require("./1-calcul.js");

describe("calculateNumber", function () {
  it("Calculates SUM", function () {
    assert.strictEqual(calculateNumber("SUM", 5.2, 1.8), 7);
    assert.strictEqual(calculateNumber("SUM", 5.21, 2.89), 8);
    assert.strictEqual(calculateNumber("SUM", 7.1, 2.5), 10);
  })
  it("Calculates SUBTRACTION", function () {
    assert.strictEqual(calculateNumber("SUBTRACT", -2.5, -6.2), 4);
    assert.strictEqual(calculateNumber("SUBTRACT", -50.1, -10.8), -39);
    assert.strictEqual(calculateNumber("SUBTRACT", 3.85, -10.2), 14);
    assert.strictEqual(calculateNumber("SUBTRACT", -10, 10), -20);
  });

  it("Calculates Division", function() {
    assert.strictEqual(calculateNumber("DIVIDE", 0, 0), "Error");
    assert.strictEqual(calculateNumber("DIVIDE", 100.6736, 0), "Error");
    assert.strictEqual(calculateNumber("DIVIDE", 0, 50.1234), 0);
  });
});
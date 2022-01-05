const { expect } = require("chai");
const calculateNumber = require("./1-calcul.js");

describe("calculateNumber", function () {
  it("Calculates SUM", function () {
    expect(calculateNumber("SUM", 5.2, 1.8)).to.equal(7);
    expect(calculateNumber("SUM", 5.21, 2.89)).to.equal(8);
    expect(calculateNumber("SUM", 7.1, 2.5)).to.equal(10);
  })
  it("Calculates SUBTRACTION", function () {
    expect(calculateNumber("SUBTRACT", -2.5, -6.2)).to.equal(4);
    expect(calculateNumber("SUBTRACT", -50.1, -10.8)).to.equal(-39);
    expect(calculateNumber("SUBTRACT", 3.85, -10.2)).to.equal(14);
    expect(calculateNumber("SUBTRACT", -10, 10)).to.equal(-20);
  });

  it("Calculates Division", function() {
    expect(calculateNumber("DIVIDE", 0, 0)).to.equal("Error");
    expect(calculateNumber("DIVIDE", 100.6736, 0)).to.equal("Error");
    expect(calculateNumber("DIVIDE", 0, 50.1234)).to.equal(0);
    expect(calculateNumber("DIVIDE", 10, 5)).to.equal(2);
  });
});

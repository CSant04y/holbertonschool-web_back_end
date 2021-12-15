const util = require('util');

export default class Airport {
  constructor(name, code) {
    this._name = name;
    this._code = code;
  }

  [util.inspect.custom]() {
    return `Airport [${this._code.toString()}] { _name: '${this._name.toString()}', _code: '${this._code.toString()}' }`;
  }

  toString() {
    return `[object ${this._code}]`;
  }
}

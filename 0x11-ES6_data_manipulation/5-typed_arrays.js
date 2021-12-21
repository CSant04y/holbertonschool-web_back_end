const createInt8TypedArray = (length, postion, value) => {
  if (postion > length) throw Error('Position outside range');

  const int8View = new Int8Array(length);
  int8View[postion] = value;

  // console.log(int8View);
  const { buffer } = int8View;
  const newView = new DataView(buffer, 0, length);

  return newView;
};

export default createInt8TypedArray;

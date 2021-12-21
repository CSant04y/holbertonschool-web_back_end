const cleanSet = (set, startString) => {
  if (!startString || !startString.length) return '';
  let value = '';

  for (const item of set) {
    if (item && item.startsWith(startString)) {
      value += value.length === 0 ? item.replace(startString, '') : item.replace(startString, '-');
    }
  }
  return value;
};

export default cleanSet;

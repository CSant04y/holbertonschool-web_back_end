# 0x11. ES6 data manipulation
# Resources
**Read or watch**:
*  [Array](https://intranet.hbtn.io/rltoken/DIsNNOXZExl3N3eb_ucyXQ) 
*  [Typed Array](https://intranet.hbtn.io/rltoken/EXbyPrXEhGoD1kPbiEPC9g) 
*  [Set Data Structure](https://intranet.hbtn.io/rltoken/dYX70DxM_ibZ0SlDbbscOQ) 
*  [Map Data Structure](https://intranet.hbtn.io/rltoken/weXVkufXRyUwQvQazDkzLg) 
*  [WeakMap](https://intranet.hbtn.io/rltoken/X1ba6W8dGSnUKOTN4CzPVA) 

# Learning Objectives
At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/1KBjL212N3602ZMIOnVK0A) , **without the help of Google**:

### How to use map, filter and reduce on arrays
```
Examples

Using the Set object
const mySet1 = new Set()

mySet1.add(1)           // Set [ 1 ]
mySet1.add(5)           // Set [ 1, 5 ]
mySet1.add(5)           // Set [ 1, 5 ]
mySet1.add('some text') // Set [ 1, 5, 'some text' ]
const o = {a: 1, b: 2}
mySet1.add(o)

mySet1.add({a: 1, b: 2})   // o is referencing a different object, so this is okay

mySet1.has(1)              // true
mySet1.has(3)              // false, since 3 has not been added to the set
mySet1.has(5)              // true
mySet1.has(Math.sqrt(25))  // true
mySet1.has('Some Text'.toLowerCase()) // true
mySet1.has(o)       // true

mySet1.size         // 5

mySet1.delete(5)    // removes 5 from the set
mySet1.has(5)       // false, 5 has been removed

mySet1.size         // 4, since we just removed one value

console.log(mySet1)
// logs Set(4) [ 1, "some text", {…}, {…} ] in Firefox
// logs Set(4) { 1, "some text", {…}, {…} } in Chrome

```

### Typed arrays

```
/*First of all, we will need to create a buffer, here with a fixed length of 16-bytes:*/

let buffer = new ArrayBuffer(16);

/*At this point, we have a chunk of memory whose bytes are all pre-initialized to 0. There's not a lot we can do with it, though. We can confirm that it is indeed 16 bytes long, and that's about it:*/

if (buffer.byteLength === 16) {
  console.log("Yes, it's 16 bytes.");
} else {
  console.log("Oh no, it's the wrong size!");
}

/*Before we can really work with this buffer, we need to create a view. Let's create a view that treats the data in the buffer as an array of 32-bit signed integers:
*/

let int32View = new Int32Array(buffer);


for (let i = 0; i < int32View.length; i++) {
  int32View[i] = i * 2;
}

/*This fills out the 4 entries in the array (4 entries at 4 bytes each makes 16 total bytes) with the values 0, 2, 4, and 6.*/

```

### The Set, Map, and Weak link data structures
Using map…
```
const contacts = new Map()
contacts.set('Jessie', {phone: "213-555-1234", address: "123 N 1st Ave"})
contacts.has('Jessie') // true
contacts.get('Hilary') // undefined
contacts.set('Hilary', {phone: "617-555-4321", address: "321 S 2nd St"})
contacts.get('Jessie') // {phone: "213-555-1234", address: "123 N 1st Ave"}
contacts.delete('Raymond') // false
contacts.delete('Jessie') // true
console.log(contacts.size) // 1

```

Using Weak Map…
```
const wm1 = new WeakMap(),
      wm2 = new WeakMap(),
      wm3 = new WeakMap();
const o1 = {},
      o2 = function() {},
      o3 = window;

wm1.set(o1, 37);
wm1.set(o2, 'azerty');
wm2.set(o1, o2); // a value can be anything, including an object or a function
wm2.set(o3, undefined);
wm2.set(wm1, wm2); // keys and values can be any objects. Even WeakMaps!

wm1.get(o2); // "azerty"
wm2.get(o2); // undefined, because there is no key for o2 on wm2
wm2.get(o3); // undefined, because that is the set value

wm1.has(o2); // true
wm2.has(o2); // false
wm2.has(o3); // true (even if the value itself is 'undefined')

wm3.set(o1, 37);
wm3.get(o1); // 37

wm1.has(o1); // true
wm1.delete(o1);
wm1.has(o1); // false

```

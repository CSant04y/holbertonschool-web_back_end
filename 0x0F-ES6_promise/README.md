# 0x0F. ES6 Promises
# Resources
**Read or watch**:
*  [Promise](https://intranet.hbtn.io/rltoken/mU4W2KkOd6iZ2j3wSekQVQ) 
*  [JavaScript Promise: An introduction](https://intranet.hbtn.io/rltoken/NHrFfJu-_sIrYPAfRq0yLQ) 
*  [Await](https://intranet.hbtn.io/rltoken/P_KRoM7eWMSM678vWJxN1w) 
*  [Async](https://intranet.hbtn.io/rltoken/-CM2Q4-f2aVv8Vpjaexghg) 
*  [Throw / Try](https://intranet.hbtn.io/rltoken/AQnTda-fFLGicQJSwrDEqA) 

# Learning Objectives
At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/4DZ-h_jfmyUXZ65YvNV7Xg) , **without the help of Google**:

### Promises (how, why, and what)?
* How? How does a Promise work? A promise acts as a proxy for the eventual completion of operation that returns a value or a failure reason. With this in mind, promises have handlers that allow you to work with the return values of promises.
* Why? We use promises because they work will with asynchronous code that requires operations to be run where callbacks would create hell.
* What? What is a promise? A promise is an object that represents the eventual completion or failure of a of an asynchronous operation and its values that it returns.

### How to use the then, resolve, catch methods.
* All of the handlers like **then**, **resolve**, and **catch** can be chained together to handle the **settled state** of a promise. This settled state is either the rejection of the promise or the fulfillment of it.
* How to use?
```
const myPromise = new Promise((resolve, reject) => {
	setTimout(() => {
	resolve('foo');
	}, 300);
});

myPromise
	.then(handleResolvedA, handleResolvedA)
	.then(handleResolvedB, handleResolvedB)
	.then(handleResolvedC, handleResolvedC);
```


### Throw / Try

### The await operator

### How to use an async function

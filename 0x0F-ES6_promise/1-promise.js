function getFullResponseFromAPI(success) {
  return new Promise((resolve, reject) => {
    if (success === true) {
      resolve({ status: 200, body: 'Success' });
      console.log('Got a response from the API');
    } else {
      reject(Error('The fake API is not working currently'));
    }
  });
}

export default getFullResponseFromAPI;

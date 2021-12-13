function handleResponseFromAPI(promise) {
  const resp = { status: 200, body: 'Success' };
  return promise
    .then(() => resp)
    .catch(() => Error())
    .finally(() => {
      console.log('Got a response from the API');
    });
}

export default handleResponseFromAPI;

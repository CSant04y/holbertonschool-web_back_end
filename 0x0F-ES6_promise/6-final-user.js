import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(firstName, lastName, fileName) {
  const user = await signUpUser(firstName, lastName)
    .then((value) => ({ status: 'fufilled', value }))
    .catch((error) => ({
      status: 'rejected',
      value: error,
    }));

  const photo = await uploadPhoto(fileName)
    .catch((error) => ({
      status: 'rejected',
      value: `${error.name}: ${error.message}`,
    }));

  return [user, photo];
}

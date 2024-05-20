import signUpuser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

async function handleProfileSignup(firstName, lastName, fileName) {
  const promise1 = {
    status: 'pending',
  };
  const promise2 = {
    status: 'pending',
  };
  try {
    const signUp = await signUpuser(firstName, lastName);
    promise1.status = 'fulfilled';
    promise1.value = signUp;
  } catch (error) {
    promise1.status = 'rejected';
    promise1.value = error.toString();
  }

  try {
    const upload = await uploadPhoto(fileName);
    promise2.status = 'fulfilled';
    promise2.value = upload;
  } catch (error) {
    promise2.status = 'rejected';
    promise2.value = error.toString();
  }

  return [promise1, promise2];
}

export default handleProfileSignup;

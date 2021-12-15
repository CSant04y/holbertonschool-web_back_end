import ClassRoom from './0-classroom';

export default function initializeRooms() {
  const numArray = [19, 20, 34];

  return numArray.map((item) => new ClassRoom(item));
}

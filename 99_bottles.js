function bottleSong(num, original) {
  if (original == undefined) original = num;
  if (num < 0) return
  if (num === 0) {
    console.log(`No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, ${original} bottles of beer on the wall.`)
  } else if (num === 1) {
    console.log(`1 bottle of beer on the wall, 1 bottle of beer.
Take one down and pass it around, no more bottles of beer on the wall.`)
  } else if (num === 2) {
    console.log(`2 bottles of beer on the wall, 2 bottles of beer.
Take one down and pass it around, 1 bottle of beer on the wall.`)
  } else {
    console.log(`${num} bottles of beer on the wall, ${num} bottles of beer.
Take one down and pass it around, ${num-1} bottles of beer on the wall.`)
  }
  return bottleSong(num - 1, original);
};

bottleSong();

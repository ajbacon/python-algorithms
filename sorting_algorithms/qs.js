function swap(arr, leftIndex, rightIndex) {
  var temp = arr[leftIndex];
  arr[leftIndex] = arr[rightIndex];
  arr[rightIndex] = temp;
}

function partition(arr, left, right) {
  var pivot = arr[Math.floor((right + left) / 2)], //middle element
    i = left, //left pointer
    j = right; //right pointer

  console.log(Math.floor((right + left) / 2));
  while (i <= j) {
    while (arr[i] < pivot) {
      console.log('here');
      i++;
    }
    while (arr[j] > pivot) {
      console.log('here2');
      j--;
    }
    if (i <= j) {
      swap(arr, i, j);
      i++;
      j--;
    }
  }
  console.log(arr);
  console.log(i);
  return i;
}

// var index;
// if (arr.length > 1) {
//   index = partition(arr, left, right);
//   if (left < index - 1) {
//     quickSort(arr, left, index - 1);
//   }
//   if (index < right) {
//     quickSort(arr, index, right);
//   }
// }
// return arr;
// }
// return quickSort(arr);
// };

partition([2, 1], 0, 1);

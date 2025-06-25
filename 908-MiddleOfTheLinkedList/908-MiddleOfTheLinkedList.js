// Last updated: 6/25/2025, 11:42:59 AM
var middleNode = function(head) {
  let length = 0
  let current = head

  while (current !== null){
    length++
    current = current.next
  }  

  let newLength = 0 

  if (length % 2 !== 0) newLength = Math.floor(length / 2)
  else newLength = length / 2
  for (let i=0;i < newLength;i++){
    head = head.next
  }
  return head
};

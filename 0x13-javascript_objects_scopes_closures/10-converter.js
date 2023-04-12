#!/usr/bin/node
converter = function (base)
{
    count = 0;
    if(base)
    {
        count++;
    }
    if (count == 1)
    {
        
    }
    if (count > 1)
    {
        return toString(base)
    }
}
let myConverter = converter(10);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));


myConverter = converter(16);

console.log(myConverter(2));
console.log(myConverter(12));
console.log(myConverter(89));
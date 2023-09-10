const prompt = require('prompt-sync')();

const num = prompt('Enter num limit: ');

const prime = [2];

for(var i = 3; i <= num; i++){
    var c = 0;
    var l = prime.length
    prime.forEach(ele => {
        if(i%ele != 0 ){
            c = c + 1
        }
    if(c == l){
        prime.push(i)
    }
      });
  }

console.log("primes:")

prime.forEach(i =>{
    console.log(i)
})

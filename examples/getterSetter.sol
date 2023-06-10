pragma solidity ^0.4.21;

contract Greeter{
  string public greeting;

//   constructor
  constructor() public{
      greeting = "Hello";
  }

// setter function
  function setGreeting(string _greeting) public {
      greeting = _greeting;
  }

// getter function 
 function greet() view public returns (string){
     return greeting;
 }


}
pragma solidity ^0.4.21;
contract HelloWorld {

    string message;

    constructor() public{
        message = "Hello world!";
    }

 function helloWorld() view public returns (string){
     return message;
 }
}
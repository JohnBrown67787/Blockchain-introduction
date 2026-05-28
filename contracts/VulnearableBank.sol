// SPDX-License-Identifier: MIT
pragma solidity ^0.8.28;

contract VulnerableBank {

    mapping(address => uint256) public balances;

    function deposit() public payable {
        balances[msg.sender] += msg.value;
    }

    function withdraw() public {

        uint256 amount = balances[msg.sender];

        require(amount > 0, "No balance");

        balances[msg.sender] = 0;

        (bool success, ) = msg.sender.call{value: amount}("");

        require(success, "Transfer failed");
    }
}
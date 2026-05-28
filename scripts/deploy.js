const { ethers } = require("hardhat");

async function main() {

    // Get LabToken contract factory
    const LabToken = await ethers.getContractFactory("LabToken");

    // Deploy contract
    const token = await LabToken.deploy();

    // Wait for deployment
    await token.waitForDeployment();

    // Print contract address
    console.log("LabToken deployed to:", await token.getAddress());

    // Print deployer balance
    const [owner] = await ethers.getSigners();

    const balance = await token.balanceOf(owner.address);

    console.log(
        "Owner token balance:",
        ethers.formatUnits(balance, 18),
        "LTK"
    );
}

main().catch((err) => {
    console.error(err);
    process.exit(1);
});
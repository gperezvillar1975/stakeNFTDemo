const Migrations = artifacts.require("StakeNFTDemo");

module.exports = function (deployer) {
  deployer.deploy(Migrations);
};

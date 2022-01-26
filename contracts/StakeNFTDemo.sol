// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/AccessControl.sol";

contract StakeNFTDemo is ERC721URIStorage, AccessControl {
    using Counters for Counters.Counter;

    // Access control ROLES
    bytes32 public constant ADMIN_ROLE = keccak256("ADMIN");
    bytes32 public constant STAKE_ADMIN = keccak256("STAKE");    

    // State variables
    Counters.Counter private _tokenIds;


    constructor(address _adminRole, address _stakeAdmin) ERC721("NFTDemo", "NFD") {
        require(_adminRole != address(0) && _stakeAdmin != address(0),"StakeNFTDemo: Invalid Address");
        _setupRole(ADMIN_ROLE, _adminRole);
        _setupRole(STAKE_ADMIN, _stakeAdmin);        
    }

    function mint(address player, string memory tokenURI)
        public
        onlyRole(ADMIN_ROLE)
        returns (uint256)
    {
        _tokenIds.increment();

        uint256 newItemId = _tokenIds.current();
        _mint(player, newItemId);
        _setTokenURI(newItemId, tokenURI);

        return newItemId;
    }

   function supportsInterface(bytes4 interfaceId) public view virtual override(ERC721, AccessControl) returns (bool) {
        return super.supportsInterface(interfaceId);
    }    
}

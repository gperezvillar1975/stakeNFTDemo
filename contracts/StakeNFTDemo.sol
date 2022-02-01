// SPDX-License-Identifier: MIT
pragma solidity >=0.4.22 <0.9.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract StakeNFTDemo is ERC721, Ownable {
    using Counters for Counters.Counter;

    // State variables
    Counters.Counter private _tokenIds;
    bool private _revealed;
    bool private _paused;
    mapping (address => uint256) private _whiteList; // wallets enbled to mint
    mapping(uint256 => string) private _tokenURIs;
    string private _unRevealedURI;

    constructor() ERC721("NFTDemo", "NFD") {
        _revealed = false;
        _paused = false;  
        _unRevealedURI  = "";      
    }

    // mint function
    function mint(string memory __tokenURI)
        public
        returns (uint256)
    {        
        require(! _paused,"Contract Paused");
        require(msg.sender != address(0),"Zero address");
        require(_whiteList[msg.sender] > 0 || msg.sender == owner(), "NOT Whitelisted" );

        _tokenIds.increment();

        uint256 newItemId = _tokenIds.current();
        _mint(msg.sender, newItemId);
        _setTokenURI(newItemId, __tokenURI);

        return newItemId;
    }
    
    // Public Functions

    function setUnRevealedUri(string memory __uri) public {
        _unRevealedURI = __uri;
    }

    function tokenURI(uint256 tokenId) public view virtual override returns (string memory) {
        require(_exists(tokenId), "ERC721URIStorage: URI query for nonexistent token");

        string memory _tokenURI = _tokenURIs[tokenId];
        string memory base = _baseURI();

        if (_revealed) {
            // If there is no base URI, return the token URI.
            if (bytes(base).length == 0) {
                return _tokenURI;
            }
            // If both are set, concatenate the baseURI and tokenURI (via abi.encodePacked).
            if (bytes(_tokenURI).length > 0) {
                return string(abi.encodePacked(base, _tokenURI));
            }

            return super.tokenURI(tokenId);
        } else {
            return _unRevealedURI;
        }
    }

    function reveal() public onlyOwner {
        require(! _paused,"Contract Paused");
        _revealed = true;
    }
    function pause() public onlyOwner {
        require(! _paused,"Contract Paused");
        _paused = true;
    }
    function resume() public onlyOwner {
        require(_paused,"Contract not paused");
        _paused = false;
    }

    function whiteList(address __wallet) public onlyOwner {
        require(! _paused,"Contract Paused");
        require(__wallet != address(0),"Zero address");
        uint256 __walletBalance = balanceOf(__wallet);
        require(__walletBalance > 0,"Not enough ether");

        _whiteList[__wallet] = __walletBalance;
    }

    // View functions

    function isPaused() public view returns (bool) {
        return _paused;
    }
    
    function isRevealed() public view returns (bool) {
        return _revealed;
    }

    function isWhitelisted(address __wallet) public view returns (bool) {
        return _whiteList[__wallet] > 0;
    }

    function getUnrevealedUri() public view returns (string memory) {
        return _unRevealedURI;
    }

    // Internal Functions

    function _setTokenURI(uint256 tokenId, string memory _tokenURI) internal virtual {
        require(_exists(tokenId), "ERC721URIStorage: URI set of nonexistent token");
        _tokenURIs[tokenId] = _tokenURI;
    }

}

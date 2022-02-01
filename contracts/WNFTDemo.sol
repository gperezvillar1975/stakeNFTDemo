// SPDX-License-Identifier: MIT

pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/utils/Strings.sol";
import "@openzeppelin/contracts/utils/math/SafeMath.sol";
import "./lib/ContentMixin.sol";
import "./lib/NativeMetaTransaction.sol";

contract OwnableDelegateProxy {}

/**
 * Used to delegate ownership of a contract to another address, to save on unneeded transactions to approve contract use for users
 */
contract ProxyRegistry {
    mapping(address => OwnableDelegateProxy) public proxies;
}

contract WNFTDemo is ERC721, ContextMixin, NativeMetaTransaction, Ownable {
    using SafeMath for uint256;
    using Counters for Counters.Counter;
    using Strings for uint256;

    // State Variables 

    bool private _revealed;
    bool private _paused;
    mapping (address => uint256) private _whiteList; // wallets enbled to mint
    string private _unRevealedURI;
    address _proxyRegistryAddress;
    Counters.Counter private _nextTokenId;

    constructor(
        address __proxyRegistryAddress,
        string memory __unRevealedUri
        )
        ERC721("WNFTDemo","WNFT")
    {
        _proxyRegistryAddress = __proxyRegistryAddress;
        _revealed = false;
        _paused = false;  
        _unRevealedURI  = __unRevealedUri;      
        _nextTokenId.increment();
        _initializeEIP712("WNFTDemo");        
    }


    // Mint Function

    function mint() public {
        require(! _paused,"Contract Paused");
        require(msg.sender != address(0),"Zero address");
        require(_whiteList[msg.sender] > 0 || msg.sender == owner(), "NOT Whitelisted" );
        address _to = msg.sender;
        uint256 currentTokenId = _nextTokenId.current();
        _nextTokenId.increment();
        _safeMint(_to, currentTokenId);
    }


    // Public Functions

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
        require(_canMint(__wallet),"Not enough ether");

        uint256 __walletBalance = __wallet.balance;
        _whiteList[__wallet] = __walletBalance;
    }

    // View functions

    function baseTokenURI() public view  returns (string memory) {
        if (_revealed) {
            return "https://gateway.pinata.cloud/ipfs/QmTkLTxhfeK4czWofZvdwASkiNhETW5cunYGCYC4xye6eQ/";
        } else {
            return "UNREVEALED TOKEN";            
        }
    }

    function contractURI() public pure returns (string memory) {
        return "";
    }

    function UnrevealedURI() public view returns (string memory) {
        return _unRevealedURI;
    }

    function canMint(address __wallet) public view returns (bool) {
        return _canMint(__wallet);
    }

    function totalSupply() public view returns (uint256) {
        return _nextTokenId.current() - 1;
    }

    function tokenURI(uint256 _tokenId) override public view  returns (string memory) {
        if (_revealed) {
            return string(abi.encodePacked(baseTokenURI(), Strings.toString(_tokenId)));
        } else {
            return string(abi.encodePacked(UnrevealedURI()));
        }
    }    

    function isApprovedForAll(address owner, address operator)
        override
        public
        view
        returns (bool)
    {
        // Whitelist OpenSea proxy contract for easy trading.
        ProxyRegistry proxyRegistry = ProxyRegistry(_proxyRegistryAddress);
        if (address(proxyRegistry.proxies(owner)) == operator) {
            return true;
        }

        return super.isApprovedForAll(owner, operator);
    }


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


    // Private Functions

    function _msgSender()
        internal
        override
        view
        returns (address sender)
    {
        return ContextMixin.msgSender();
    }

    function _canMint(address __wallet) internal view returns (bool) {
        return (__wallet.balance > 0 || __wallet == owner());
    }
}
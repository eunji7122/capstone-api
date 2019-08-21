const Caver = require('caver-js');
const caver = new Caver('https://api.baobab.klaytn.net:8651/');
caver.klay.accounts.signTransaction({
    from:"0xb740db8a51e013535869F78eb1d9fC1C63cF1A41",
    to:"0xb740db8a51e013535869F78eb1d9fC1C63cF1A41",
    value: caver.utils.toPeb('0.1', 'KLAY'),
    gas: 900000,
}, '0xc391960963382589542407169cd7e8238b4bd07f459b23bfc6e418dee1b296fd').then(signedTx => {
    console.log(JSON.stringify(signedTx));
});
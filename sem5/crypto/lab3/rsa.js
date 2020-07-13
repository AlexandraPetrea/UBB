var p, q, e, d, n;
e = 67;
n = 1643;
d = 163;
var eps;
var n;
let l = 2;
let k = 3;
var wasInited = 0;
const plaintext = ' abcdefghijklmnopqrstuvwxyz'
const cyphertext = plaintext.toUpperCase()

function gcd(a, b) {
    if (!b) {
        return a;
    }

    return gcd(b, a % b);
}
const mod = (x, n) => (x % n + n) % n

function pow(a, b, n){
    a = a % n;

    var result = 1;

    var x = a;



    while(b > 0){

        var leastSignificantBit = b % 2;

        b = Math.floor(b / 2);



        if (leastSignificantBit == 1) {

            result = result * x;

            result = result % n;

        }



        x = x * x;

        x = x % n;

    }

    return result;
}


function init(_p, _q) {
    wasInited = 1;
    p = _p;
    q = _q;
    n = p*q;
    eps = (p-1) * (q-1);
    e = Math.floor(Math.random() * (eps-1) + 1);
    // e  = 67;
    while(gcd(e,eps) !== 1)
    {
        e = Math.floor(Math.random() * (eps-1) + 1);
    }
    console.log(e);
    d = modInv(e, eps)[0];
    if(d < 0)
        d = eps + d;
    console.log(d);
    console.log(n);


}


function chunkToNr(chunk, chunkSize){
    var res = 0;
    for(i=0; i < chunkSize; ++i)
    {
        var nr = 0;
        if(i < chunk.length && chunk[i] !== " ")
        {
            nr = chunk.charCodeAt(i)- "a".charCodeAt(0) + 1;
        }
        res = 27 * res + nr;
    }
    return res;
}

function nrToChunk(nr, chunkSize){
    idx = chunkSize-1;
    result = [];
    for(i = 0; i < chunkSize; ++i)
    {
        rem = nr % 27;
        console.log(rem)
        if(rem === 0)
            result.push(" ");
        else
            result.push(String.fromCharCode("a".charCodeAt(0) + rem - 1));
        nr = Math.floor(nr / 27);
    }
    return result.reverse().join("");
}


function split(input, size){
    var re = new RegExp('.{1,' + size + '}', 'g');
    var chunks = input.match(re);
    var result = [];

    while(chunks[chunks.length-1].length < size)
    {
        chunks[chunks.length-1] = chunks[chunks.length-1].concat(" ");
    }
    console.log(chunks);

    for(idx in chunks)
    {
        result.push(chunkToNr(chunks[idx], size))
    }
    return result
}

console.log(split("algebra", 2));
console.log(nrToChunk(498,3));


function modInv(a, b) {
    // console.log(a.toString() + ' ' + b.toString())
    if (b === 0) {
        return [1, 0, a];
    }

    temp = modInv(b, a % b);
    x = temp[0];
    y = temp[1];
    d = temp[2];
    return [y, x-y*Math.floor(a/b), d];
}

function modInvWrapper(a , b) {
    alert(modInv(a, b)[0]);
}

function generatePrimes(upperLimit){
    const primes = [];
    const isPrime = [];
    for (i = 0; i < upperLimit; i++){
        isPrime.push(true);
    }

    for (i = 2; i < upperLimit ; i++) {
        if (isPrime[i]){
            primes.push(i);
            for (j = 2 * i; j < upperLimit; j += i){
                isPrime[j] = false;
            }
        }
    }

    return primes;
}

function isPrime(number){
    if (number < 2)
        return false;

    for (i = 2; i < Math.sqrt(number) + 1; i++){
        if (number % i === 0) {
            return false;
        }
    }

    return true;
}

function getText() {
    var textElem = document.getElementById('text')
    return (textElem != null) ?  textElem.value : ''
}

function getKey(name) {
    var keyElem = document.getElementById(name)
    return (keyElem != null) ? parseInt(keyElem.value) : NaN
}

function crypt() {
    var text = getText().toLowerCase();
    var primeNumber1 = getKey('primeNumber1')
    var primeNumber2 = getKey('primeNumber2')
    // var primeNumber1 = p;
    // var primeNumber2 = q;


    var result = '';

    if(wasInited === 0)
        init(primeNumber1, primeNumber2);
    var codesPlain = split(text, l);
    for(idx in codesPlain)
    {
        var codePlain = codesPlain[idx];
        var codeCypher = pow(codePlain, e, n);
        var stringCypher = nrToChunk(codeCypher, k);
        result = result.concat(stringCypher);
    }

    document.getElementById('text').value = result.toUpperCase();
    validateInputs()
}

function decrypt() {
    var text = getText().toLowerCase();
    var primeNumber1 = getKey('primeNumber1')
    var primeNumber2 = getKey('primeNumber2')
    // var primeNumber1 = p;
    // var primeNumber2 = q;


    var result = '';

    if(wasInited === 0)
        init(primeNumber1, primeNumber2);

    var codesCypher = split(text, k);
    console.log(codesCypher);
    for(idx in codesCypher)
    {
        var codeCypher = codesCypher[idx];
        console.log(codeCypher);
        var codePlain = pow(codeCypher, d, n);
        console.log(codePlain);
        var stringPlain = nrToChunk(codePlain, l);
        console.log(stringPlain)
        result = result.concat(stringPlain);
    }
    document.getElementById('text').value = result;
    validateInputs()
}

function validateInputs() {
    deactivateButtons()

    text = getText()
    primeNumber1 = getKey('primeNumber1');
    primeNumber2 = getKey('primeNumber2');




    var containsPlainChars = false
    var containsCypherChars = false
    var containsIllegalChars = false
    var containsCommonChars = false

    for (index in text) {
        if (plaintext.includes(text[index]) && cyphertext.includes(text[index])){
            containsCommonChars = true
        }else if (plaintext.includes(text[index])) {
            containsPlainChars = true
        }else if (cyphertext.includes(text[index])) {
            containsCypherChars = true
        }else {
            containsIllegalChars = true
        }
    }

    if (text === '') {
        hideAlert()
    } else if (isNaN(primeNumber1)) {
        setAlert('PrimeNumber1 is not set!')
    } else if (!isPrime(primeNumber1)) {
        setAlert('PrimeNumber1 is not PRIME!')
    } else if (isNaN(primeNumber2)) {
        setAlert('PrimeNumber2 is not set!')
    } else if (!isPrime(primeNumber2)) {
        setAlert('PrimeNumber1 is not PRIME!')
    } else if (containsIllegalChars) {
        setAlert('Text contains illegal characters!')
    } else if(primeNumber1 * primeNumber2 < pow(27,l,99999999) || primeNumber1 * primeNumber2 > pow(27,k,999999)) {
        console.log(pow(27,l,99999999))
        console.log(pow(27,k,99999999))

        setAlert('NUMBER NOT IN INTERVAL')
    } else if (containsPlainChars && containsCypherChars) {
        setAlert('Do not mix plaintext and cyphertext!')
    } else if (containsPlainChars) {
        hideAlert()
        activateCryptButton()
    } else {
        hideAlert()
        activateDecryptButton()
    }
}

function activateCryptButton() {
    document.getElementById('crypt-btn').disabled = false
}

function deactivateCryptButton() {
    document.getElementById('crypt-btn').disabled = true
}

function activateDecryptButton() {
    document.getElementById('decrypt-btn').disabled = false
}

function deactivateDecryptButton() {

    document.getElementById('decrypt-btn').disabled = true
}

function deactivateButtons() {
    deactivateCryptButton()
    deactivateDecryptButton()
}

function setAlert(text) {
    document.getElementById('danger-alert').style.display = 'block'
    document.getElementById('danger-alert').innerHTML = text
}

function hideAlert() {
    document.getElementById('danger-alert').innerHTML = ''
    document.getElementById('danger-alert').style.display = 'none'
}

validateInputs()
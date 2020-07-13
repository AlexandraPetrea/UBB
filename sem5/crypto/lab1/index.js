const plaintext = " abcdefghijklmnopqrstuvwxyz"
const cyphertext = plaintext.toUpperCase()

//this function take the input text 
function getText() {
  var textElem = document.getElementById('text')
  return (textElem != null) ? textElem.value : ''
}

//this function take the key 
function getKey() {
  var keyElem = document.getElementById('key')
  return (keyElem != null) ? keyElem.value : ''
}
/*
this function encrypt the given text using the given key
we define the alphabet as space and then the 26 letters
the encryption is made in the following way: we take the postion of the first letter from the given text and add 
to it the position of the first letter in the given key. Because the given text cand exced the keyword length, we use here
the (% keyword.length) in order separate the given text in blocks of keyword length. We obtain an integer and then we take the letter corresponding 
to that position from the alphabet. We apply here the (mod alphabet) because the integer can exced the limits. Now, we have
the encrypt letter for the first letter. In this way, we continue until the last letter.
*/  
function crypt() {
  var word = getText().toLowerCase()
  var keyword = getKey()
  var alphabet = " abcdefghijklmnopqrstuvwxyz";
  var encryptWord = ''
  for (var i = 0;i < word.length;i++) {
    wordPos = alphabet.indexOf(word.charAt(i));
    keywordPos = alphabet.indexOf(keyword.charAt(i % keyword.length));
    encryptWord += alphabet.charAt((wordPos + keywordPos) % alphabet.length);
  }
  document.getElementById('text').value = encryptWord.toUpperCase()
  activateDecryptButton()
  validateInputs()
}

/* Decyption is the reverse operation of the encryption. We take the letter from the position i from the given text and add to it the
length of the alphabet then we substract the letter from the position i from the given keyword and apply the % alphabet to the result in 
order to obtain a correct result.
*/
function decrypt() {
  var word = getText().toLowerCase()
  var keyword = getKey()

  var result = ''

  var alphabet = " abcdefghijklmnopqrstuvwxyz";

  for (var i = 0;i < word.length;i++) {
  	wordPos = alphabet.indexOf(word.charAt(i));
  	keywordPos =  alphabet.indexOf(keyword.charAt(i % keyword.length))
    result += alphabet.charAt((( wordPos + alphabet.length) - keywordPos) % alphabet.length);
  }

  document.getElementById('text').value = result.toLowerCase()
  validateInputs()
}

/* Here we make some validations for checking that the plain text and the cyper text don't contain illegal characters, the key is set
and the plain text and cyper text aren't mixt.
*/

function validateInputs() {
  //deactivateButtons()

  text = getText()
  key = getKey()

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
  }else if (key === '') {
    setAlert('Key is not set!')
  } else if (containsIllegalChars) {
      setAlert('Text contains illegal characters!')
    } else if (containsPlainChars && containsCypherChars) {
      setAlert('Do not mix plaintext and cyphertext!')
      }else if (containsPlainChars) {
        hideAlert()
        activateCryptButton()
      }else {
        hideAlert()
        activateDecryptButton()
      }
}

//activate the crypto button
function activateCryptButton() {
  document.getElementById('crypt-btn').disabled = false
}

//deactivate the crypto button in case that something goes wrong
function deactivateCryptButton() {
  document.getElementById('crypt-btn').disabled = true
}

//activate the decrypt button
function activateDecryptButton() {
  document.getElementById('decrypt-btn').disabled = false
}

//deactivate the decyrpt button
function deactivateDecryptButton() {

  document.getElementById('decrypt-btn').disabled = true
}

//deactivate all buttons
function deactivateButtons() {
  deactivateCryptButton()
  deactivateDecryptButton()
}

//in case that something goes wrong, we set an allert
function setAlert(text) {
  document.getElementById('danger-alert').style.display = 'block'
  document.getElementById('danger-alert').innerHTML = text
}

//deactivate the alert in case that the problem was fixed
function hideAlert() {
  document.getElementById('danger-alert').innerHTML = ''
  document.getElementById('danger-alert').style.display = 'none'
}

//validateInputs()
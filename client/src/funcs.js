import {AES, enc} from "crypto-js"

export const isWhitespaceString = str => !str.replace(/\s/g, '').length

export function encryptMessage(message, key) {
  const encrypted = AES.encrypt(message, key).toString();
  return encrypted;
}
export function decryptMessage(encryptedMessage, key) {
  const decrypted = AES.decrypt(encryptedMessage, key).toString(enc.Utf8);
  return decrypted;
}


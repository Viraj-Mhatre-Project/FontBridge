# Conversion Rules

This document defines the rules used to convert Shivaji font encoded text
into Unicode Marathi text.

## 1. Character Mapping

Each Shivaji encoded character is mapped to its corresponding Unicode
Devanagari character using the mapping dataset defined in `shivaji_mapping.json`.

Example:

Shivaji Input:
kava Ahe

Unicode Output:
कसा आहे


## 2. Consonant Handling

Basic consonants are converted directly using the mapping table.

Example:

k → क  
g → ग  
c → च


## 3. Matra Handling

Matras modify the preceding consonant.

Example:

k + a → का  
k + i → कि  
k + e → के


## 4. Vowel Handling

Standalone vowels should be converted directly.

Example:

A → अ  
Aa → आ  
I → इ  


## 5. Special Characters

Special phonetic symbols must be converted properly.

Examples:

M → ं  
H → ः  
~ → ँ  


## 6. Unknown Characters

If a character does not exist in the mapping table, the converter should
leave it unchanged.

Example:

Input:
Hello kava

Output:
Hello कसा


## 7. Processing Flow

The conversion engine processes text in the following order:

1. Read raw text
2. Identify Shivaji encoded characters
3. Apply mapping rules
4. Reconstruct Unicode string
5. Return converted text


## 8. Future Improvements

Future versions will support:

- compound characters
- ligatures
- context-based conversion
- better punctuation handling
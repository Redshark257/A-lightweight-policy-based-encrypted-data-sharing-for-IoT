# Light-SABRE

Light-SABRE is a lightweight encrypted data distribution framework for Internet of Things (IoT) environment. The system combines:

* Proxy Re-Encryption (PRE)
* Ciphertext-Policy Attribute-Based Encryption (CP-ABE)
* ElGamal Encryption method
* Pairing-based cryptography


to enable secure, flexible, and scalable encrypted data sharing across distributed IoT systems.

This repository contains a research prototype implementation of the Light-SABRE framework using the Charm-Crypto library

---

# Features

* Lightweight encrypted data distribution
* Proxy-assisted ciphertext transformation
* Fine-grained attribute-based access control
* Pairing-based cryptographic construction
* CP-ABE policy enforcement
* Modular architecture for experimentation and extension

--- 

# System Architecture

The implementation contains four primary entities

KGC: Key Generaton Center responsible for setup and key issuance
Data Owner: Encrypts IoT data using ElGamal-style encryption
Proxy/CSP: Performs policy-aware proxy re-encryption
Third Party User: Can Decrypt ciphertexts if their attributes satisfy the policy requirements

---

# Cryptographic Flow


## 1. System Setup


## 2. Data Encryption


## 3. Policy Parsing


## 4. Re-Encryption Key Generation


## 5. Proxy Re-Encryption


## 6. User Key Generation


## 7. Decryption


## 8. Project Structure



--- 

# Installation

* Python 3.9+
* Charm

---

## Clone Repository



## Install Dependencies

Install all required Python packages using requirements.txt


---

# Running the Demo

First install the setup

pip install -e .

Example output: 

SUCCESS



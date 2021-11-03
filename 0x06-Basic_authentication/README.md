# 0x06. Basic authentication

## Background Context
In this project, you will learn what the authentication process means and implement a **Basic Authentication** on a simple API.
In the industry, you should **not** implement your own Basic authentication system and use a module or framework that doing it for you (like in Python-Flask:  [Flask-HTTPAuth](https://intranet.hbtn.io/rltoken/ck5nE4pv5NdWV38srlET0Q) ). Here, for the learning purpose, we will walk through each step of this mechanism to understand it by doing.

## Resources
**Read or watch**:
*  [REST API Authentication Mechanisms](https://intranet.hbtn.io/rltoken/Yx1Na2qEzCLnke8RnpACDw) 
*  [Base64 in Python](https://intranet.hbtn.io/rltoken/R2kTeyWl2ef19mdxQuffww) 
*  [HTTP header Authorization](https://intranet.hbtn.io/rltoken/5BfGd-_oV9Asi_Ymi_lRSA) 
*  [Flask](https://intranet.hbtn.io/rltoken/3ivma6PpGZfjzDrA2zLq7g) 
*  [Base64 - concept](https://intranet.hbtn.io/rltoken/8ckHTvJq00WnvgEmn6GGtg) 

## Learning Objectives
At the end of this project, you are expected to be able to  [explain to anyone](https://intranet.hbtn.io/rltoken/SzP_ze3i3creBPylmPrRZQ) , **without the help of Google**:
## **General**
### What authentication means?
Authentication is the use of the header in a http/https request in which the client sends a request to a Restless API to authenticate the current session.

### What Base64 is?
Base64 is a format of encoding a string in way that is able to be sent with the HTTP protocol which doesn’t accept certain characters. Thus, the need to encode a string is for the purpose of sending information to a API so that it can be decoded and used to authenticate a user. 

### How to encode a string in Base64?
To encode a string in Base64 you will need a python module called **base64**. This module provides methods to encode strings into base64 strings.

### What Basic authentication means?
Basic Authentication is the type of authentication in which the client sends the server information such as Username/password and does so every time that it is sending it.
### How to send the Authorization header?
To send an authorization header all you have to do in the header Object is:
```
header_obj = {
	Authorization: Basic <credentials>
}
```

# Arithmetic-as-a-Service
Implementing arithmetic operations as a service because why not.

# How to use my AaaS

The format of the URL is `https://arithmetic-service.herokuapp.com/<operation>/<values>`. The currently possible values for the `operation` include 

* `add`
* `sub`
* `mul`
* `div`
* `sin`
* `cos`
* `tan`
* `fact`

You can chain together as many values - both integer as well as floating point, as needed. Do note that the operation being performed is of the type `operand 1 <operator> operand 2 <operator> operand N`. For example, here is an example request to add
0 and 1 - `https://arithmetic-service.herokuapp.com/add/0/1`. Attached below are few more examples.

* To obtain `4 + 2 + 0`, you can use `/add/4/2/0`

* To find `4!`, use `/mul/1/2/3/4` or `/fact/4`

* To find the value of `8 - 24 - 32`, use `/sub/8/24/32`

* To find the answer to `32 / 3` use `/div/32/3`

To use in a script, Here is a simple Python example that calculates `5!` using my AaaS

```Python
>>> import requests
>>> url = "https://arithmetic-service.herokuapp.com/mul/1/2/3/4/5"
>>> response = requests.get(url)
>>> print(response.text)
>>> '120.0'
```

# Inspiration to make my own AaaS

Life is everchanging and filled with uncertainty. Sometimes, you do things in life just so that you can look back to it later and regret the bad decisions you made. But this is not one of those decisions.

I thought publishing my AaaS to the world would be a cool idea, and here we are.

# Contributing to my AaaS

Contributions are welcome to make my AaaS more robust and complete. Suggestions for future contributions include `mod`, along with other mathematical operators like trigonometric functions.

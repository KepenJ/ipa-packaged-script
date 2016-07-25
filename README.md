# ipa-packaging-script
A script packaging local project to ipa written with python. 

### Platform

Python 2.7

### Usage

1. Drag the script into the document of project which needs to be packaged.
2. Use terminal `cd` the current project folder.
3. Use terminal `python ipa-packaged-script.py`

### Script commands

+ `--config` or `-c` show config file content.
+ `--edit` or `-e` edit file about config.

### Packing parameters

+ `PROJECT PATH` default is current project document path.
+ `PROJECT NAME` your project name.
+ `TAG NAME` your targets name.
+ `TAG VERSION` default is 1.0.0.
+ `CERTIFICATE NAME` you can find your certificate in Keychain Access,we just need name
+ `PROVISIONING PROFILE NAME` you can the provisioning profile  in `~/Library/MobileDevice/Provisioning Profiles/`
+ `FIR TOKEN(Optional)` it's optional,a token which given by [fir.im](http://fir.im/).

### Supports uploading fir.im (Optional)

If you want to use third-party distribution platform to test your application , here I chose [fir.im](http://fir.im/),you need  
 
1. Install [fir-cli](https://github.com/FIRHQ/fir-cli).
2. Register an account,and copy the token.
3. Input the `FIR TOKEN(Optional)` by the given.
4. Run the script.

Of course, this is just an optional option , you can change the function `upload_to_fir()`, to achieve upload other platforms.

### License

Copyright (c) 7/14/2016 KepenJ

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

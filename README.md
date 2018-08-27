# Photo Enhancer

> A mini function to enhance my friend's gallery photos on-the-go.

#### Concepts

```text
blend1 = {blend(filter1, filter2)}
blend2 = {blend(blend1, filter3)}
enhance1 = {enhance-color(blend2)}
enhance2 = {enhance-contrast(enhance1)}
enhance3 = {enhance-brightness(enhance2)}
output = enhance3
```

#### Install necessary components.

You will need to have `Python3` and `pip3` installed.

```bash
$ sudo -H pip3 install -r requirements.txt
```

#### Change to your image path or create new one.

Edit `photo-enhance.py` file and look for line as below, change the path.

```python
path = "/path/to/your/images/"
```

#### Run the script.

```bash
$ python3 photo-enhance.py
```

---

MIT License

Copyright (c) 2018 Loouis Low

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

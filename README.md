# Passive Image Enhancer

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

Edit `passive_image_enhancer.py` file and look for line as below, change the path.

```python
path = "/path/to/your/images/"
```

#### Run the script.

```bash
$ python3 passive_image_enhancer.py
```

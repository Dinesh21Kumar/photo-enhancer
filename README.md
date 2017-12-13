# Passive Image Enhancer

> A mini function to enhance my blog photos on the go.

```text
blend1 = {blend(filter1, filter2)}
blend2 = {blend(blend1, filter3)}
enhance1 = {enhance-color(blend2)}
enhance2 = {enhance-contrast(enhance1)}
enhance3 = {enhance-brightness(enhance2)}
output = enhance3
```

Install necessary components.

```bash
$ sudo -H pip3 install -r requirements.txt
```

Change to your image path or create new one.

```python
path = "/path/to/your/images/"
```

Run the script.

```bash
$ python3 passive_image_enhancer.py
```

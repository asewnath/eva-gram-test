# eva-gram-test

Extracting div/script from pkl files

```
import pickle

with open('sample.pkl', "rb") as f:
    dictionary = pickle.load(f)

#dictionary['div'] is div component
#dictionary['script'] is script component
```

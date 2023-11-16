# eva-gram-test

Extracting div/script from pkl files

```
import pickle

with open('corscat_hofx_vs_gsihofx.pkl', "rb") as f:
    dictionary = pickle.load(f)

#dictionary['div'] is div component
#dictionary['script'] is script component
```

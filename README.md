# Attributetools
A decorator to set some attribute to a function.

## Install
```console
pip install attributetools
```

## Usage
```python
from attributetools import attribute


@attribute(short_description='Mark me as paid')
def doitfunc(request, queryset):
    pass
```

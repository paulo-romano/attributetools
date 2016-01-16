# attributetools
A decorator to set some attribute to a function

## install
pip install git+https://github.com/paulo-romano/attributetools.git

## usage
```python
from attributetools import attribute

@attribute(short_description='Mark me as paid')
def doitfunc(request, queryset):
    pass
```

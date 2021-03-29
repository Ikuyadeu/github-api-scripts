# pprint

Pretty Printing for Torch and Lua.

`pprint` will print a human readable printout of Lua tables and torch tensors.

## Features

The visual improvements offered by pprint are the following:

* Keys are printed alphabetically
* Nested tables are indented
* Loops are detected
* Metatable info is printed
* Torch tensors are printed if they contain less than 20 elements, 
otherwise just the dimensions are printed

## Differences with Penlight.pretty

All the mentioned features, except for loop detection, 
are not included in `Penlight.pretty`. In addition `Penlight.pretty`
substitutes loops by a `<cycle>` tag, making it impossible to see
the table causing the loop.

Apart from this, `Penlight.pretty` introduces new lines per table element,
whereas pprint only creates them based on non-numerical indices of the table.

## Usage

There are different ways in which pprint can be used:

### General (torch and lua) usages 

* Using `pprint(data)` directly, as seen in the example below:

```lua
require 'pprint'
a = {1, 2}
a[3] = a
a[4] = torch.zeros(21)
pprint(a)
```

Outputs:

```lua
{ 1, 2, { 1, 2, { 1, 2, { 1, 2, {...}, [torch.DoubleTensor of dimension 21] },
[torch.DoubleTensor of dimension 21] }, [torch.DoubleTensor of dimension 21] },
[torch.DoubleTensor of dimension 21] }
```

* Calling `pprint.pretty_string(data)`, which differs from
`pprint(data)` in that the method returns the generated string instead
of printing it. 

* Calling `pprint.string(data)`, which is the inline result
version of `pprint.pretty_string(data)`.

* Using `pprint.printer()` to create a printer that returns a the
concatenated `pretty_string` version of an arbitrary amount of parameters.

* When printing a table, the default depth is 4. This depth can be modified:

```lua
require 'pprint'
a = {1, {2, {3, {4, {5}}}}}
pprint(a, 2)
print(pprint.pretty_string(a, 3))
pprint(a)
```

Outputs:

```lua
{ 1, { 2, {...} } }	
{ 1, { 2, { 3, {...} } } }	
{ 1, { 2, { 3, { 4, {...} } } } }
```

### Tensor specific usage

* `pprint.dims(tensor)` returns a string containing the dimensions of the
`tensor` passed as an argument.

* `pprint.info(data)` returns a string containing information of the tensors
(dimensions, minimum value, mean value, maximum value, type) found in `data`.

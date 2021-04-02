## KriaSoft Core Library

This is a collection of various helper classes and utilities released under [Apache License 2.0](https://github.com/kriasoft/core/blob/master/LICENSE.txt).

### Usage samples

Reading .xpo files (Omega Research Export File Type)

```csharp
using KriaSoft.IO;

using (var xpo = new XpoReader("quotes.xpo"))
{
    var symbols = xpo.GetSymbols();
}
```
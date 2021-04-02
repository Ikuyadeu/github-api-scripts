influxdb-csharp
===============

# This library is not updated for InfluxDB 0.9. There are breaking changes to the API, use at your own risk.

We encourage you to submit a pull request if you have a contribution. If you make a PR please explicitly call @beckettsean to get eyes on your PR.

----------

C# client for Influxdb

Only very basic features are implemented so far.

```cs
var client = new InfluxDBClient("192.168.1.100", 8086, "root", "root", "MyDataBase");

// Create series
var serie = new Serie { Name = "foo", ColumnNames = new[] { "value", "value_str" } };
serie.Points.Add(new object[] { 1.0, "first" });
var series = new List<Serie> { serie };

// Insert series
client.Insert(series);

// Query database
List<Serie> result = client.Query("select * from foo");
```

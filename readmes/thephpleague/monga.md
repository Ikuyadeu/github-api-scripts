# Monga

[![Latest Version on Packagist][ico-version]][link-packagist]
[![Software License][ico-license]](LICENSE.md)
[![Build Status][ico-travis]][link-travis]
[![Total Downloads][ico-downloads]][link-downloads]

A simple and swift MongoDB abstraction layer for PHP 5.4+

## What's this all about?

* An easy API to get connections, databases and collections.
* A filter builder that doesn't make your mind go nuts.
* All sorts of handy update functions.
* An abstraction for sorting single results.
* GridFS support for a Mongo filesystem.
* Easy aggregation and distinct values.

## Vision

Monga was created with the acknowledgment of the MongoDB PHP package already being pretty awesome. That's why in a lot of cases Monga is just a simple wrapper around the MongoDB classes.
It provides some helpers and helps you set up queries using a query builder. Which you can also choose not to use! Everything will still work accordingly.
During the development, a lot of planning has gone into creating a nice streamlined API that closely follows the MongoDB base classes, while complementing existing query builders for SQL-like databases.

## Install

Via Composer

``` bash
$ composer require league/monga
```

## Usage

```php

use League\Monga;

// Get a connection
$connection = Monga::connection($dns, $connectionOptions);

// Get the database
$database = $connection->database('db_name');

// Drop the database
$database->drop();

// Get a collection
$collection = $database->collection('collection_name');

// Drop the collection
$collection->drop();

// Truncate the collection
$collection->truncate();

// Insert some values into the collection
$insertIds = $collection->insert([
	[
		'name' => 'John',
		'surname' => 'Doe',
		'nick' => 'The Unknown Man',
		'age' => 20,
	],
	[
		'name' => 'Frank',
		'surname' => 'de Jonge',
		'nick' => 'Unknown',
		'nik' => 'No Man',
		'age' => 23,
	],
]);

// Update a collection
$collection->update(function ($query) {
	$query->increment('age')
		->remove('nik')
		->set('nick', 'FrenkyNet');
});

// Find Frank
$frank = $collection->findOne(function ($query) {
	$query->where('name', 'Frank')
		->whereLike('surname', '%e Jo%');
});

// Or find him using normal array syntax
$frank = $collection->find([
	'name' => 'Frank',
	'surname' => new MongoRegex('/e Jo/imxsu')
]);

$frank['age']++;

$collection->save($frank);

// Also supports nested queries
$users = $collection->find(function ($query) {
	$query->where(function ($query) {
		$query->where('name', 'Josh')
			->orWhere('surname', 'Doe');
	})->orWhere(function ($query) {
		$query->where('name', 'Frank')
			->where('surname', 'de Jonge');
	});
});

// get the users as an array
$arr = $users->toArray();
```

## Aggregation

A big part of the newly released MongoDB pecl package is aggregation support. Which is super easy to do with Monga:

```php
$collection->aggregate(function ($a) {
	$a->project([
		'name' => 1,
		'surname' => -1,
		'tags' => 1,
	])->unwind('tags');

	// But also more advanced groups/projections
	$a->project(function ($p) {
		$p->select('field')
			->select('scores')
			->exclude('other_field');
	})->group(function ($g) {
		$g->by(['$name', '$surname'])
			->sum('scores');
	});
});
```

## Contributing

Please see [CONTRIBUTING](CONTRIBUTING.md) and [CONDUCT](CONDUCT.md) for details.

## Security

If you discover any security related issues, please email bryan@bryan-crowe.com instead of using the issue tracker.

## Credits

- [Frank de Jonge][link-author]
- [All Contributors][link-contributors]

## License

The MIT License (MIT). Please see [License File](LICENSE.md) for more information.

[ico-version]: https://img.shields.io/packagist/v/league/monga.svg?style=flat-square
[ico-license]: https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat-square
[ico-travis]: https://img.shields.io/travis/thephpleague/monga/master.svg?style=flat-square
[ico-downloads]: https://img.shields.io/packagist/dt/league/monga.svg?style=flat-square

[link-packagist]: https://packagist.org/packages/league/monga
[link-travis]: https://travis-ci.org/thephpleague/monga
[link-downloads]: https://packagist.org/packages/league/monga
[link-author]: https://github.com/frankdejonge
[link-contributors]: ../../contributors

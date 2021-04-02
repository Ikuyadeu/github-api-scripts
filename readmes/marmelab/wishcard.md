# Integrating Raphael.js With Backbone.js

Client-side MVC frameworks usually bind model elements with DOM elements. But for more graphical applications, the view layer cannot be restricted to div and span tags. How can we bind Model elements with SVG charts?

Complex frontend applications require a decoupled MVC architecture, just like for the backend part.
Recently, a few frameworks emerged like Angluar, Backbone.js & ExtJs, each with their own benefits.
For this article, we've chosen Backbone, both for his maturity and his lightness.

Rahpael.js is a well known library used to display SVG in a web page easily. It encapsulates some methods to draw SVG elements independently of the browser.

## How To Integrate Raphael.js With Backbone.js

Now that we have chosen those 2 powerful components, how can we combine both?

We are going to see this through a simple example: Display a snowman and change the color if its parts when clicking on it. The sownman information will be stored in localstorage to save modifications for the future.

I know it's not the good season to make a snowman but here in France the weather will soon let it be possible.

To do so, we will have to focus on various aspects:
- create the Backbone project and include the Raphael.js (link) library
- create a model and its collection to store the body parts of the snowman
- initialise the view
- handle the click event

## Including the right files

First of all, we're going to download the [backbone](http://backbonejs.org/backbone-min.js), [underscore](http://underscorejs.org/underscore-min.js), [Backbone local storage](https://github.com/jeromegn/Backbone.localStorage) and [Raphael](http://github.com/DmitryBaranovskiy/raphael/raw/master/raphael-min.js) libraries.

Theses files will be included this way:

```js
<script type="text/javascript" src="js/lib/jquery-1.9.1.min.js"></script>
<script type="text/javascript" src="js/lib/underscore-min.js"></script>
<script type="text/javascript" src="js/lib/backbone.js"></script>
<script type="text/javascript" src="js/lib/backbone.localStorage.js"></script>
<script type="text/javascript" src="js/lib/raphael.js"></script>
```

We can now use these libraries to draw our snowman.

## Creating A Model And A Collection

We will create a Model which will store 3 circles that represents the snowman.
It should store the center of a circle, the radius and fill color:

```js
var MyCircle = Backbone.Model.extend({
  defaults: {
		id:       null,
		cx:       null,
		cy:       null,
		r:       null,
		fill:    null
	}
});
```

A Backbone collection is created to group our 3 circles:

```js
var MyCircles = Backbone.Collection.extend({
	model: MyCircle,
	url: 'circles',
	localStorage: new Store("circles")
});
```

The `localStorage` property points out the storage method for our collection (here in the localStorage thanks to the `backbone.localStorage` library) with a specific name.


## Let's Build The Snowman

Each backbone view needs a DOM element to apply changes on.
In our case this element is the same as the SVG container.

```js
var MyView = Backbone.View.extend({
	el: 	'#container',
	paper: 	null
	},
	
	initialize: function() {
		// Create a raphael paper where the SVG elements will be displayed
		this.paper        = Raphael(this.$el[0], 300, 300);
		// Instanciate the collection
		this.collection   = new MyCircles();
		
		var self          = this;
		// Retrieve elements of the collection
		this.collection.fetch().done(function () {
			// Add circles if the collection is empty
			if (self.collection.isEmpty()) {
				self.addDefaultCircles();
			}

			// Display the snowman
			self.render();
		});
	},

	// ...
}
```

The `initialize()` method works like a constructor of the view.
Here we retrieve the collection and if it's empty we will store the circles:

```js
addDefaultCircles: function() {
	// Add 3 circle to the backbone collection
	var topCircle     = new MyCircle({cx: 150, cy:90, r:30});
	var middleCircle  = new MyCircle({cx: 150, cy:160, r: 40});
	var bottomCircle  = new MyCircle({cx: 150, cy:250, r: 50});

	this.collection.add([topCircle, middleCircle, bottomCircle]);
	topCircle.save();
	middleCircle.save();
	bottomCircle.save();
},
```

Now that we've got our circles, let display them:

```js
render: function() {
	var self          = this;
	var elementsToAdd = [];
	_.each(self.collection.models, function (circleData) {
		circleData.attributes.type = 'circle';
		elementToAdds.push(circleData.attributes);
	});

	var circlesSet = self.paper.add(elementsToAdd);
	circlesSet.attr('fill', '#def');
},
``` 

We have loaded the collection on the `initialize()` method, we can loop on each elements.
Raphael's `paper.add()` method needs an array of properties (position, radius, length, ...) and the type of shape.

We contruct this array with the retrieved data and add a type 'circle' property.

## Handling Events

Handling events on Raphael’s objects is similar to regular DOM events. The key is to keep an association between the Raphael’s object and the DOM element.

To do so, the Raphael element’s id is set on the DOM element.

When catching an event, as it returns the DOM element, we can easily get the Raphael element from its id.

```js
events: {
	'click circle': onElementClicked
},

onElementClicked: function(evt) {
	var domElement = evt.target;
	var raphaelId = domElement.raphaelid;
	if (raphaelId == undefined && domElement.parentNode) {
		raphaelId = domElement.parentNode.raphaelid;
	}
	
	var circle = this.paper.getById(raphaelId);
	circle.animate(Raphael.animation({fill: '#0084B4'}, 2000));
}
```

Be sure to handle every case.

In this example, we also deal with click on text tags. The event doesn’t return the text element, but its child (a tspan tag). That's why we get the `raphaelId` from the parent’s element.

An alternative would be to use Raphael's event binding methods. But it doesn't use event delegation, and it diverges from the usual Backbone behavior, so we found preferable to stick with Backbone event handlers.

## Collections And Sets

Although Backbone's collections and Raphael sets allow to handle a group of elements, do not get confused about theses.

A Backbone collection handles Backbone models (allowing saving / updating and retrieving them) and a Raphael set aims to group SVG elements to apply transformations on them directly:

```js
// Display hat
var hat = this.paper.set();
hat.push(
	this.paper.rect(125, 35, 50, 20),
	this.paper.rect(115, 55, 70, 5)
);

// Find the center of the hat
var cX = hat.getBBox().x + hat.getBBox().width/2;
var cY = hat.getBBox().y + hat.getBBox().height/2;

var hatAnimation = Raphael.animation({transform: ['R', 30, cX, cY, 'T', 20, 5]}, 1000);
hat
	.attr('fill', '#eee')
	.animate(hatAnimation);
```

A Backbone collection can be converted as a Raphael set the same way as we have done in the `render()` method.

## Conclusion ##

I hope this introduction to the integration of Raphael with Backbone will convince you to make beautiful and interactive masterpieces in SVG.

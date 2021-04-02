# IBM Bluemix DevOps Services - node-swagger-ui-middleware

This module offers an express middleware for generating a swagger UI from a spec. It provides endpoints for a instance of Swagger UI where mounted.  The data for the UI is gathered from the provided object/spec.

Link to [Bluemix Public IDS Experiment](https://new-console.ng.bluemix.net/dashboard/devops).

This is one of hundreds of [IBM Open Source projects at GitHub](http://ibm.github.io).

# License

[The MIT License (MIT)](LICENSE.txt)

# Contributing

Contributions are welcome via Pull Requests. Please submit your very first Pull Request against the [Developer's Certificate of Origin](DCO.txt), adding a line like the following to the end of the file... using your name and email address of course!

Signed-off-by: John Doe <john.doe@example.org>


# USAGE

	/* Creates a swagger API viewer on port 8080 under /swagger, using the spec in spec/swagger-spec.json */

	var
	 express = require("express"),
	 swaggerSpec = require(path.join(__dirname, "spec", "swagger-spec.json")),
	 swaggerUi = require("swagger-ui-middleware")
	;

	var app = express();
	app
	.use("/swagger", swaggerUi(swaggerSpec))
	.listen(8080)
	;

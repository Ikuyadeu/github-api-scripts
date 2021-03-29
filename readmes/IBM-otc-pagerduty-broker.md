# IBM Bluemix DevOps Services - PagerDuty broker

This component is an implementation of OpenToolChain Service Broker that allows to integrate PagerDuty in a toolchain.
The PagerDuty broker's main responsibility is to create PagerDuty incidents out of major tool failures in OTC, e.g. when a Deploy stage fails in the OTC pipeline.
It is written using Node.js.

See [IBM Garage Method and Slack Tool (Culture)](https://www.ibm.com/devops/method/content/manage/tool_pagerduty) and 
[IBM Bluemix Toolchain tutorial](https://www.ibm.com/devops/method/tutorials/tutorial_toolchain_flow)

Also see [Bluemix Public IDS Experiment](https://new-console.ng.bluemix.net/dashboard/devops).

This is one of hundreds of [IBM Open Source projects at GitHub](http://ibm.github.io).

# License

[The MIT License (MIT)](LICENSE.txt)

# Contributing

Contributions are welcome via Pull Requests. Please submit your very first Pull Request against the [Developer's Certificate of Origin](DCO.txt), adding a line like the following to the end of the file... using your name and email address of course!

Signed-off-by: John Doe <john.doe@example.org>

# Usage

Local Usage
-----------
    # Create a local config file from the provided template
    cp config/local-dev.json.template config/local-dev.json
    
    # Edit config/local-dev.json and update the following:
    - Replace CLOUDANT_URL with your Cloudant URL:
        https://<cloudant id>:<cloudant pw>@<cloudant id>.cloudant.com
    - Provide values for TIAM* properties:
           Contact Simon H for Stage1 values.
    - Update services:
        Use the URLs according to your environment
    - Provide value for IBM_SNIP_API_KEY (this creates the short URL for the user - see http://ibm.biz/api for obtaining such key)

    # Tell the broker to use your local config
    export NODE_ENV=local-dev
    
    # Install the module dependencies
    npm install
    
    # Start the node app
    npm start

    # Create a test configuration from the provided template 
    cp config/testUtils.json.template config/testUtils.json

    # Edit config/testUtils.json and update the following:
    - pagerduty site_name and api_key (corresponding to the configuration for test user)
    - test_tiam_id and test_tiam_secret (TIAM properties required to invoke the broker API)
    
    # To run the tests, run:
    npm test
    
    Note: test configuration


Dependencies
------------
The PagerDuty Broker has the following dependencies:
- Cloudant
- IBM Snip API
- PagerDuty
- TIAM

Logging
-------
Logging for the PagerDuty Broker is handled using log4js.
To configure the logging levels and output location, modify the config/log4js.json file.
The `request` filter will output Express requests.
The `otc-pagerduty-broker` filter indicates any logging for this component.
Note: Environment variable LOG4J_LEVEL can be set to change the logging level for otc-pagerduty-broker filter at runtime


# API

Refer to the [swagger](https://otc-pagerduty-broker.ng.bluemix.net/swagger/) for more information on the PagerDuty broker's endpoints.

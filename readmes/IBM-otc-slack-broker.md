# IBM Bluemix DevOps Services - Slack broker

This component is an implementation of OpenToolChain Service Broker that allows to integrate Slack in a toolchain.
The Slack Broker main responsibity is to create the Slack messages out of the events coming from OTC.
It is written using Node.js.

Link to [IBM Garage Method and Slack Tool (Culture)](https://www.ibm.com/devops/method/content/culture/tool_slack) and 
[IBM Bluemix Toolchain tutorial](https://www.ibm.com/devops/method/tutorials/tutorial_toolchain_flow)

Link to [Bluemix Public IDS Experiment](https://new-console.ng.bluemix.net/dashboard/devops).

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
        Use the services and icons URLs according to your environment (services:* and icons:*)


    # Tell the broker to use your local config
    export NODE_ENV=local-dev
    
    # Install the module dependencies
    npm install
    
    # Start the node app
    npm start
    
    # Create a test configuration from the provided template 
    cp config/testUtils.json.template config/testUtils.json

    # Edit config/testUtils.json and update the following:
    - slack_domain and slack_token (corresponding to the configuration for test user)
    - test_tiam_id and test_tiam_secret (TIAM properties required to invoke the broker API)
        
    # To run the tests, run:
    npm test

Dependencies
------------
The Slack Broker has the following dependencies:
- Cloudant
- Slack (usage of [Slack Web API](https://api.slack.com/web) thru [slack-node](https://www.npmjs.com/package/slack-node) module) 
- TIAM

Logging
-------
Logging for the Slack Broker is handled using log4js.
To configure the logging levels and output location, modify the config/log4js.json file.
The `request` filter will output Express requests.
The `otc-slack-broker` filter indicates any logging for this component.
Note: Environment variable LOG4J_LEVEL can be set to change the logging level for otc-slack-broker filter at runtime

<include if applicable>

# API

Refer to the [swagger](https://otc-slack-broker.ng.bluemix.net/swagger/) for more information on the implemented endpoints.

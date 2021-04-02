This repository contains java sdk and samples for Invoicing API.

## Support

> Please contact [PayPal Technical Support](https://developer.paypal.com/support/) for any live or account issues.

Prerequisites:
---------------
*	Java jdk-1.5 or higher
*	Apache Maven 3 or higher
*	Please refer http://maven.apache.org/guides/getting-started/maven-in-five-minutes.html for any help in Maven.

To build sdk and samples:
--------------------------
*	Build core files from https://github.com/paypal/sdk-core-java, as it is a dependency for sdk.
*	Then, run 'mvn install' to build sdk jar and sample war files.

SDK Integration:
----------------
For Non-Maven Users:
--------------------
*   Create a new application.

*   Copy  all the jar files present inside 'lib' folder to your application.

For Maven Users:
----------------
*   Install all the jar files present inside 'lib' folder manually to local repository. 

        mvn install:install-file -Dfile=commons-codec-1.3.jar -DgroupId=commons-codec -DartifactId=commons-codec -Dversion=1.3 -Dpackaging=jar
        mvn install:install-file -Dfile=paypal-core-1.0.jar -DgroupId=com.paypal.sdk -DartifactId=paypal-core -Dversion=1.0 -Dpackaging=jar
		mvn install:install-file -Dfile=invoicesdk-2.6.117.jar -DgroupId=com.paypal.sdk -DartifactId=invoicesdk -Dversion=2.6.117 -Dpackaging=jar	

For Non-Maven Users:
--------------------
*   Create a new application.

*   Copy  all the jar files present inside 'lib' folder to your application.

For Maven Users:
----------------
*   Install all the jar files present inside 'lib' folder manually to local repository. 

        mvn install:install-file -Dfile=commons-codec-1.3.jar -DgroupId=commons-codec -DartifactId=commons-codec -Dversion=1.3 -Dpackaging=jar
        mvn install:install-file -Dfile=paypal-core-1.0.jar -DgroupId=com.paypal.sdk -DartifactId=paypal-core -Dversion=1.0 -Dpackaging=jar
		mvn install:install-file -Dfile=invoicesdk-2.6.117.jar -DgroupId=com.paypal.sdk -DartifactId=invoicesdk -Dversion=2.6.117 -Dpackaging=jar	

*	Create a new maven application.

*	Add dependency to sdk in your application's pom.xml as below.

    ```xml
    <dependency>
        <groupId>com.paypal.sdk</groupId>
        <artifactId>invoicesdk</artifactId>
        <version>2.6.117</version>
    </dependency>
    ```

To make an API call:
--------------------		
*	Import InvoiceService.java into your code.
		
*	Create a configuration file 'sdk_config.properties' with parameters specified in configuration section (make sure the file is in class path). Use the default constructor to run with configuration used from 'sdk_config.properties' found in classpath.
	```java
	new InvoiceService();
	```
*	For Dynamic configuration(configuration is tied to the lifetime of the service object)
	```java
	new InvoiceService(new File("/pathto/custom.properties"));
			Or
	new InvoiceService(new FileInputStream(new File("/pathto/custom.properties")));
			Or
	new InvoiceService("/pathto/custom.properties");
			Or
	new InvoiceService(Map<String, String> customConfigurationMap);
			Or
	new InvoiceService(Properties customProperties);
	```
*	The SDK takes defaults for certain parameters (eg: Account Credentials and either of 'mode' or 'service.Endpoint' are mandatory parameters).

*	Create a service wrapper object.

*	Create a request object as per your project needs. 

*	Invoke the appropriate method on the service wrapper object.

    For example,

          
    ```java
    import com.paypal.svcs.services.InvoiceService;
    import com.paypal.svcs.types.common.RequestEnvelope;
    import com.paypal.svcs.types.pt.*;
    ...
    RequestEnvelope env = new RequestEnvelope();
    env.setErrorLanguage("en_US");
    ...
    List<InvoiceItemType> items = new ArrayList<InvoiceItemType>();
    InvoiceItemListType invoiceItem = new InvoiceItemListType();
    InvoiceItemType item = new InvoiceItemType();
    item.setName("product1");
    invoiceItem.setItem(item);
    ...
    InvoiceType invo = new InvoiceType();
    invo.setCurrencyCode("USD");
    invo.setItemList(invoiceItem);
    ...
    CreateInvoiceRequest createInvoiceRequest = new CreateInvoiceRequest();
    createInvoiceRequest.setInvoice(invo);
    createInvoiceRequest.setRequestEnvelope(env);
    ...
    InvoiceService invoiceService = new InvoiceService();
			Or
    Map<String, String> customConfigurationMap = new HashMap<String, String>();
    customConfigurationMap.put("mode", "sandbox"); // Load the map with all mandatory parameters
    ...
    InvoiceService invoiceService = new InvoiceService(Map<String, String> customConfigurationMap);    
    CreateInvoiceResponse createInvoiceResponse = invoiceService.createInvoice(createInvoiceRequest,userName);
    ```

SDK Logging:
------------
*	For logging - java.util.logging has been used. To change the default configuration, edit the logging.properties file in 'jre/lib' folder under your JDK root.		  

		  
SDK Configuration:
------------------
The SDK uses dynamic configuration map or '*.properties' format configuration file as shown in code snippet above, to configure

*	Mode is specified using the parameter name 'mode' with values 'sandbox' or 'live', if specified 'service.EndPoint' parameter is not required and the SDK chooses the sandbox or live endpoints automatically.

*	(Multiple) API account credentials, by appending a '.' (dot) character and the service name to 'service.EndPoint' parameter.

*	HTTP connection parameters, if certain connection parameters are not specified, the SDK will assume defaults for them.

*	Service configuration.

*   You can refer full list of configuration parameters in [wiki](https://github.com/paypal/sdk-core-java/blob/master/README.md) page.

Multiple SDK usage (Multiple End-points Support)
---------------------------
Multiple end-points configuration can be done by specifying mulitple end-points identified by specific property keys. 
When using multiple SDKs in combination, like Merchant and Permissions etc..configure the endpoints as shown below 
one for each service used, The existing service.EndPoint property is still supported for backward compatibility (using 
a single SDK). The list below specifies endpoints for different services, in SANDBOX and PRODUCTION, with their 
property keys and end-point as property values.

For additional information on Invoicing API, please refer to https://www.x.com/developers/paypal/documentation-tools/api

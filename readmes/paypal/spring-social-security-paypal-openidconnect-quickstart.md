Spring Social PayPal Quickstart (Spring 3.2.x)
==============================================

This sample app shows how use [Spring Social PayPal OpenIdConnect] to login with a PayPal user and obtain identity information.

    git clone git@github.com:paypal/spring-social-paypal-openidconnect.git
    cd spring-social-paypal-openidconnect
	mvn clean install
	cd ..
    git clone git@github.com:paypal/spring-social-security-paypal-openidconnect-quickstart.git
    cd spring-social-security-paypal-openidconnect-quickstart
    mvn clean install
    mvn tomcat:run

Then browse: `http://localhost:8080/spring-social-paypal-quickstart-32x/signin`

This example application is based on 'https://github.com/SpringSource/spring-social-samples/tree/master/spring-social-quickstart-3.0.x' sample.
It has been updated to use Spring 3.2 version.  Config files are under org.springframework.social.quickstart.config package.

Spring Social Paypal extension is based on OpenId Connect protocol.  It includes both JDBC and InMemory connection repository implementation.

SocialConfig has a commented out line: 
```//InMemoryUsersConnectionRepository repository = new InMemoryUsersConnectionRepository(connectionFactoryLocator());```

Please uncomment this one if you do not intend to use H2 database.

For any help or more info, please write an email to *abprabhakar@paypal.com*

Note:  clientid and secret used in application.properties is already registered sample application.  Please replace with your own if you desire.



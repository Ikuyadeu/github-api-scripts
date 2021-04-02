[![Build Status](https://travis-ci.org/localstack/localstack-java-utils.svg)](https://travis-ci.org/localstack/localstack-java-utils)
[![Maven Central](https://img.shields.io/maven-central/v/cloud.localstack/localstack-utils)](https://mvnrepository.com/artifact/cloud.localstack/localstack-utils)

# LocalStack Java Utils

Java utilities and JUnit integration for [LocalStack](https://github.com/localstack/localstack).

## Prerequisites

* Java
* Maven
* Docker
* LocalStack

## Usage

In order to use LocalStack with Java, this project provides a simple JUnit runner and a JUnit 5
extension. Take a look at the example JUnit tests in `src/test/java`.

By default, the JUnit Test Runner starts LocalStack in a Docker container, for the duration of the test.
The container can be configured by using the `@LocalstackDockerProperties` annotation.

```java
...
import cloud.localstack.LocalstackTestRunner;
import cloud.localstack.ServiceName;
import cloud.localstack.TestUtils;
import cloud.localstack.docker.annotation.LocalstackDockerProperties;

@RunWith(LocalstackTestRunner.class)
@LocalstackDockerProperties(services = { ServiceName.S3, "sqs", "kinesis" })
public class MyCloudAppTest {

  @Test
  public void testLocalS3API() {
    AmazonS3 s3 = TestUtils.getClientS3()
    List<Bucket> buckets = s3.listBuckets();
    ...
  }

}
```

Or with JUnit 5:

```java
@ExtendWith(LocalstackDockerExtension.class)
@LocalstackDockerProperties(...)
public class MyCloudAppTest {
   ...
}
```

## Installation

The LocalStack JUnit test runner is published as an artifact in Maven Central.
Simply add the following dependency to your `pom.xml` file:

```xml
<dependency>
    <groupId>cloud.localstack</groupId>
    <artifactId>localstack-utils</artifactId>
    <version>0.2.9</version>
</dependency>
```

## Configuration

You can configure the Docker behaviour using the `@LocalstackDockerProperties` annotation with the following parameters:

| property                    | usage                                                                                                                        | type                         | default value |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------|------------------------------|---------------|
| `pullNewImage`              | Determines if a new image is pulled from the docker repo before the tests are run.                                           | boolean                      | `false`         |
| `services`                  | Determines which services should be run when the localstack starts.                                                          | String[]                     | All           |
| `imageName`                 | Use a specific image name (organisation/repo) for docker container                                                           | String                       | `localstack/localstack`  |
| `imageTag`                  | Use a specific image tag for docker container                                                                                | String                       | `latest`        |
| `portEdge`                  | Port number for the edge service, the main entry point for all API invocations                                               | String                       | `4566`        |
| `portElasticSearch`         | Port number for the elasticsearch service                                                                                    | String                       | `4571`        |
| `hostNameResolver`          | Used for determining the host name of the machine running the docker containers so that the containers can be addressed.     | IHostNameResolver            | `localhost`     |
| `environmentVariableProvider` | Used for injecting environment variables into the container.                                                               | IEnvironmentVariableProvider | Empty Map     |
| `bindMountProvider          | Used bind mounting files and directories into the container, useful to run init scripts before using the container.          | IBindMountProvider           | Empty Map     |
|  initializationToken        | Give a regex that will be searched in the logstream of the container, start is complete only when the token is found. Use with bindMountProvider to execute init scripts. | String | Empty String |
| `useSingleDockerContainer`  | Whether a singleton container should be used by all test classes.                                                            | boolean | `false`     |

For more details, please refer to the README of the main LocalStack repo: https://github.com/localstack/localstack

> **_NOTE:_** These utilities assume docker is installed in one of the default locations (`C:\program files\docker\docker\resources\bin\docker.exe`,
`C:\program files\docker\docker\resources\docker.exe`, `usr/local/bin/docker` or `usr/bin/docker`). If your docker executable is in a
different location, then use the `DOCKER_LOCATION` environment variable to specify it.

### Deprecated Configurations

Due to recent changes in LocalStack (exposing all services via a single edge port, `4566`), the following configuration parameters are now deprecated in the latest version:

| property                    | usage                                                                                                                        | type                         | default value |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------|------------------------------|---------------|
| `randomizePorts`            | Determines if the container should expose the default local stack ports (4567-4583) or if it should expose randomized ports. | boolean                      | `false`         |

_Note: When specifying the port in the `services` property, you cannot use `randomizePorts = true`_

## Building

To build the latest version of the code via Maven:

```sh
make build
```

## Change Log

* v0.2.10: Add Lambda async utils for AWS SDK v2; add support for specifying bind mounts and init scripts via `@LocalstackDockerProperties`; add PowerMock integration for easy patching of AWS SDK to use local endpoints; add support for configuring the Docker image name via `@LocalstackDockerProperties`; add tests for templated emails
* v0.2.8: Allow overwriting the port binding via environment variables
* v0.2.7: Extend `@LocalstackDockerProperties` to include port binding
* v0.2.6: Add new path to possible docker exe locations in Windows; add various additional tests for v1 and v2 SDKs (Kinesis, SQS, SSM & SecretsManager, ...)
* v0.2.5: Refactor code to accommodate edge port config for all services; add CloudWatch Logs endpoint configuration
* v0.2.2: Addition of CloudWatch Logs endpoint configuration; adjust tests to use central edge service endpoint
* v0.2.1: Move Java sources into separate project; mark non-Docker Java `LocalstackExtension` as deprecated; update paths for Python code lookup in Docker container
* v0.2.0: Last version still maintained in LocalStack main repo

## PowerMock

You can use the PowerMock Library to call the builders default method and still get LocalStack version of the AWS clients.

```java
...
@RunWith(PowerMockRunner.class)
@PowerMockRunnerDelegate(LocalstackTestRunner.class)
@LocalstackDockerProperties(services = { "ses" })
@PrepareForTest({ AmazonSimpleEmailServiceClientBuilder.class, AmazonSimpleEmailServiceAsyncClientBuilder.class })
@PowerMockIgnore({"javax.crypto.*", "org.hamcrest.*", "javax.net.ssl.*", "com.sun.org.apache.xerces.*", "javax.xml.*", "org.xml.*", "javax.management.*", "javax.security.*", "org.w3c.*"})
public class SESMessagingTest {
....
    @Before
    public void mockSES() {
        AmazonSimpleEmailService mockSes = TestUtils.getClientSES();
        PowerMockito.mockStatic(AmazonSimpleEmailServiceClientBuilder.class);
        when(AmazonSimpleEmailServiceClientBuilder.defaultClient()).thenReturn(mockSes);
    }
    @Test
    public void testSendEmail() throws Exception {
        AmazonSimpleEmailService client = amazonSimpleEmailServiceClientBuilder.defaultClient();
    ....
```

## PowerMockLocalStack Utility

This utility makes easier to use PowerMock with Localstack.

```java
...
public class PowerMockLocalStackExampleTest extends PowerMockLocalStack{
    private static final String TOPIC = "topic";
    @Before
    public void mock() {
        PowerMockLocalStack.mockSNS();
    }

    @Test
    public void testSendMessage() throws JMSException {
        final AmazonSNS clientSNS = AmazonSNSClientBuilder.defaultClient();
        ...
    }
}
```

## Acknowledgements
I thank you [Keith Humphreys](https://gitlab.com/keithh), for showing us how to empower LocalStack with PowerMock to write tests even easier.

## License

This code is released under the Apache License, Version 2.0 (see LICENSE.txt).

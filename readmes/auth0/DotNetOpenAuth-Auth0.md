# This project is now deprecated. 

Auth0 authentication client for the [DotNetOpenAuth library](http://www.dotnetopenauth.net/).

## Installation

    Install-Package DotNetOpenAuth-Auth0

## Usage

If you are working with the default template of Asp.NET MVC 4, the easiest way to get you up and running is to modify the ```AuthConfig``` file inside of App_Start as follows

~~~csharp
public static void RegisterAuth()
{
    Auth0.OpenAuthClient.RegisterAllSocialProviders(
            "your client id",
            "your client secret",
            "your domain");
}
~~~

## Documentation

For more information about [auth0](http://auth0.com) visit our [documentation page](http://docs.auth0.com/).

## Issue Reporting

If you have found a bug or if you have a feature request, please report them at this repository issues section. Please do not report security vulnerabilities on the public GitHub issue tracker. The [Responsible Disclosure Program](https://auth0.com/whitehat) details the procedure for disclosing security issues.

## Author

[Auth0](https://auth0.com)

## License

This project is licensed under the MIT license. See the [LICENSE](LICENSE) file for more info.

This is a project integrating the log4j logger with Exceptional to report a configurable number of log errors to Exceptional. Exceptional4j is licensed under the Apache 2 license.

To include it with maven, you can do:

```
    <dependency>
      <groupId>org.getlantern</groupId>
      <artifactId>exceptional4j</artifactId>
      <version>0.1-SNAPSHOT</version>
    </dependency>
```

We'll sync it with Maven central as soon as it's stable, but until then you need to add the Sonatype SNAPSHOTS repo if you don't already include it, as in:

```
    <repository>
      <id>sonatype-nexus-snapshots</id>
      <name>Sonatype Nexus Snapshots</name>
      <url>
        https://oss.sonatype.org/content/repositories/snapshots
      </url>
      <releases>
        <enabled>false</enabled>
      </releases>
      <snapshots>
        <enabled>true</enabled>
      </snapshots>
    </repository>
```

Exceptional4j is currently set up to be integrated programmatically when your application first loads, for example:

```
    private void configureProductionLogger() {
        final File logFile = new File("/var/log/myapp.log");
        final Properties props = new Properties();
        try {
            final String logPath = logFile.getCanonicalPath();
            props.put("log4j.appender.RollingTextFile.File", logPath);
            props.put("log4j.rootLogger", "warn, RollingTextFile");
            props.put("log4j.appender.RollingTextFile",
                "org.apache.log4j.RollingFileAppender");

            PropertyConfigurator.configure(props);
            final ExceptionalAppenderCallback callback = 
                new ExceptionalAppenderCallback() {
                    @Override
                    public boolean addData(final JSONObject json, final LoggingEvent le) {
                        json.put("version", LanternConstants.VERSION);
                        return true;
                    }
            };
            final Appender bugAppender = new ExceptionalAppender(
               "YOUR_API_KEY", callback);
            BasicConfigurator.configure(bugAppender);
        } catch (final IOException e) {
            System.out.println("Exception setting log4j props with file: "
                    + logFile);
            e.printStackTrace();
        }
    }
```

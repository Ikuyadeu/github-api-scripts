Logentries agent
================

[![License](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)](https://github.com/mdp/rotp/blob/master/LICENSE)

A command line utility for a convenient access to Logentries logging
infrastructure.

  * [How to use](#how-to-use)
  * [Repositories](#repositories)
  * [Configuration file](#configuration-file)
  * [Follow log files through server-side configuration](#follow-log-files-through-server-side-configuration)
  * [Follow log files through your configuration file](#follow-log-files-through-your-configuration-file)
  * [Using local configuration only](#using-local-configuration-only)
  * [List IP addresses the agent uses](#list-ip-addresses-the-agent-uses)
  * [Follow logs that change their names](#follow-logs-that-change-their-names)
  * [Follow a log that appears across multiple directories](#follow-a-log-that-appears-across-multiple-directories)
  * [Save state of file positions](#state-file)
  * [Manipulate your data in transit](#manipulate-your-data-in-transit)
  * [Format output entries](#format-output-entries)
  * [Filtering file names](#filtering-file-names)
  * [Multiline log entries](#multiline-log-entries)
  * [System metrics (beta)](#system-metrics-beta)
    * [CPU](#cpu)
    * [VCPU](#vcpu)
    * [Memory](#memory)
    * [Swap](#swap)
    * [Network](#network)
    * [Disk IO](#disk-io)
    * [Disk space](#disk-space)
    * [Processes](#processes)
  * [Deployment best practices](#deployment-best-practices)
  * [Linux Agent Installation](#linux-agent-le-agent-installation)



How to use
----------

	usage: le COMMAND [ARGS]

	Where COMMAND is one of:
	init      Write local configuration file
	reinit    As init but does not reset undefined parameters
	register  Register this host
	--name=  name of the host
	--hostname=  hostname of the host
	whoami    Displays settings for this host
	monitor   Monitor this host
	follow <filename>  Follow the given log
	--name=  name of the log
	--type=  type of the log
	--multilog option used with directory wildcard (restricted behaviour - see below for details)
	followed <filename>  Check if the file is followed
	clean     Removes configuration file
	ls        List internal filesystem and settings: <path>
	ls ips    List IP addresses used by the agent
	rm        Remove entity: <path>
	pull      Pull log file: <path> <when> <filter> <limit>

	Where ARGS are:
	--help            show usage help and exit
	--version         display version number and exit
	--account-key=    set account key and exit
	--host-key=       set local host key and exit, generate key if key is empty
	--no-timestamps   no timestamps in agent reportings
	--force           force given operation
	--datahub         send logs to the specified data hub address
	                  the format is address:port with port being optional
	--suppress-ssl    do not use SSL with API server
	--yes	          always respond yes
	--pull-server-side-config=False do not use server-side config for following files


Repositories
------------

For Debian/Ubuntu systems include this line in `/etc/apt/sources.list.d/logentries.list`:

	deb http://rep.logentries.com/ XXX main

Replace `XXX` with the name of your system, i.e. one of wheezy, jessie,
lucid, precise, quantal, saucy, trusty, utopic, vivid. You also need to add
Logentries release key:

	apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys A5270289C43C79AD

(Keyservers are not always reliable. In automated scripts do the following.)

	apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys A5270289C43C79AD \
	|| apt-key adv --keyserver hkp://pgp.mit.com:80 --recv-keys A5270289C43C79AD

Then run `apt-get update` and `apt-get install logentries`. If you want to run
the agent as daemon, install it via `apt-get install logentries-daemon`.

For rpm-based systems RH, CentOS, Fedora, add this in `/etc/yum.repos.d/logentries.repo`

	[logentries]
	name=Logentries repo
	enabled=1
	metadata_expire=1d
	baseurl=https://rep.logentries.com/XXX/\$basearch
	gpgkey=https://rep.logentries.com/RPM-GPG-KEY-logentries

Replace `XXX` with the name of your system; eg., one of `fedora21`, `rh5`,
`rh6`, `amazonlatest`, `centos5`, `centos6`, or `centos7`. Other distributions
and versions may be supported as well; if your distribution isn't listed here,
be sure to check [rep.logentries.com](https://rep.logentries.com).

Then run `yum update` and `yum install logentries`. If you want to run the agent
as daemon, install it via `yum install logentries-daemon`.


Configuration file
------------------

The agent stores configuration in `~/.le/config` for ordinary users and in
`/etc/le/config` for root (daemon). It is created with `init` or `reinit`
commands and can be created or modified manually.

The agent supports loading multiple configuration files from a configuration
directory. By default the configuration directory is `~/.le/conf.d/` for
ordinary users and `/etc/le/conf.d` for root (daemon). Only files with `.conf`
extension are recognized as configuration files.

The structure of a configuration file follows standard similar to what you
find in `.git/config` or Windows INI files. For example:

	[Main]
	user-key = e720a1e8-a7d5-4f8b-8879-854e51c9290d
	agent-key = 428b888a-29ab-4079-99ec-9cb7aa2ffea7

	[cassandra]
	metrics-process = org.apache.cassandra.service.CassandraDaemon
	path = /var/log/cassandra/system.log
	token = a846bd59-a674-4088-b9fd-e72da1df5946

Main section `[Main]` contains agent-wide general configuration. Any other
section defines per-application settings such as log filenames and metrics.

In the main section, `user-key` (account key) which identifies account, and
`agent-key` which identifies host (host key).

Note the `monitor` command requires both `user-key` and `agent-key` defined.

### User-specified configuration directory

Additionaly to the default configuration directory, the agent allows to specify
a secondary configuration directory. Just specify the `include` parameter in
the main section as follows:

	[Main]
	user-key = e720a1e8-a7d5-4f8b-8879-854e51c9290d
	include = /opt/configurations/logentries/conf.d

Again, the agent recognizes all files with `.conf` extension.


Follow log files through server-side configuration
--------------------------------------------------

After registering the host (via `register` command or specifying `agent-key` in
configuration) you can add a file to follow via `follow` command:

	sudo le follow /srv/log/cassandra/system.out [--name Cassandra]

You can repeat the command for additional logs. The agent creates a new log
entry in Logentries under the host specified. It will also enable the file to
be followed by the agent.

Note `--name` is optional to specify log name as it will appear in UI and log
listing. If not specified, plain file name is used.

You need to restart the agent to pick up the new configuration:

	sudo service logentries restart


Follow log files through your configuration file
------------------------------------------------

Apart from server-side configuration you can configure log files to be followed
locally. Locally configured logs use token-based inputs and enables to collect
log entries from multiple sources into one destination log. This can be useful
in an autoscaling environment. You can reuse the same configuration file
multiple times without creating new hosts.

Each log to follow has a separate section in the configuration of the form:

	[name]
	path = /path/to/log/file
	token = MY_TOKEN

Where:

-  *name* is an identifier of the application that is added to your log entries
-  *path* is an absolute path to the file you wish to follow
-  *token* is the token for destination log created in Logentries

Alternatively, instead of `token` specify `destination` parameter in the format
of `host name/log name'. The agent will search for the host and log identified
by their name and retrieve the token automatically. If the host or log does not
exist, it is created.

**Note**: When using the destination parameter it is advised not to initialize
multiple agents with the same configuration file at the same time. This is to
prevent a race condition where duplicate Log Sets may be created.

Example:

	[name]
	path = /path/to/log/file
	destination = MyHost/MyLog


Using local configuration only
------------------------------

In an auto scaling environment you may not want to create a Host (log set) each
time you install the agent.

To disable pulling server-side configuration (and thus avoiding communication
with Logentries API) add this line in the `[Main]` section of the configuration:

	pull-server-side-config=False

Or specify `--pull-server-side-config=False` on the command like for the `init`
or `reinit` commands:

	sudo le reinit --pull-server-side-config=False

When set to False, the agent requires token for all configured logs. Tokens may
be specified in the configuration file, or--in case of logs created by the
agent--it is stored in local cache file.

By default, locally configured logs are sent to Logentries in Syslog format RFC
5424 which prepends a timestamp and other useful information. If you wish to
disable this, you can set the formatter to 'plain' in the `[Main]` section of
the configuration.

	formatter = plain


List IP addresses the agent uses
--------------------------------

Run the `ls ips` command to get a list of IP addresses the agent uses. These IP
addresses needs to be whitelisted in firewall.


Follow logs that change their names
--------------------------------------

Certain log rollover policies do not allow to specify destination file name.
That is typical when log files are timestamped or assigned a sequential number.
The Logentries agent can handle there cases for you.  The Logentries agent can
be pointed at particular folders to gather any active logs from that directory
or its subdirectories using wildcards in file names.  For example, the
following patterns can be used with the follow command to gather logs from the
given directories:

	/var/log/mysystem/mylog-*.log

Using wildcards when specifying the log to follow allows for situations where
you need to follow the most recent log in a particular folder. The agent looks
for any active log in the folder and will monitor the events in that log.

**Note** wildcards are NOT needed in typical syslog log rotation scheme, where
log file named `xxx.log` is renamed to `xxx.log.0` and a new `xxx.log` file is
created. In this situation follow the `xxx.log` file only, do not specify
wildcards.


Follow a log that appears across multiple directories
-----------------------------------------------------
When using the 'follow' command to set up which log file to be followed, a special
wildcard with restricted behaviour can be used for (or as part of) a directory
name. This option is intended for where multiple log files, with the same filename
but with each log file in a different directory, are to be followed. The log
events captured in all these log files are then sent to a single destination log in
the Logentries infrastructure. Note that this behaviour is different from where
a wildcard is used in the log filename - which is not allowed in this case.

Example:
For this example there is a number of directories in /var/log/, each called 'apache-xx',
where the xx is a number that varies for each directory, such as 'apache-01',
'apache-02' and so on. In addition, within each directory, is a file called 'apache.log'.

We want to follow all 'apache.log' files in each of these directories, with the log
events from all log files sent to a destination log in the Logentries infrastructure
that we want to name 'Apache'.

The command 'follow' is combined with the '--multilog' option to use the wildcard
in the directory name in the path that is passed to the agent.

    le follow '/var/log/apache-*/apache.log' --multilog [--name Apache]

#### Usage
The agent behaviour when usage of the --multilog is made is dependant on
the rules below:

-   The pathname to be passed to the agent must be in single quotes as shown
    in the example. This is necessary, so that the wildcard is not expanded
    by the shell, but processed by the agent internally.
-   The wildcard * is the only one allowed for this behaviour.
-   Only one wildcard is allowed in the pathname.
-   The wildcard can be used in place of a directory name or in place of part
    of a directory name.
-   At all times a full filename must be given.
-   No wildcard is allowed in the filename.
-   Only the one file in each directory found that matches the pattern with
    the wildcard is followed.
-   The wildcard is not required, but then only a single file is followed.
    In such a case, the --multilog option is unnecessary as the default
    behaviour of the 'follow' command can be used to follow a single file.
-   Where the --name is not used, the filename is used to name the destination
    log - which in the case of the example above is 'apache.log'
-   The agent expects the last / as being followed by a filename - it cannot
    be blank - the log filename does not need to have an extension such
    as .log; a log file named 'apache', such as '/var/log/apache*/apache'
    is accepted - as long as it is a full and valid filename.

#### Displayed Lists

If the pathname with the wildcard is valid and accepted by the agent, it will
display to the user two lists that are shown as an aid to help the user
make the most of the wildcard usage.

The first list will display all the existing destination logs for that host found
in use from the server with the pathname of the local log file (or files) associated
with each log. Where there is a log with a pathname that was set up using the --multilog
option a prefix to the pathname 'Multiple:' is shown. This list may show a mix of pathnames -
as some will have been set-up using the --mulitlog option and some not.

So as per the example above, for the log 'Apache', may return a list like this:

    LOG         PATHNAME
    mylog       /var/log/mysystem/mylog-*.log
    Apache      Multiple:/var/log/apache*/apache.log
    Cassandra   /srv/log/cassandra/system.out

The second list will display any files found by the agent at this time after
processing the pathname that fall within the scope of the wildcard. This list
reflects the files that will be followed by the agent for this pathname however,
the files actually followed may differ if directories are deleted or added
before the agent has been restarted or is actively monitoring the log files.

The agent will detect where directories that have a file being followed
is deleted, and will stop following that file. Like wise the agent will monitor
for directories with a file that falls within the scope of the wildcard expansion.
If such a directory is created while the agent is active, it will attempt to
follow this new file - with the same log settings.

The user then has the option to quit without setting any new files to be followed
or the user may continue, in which case the agent will process the pathname.

**Note** that there is no restriction on different destination logs having pathnames
with wildcards that are similar. It is possible therefore that a number of files
will appear to be common to these destination logs. The agent will not prevent this.
It is dependant on the user to understand the scope of the wildcard in the pathname
that is being applied.

For example the following two examples result in a subset of directories with the
same log file falling within the scope of both destination directories:

    le follow '/var/log/apache*/apache.log' --multilog --name=Apace
    le follow '/var/log/*/apache.log' --multilog --name=WebLogs

It is recommended to avoid scenarios like this.

### Client Configuration File
As explained above in the section on using the client side configuration to
follow files, a similar configuration section can used to set up a pathname
with a wildcard - as long as the pathname meets the same rules for one
entered via the command line.

The prefix Multilog: is mandatory.

Example:

    [Apache]
	path = Multilog:/var/log/apache*/current
	token = MY_TOKEN


Save state of file positions
----------------------------

When started in the monitoring mode, the agent follows logs from their current
position. Infrequently, in cases which requires restarting the agent, log
entries logged in the stop-start time period are not captured.

To ensure all entries are captured even during restarts, specify a file where
to store file positions. Upon startup the agent picks the latest position in
the file:

	state-file = /path/state_file_name

Note that this feature may have unpredictable consequences in long stop-start
periods when log files are being rotated. The agent may start from the last
position in a new file, while the origian one has already been renamed.


Manipulate your data in transit
-------------------------------

If you want to modify log entries before they are sent to Logentries, the agent
enables you to do so via filters. Filters are useful for filtering sensitive
information, obfuscating, or explicit parsing (adding key-value pairs).

Specify a Python module directory in your configuration by adding a line in the form of:

	filters = /opt/le/le_filters

Create empty `__init__.py` to set up a module. Then add filters.py file which
contains filters dictionary. The dictionary informs the agent that for the
given log name, log ID, or token, the specified filtering function should be
used. For example the following dictionary:

	filters = {
		"example.log": filter_logname,
		"7e518e54-40e4-4c5a-88df-4559d03126e6": filter_logid,
	}

Where `filter_logname` and `filter_loguuid` are functions which filters events
for the respective log. Filtering functions receive a single string containing
log entries terminated with a new line. Function can modify input entry in any way
and return is back for sending to Logentries servers.
The following skeleton displays typical structure of the
filtering function:

	def filter_example(entry):
		# Do something with entry
		new_entry = entry # XXX
		# Return modified output
		return new_entry

Typical filtering function is much simpler though. For example the following
filtering function removes all occurrences of credit card numbers:

	import re

	# Credit card number matcher
	CREDIT_CARD = re.compile( r'\d{4}-\d{4}-\d{4}-\d{4}')
	# Credit card number replacement
	CC_REPLACEMENT = 'xxxx-xxxx-xxxx-xxxx'  # '-'.join( ['x'*4]*4) if you prefer

	def filter_credit_card( events):
		return CREDIT_CARD.sub( CC_REPLACEMENT, events)

Format output entries
---------------------

The agent allows to format log entries on transit. By default the agent formats entries according to syslog format specification RFC 5424 for locally configured log and plain format for server-side logs.

Default formatter can be overriden by global formatter specified in `[Main]` section. Formatter can be also specified for each application which has a precedence. Lastly, formatters can be implemented by a user-specified code.

### Standard formatters

Standard formatter are `plain` which does not format entries at all, and `syslog` which formats log entries according to syslog format RFC 5424:

	formatter = syslog

### Custom formatters

Format of log entry can be specified directly as a simple substitution template. Selected $-prepended variables are substituted with real values. Recognized variables are:

	$isodatetime ISO date time, for example `2015-08-31T23:05:34.159291`
	$appname application's name
	$hostname local hostname
	$line log entry

For example, the following specification:

	formatter = $isodatetime $appname[$hostname]: $line

Will result in the following log entry:

	2015-08-31T23:05:34.159350 web[myhost]: GET /

### User-implemented formatters

If the standard set of formatters or custom templates do not satisfy your needs, you may provide your own Python implementation.

Specify a Python module directory in your configuration by adding a line in the form of:

		formatters = /opt/le/le_formatters

Create empty `__init__.py` to set up a module. The add `formatters.py` file which contains the `formatters` dictionary. The dictionary informs the agent that for the given log name, log ID, or token, the specified formatting function should be used. For example the following dictionary:

	formatters: {
		'apache': setup_apache_filter,
		'ba543c25-844c-4505-be10-b5aa0b678328': setup_cassandra_filter,
	}

will assign a filter crated by `setup_apache_filter` function to any log with `apache` name. Similarly, log with the token `ba543c25-844c-4505-be10-b5aa0b678328` will be formatted by output of the `setup_cassandra_filter` function.

Setup functions must accept hostname, log name, and token and return a function that accepts log entry. For example:


class Form(object):
	def __init__(self, hostname, log_name, token):
		self.hostname = hostname
		self.log_name = log_name
		self.token = token

	def format_line(self, line):
		return '%sapache on %s: %s'%(self.token, self.hostname, line)

formatters = {
	'apache' : lambda hostname, log_name, token: Form( hostname, log_name, token).format_line,
}


Filtering file names
--------------------

If you want to explicitly restrict which files can the agent follow, create the
filters module as described in the previous section and define the
`filter_filenames` function. The `filter_filenames` function accepts full path to a
file which is about to be followed. The function returns True if the file name
is acceptable or False otherwise. The agent will ignore files which does not
pass this test. The following example defines filter which allows the agent to
follow log files only:

	def filter_filenames( filename):
		return filename.endswith( '.log')

Alternatively, the following example defines filter which denies to follow any
file outside /var/log/ directory:

	def filter_filenames( filename):
		return filename.startswith( '/var/log/')

Note the examples above do not take into account symbolic links.


Multiline log entries
---------------------

If you want to merge multiple lines into one entry, use the `entry_identifier` parameter. It defines via regular expression the beginning of a new entry. In most cases it is a timestamp.

The `entry_identifier` can be used in the global `Main` section to be applied for all logs, or in individual sections.

For example, the following pattern identifies entries based on timestamp encoded in regular expression:

	[cassandra]
	entry_identifier = \d{4}-\d\d-\d\d \d\d:\d\d:\d\d,\d{3}


System metrics
---------------------

**Note:** The agent requires [psutil](https://github.com/giampaolo/psutil) library
installed. This library is commonly available from OS repositories named
`python-psutil`.

The agent collects system metrics regarding CPU, memory, network, disk, and
processes. Example configuration may look like this:

	[Main]
	user-key = ...
	agent-key = ...
	metrics-interval = 5s
	metrics-token = ...
	metrics-cpu = system
	metrics-vcpu = core
	metrics-mem = system
	metrics-swap = system
	metrics-net = sum eth0
	metrics-disk = sum sda4 sda5
	metrics-space = /

	[cassandra]
	metrics-process = org.apache.cassandra.service.CassandraDaemon


Example output may look like this:

	<14>1 2015-01-28T23:42:03.668428Z myhost le - cpu - user=1.1 nice=0.0 system=0.2 load=1.3 idle=98.6 iowait=0.0 irq=0.0 softirq=0.1 steal=0.0 guest=0.0 guest_nice=0.0 vcpus=8
	<14>1 2015-01-28T23:42:03.668566Z myhost le - vcpu - vcpu=0 user=14.4 nice=0.0 system=0.0 load=14.4 idle=785.6 iowait=0.0 irq=0.0 softirq=0.0 steal=0.0 guest=0.0 guest_nice=0.0 vcpus=8
	<14>1 2015-01-28T23:42:03.668588Z myhost le - vcpu - vcpu=1 user=24.0 nice=0.0 system=1.6 load=25.6 idle=774.4 iowait=0.0 irq=0.0 softirq=0.0 steal=0.0 guest=0.0 guest_nice=0.0 vcpus=8
	<14>1 2015-01-28T23:42:03.668603Z myhost le - vcpu - vcpu=2 user=12.8 nice=0.0 system=1.6 load=14.4 idle=785.6 iowait=0.0 irq=0.0 softirq=0.0 steal=0.0 guest=0.0 guest_nice=0.0 vcpus=8
	<14>1 2015-01-28T23:42:03.668617Z myhost le - vcpu - vcpu=3 user=11.2 nice=0.0 system=1.6 load=12.8 idle=785.6 iowait=0.0 irq=0.0 softirq=1.6 steal=0.0 guest=0.0 guest_nice=0.0 vcpus=8
	<14>1 2015-01-28T23:42:03.668631Z myhost le - vcpu - vcpu=4 user=0.0 nice=0.0 system=0.0 load=0.0 idle=800.0 iowait=0.0 irq=0.0 softirq=0.0 steal=0.0 guest=0.0 guest_nice=0.0 vcpus=8
	<14>1 2015-01-28T23:42:03.668645Z myhost le - vcpu - vcpu=5 user=4.9 nice=0.0 system=4.9 load=9.9 idle=780.3 iowait=0.0 irq=0.0 softirq=9.9 steal=0.0 guest=0.0 guest_nice=0.0 vcpus=8
	<14>1 2015-01-28T23:42:03.668658Z myhost le - vcpu - vcpu=6 user=6.4 nice=0.0 system=1.6 load=8.0 idle=792.0 iowait=0.0 irq=0.0 softirq=0.0 steal=0.0 guest=0.0 guest_nice=0.0 vcpus=8
	<14>1 2015-01-28T23:42:03.668673Z myhost le - vcpu - vcpu=7 user=0.0 nice=0.0 system=0.0 load=0.0 idle=800.0 iowait=0.0 irq=0.0 softirq=0.0 steal=0.0 guest=0.0 guest_nice=0.0 vcpus=8
	<14>1 2015-01-28T23:42:03.668762Z myhost le - mem - total=16770625536 available=86.8 used=45.2 free=54.8 active=12.1 inactive=26.9 buffers=0.7 cached=31.2
	<14>1 2015-01-28T23:42:03.668853Z myhost le - swap - total=0 used=0.0 free=0.0 in=0 out=0
	<14>1 2015-01-28T23:42:03.668977Z myhost le - disk - device=sum reads=0 writes=0 bytes_read=0 bytes_write=0 time_read=0 time_write=0
	<14>1 2015-01-28T23:42:03.669071Z myhost le - disk - device=sda4 reads=0 writes=0 bytes_read=0 bytes_write=0 time_read=0 time_write=0
	<14>1 2015-01-28T23:44:29.185629Z myhost le - disk - device=sda5 reads=19 writes=2135 bytes_read=81920 bytes_write=1005879296 time_read=29 time_write=33004
	<14>1 2015-01-28T23:42:03.669123Z myhost le - space - path="/" size=638815010816 used=87.8 free=7.1
	<14>1 2015-01-28T23:42:03.669212Z myhost le - net - net=eth0 sent_bytes=36230 recv_bytes=1260226 sent_packets=481 recv_packets=848 err_in=0 err_out=0 drop_in=0 drop_out=0
	<14>1 2015-01-28T23:52:48.741521Z myhost le - cassandra - cpu_user=0.6 cpu_system=0.0 reads=250 writes=0 bytes_read=0 bytes_write=8192 fds=141 mem=4.4 total=16770625536 rss=734867456 vms=3441418240


### CPU

Specify the `metrics-cpu` parameter to collect CPU metrics. Allowed values are
`system` which will normalize usage of all CPUs to 100%, or `core` which will
normalize usage to single CPU (typical for `top` command).

Example:

	metrics-cpu = core
	metrics-cpu = system

Example log entry:

	<14>1 2015-01-28T23:42:03.668428Z myhost le - cpu - user=1.1 nice=0.0 system=0.2 load=1.3 idle=98.6 iowait=0.0 irq=0.0 softirq=0.1 steal=0.0 guest=0.0 guest_nice=0.0 vcpus=8

Fields explained:

-  *user* time spent processing user level processes with normal or negative
   nice value (higher priority)
-  *nice* time spent processing user level processes with positive nice value
   (lower priority)
-  *system* time spent processing system level tasks
-  *usage* total time spent processing
-  *idle* time spent idle, with no outstanding tasks and no incomplete I/O
   operations
-  *iowait* time spent waiting for I/O operation to complete (idle)
-  *irq* time spent servicing/handling hardware interrupts
-  *softirq* time spent servicing/handling soft interrupts. Commonly servicing
   tasks scheduled independently of hardware interrupts.
-  *steal* time not available for the virtual machine, i.e. stolen by
   hypervisor in concurrent virtual environments
-  *guest* time spent running guest operating systems with normal nice value
-  *guest_nice* time spent running guest operating systems with positive nice
   value
-  *vcpus* total number of CPUs

### VCPU

Specify the `metrics-vcpu` parameter to collect metrics for each individual CPU.
The only viable value is `core` which will normalize usage to single CPU.

Example:

	metrics-vcpu = core

Example log entry:

	<14>1 2015-01-28T23:42:03.668566Z myhost le - vcpu - vcpu=0 user=14.4 nice=0.0 system=0.0 load=14.4 idle=785.6 iowait=0.0 irq=0.0 softirq=0.0 steal=0.0 guest=0.0 guest_nice=0.0 vcpus=8

Fields are similar to CPU section.

### Memory

Specify the `metrics-mem` parameter to collect memory metrics. The only viable
value is `system`.

Example:

	metrics-mem = system

Example log entry:

	<14>1 2015-01-28T23:42:03.668762Z myhost le - mem - total=16770625536 available=86.8 used=45.2 free=54.8 active=12.1 inactive=26.9 buffers=0.7 cached=31.2

Fields explained:

-  *total* physical memory size in bytes
-  *available* amount of memory that is available for processes, typically
   free + buffers + cached
-  *used* memory used by OS (includes caches and buffers)
-  *free* memory not used by OS
-  *active* memory marked as recently used (dirty pages)
-  *inactive* memory marked as not used (old pages)
-  *buffers* memory reserved for temporary I/O storage
-  *cached* part of the memory used as disk cache, tmpfs, vms, and
   memory-mapped files

### Swap

Specify the `metrics-swap` parameter to collect swap area metrics. The only
viable value is `system`.

Example:

	metrics-swap = system

Example log entry:

	<14>1 2015-01-28T23:42:03.668853Z myhost le - swap - total=0 used=0.0 free=0.0 in=0 out=0

Fields explained:

-  *total* size of all swap areas
-  *used* % of swap areas being used
-  *free* % of swap areas being unused
-  *in* input traffic in bytes
-  *out* output traffic in bytes

### Network

In the `metrics-net` configuration parameter specify network interfaces for
which the agent will collect metrics.

Special interfaces are `all` which instructs the agent to follow all interfaces
(including lo), `select` which will follow selected interfaces such as eth and
wlan, and `sum` which aggregates usage of all interfaces in the system.

Example:

	metrics-net = eth0
	metrics-net = sum select
	metrics-net = all

Example log entry:

	<14>1 2015-01-28T23:42:03.669212Z myhost le - net - net=eth0 sent_bytes=36230 recv_bytes=1260226 sent_packets=481 recv_packets=848 err_in=0 err_out=0 drop_in=0 drop_out=0

Fields explained:

-  *net* network interface
-  *bytes_sent* number of bytes sent since last record
-  *bytes_recv* number of bytes received since last record
-  *packets_sent* number of packets sent since last record
-  *packets_recv* number of packets received since last record
-  *err_in* number of errors while receiving
-  *err_out* number of errors while sending
-  *drop_in* number of incoming packets which were dropped
-  *drop_out* number of outgoing packets which were dropped

### Disk IO

In the `metrics-disk` configuration parameter specify devices for which will the agent
collect metrics.

Special device is `all` which instructs the agent to collect metrics for all devices.


Example:

	metrics-disk = sum sda4 sda5
	metrics-disk = all

Example log entry:

	<14>1 2015-01-28T23:44:29.185629Z myhost le - disk - device=sda5 reads=19 writes=2135 bytes_read=81920 bytes_write=1005879296 time_read=29 time_write=33004

Fields explained:

-  *device* device name
-  *reads* number of read operations since last record
-  *writes* number of write operations since last record
-  *bytes_read* number of bytes read since last record
-  *bytes_write* number of bytes written since last record
-  *time_read* time spent reading from device in milliseconds since last record
-  *time_write* time spent writing to device in milliseconds since last record

### Disk space

In the `metrics-space` configuration parameter specify mount points for which
will the agent collect usage metrics.

Example:

	metrics-space = /

Example log entry:

	<14>1 2015-01-28T23:42:03.669123Z myhost le - space - path="/" size=638815010816 used=87.8 free=7.1

Fields explained:

-  *path* disk mount point
-  *size* size of the disk in bytes
-  *used* % of disk space used
-  *free* % of disk space free

Note that used + free might not reach 100% in certain cases.

### Processes

To follow a particular process, specify a pattern matching process' command
argument in `metrics-process`. Specify this parameter in a separate section.

Example:

	[cassandra]
	metrics-process = org.apache.cassandra.service.CassandraDaemon

Example log entry:

	<14>1 2015-01-28T23:52:48.741521Z myhost le - cassandra - cpu_user=0.6 cpu_system=0.0 reads=250 writes=0 bytes_read=0 bytes_write=8192 fds=141 mem=4.4 total=16770625536 rss=734867456 vms=3441418240

Fields explained:

-  *cpu_user* the amount of time process spent in user mode
-  *cpu_system* the amount of time process spent in system mode
-  *reads* the number of read operations since last record
-  *writes* the number of write operations since last record
-  *bytes_read* the number of bytes read since last record
-  *bytes_write* the number of bytes written since last record
-  *fds* the number of open file descriptors
-  *mem* % of memory used
-  *total* total amount of memory
-  *rss* resident set size - the amount of memory this process currently has in
   main memory
-  *vms* virtual memory size - the amount of virtual memory the process has
   allocated, including shared libraries

Deployment best practices
-------------------------

Logentries agent provides several methods of configuration. The method you
choose depends on the size and structure of your environment. You are free to
combine both methods.

**For small systems** such as single web server, mail server, workstation, the
easiest way is to register the host and logs followed via the agent. The agent
will create a Host entry in the UI and send log entries to this Host for each
followed file. Configuration will be stored on Logentries systems and the agent
will pull the latest configuration during startup.

**For large systems** such as computational clusters, autoscaling setups, the
meaning of particular host is losing its meaning as they are becoming
ephemeral. The best option for these systems is to share the same configuration
across servers in the cluster, using locally defined logs only with
pull-server-side-config set to False. Logs are separated per application.
Applications of the same type (i.e. web, mail, DB) will send data to their own log.
Hosts are distinguished by their hostname which is appended to each log entry.


Linux Agent (LE Agent) Installation
-----------------------------------

There are two ways to install the LE Agent.

1. Interactive - Simply run `sudo bash logentries_install.sh`. This will download and install the LE Agent on your machine and prompt you for your Logentries account email and Logentries account password.
2. Automated, using your Logentries' account key - Run the Linux installer using your Logentries Account Key as the first command line arguemnt as in `sudo bash logentries_install.sh <account_key>` for example `sudo bash logentries_install.sh xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`.  This will bypass the prompts for your Email or password and simply download and install the LE Agent adding this Host and its Logs to your Account.

To attain your Logentries Account Key from the Logentries web UI see: https://logentries.com/doc/accountkey/

# axrelay

axrelay is an anonymizing xmpp relay component for xmpp servers.
See [Testing axrelay](#testing-axrelay) below for demonstrations with screenshots.

The official Lantern axrelay instance is running against [prosody](https://prosody.im) on lantern.io
but is not yet in use in production since Googleʼs xmpp servers do not yet support encrypted server-to-server (s2s) connections.
IM Observatory test results are available at https://xmpp.net/result.php?domain=lantern.io&type=client and https://xmpp.net/result.php?domain=lantern.io&type=server.

## Setting up a server

*The following steps were tested on a freshly created and updated Ubuntu 13.10 Digital Ocean droplet in March 2014.*

*Become root as needed.*

### Install dependencies

    apt-get install git memcached python-setuptools python-pylibmc python-crypto prosody

Note that this installs prosody 0.8.2-4 as the xmpp server, and memcached 1.4.14-0ubuntu4.1 as the anonymized jid store.

Install up-to-date versions of pip and virtualenv:

    easy_install-2.7 pip
    pip install virtualenv

### Set up prosody

    vim /etc/prosody/prosody.cfg.lua

In the "Virtual hosts" section, add the following line:

```lua
VirtualHost "lantern.io"
```

where "lantern.io" is the domain you want prosody to listen on.

In the "Components" section, add the following:

```lua
Component "axr.lantern.io"
	component_secret = "axrelay_secret"
```

where "axr.lantern.io" is the subdomain you want axrelay to listen on,
and where "axrelay\_secret" is a secure passphrase.

#### SSL/TLS

As advised by http://wiki.xmpp.org/web/Securing\_XMPP#Prosody, locate

```lua
c2s_require_encryption = false
s2s_require_encryption = false
```

and change "false" to "true", and add `s2s_secure_auth = true` while youʼre at it.

Copy the PEM-encoded certificate and RSA private key for the domain into /etc/prosody/certs.
chgrp them both to group "ssl-cert",
chmod them both to g+rw,
and make the private key chmod o-rwx.

Then locate the global ssl configuratio in prosody.cfg.lua:

```lua
ssl = {
	key = "/etc/prosody/certs/localhost.key";
	certificate = "/etc/prosody/certs/localhost.cert";
}
```

and change the "localhost.{key,cert}" paths to the files you copied.

Now run "/etc/init.d/prosody restart" and check /var/log/prosody/prosody.log to make sure all looks well.

### DNS

You could create an SRV record for xmpp on your domain,
but an A record for "lantern.io" pointing to your serverʼs IP
and a CNAME for "axr" pointing to "lantern.io" will also do the trick.

### Set up axrelay

Install axrelay in a virtualenv using pip:

    virtualenv --system-site-packages /axrelay
    /axrelay/bin/pip install -e 'git+https://github.com/getlantern/axrelay.git#egg=axrelay-dev'

Make sure you can now run the axrelay binary:

    /axrelay/bin/axrelay help

Create a configuration file:

    cp /axrelay/src/axrelay/sample.conf /etc/axrelay.conf
    vim /etc/axrelay.conf

(axrelay looks for configuration in /etc/axrelay.conf by default.)

The configuration in the **[relay]** section
must match the configuration for the axrelay component in prosody.cfg.lua documented above, e.g.

```ini
[relay]
jid      = axr.lantern.io
# using "localhost" instead of "127.0.0.1" here causes axrelay to use ipv6,
# which can make it fail to connect to the xmpp server:
server   = 127.0.0.1
# the default prosody port for external components
port     = 5347
# the secure passphrase you set in prosody.cfg.lua
password = axrelay_secret
```

For the **[hash]** section,
run "axrelay secret" to create a new secret for the "secret" setting.
The "domain" setting is the domain which will be used for anonymized jids
(e.g. "axr.lantern.io")
and should be the domain the xmpp server is listening on
to allow messages sent to the anonymized addresses to be received and relayed to the original addresses by axrelay.

axrelay supports an in-memory store for the jid mappings,
but the memcached store is appropriate for production use.

(This allows mappings to be stored and retrieved from the command line
while memcached is running
via "axrelay hash --store \<original\_jid\>" and "axrelay hash --lookup \<anonymized\_jid\>",
which is handy for testing.)

To use the memcached store,
leave the **[memcache]** section of the axrelay config uncommented,
and leave the **[local\_storage]** section commented out.

After running the "apt-get install" command above, a memcached instance was installed and automatically started on your server. Run "/etc/init.d/memcached status" to verify itʼs running.

To use this memcached instance as axrelayʼs anonymized jid store, leave the "servers" setting set to "localhost".

Run "axrelay secret" again and use the result for the "encrypt" setting
to make axrelay encrypt keys and values in the store.

Finally, run axrelay:

    axrelay/bin/axrelay run --debug

You should see something like the following indicating it connected to ejabberd successfully:

```
2014-03-11 15:25:41,095 DEBUG    Connecting to 127.0.0.1:5347
2014-03-11 15:25:41,097 DEBUG    Event triggered: connected
2014-03-11 15:25:41,097 DEBUG     ==== TRANSITION disconnected -> connected
2014-03-11 15:25:41,097 DEBUG    SEND (IMMED): <stream:stream xmlns="jabber:component:accept" xmlns:stream="http://etherx.jabber.org/streams" to='axr.lantern.io'>
2014-03-11 15:25:41,098 DEBUG    RECV: <stream:stream from="axr.lantern.io" id="da4cd8e0-87c6-4649-b0a7-b5f0a4b29846">
2014-03-11 15:25:41,098 DEBUG    SEND (IMMED): <handshake xmlns="jabber:component:accept">4ee77380535665a37e88180f6cc6df2d46a6df8e</handshake>
2014-03-11 15:25:41,099 DEBUG    RECV: <handshake />
2014-03-11 15:25:41,100 DEBUG    Event triggered: session_bind
2014-03-11 15:25:41,100 DEBUG    Event triggered: session_start
```

## Testing axrelay

### Test axrelay with non-Google xmpp accounts

On your own machine, log in to an xmpp client with two different xmpp accounts.
Weʼll refer to one as account *A*, and the other as account *B*.

*Test with dukgo.com accounts first since they are free to create
and the dukgo.com xmpp server reliably federates with other xmpp servers.
Googleʼs xmpp servers have been known to not always federate with other xmpp servers.*

*As of 2014-03-09, gmail.comʼs and Google apps domainsʼ xmpp servers were not supporting encrypted connections.*

Now send a message from *A* to axr.lantern.io with body "/whoami".
You should get a reply with *A*ʼs new anonymized jid, *Aʹ*:

![screenshot](screenshots/0.A-whoami-A'.png)

Now send a message from *B* to axr.lantern.io with body "/whoami".
You should get a reply with *B*ʼs new anonymized jid, *Bʹ*:

![screenshot](screenshots/1.B-whoami-B'.png)

Now send a message from *B* to *Aʹ*:

![screenshot](screenshots/2.B-messages-A'.png)

*A* should now receive a message with the body of the message you just sent, **but coming from *Bʹ*, not *B*:**

![screenshot](screenshots/3.A-receives-message-from-B'.png)

*A* can now reply to this message:

![screenshot](screenshots/4.A-replies-to-B'.png)

and *B* should get a matching message from *Aʹ*:

![screenshot](screenshots/5.B-receives-message-from-A'.png)

So axrelay allows *A* and *B* to communicate with each other without ever discovering one anotherʼs real addresses.

**RESULT: Great success.**

----
***The following tested axrelay running against ejabberd on xmpp.getlantern.org, before getting a new axrelay instance set up against prosody on lantern.io:***

### Test axrelay with gmail.com xmpp accounts

Log in to Adium with a gmail.com xmpp account, e.g. LanternFriend@gmail.com. Go to Contact \> Add Contact (⌘D), select "XMPP" from the "Contact Type" dropdown, fill in axrelay@xmpp.getlantern.org in the "Jabber ID" field, and hit Add:

![screenshot](screenshots/add_axrelay.png)

(Donʼt worry that axrelay does not accept the presence subscription request and therefore does not appear as online. It seems that simply having axrelay on your roster is all thatʼs necessary to get Googleʼs xmpp server to send messages to axrelay.)

Send a "/whoami" message to axrelay@xmpp.getlantern.org. You should get back LanternFriend's anonymous jid:

![screenshot](screenshots/whoami_LanternFriend.png)

(You may notice that if you try to send subsequent "/whoami" messages, Google's xmpp server will not deliver them. Logging out and back in can fix this, though you'll get a new resource in your jid and so axrelay will give you a new anonymized jid.)

Log in to Messages.app with a different gmail.com xmpp account, e.g. requiredfield256@gmail.com. Hit ⌘N to compose a new message, type axrelay@xmpp.getlantern.org in the "To:" field and press enter. Hover over it so it becomes a blue address widget, click the down arrow inside it to expand its popup menu, and select "Add Buddy":

![screenshot](screenshots/add_buddy.png)

Accept the defaults in the resulting dialog and now you should see axrelay in your roster:

![screenshot](screenshots/messages_roster.png)

(Again don't worry that axrelay does not accept the presence subscription request and therefore shows up as "Waiting for authorization".)

Send axrelay a "/whoami" message. You should get back requiredfield256's anonymous jid:

![screenshot](screenshots/whoami_requiredfield256.png)

Now send a message from LanternFriend to requiredfield256's anonymous jid, **with the resource "/a" appended to it so Google will actually deliver it**:

![screenshot](screenshots/to_anon_jid_with_resource.png)

![screenshot](screenshots/testing_relay_gmail_jid.png)

requiredfield256 should receive a corresponding message coming from LanternFriend's anonymized jid:

![screenshot](screenshots/testing_relay_gmail_jid_received.png)

However, the anonymized "from" address in this message is just a bare jid,
so if requiredfield256 tries to reply, Google will not deliver the message due to the missing resource.

But sending a new message to this address with the "/a" resource appended works:

![screenshot](screenshots/testing_relay_back.png)

**RESULT: Pretty much success.
TODO: Change axrelay to include the "/a" resource in the "from" field when relaying messages so clients don't have to append it manually?**

### Test axrelay with Google Apps domains xmpp accounts

If you try to send a message to axrelay@xmpp.getlantern.org from a Google Apps for Domains xmpp account,
Google's xmpp server will refuse to send it, even if you've added axrelay@xmpp.getlantern.org to your roster,
and you'll get an error that the message could not be sent.
This is apparently due to the missing resource,
i.e. Google Apps for domains xmpp servers are apparently more strict
and always require a resource in the jid when sending to an address whose presence you're not subscribed to:
If you append some resource like "/foo" to the jid, Google will send the message.
However, apparently, since axrelay runs as a component, it doesn't actually have a resource,
and so will not receive any message addressed to it with a resource.

**RESULT: Fail.**

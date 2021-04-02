<table>
        <tr>
            <td><img width="20" src="https://cdnjs.cloudflare.com/ajax/libs/octicons/8.5.0/svg/archive.svg" alt="archived" /></td>
            <td><strong>Archived Repository</strong><br />
            This code is no longer maintained. Feel free to fork it, but use it at your own risks.
        </td>
        </tr>
</table>

# Ninja Block's Boss Dectector

This repository aims to reflect code published in an article on the [marmelab's blog](http://marmelab.overblog.com/using-connected-objects-to-keep-your-job).

## Installation

```sh
npm install
```

Edit the `config/default.yml` with a [Skybiometry](http://www.skybiometry.com/) key

Change hotnames in `clients.js`  with the hostname where your `server.js` is running.
Update `server.js` with the Ninja block's hooks that you have created.

### Dependencies

The client uses [imagesnap](http://iharder.sourceforge.net/current/macosx/imagesnap/) to take snapshot of an invader.


## Usage

Running the server :
```sh
node server.js
```

The client :
```sh
node client.js
```

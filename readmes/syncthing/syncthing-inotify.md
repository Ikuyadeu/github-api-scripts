:exclamation:Deprecation:exclamation:
==========

As of version v0.14.40, the functionality of syncthing-inotify is integrated in Syncthing and can be enabled in the advanced configuration menu for individual folders. We expect to expose it in the folder configuration UI in the near future.

Syncthing-inotify still works and is expected to keep working, but maintaining efforts will be focussed on the integrated functionality. Therefore it is recommended to switch soon(ish). You are very welcome to switch right now: It is already running on many devices, yet it is still fresh - (minor) bugs are to be expected.

### Old readme

#### What is this?
Syncthing ([core](https://github.com/syncthing/syncthing)) uses a rescan interval to detect changes in folders. This application (syncthing-inotify) uses OS primitives to detect changes as soon as they happen. Therefore, if you save a file, syncthing-inotify will know about it and pass this information to Syncthing such that near real-time synchronisation can be achieved.

#### Where do I get it?
Syncthing-inotify binaries are released on [github](https://github.com/syncthing/syncthing-inotify/releases/latest)

#### How do I run it?
Syncthing-inotify will automatically read the Syncthing config if it is found in the standard path.
  * Run and hide on unix in a screen
```
screen -S inotify -dm ./syncthing-inotify
```
  * Run and hide on windows in .vbs script
```
CreateObject("Wscript.Shell").Run "syncthing-inotify.exe", 0, True
```
  * Run and hide on windows using API key in .vbs script
```
CreateObject("Wscript.Shell").Run "syncthing-inotify.exe -api=""...""", 0, True
```
  * Install as a service, see the etc/ folder

#### I'm confused
  * Try [Syncthing-GTK](https://github.com/syncthing/syncthing-gtk), [QSyncthingTray](https://github.com/sieren/QSyncthingTray/releases) (both cross-platform) or [SyncTrayzor](https://github.com/canton7/SyncTrayzor/releases) (Windows only).
  * Read the commandline options: ```./syncthing-inotify -help```. Settings, such as an API key, need to be manually provided if you use a custom home for Syncthing.

#### Building syncthing-inotify
```
# To clone
mkdir -p src/github.com/syncthing
git clone https://github.com/syncthing/syncthing-inotify.git src/github.com/syncthing/syncthing-inotify
# Following commands are needed every time you want to build (unless you use Golang's specific folder structure: C:\src  or ~/src/)
export GOPATH=$(pwd)
cd src/github.com/syncthing/syncthing-inotify
go get
go build
# To tag the build with a version number, use
go build -ldflags "-w -X main.Version `git describe --abbrev=0 --tags`"
# See cross-compile.rb for further compilation details
# - Please prefix the build with GO386=387 when building for i386
# - Please prefix the build with GOARM=5 when building for arm
# - Depends on darwin_amd64/notify.a for OSX builds
```


#### Troubleshooting for folders with many files on Linux
* Linux limits the amount of inotify watchers (typically to [8192](http://stackoverflow.com/a/20355253)). Therefore, if you wish to sync many files and folders, you'll need to increase the upper limit:

  Permanently fix `Too many open files` on most Linux distributions: ```echo "fs.inotify.max_user_watches=204800" | sudo tee -a /etc/sysctl.conf```
  
  On Arch Linux, instead run: ```echo "fs.inotify.max_user_watches=204800" | sudo tee -a /etc/sysctl.d/90-override.conf``` (see [this forum post](https://bbs.archlinux.org/viewtopic.php?id=193020))

  Fix `Too many open files` for Linux until next reboot: ```sudo sh -c 'echo 204800 > /proc/sys/fs/inotify/max_user_watches'``` (should be applied before launching syncthing-inotify)

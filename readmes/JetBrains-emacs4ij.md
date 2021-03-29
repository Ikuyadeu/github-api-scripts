[![obsolete project](http://jb.gg/badges/obsolete.svg)](https://confluence.jetbrains.com/display/ALL/JetBrains+on+GitHub)

This is a plugin for GNU Emacs support in IntelliJ IDEA. 

To use this plugin you have install GNU Emacs and to download full Emacs sources (http://ftp.gnu.org/pub/gnu/emacs/). Please, use Emacs 23.4.
When started IDEA with this plugin installed, to activate the Emacs functionality you have to specify Emacs location in a special menu at IDEA's main toolbar. For screenshot, see doc/settings.png. 
When you do everything ok, it will take about 7 minutes to index the sources. The plugin is ready to work.

At the moment the plugin provides the following features:
- Emacs Lisp code evaluation from editor (eval-last-sexp, with C-x C-e) 
- Emacs keybindings, ability to assign Emacs commands to keyboard shortcuts with Emacs commands
- work with IDEA editor's tabs as with Emacs buffers 
- text editing commands
- help 
- minibuffer
- interactive commands
Text highlighting is not supported yet.

To get more information about this plugin, you can read doc/paper.pdf.

url-encode-gedit-plugin
=======================

Gedit Plugin to URL encode/decode selected text.


Installaion
-----------

Copy urlencode.plugin and urlencode.py to ~/.local/share/gedit/plugins/.
Open (or re-open) Gedit.
From Gedit's Edit menu, select "Preferences".
Under the "Plugins" tab, find the "URL En/De-coder" and select it.

Usage
-----

1. Highlight the text you would like to URL encode or decode.
2. To URL encode, go to "Edit" > "Url Characters" > "Url encode" or type Ctrl + Alt + u.
3. To URL decode, go to "Edit" > "Url Characters" > "Url decode" or type Ctrl + Alt + v.

Credit Where It's Due
---------------------

* Micah Carrick's invaluable tutorial (http://www.micahcarrick.com/writing-plugins-for-gedit-3-in-python.html)
* Marco Cripa's Convert Special gedit plugin. (http://krypt77.altervista.org/download/gedit/Convert_special_3_0.zip) Structure below apapted from that plugin.

Still to Come
-------------

* Keep replaced text selected.

# -*- coding: utf-8 -*-
# sudo systemctl restart xkeysnail

import re
from xkeysnail.transform import *
 
terminals = ["konsole","yakuake","terminator","sakura","tilda","xterm","eterm","kitty","alacritty"]
terminals = [term.casefold() for term in terminals]
termStr = "|".join(str(x) for x in terminals)

# define timeout for multipurpose_modmap
define_timeout(0.2)

define_modmap({
    Key.LEFT_ALT: Key.RIGHT_CTRL, # Paste/Ctrl
    Key.RIGHT_ALT: Key.RIGHT_META, 	# Hold RAlt and Shift for screen draw :plasmascreendraw:
    Key.BACK: Key.PAGE_UP,  # Standardize x200 with x220 keyboard
    Key.FORWARD: Key.PAGE_DOWN, # Standardize x200 with x220 keyboard

})

define_multipurpose_modmap({

  #Computer QWERTY Keyboard Key Frequency: 
    # Space e t Shift a o i n s r h Del l d c u Enter 
    # m f p g w y b , . v k ( ) _ ; ” = ‘ – Tab x / 0 $ *
    # 1 j : { } > q [ ] 2 z ! < ? 3 + 5 \ 4 # @ | 6 & 9 8 7 % ^ ~ `

  # alt tab and ctrl-f13 can flip windows
    Key.F1: [Key.F1, Key.RIGHT_META],
    Key.F2: [Key.F2, Key.RIGHT_META],
    Key.F3: [Key.F3, Key.RIGHT_META],
    Key.F4: [Key.F4, Key.RIGHT_META],
    Key.F5: [Key.F5, Key.RIGHT_META], 
    Key.F6: [Key.F6, Key.RIGHT_META],
    Key.F7: [Key.F7, Key.RIGHT_META],
    Key.F8: [Key.F8, Key.RIGHT_META],
    Key.F9: [Key.F9, Key.RIGHT_META],
    Key.F10: [Key.F10, Key.RIGHT_META],
    Key.F11: [Key.F11, Key.RIGHT_META],
    Key.F12: [Key.F12, Key.RIGHT_META],

  # Free: SCALE DASHBOARD CALC PROG2-4 F13-18 F21-23 NUMLOCKl
  # KP1-0 KPDOT KPCOMMA as long as you bind them, FILE XFER
  # fn, phone, finance, shop, ~, :-L, q-W, 
  # meta-A, ctrl-space, meta-K could be leader keys

  # Key.ESC: [Key.ESC, RIGHT_META], # I dont want to mess with thebehavior of ESC for now
    Key.GRAVE: [Key.DASHBOARD, Key.RIGHT_CTRL], # Launch(D)
    Key.TAB: [Key.TAB, Key.RIGHT_ALT],
    Key.CAPSLOCK: [Key.SCALE, Key.RIGHT_META], # Launch(C)
    Key.LEFT_SHIFT: [Key.CALC, Key.LEFT_SHIFT], #Launch(1)

    Key.LEFT_CTRL: [Key.SPORT, Key.LEFT_ALT],
    Key.LEFT_META: [Key.CHAT, Key.LEFT_META],

    
   # Key.RIGHT_ALT: [Key.FINANCE, Key.RIGHT_META], #being used for #plasma screen draw
   # Key.RIGHT_CTRL: [Key.SHOP, Key.RIGHT_CTRL],  #default ctrl behvahior for multi select and others. 

  # Less-used keys to remap
    #Key.LEFT_BRACE: [Key.LEFT_BRACE, Key.LEFT_ALT],   # PROG3=Launch(5)
    #Key.RIGHT_BRACE: [Key.RIGHT_BRACE, Key.LEFT_META], # PROG4=Launch(6)
    Key.BACKSLASH: [Key.F14, Key.RIGHT_META],    # F14=Launch(7)/Ctrl
    Key.SEMICOLON: [Key.F15, Key.RIGHT_META],    # F15=Launch(8)

  #Key.APOSTROPHE: [Key.APOSTROPHE, Key.RIGHT_CTRL], # '
  #Key.PAGE_UP: [Key.PAGE_UP, Key.RIGHT_META],
  #Key.PAGE_DOWN: [Key.PAGE_DOWN, Key.RIGHT_CTRL],


})

define_keymap(None,{

    K("Chat"): K("RC-v"),   # [Paste (Cmd)
    K("CALC"): K("RC-c"),    # [Copy (Shift)

    #K("VOLUMEDOWN"): K("BACK"),
    #K("VOLUMEUP"): K("FORWARD"),

  # Pass though remapped keys
    K("Shift-DASHBOARD"): K("Shift-GRAVE"), # ~ 
    K("RSuper-DASHBOARD"): K("GRAVE"), # ~ 

    #keys are default 
    #K("Shift-PROG3"): K("Shift-LEFT_BRACE"),
    #K("RSuper-PROG3"): K("LEFT_BRACE"),
    #K("RC-PROG3"): K("C-LEFT_BRACE"),

    #keys are default
    #K("Shift-PROG4"): K("Shift-RIGHT_BRACE"),
    #K("RSuper-PROG4"): K("RIGHT_BRACE"),
    #K("RC-PROG4"): K("C-RIGHT_BRACE"),

    K("Shift-F14"): K("Shift-BACKSLASH"),   
    K("RSuper-F14"): K("BACKSLASH"),

    K("Shift-F15"): K("Shift-SEMICOLON"), # : 
    K("RSuper-F15"): K("SEMICOLON"),      # ;

})

define_keymap(re.compile("anki", re.IGNORECASE),{

	K("F2") : K("RC-d"),   # change deck
  #K("RC-C") : K("Alt-Shift-o"),   # Overlapping CLose
  #K("RC-V") : K("C-Shift-o"),     # Image Occlusion

	# reserved keys free to remap in anki
	# f1(suspend) f2(change deck), f3(focus tag), f10, f11.
  # ct-wert ct-sdg ct-xcvb ct-~12345 ct-f12345
}, "Anki")

# Keybindings for Firefox/Chrome
define_keymap(re.compile("firefox|navigator|FoxitReader|Foxit Reader|DATFox|firefox1|firefox2|firefox3", re.IGNORECASE),{

  K("F1"): K("PAGE_UP"),     # 
  K("F2"): K("PAGE_DOWN"),     #

  K("RSuper-KEY_3"): K("RC-PAGE_UP"),     # tab left
  K("RSuper-KEY_4"): K("RC-PAGE_DOWN"),     # tab right
	#K("RC-E"): K("RC-k"),           # search web
}, "Firefox, Foxit"),

define_keymap(re.compile("Dolphin", re.IGNORECASE),{

  K("RSuper-KEY_3"): K("RC-PAGE_UP"),     # tab left
  K("RSuper-KEY_4"): K("RC-PAGE_DOWN"),     # tab right
  #K("RC-E"): K("RC-k"),           # search web
}, "Dolphin"),

define_keymap(re.compile(termStr, re.IGNORECASE),{

    K("RC-V"): K("C-Shift-V"),
    K("RC-MINUS"): K("C-Shift-MINUS"),
    K("RC-EQUAL"): K("C-Shift-EQUAL"),
    K("RC-BACKSPACE"): K("C-Shift-BACKSPACE"),
    K("RC-Q"): K("C-Shift-Q"),
    K("RC-W"): K("C-Shift-W"),
    K("RC-E"): K("C-Shift-E"),
    K("RC-R"): K("C-Shift-R"),
    K("RC-T"): K("C-Shift-t"),
    K("RC-Y"): K("C-Shift-Y"),
    K("RC-U"): K("C-Shift-U"),
    K("RC-I"): K("C-Shift-I"),
    K("RC-O"): K("C-Shift-O"),
    K("RC-P"): K("C-Shift-P"),
    K("RC-LEFT_BRACE"): K("C-Shift-LEFT_BRACE"),
    K("RC-RIGHT_BRACE"): K("C-Shift-RIGHT_BRACE"),
    K("RC-A"): K("C-Shift-A"),
    K("RC-S"): K("C-Shift-S"),
    K("RC-D"): K("C-Shift-D"),
    K("RC-F"): K("C-Shift-F"),
    K("RC-G"): K("C-Shift-G"),
    K("RC-H"): K("C-Shift-H"),
    K("RC-J"): K("C-Shift-J"),
    K("RC-K"): K("C-Shift-K"),
    K("RC-L"): K("C-Shift-L"),
    K("RC-SEMICOLON"): K("C-Shift-SEMICOLON"),
    K("RC-APOSTROPHE"): K("C-Shift-APOSTROPHE"),
    K("RC-GRAVE"): K("C-Shift-GRAVE"),
    K("RC-BACKSLASH"): K("C-Shift-BACKSLASH"),
    K("RC-Z"): K("C-Shift-Z"),
    K("RC-X"): K("C-Shift-X"),
    K("RC-C"): K("C-Shift-C"),
    K("RC-V"): K("C-Shift-V"),
    K("RC-B"): K("C-Shift-B"),
    K("RC-N"): K("C-Shift-N"),
    K("RC-M"): K("C-Shift-M"),
    K("RC-COMMA"): K("C-Shift-COMMA"),
    K("RC-DOT"): K("C-Shift-DOT"),
    K("RC-SLASH"): K("C-Shift-SLASH"),
    K("RC-KPASTERISK"): K("C-Shift-KPASTERISK"),

}, "terminals")

# Kern Tool
> *WARNING! Any kerning changes are applied to the font at once, so make sure you have a backup copy of the font before testing them.*

**KernObserver** (KO) and **KernTool** (KT) are two extensions for working with kerning in **Robofont**. **KO** and **KT** interact with each other. **KO** allows viewing the existing kerning, and **KT** allows editing it. 
*These extensions are still under development, and will get updates and new options in the future*.
*Several new extensions are to be added soon, which will allow changing the contents of the kerning groups, as well as performing various kerning transformations*.




## Kern Observer

The main function of this extension is to show the existing kerning in a font.

There are 3 ways to view the kerning:

1. The fastest one is to select several glyphs in the open font, switch to **KO** and press **Refresh**. **KO** will form pairs and show them.

2. Open **KO** menu and click **Make Pairs**. You will then see two lists of glyphs in the open window. These lists can be filled by selecting the necessary glyphs in the font window and by pressing the necessary key. If you need an additional sequence of glyphs to be displayed to the left or to the right of the pair, you can enter this sequence into the corresponding fields. Once you press Apply, **KO** will form pairs. *Other options will be added to this way of viewing the kerning, for example, presets, patterns, loading from a file and saving into one, etc*.

3. You can also open any text file in **KO** and view the kerning in the text. The file must be in text format (.txt), UTF-8 encoding, and/or contain the glyph names after ‘/‘ (slash). *For example, /Agrave /afii10028 /g.alt*.

In the first two ways **KO** displays kerning pairs as sequences of ‘left glyph + all the right glyphs’ blocks. Each block is divided into lines of pairs, the length of which can be limited with a designated slider (line lenght slider). To keep the pairs from breaking in the end of the line, the left glyph is displayed twice: in the end of the line, and in the beginning of the new one.

To the left of the **KO** window there’s an indicator of the current block and the line.

You can switch from one line/block to another either with your mouse or arrow keys.

**KO** displays the kerning as colored bars.

The **lightning icon** under a bar means that this pair is an **exception** from the group kerning.

**Show Values** menu allows you to either display or hide the numerical values of the kerning.

When **Show Touches** mode is active, it highlights the pairs red if the glyphs touch contours.

When **Light Mode** is on, the entire interface is hidden, and the text alone is displayed.

Glyph size can be changed with **+**/**–** keys, and it doesn’t affect the line length.
 
To change the kerning of the pairs displayed in **KO** you should run **KernTool** extension, and double-click the line of pairs. It will copy the entire line of pairs into **KT**. To copy a full block of pairs into **KT**, press *Alt* and double-click the needed block.


## Kern Tool

This extension is meant for editing the kerning.

Kerning pairs can be entered in the upper text field, or imported from **KernObserver**.

If you got your kerning pairs from **KO**, pressing Up and Down keys will import the next or the previous line of pairs. If you hold *Alt* while doing this, you will import either next or the previous block of pairs.

The current pair is highlighted with a cursor in the middle, and also with a blue-green cursor on the metric scale in the bottom part of the window.

The left part of the pair is highlighted blue; the right one is highlighted green.

The current pair can be selected either with your mouse or with **TAB** key. 

```
TAB = next pair
Alt+TAB = previous pair
```

The kerning value is changed by pressing **Left** and **Right** arrows.

```
Left = -10; Shift+Left = -5; Alt+Left = -1
Right = +10; Shift+Right = +5; Alt+Right = +1
```

To multiply kerning press **0 .. 9** keys after **Left/Right** Arrow. For example, pressing **Left** Arrow sets your kerning value to **-10**, and if you press **6** after that you change kerning to **-60** (-10*6=-60). If you press **0** you multiply kerning by **10**.


In the bottom of the window there’s a metric scale, where every glyph is marked with a square of a certain color:
- green, if the glyph is in the right group;
- blue, if the glyph is in the left group;
- red, if the glyph is in a group, but is also an exception.

If a glyph has no square, it means it is not in a group.

Glyph size can be changed with **+**/**–** keys.

To keep the pairs from breaking in the end of the line, the left glyph is displayed twice: in the end of the line, and in the beginning of the new one.

To delete the current pair press *Backspace*. Keep in mind that if you’re deleting an exception pair, the exception will be deleted first, and the group kerning will be applied to the pair. Once you press *Backspace* again, the applied group kerning will also be deleted.

To create an **exception** press **E**. If the current pair has group kerning, several exceptions will be suggested.

In the bottom part of the screen there are two scales showing kerning between the glyph groups of the current pair. If there are any exceptions present, they’re marked with red lightnings. *A click on any scale of the groups sends all its pairs into the upper editing window, which might be useful if you discover that an exception has to be made in a certain group*.

## Interaction of Kern Observer and Kern Tool

**KO** and **KT** can exchange pairs and kerning data. By default they both work with the current font. If you need to work with kerning of several fonts at once, or view different pairs within a single font, you can run several **KOs** and **KTs**. However, this option is only in a test mode so far, and it is not recommended to run more than one **KT**. You can select a font to view in each **KO** via *Select Font* menu. **KT** will work with the **KO** it imported the set of pairs from.

## Kern Preferences
Both **KO** and **KT** accept group names in **MetricsMachine** format as default (group name looks like **@MMK_L_groupname**/**@MMK_R_groupname**). But **Kern Preferences** allows default format changing. For example in group name like **@KERN_LEFT_groupname** the meaning for **Group Name ID** is **@KERN** and meanings for **Left ID**/**Right ID** are **_LEFT_**/**_RIGHT_**. 
All these meanings must be *unique*. Restart **KO** and **KT** to apply all your changes.





# **********************************************************
# *                                                        *
# *                    Y  A  S  A  R  A                    *
# *                                                        *
# * Yet Another Scientific Artificial Reality Application  *
# *                                                        *
# **********************************************************
# *         Watching Nature@Work - www.yasara.org          *
# **********************************************************
# *            (C) 1993 - 2015 by Elmar Krieger            *
# **********************************************************
# *    yasara.py - A support module for Python plugins     *
# *   License for this Python module: GPL (www.gnu.org)    *
# **********************************************************

"""
<H1> Plugins - Extend YASARA with your own functions

<H2> Plugins allow you to add your own menu options

A YASARA plugin is a Python script or {Yanaconda macro<Macros2>} that adds menu options and
windows to the YASARA user interface and gets executed when you activate the respective
option. Plugins are the ideal solution to add your own favorite functions to YASARA
without having to play around with compilation, C and Assembler code.

All plugins are collected in the yasara/plg subdirectory, for latest developments visit
the plugin repository at <www.yasara.org/plugins>. In MacOS, you need to enter the context
menu of the YASARA application in Finder and choose 'show package contents' to see the plugin folder.

<H2> Plugins can be written in Yanaconda or Python

Even though YASARA has its own {built-in macro language<Macros2>}, there are some applications
where {Yanaconda macros<Macros2>} cannot help, like web-services and database-interfaces.
Python is a well established, user friendly scripting language with excellent support
for the above topics and was therefore the first choice.

In either case, YASARA changes the `current working directory` to the location of the
plugin before running it, i.e. yasara/plg in Linux and Windows, or YASARA.app/yasara/plg
in MacOS (you need to enter the context menu of the YASARA application in Finder and choose
'show package contents' to see the plugin folder).

<H2> Python can be downloaded from www.python.org

If you are a Linux or MacOS user, Python is already present. If you are running Windows,
it depends on your installation. Try to click Help > Install program > Python.
If this option is not available, Python is already installed.

If you are new to Python, you can {find a tutorial here<http://docs.python.org/tut/tut.html>}.

<H2> Plugins must stick to format conventions

All plugins must be stored in YASARA's 'yasara/plg' subdirectory (in MacOS, this folder
can be found at YASARA.app/yasara/plg). Look at some of the files
present there and pick the one closest to your needs as a programming scaffold.

<H3> The header identifies a plugin

The first line of a YASARA Python plugin must always read '# YASARA PLUGIN'.
Adapt the remaining fields to describe your plugin. This information will be
used if you decide to add it to the YASARA plugin
repository at <www.yasara.org/plugins> in return for YASARA thank-you credits.
Go to <www.yasara.org/contribute> to submit your plugin.

<P>
# YASARA PLUGIN
# TOPIC:       Database interfaces
# TITLE:       Retrieve a PDB file by FTP
# AUTHOR:      Elmar Krieger
# LICENSE:     GPL (www.gnu.org)
# DESCRIPTION: This plugin asks for a PDB ID and retrieves the file by FTP
#
<P>

<H3> The menu structure is enclosed in a triple-quote comment

After the header, the plugin specifies where to add which entries to YASARA's user
interface to make selections and run the plugin. These definitions will be read when
YASARA registers the plugin during startup and must be enclosed in triple-quotes (""\"),
so that Python ignores them. If you make changes here, you must restart YASARA.
The indentation has to be a multiple of two spaces, Tabs are not allowed.

Here is an example:

<P>
""\"
MainMenu: File
  PullDownMenu: Load
    SubMenu after PDB file from local PDB: PDB file from I_n_ternet
      TextInputWindow: Download PDB file from the web (IconDOWNLOAD)
        Text: Please input the four letter PDB ID code
        Text: _P_DB ID
      Request: DownloadPDB
""\"
<P>

The example above tells YASARA to:
1) Enter the main menu, search for entry 'File' (add it if not found).
*) Open a pull down menu, search for entry 'Load' (add it if not found).
*) Open a submenu (attached to the pull down menu), search for entry
   'PDB file from local PDB', and add the new entry
   'PDB file from Internet' immediately afterwards, with the 'n' underlined.
*) Open a text input window with the header 'Download PDB file from the web', display a Download icon.
*) Within the text input window, print the text 'Please input the four letter PDB ID code'.
*) On top of the first (and only) text input box, print the text 'PDB ID' with the 'P' underlined.
*) Run the plugin with the request 'DownloadPDB'

The triple-quote comment may contain the following keywords to identify certain
menu and window types:

<H4> MainMenu - Add an option to the top menu line

The indentation level for this keyword must be 0. You can use 'after' and 'before'
to specify the location of the new option. Underscores surround underlined characters.

Examples:
<P>
MainMenu: File
MainMenu after Effects: A_n_imations
MainMenu before Analyze: _T_ools
<P>

<H4> AtomContextMenu - Add an option to the atom context menu

The atom context menu appears when you click on a marked atom with the right mouse button,
the indentation level for this keyword must be 0. You can use 'after' and 'before'
as known from <MainMenu>.

The descriptor of the clicked atom can be accessed as {yasara.selection[0].atom[0] from Python<Ppcaanopv>}
and as {selection(1) from Yanaconda<Ypcaanopv>}.

Example:
<P>
AtomContextMenu: _Q_uery mutation effects
<P>

<H4> ResidueContextMenu - Add an option to the residue context menu

The residue context menu appears when you click on a residue in the sequence selector
with the right mouse button, the indentation level for this keyword must be 0.
You can use 'after' and 'before' as known from <MainMenu>.

The descriptor of the clicked residue can be accessed as {yasara.selection[0].residue[0] from Python<Ppcaanopv>}
and as {selection(1) from Yanaconda<Ypcaanopv>}.

Example:
<P>
ResidueContextMenu before Label: _Q_uery mutation effects
<P>

<H4> SelectionContextMenu - Add an option to the selection context menu

The selection context menu appears when you first select atoms using the interactive
{box<SelectBox>}, {lasso<SelectArea>} or {sphere selection tools<SelectSphere>}
(or directly with the <Select> command), and then right-click on one of the selected
atoms. The indentation level for this keyword must be 0.

The descriptors of the selected atoms can be accessed as {yasara.selection[0].atom[i] from Python<Ppcaanopv>}
and as {selection(1) from Yanaconda<Ypcaanopv>} (which simply contains {the string 'selected'<aisawvp>}).

Example:
<P>
SelectionContextMenu after Mass: _B_-factor
<P>

<H4> HUD*ContextMenu - Add an option to one of the HUD context menus

The {head-up-display (HUD) in the top right corner<HUD>} allows to {browse the soup<ShowHUD>}
and offers context menus for atoms, residues, molecules and objects. You can add
options to these menus using the following keywords (whose indentation level must be 0):

<T>
`Keyword`              | `Python access to selection`
HUDAtomContextMenu     | yasara.selection[0].residue[0]
HUDResidueContextMenu  | yasara.selection[0].residue[0]
HUDMoleculeContextMenu | yasara.selection[0].molecule[0]
HUDObjectContextMenu   | yasara.selection[0].object[0]
<T>

In Yanaconda, the ID of the selected unit can simply be found in variable 'selection(1)'.

Example:
<P>
HUDObjectContextMenu: _S_ample
<P>

<H4> PullDownMenu - Add an option to a pull-down menu

This keyword must only be used after <MainMenu> with an indentation level of 1.

Example:
<P>
MainMenu: File
  PullDownMenu after Load: _G_et by FTP
<P>

<H4> SubMenu - Add an option to a submenu

Submenus are little windows appearing on the side of pull-down menus or context
menus. This keyword must therefore only be used after <PullDownMenu>, <AtomContextMenu> or <ResidueContextMenu>,
with an indentation level of 1 or 2.

Example:
<P>
MainMenu: View
  PullDownMenu: Color
    SubMenu: by properties
<P>

<H4> ObjectSelectionWindow - Add a window allowing to select objects

This keyword adds a standard object selection window, the selections are passed
to the Python plugin via <object descriptors>. The specified text appears as the window
header.

In Python, the jth {object descriptor<Odiso>} in the ith selection window can be accessed as
{yasara.selection[i].object[j]<Ppcaanopv>}, while Yanaconda stores a simple
object selection string in {selection(i)<Ypcaanopv>}, which can be passed to
YASARA commands directly, e.g. to <ListObj> to obtain an object list.
Note that counting for 'i' starts at 0 in Python and 1 in Yanaconda.

Example:
<P>
MainMenu: Analyze
  PullDownMenu: _M_CSIS mutations
    ObjectSelectionWindow: Select objects to map mutations stored in the MCSIS
    Request: MapMutations
<P>

<H4> MoleculeSelectionWindow - Add a window allowing to select molecules

This keyword adds a standard molecule selection window, the selections are passed
to the plugin via <molecule descriptors>. See <ObjectSelectionWindow> above for
an example.

In Python, the jth {molecule descriptor<Mdism>} in the ith selection window can be accessed as
{yasara.selection[i].molecule[j]<Ppcaanopv>}, while Yanaconda stores a simple
molecule selection string in {selection(i)<Ypcaanopv>}, which can be passed to
YASARA commands directly, e.g. to <ListMol> to obtain a molecule list.
Note that counting for 'i' starts at 0 in Python and 1 in Yanaconda.

Example:
<P>
MainMenu: Analyze
  PullDownMenu: _C_ompare amino acid sequence of two molecules
    MoleculeSelectionWindow: Select first molecule to compare sequence
    MoleculeSelectionWindow: Select second molecule to compare sequence
    Request: CompareSequence
<P>

<H4> ResidueSelectionWindow - Add a window allowing to select residues

Not surprisingly, this keyword adds a residue selection window, the selections are passed
to the plugin via <residue descriptors>. See <ObjectSelectionWindow> above for
an example.

In Python, the jth {residue descriptor<Rdisr>} in the ith selection window can be accessed as
{yasara.selection[i].residue[j]<Ppcaanopv>}, while Yanaconda stores a simple
residue selection string in {selection(i)<Ypcaanopv>}, which can be passed to
YASARA commands directly, e.g. to <ListRes> to obtain a residue list.
Note that counting for 'i' starts at 0 in Python and 1 in Yanaconda.

Example:
<P>
MainMenu: Analyze
  PullDownMenu: _P_roscan
    ResidueSelectionWindow: Select residues for ProScan
    Request: Proscan
<P>

<H4> AtomSelectionWindow - Add a window allowing to select atoms

The last keyword of this type adds an atom selection window, the selections are passed
to the plugin via <atom descriptors>. See <ObjectSelectionWindow> above for
an example.

In Python, the jth {atom descriptor<Adisa>} in the ith selection window can be accessed as
{yasara.selection[i].atom[j]<Ppcaanopv>}, while Yanaconda stores a simple
atom selection string in {selection(i)<Ypcaanopv>}, which can be passed to
YASARA commands directly, e.g. to <ListAtom> to obtain an atom list.
Note that counting for 'i' starts at 0 in Python and 1 in Yanaconda.

Example:
<P>
MainMenu: View
  PullDownMenu: Color
    SubMenu: by force
      AtomSelectionWindow: Select atoms to color by force
      Request: ColorByForce
<P>

<H4> TextInputWindow - Add a window allowing to input one to four text strings

This keyword adds a window with one to four text input boxes. In addition to the
window header, you must specify a general explanation for the user and then
one header for each text input box.

The content of the jth text input box in the ith
selection window can be accessed as {yasara.selection[i].text[j] from Python<Ppcaanopv>}
and as {selection(i)text(j) from Yanaconda<Ypcaanopv>}.
Note that counting for 'i' and 'j' starts at 0 in Python and 1 in Yanaconda.

Example for a window with two text input boxes:
<P>
MainMenu: Options
  PullDownMenu: _R_eport error
    TextInputWindow: Send an error report by e-mail
      Text: Please give a brief description of the problem:
      Text: _D_escription part 1 (header for the first input box)
      Text: _D_escription part 2 (header for the second input box), Default text
<P>

Note in the last line that a default text can be provided, separated with a comma ','.
If the default is not always the same (e.g. a username), you can use 'TextFile:' instead
of 'Text:' to {read the data from a file as described here<ListWindow>}. This file must then be
created {by the 'CheckIfDisabled' startup code<TlftrpdbPaY>}.

<H4> NumberInputWindow - Add a window allowing to input one to six numbers

This keyword adds a window with one to six number input boxes. In addition to the
window header, you must specify a general explanation text and then one descriptor
for each number input box. A number descriptor contains four elements, separated by commas:
the title of the number box, the default value, the minimum allowed value and the maximum
allowed value. If the default value contains a dot '.', the field accepts floating point
numbers, otherwise just integers are allowed.

The content of the jth number input box in the ith
selection window can be accessed as {yasara.selection[i].number[j] from Python<Ppcaanopv>}
and as {selection(i)number(j) from Yanaconda<Ypcaanopv>}.
Note that counting for 'i' and 'j' starts at 0 in Python and 1 in Yanaconda.

Example for a window with one number input box:
<P>
MainMenu: Edit
  PullDownMenu after Build: Sample
    SubMenu: _O_bject
      ObjectSelectionWindow: Select protein to sample conformational space with CONCOORD
      NumberInputWindow: Select ensemble size
        Text: Number of structures in the CONCOORD ensemble:
        Number: _S_tructures,10,1,98
      Request: SampleObj
<P>

<H4> RadioButtonWindow - Add a window allowing to switch between two to five options

This keyword adds a window with two to five radio buttons, where exactly one
button can be selected. This allows to choose between up to five exclusive options,
you must specify a general explanation for the user and then
one additional text for every radio button.

The number of the selected radiobutton in the ith selection window can be accessed as
{yasara.selection[i].radiobutton from Python<Ppcaanopv>} and as
{selection(i)radiobutton from Yanaconda<Ypcaanopv>}.
Note that counting for 'i' starts at 0 in Python and 1 in Yanaconda,
while counting for 'radiobutton' always starts at 1.

Example for a window with two radiobuttons:
<P>
MainMenu: Options
  PullDownMenu: _R_eport error
    RadioButtonWindow: Concretize the error
      Text: Did the problem occur right now?
      Text: _Y_es, I did not exit YASARA since then.
      Text: _N_o, just before, I had to restart YASARA to get here.
<P>

<H4> CheckBoxWindow - Add a window allowing to toggle one to five options

This keyword adds a window with one to five check boxes, that can be activated
individually. This allows to toggle up to five independent options,
you must specify a general explanation for the user and then
one additional text for every check box.

The state of the jth check box in the ith selection window can be accessed as
{yasara.selection[i].checkbox[j] from Python<Ppcaanopv>} and as
{selection(i)checkbox(j) from Yanaconda<Ypcaanopv>}.
Note that counting for 'i' and 'j' starts at 0 in Python and 1 in Yanaconda,
the state is either 0 (not checked) or 1 (checked).

Example for a window with two check boxes:
<P>
MainMenu: NMR
  PullDownMenu: _L_ist restraints
    CheckBoxWindow: List distance and dihedral angle restraints
      Text: Select the type of restraints to list
      Text: Distance restraints
      Text: Dihedral restraints (Checked)
<P>

By default, all boxes are unchecked. To check a box, add the text '(Checked)' at the end
as in the example above.

<H4> ListWindow - Add a window allowing to select from a list

This keyword adds a window with a list of options. Set the 'MultipleSelections' flag
to 'Yes' if the user is allowed to select more than one list entry and to 'No' otherwise.
The first text is displayed above the list, the other texts are the actual list entries.

The total number of selected list entries can be accessed as
{yasara.selection[i].listentries from Python<Ppcaanopv>} and as
{selection(i)listentries from Yanaconda<Ypcaanopv>}.

The jth selected list entry in the ith selection window can be accessed as
{yasara.selection[i].list[j] from Python<Ppcaanopv>} and as
{selection(i)list(j) from Yanaconda<Ypcaanopv>}.
Note that counting for 'i' and 'j' starts at 0 in Python and 1 in Yanaconda.

Example:
<P>
MainMenu: Analyze
  PullDownMenu: _P_DBFinder2 properties
    ResidueSelectionWindow: Select residues to color by PDBFinder2 properties
    ListWindow: Select PDBFinder2 properties
      MultipleSelections: Yes
      Text: Select more than one list entry to color by the average value
      Text: Nalign - Number of HSSP alignments
      Text: Nindel - Number of insertions and deletions
      Text: Entropy - HSSP sequence entropy
    Request: ColorResidues
<P>

If the list is long and has dynamic content, you can also read it from disk using the
'TextFile' keyword:

<P>
ListWindow: Select PDBFinder2 properties
  MultipleSelections: Yes
  Text: Select more than one list entry to color by the average value
  TextFile: options.txt
<P>

In the above example, the file 'options.txt' is read from the yasara/plg subdirectory,
and each line becomes an entry in the list. (This approach works for all keywords,
just append 'File' to the keyword name).

<H4> FileSelectionWindow - Add a window allowing to select files

This keyword adds a window with a file browser. Set the 'MultipleSelections' flag
to 'Yes' if the user is allowed to select more than one list entry and to 'No' otherwise.
The Filename keyword specifies a wildcard with the initial path. Use forward slashes
also under Windows.

The total number of selected filenames can be accessed as
{yasara.selection[i].filenames from Python<Ppcaanopv>} and as
{selection(i)filenames from Yanaconda<Ypcaanopv>}.

The jth selected filename in the ith selection window can be accessed as
{yasara.selection[i].filename[j] from Python<Ppcaanopv>} and as
{selection(i)filename(j) from Yanaconda<Ypcaanopv>}.
Note that counting for 'i' and 'j' starts at 0 in Python and 1 in Yanaconda.

Example:
<P>
MainMenu: File
  PullDownMenu: Load
    SubMenu after PDB file: _N_MR ensemble
      FileSelectionWindow: Select a PDB file containing an NMR ensemble
        MultipleSelections: No
        Filename: pdb/*.pdb
      Request: LoadEnsemble
<P>

<H4> ColorSelectionWindow - Add a window allowing to choose a color

This keyword adds a window to select a color. The 'ColorType' parameter
decides if a rainbow color ('Bow', used to {color atoms<ColorAtom>}) or
an RGB/HTML color ('RGB', used to color other things) should be selected.
The 'ColorName' parameter sets a name for the color input box,
a default color must be provided too (separated with a comma).

The selected color can be accessed as
{yasara.selection[i].color from Python<Ppcaanopv>} and as
{selection(i)color from Yanaconda<Ypcaanopv>}.
Note that counting for 'i' and 'j' starts at 0 in Python and 1 in Yanaconda.

<P>
MainMenu: View
  PullDownMenu: Color
    SubMenu after Hydrogen bonds: Disulfide bonds
      ColorSelectionWindow: Please choose color for bridged cysteines
        ColorType: Bow
        ColorName: _C_ys color, Yellow
      Request: ColorCys
<P>

<H4> CustomWindow - Add a window with custom design

The previous examples were predefined windows, with widgets placed automatically
depending on the window type and the number of options required. It is also possible
to design windows freely, by placing the widgets individually. The code is almost
exactly the same as described for {the Custom window type of the ShowWin command<ShowWin>},
that's why only an example is provided here, please refer to <ShowWin> for a description
of the widgets:

<P>
MainMenu: Window
  PullDownMenu: Show custom window
    CustomWindow: This is a custom window
      Width: 600
      Height: 400
      Text:        X= 20,Y= 48,Text="A simple text at position 20/48, the top left corner"
      TextCen:     X=300,Y= 88,Text="A centered text"
      NumberInput: X= 20,Y= 88,Text="_F_loat",Default=5.0,Min=0,Max=10
      NumberInput: X=450,Y= 88,Text="_I_nteger",Default=25,Min=-100,Max=100
      TextInput:   X= 20,Y=158,Text="_E_nter any text",Width=380,Chars=100
      TextInput:   X=430,Y=158,Text="_P_assword",Width=150,Chars=10
      CheckBox:    X= 20,Y=228,Text="_T_ag this and/or..",Default=No
      CheckBox:    X= 20,Y=280,Text=".._t_his and/or..",Default=Yes
      CheckBox:    X= 20,Y=332,Text="..t_h_is one here.",Default=Yes
      RadioButtons:Options=3,Default=1
                   X=420,Y=228,Text="_S_elect this or.."
                   X=420,Y=268,Text="..this or.."
                   X=420,Y=308,Text="..this one here."
      List:        X=210,Y=238,Text="_C_hoose from a list:"
                   Width=190,Height=128,MultipleSelections=Yes
                   Options=6,  Text="Pick option 1"
                               Text="and/or option 2,"
                               Text="keep Ctrl pressed"
                               Text="to select more"
                               Text="than one option,"
                               Text="up to option 6 here"
      Button:      X=542,Y=348,Text="_O_ K"
    Request: PrintSelection
<P>

Here is the corresponding Python code to access the selections made:

<P>
print('The floating point number was %f'%yasara.selection[0].number[0])
print('The integer number was %d'%yasara.selection[0].number[1])
print('Username was %s, password was %s'%(yasara.selection[0].text[0],yasara.selection[0].text[1]))
for i in range(3):
  print('Checkbox %d state was %d'%(i+1,yasara.selection[0].checkbox[i]))
print('Radiobutton %d was selected'%yasara.selection[0].radiobutton)
print('These were the %d selected list entries:'%yasara.selection[0].listentries)
print(yasara.selection[0].list)
<P>

And here is the corresponding Yanaconda code to access the selections made:

<P>
print 'The floating point number was (0.000+selection(1)number(1))'
print 'The integer number was (selection(1)number(2))'
print 'Username was (selection(1)text(1)), password was (selection(1)text(2))'
for i=1 to 3
  print 'Checkbox (i) state was (selection(1)checkbox(i))'
print 'Radiobutton (selection(1)radiobutton) was selected'
print 'These were the (selection(1)listentries) selected list entries:'
print (selection(1)list)
<P>

To keep access to the input compatible with the other selection windows,
each custom window may currently contain only a single list, a single radio
button selection, and a single button (usually named 'OK'). This limitation
does not apply to the <ShowWin> command.

<H3> The layout for the remaining plugin differs between Python and Yanaconda

When using Yanaconda, the rest of the plugin is a straightforward macro.
The variable 'request' contains the specified request, e.g. 'DownloadPDB' and
can be used to execute different parts of the macro. Selections can currently
not be accessed.

When using Python, the first command must be

<P>
import yasara
<P>

Immediately afterwards, you can access the data passed to the plugin as well
as call YASARA functions. The predefined variables are listed below, the most
important one is yasara.request, a string indentifying the user's request,
as specified after 'Request:', e.g. 'DownloadPDB'.
When YASARA registers the plugins during startup, it also sends a 'CheckIfDisabled'
request, giving the plugin the possibility to exclude itself from registration.

The remaining plugin scaffold therefore looks like that:

<P>
if (yasara.request=="CheckIfDisabled"):
  # Assign a 1 to yasara.plugin.exitcode if this plugin cannot work and should
  # be disabled (data missing, wrong operating system etc.)
  if (....) yasara.plugin.exitcode=1

elif (yasara.request=="DownloadPDB"):
  # Do the work

# End the plugin, must be the last command
yasara.plugin.end()
<P>

Note that the 'CheckIfDisabled' costs time since Python has to be run, and therefore
slows down YASARA's start. It is therefore avoided if possible. If a plugin does not
work in all operating systems, this should be declared in the header instead, using the
'PLATFORMS:' field:

<P>
# YASARA PLUGIN
# TOPIC:       Molecular Modeling
# TITLE:       Align3D
# AUTHOR:      Mikael Roche & Emmanuel Bettler
# LICENSE:     GPL
# DESCRIPTION: This plugin performs a structural alignment [...]
# PLATFORMS:   Linux,MacOS
<P>

Also note that you cannot run YASARA commands when handling the 'CheckIfDisabled' request,
since this happens during startup, before the user interface is created.

<H3> Plugins can be rerun quickly by pressing Alt or Tab

Many YASARA commands can be repeated by {holding down Alt or Tab and clicking on an atom<Editing>}.
This approach also works with plugins that are hooked into one of the context menus
like the <AtomContextMenu>.

YASARA will display a message at the bottom which is derived by splitting the 'Request'
keyword at capital letters.

<H2> Plugins can access most YASARA functions

For Yanaconda plugins this is trivial, as they are just macros. For Python plugins,
the YASARA functions are wrapped so that they can be accessed with a syntax that
matches Python's requirements.

Example: The YASARA command to choose a new 3D font..
<P>
Font Arial,Height=2,Spacing=1.5,Color=Yellow,Depth=5,DepthCol=Red
<P>
becomes
<P>
yasara.Font("Arial",height=2,spacing=1.5,color="Yellow",depth=5,depthcol="Red")
<P>

Note that argument names are lowercase in Python, because in contrast to Yanaconda,
Python's variable names are case-sensitive, and the capitalization is often ambiguous
and hard to remember, raising the error rate.

The documentation page of each YASARA command lists the prototype of the corresponding
Python function, e.g. the <Font> command (look at the 'Python:' row in the table at the
top of each page).

A few YASARA commands support more than one format with different argument types.
This is not possible in Python, the command thus has to be wrapped by different
Python functions. The names of these Python functions differ at the end, using
either an increasing number or the name of the first argument. More details
{are available here<YcwmfmtdPf>}.

You can of course also access the return values of YASARA commands:
<P>
# Load a PDB file and color it red
obj = yasara.LoadYOb("1crn")
yasara.ColorObj(obj,"Red")
<P>
More details about return values {can be found here<Pfrenasvoal>}.

It should also be noted that calling a YASARA command from Python is slower
than using a Python method, since it involves communication between Python
and YASARA. So calls to YASARA commands should be taken out of loops when
possible:
<P>
# Load a PDB file
yasara.LoadPDB("1crn")
# Switch off the console to avoid screen updates
yasara.Console("off")
# Print atom names the slow way
for i in range(yasara.CountAtom("all")[0]):
  name = yasara.NameAtom(i+1)[0]
  print "Atom %d has name %s"%(i+1,name)
# Print atom names the fast way
namelist = yasara.NameAtom("all")
for i in range(len(namelist)):
  print "Atom %d has name %s"%(i+1,namelist[i])
<P>

If all fails, you can still use the 'run' function to execute any command,
also those without a Python wrapper (mostly WHAT IF commands in the Twinset):
<P>
# Load 1crn, avoiding the Python wrapper 'LoadPDB("1crn")'
yasara.run("LoadPDB 1crn")
# Enter WHATIF's GRAFIC menu
yasara.run("WHATIF")
yasara.run("GRAFIC")
# Show a wire frame
yasara.run("SHOTOT 1 Crambin")
# Go back to YASARA
yasara.run("YASARA")
# List all objects without the Python wrapper 'ListObj("all")'
yasara.run("ListObj all")
<P>

<H2> Python plugins can access a number of predefined variables

Right after the 'import yasara' statement, the following variables can be
accessed. Note that [i] specifies the number of the selection window, counting starts
with zero at each chain of selection windows leading to a 'Request' keyword.
[j] specifies the number of the selected item, counting starts at 0 in every
selection window.

<T>
<P>yasara.request<P>                     | The request string sent by YASARA to the plugin
<P>yasara.opsys<P>                       | The current operating system, "Linux", "MacOS" or "Windows"
<P>yasara.version<P>                     | The YASARA version string X.Y.Z
<P>yasara.serialnumber<P>                | YASARA's serial number
<P>yasara.stage<P>                       | The YASARA stage View, Model, Dynamics or Structure
<P>yasara.plugin.name<P>                 | The name of the plugin (e.g. ftppdb.py)
<P>yasara.plugin.config<P>               | A Python dictionary with the options from the plugin config file *.cnf
<P>yasara.plugin.exitcode<P>             | The exit code returned to YASARA when the plugin ends
<P>yasara.owner.firstname<P>             | Your first name
<P>yasara.owner.email<P>                 | Your e-mail address
<P>yasara.permissions<P>                 | The permissions of the 'yasara' directory, to be propagated to files updated by the plugin
<P>yasara.workdir<P>                     | YASARA's {current working directory<CD>}, which differs from the plugin's working directory (yasara/plg)
<P>yasara.selection<P>                   | A list of selections with one entry for every selection window you defined
<P>yasara.selection[i].objects<P>        | The number of objects selected in the ith selection window
<P>yasara.selection[i].object[j]<P>      | The obj_descriptor (see below) for the jth selected object in the ith selection window
<P>yasara.selection[i].molecules<P>      | The number of molecules selected in the ith selection window
<P>yasara.selection[i].molecule[j]<P>    | The mol_descriptor (see below) for the jth selected molecule in the ith selection window
<P>yasara.selection[i].residues<P>       | The number of residues selected in the ith selection window
<P>yasara.selection[i].residue[j]<P>     | The res_descriptor (see below) for the jth selected residue in the ith selection window
<P>yasara.selection[i].atoms<P>          | The number of atoms selected in the ith selection window
<P>yasara.selection[i].atom[j]<P>        | The atom_descriptor (see below) for the jth selected atom in the ith selection window
<P>yasara.selection[i].texts<P>          | The number of text input boxes in the ith selection window
<P>yasara.selection[i].text[j]<P>        | The text typed into the jth text input box in the ith selection window
<P>yasara.selection[i].numbers<P>        | The number of number input boxes in the ith selection window
<P>yasara.selection[i].number[j]<P>      | The number typed into the jth number input box in the ith selection window
<P>yasara.selection[i].checkboxes<P>     | The number of checkboxes in the ith selection window
<P>yasara.selection[i].checkbox[j]<P>    | The state of the jth checkbox in the ith selection window (1=hooked, 0=not hooked)
<P>yasara.selection[i].radiobutton<P>    | The number of the selected radiobutton in the ith selection window if there were <=1 radiobutton sets (1=first, 2=second.., None if there was no radiobutton).
<P>yasara.selection[i].radiobutton[j]<P> | The number of the selected radiobutton in the jth radiobutton set of the ith selection window (1=first, 2=second.., None if there was no radiobutton).
<P>yasara.selection[i].listentries<P>    | The number of selected list entries in the ith selection window
<P>yasara.selection[i].list[j]<P>        | The jth selected list entry in the ith selection window
<P>yasara.selection[i].filenames<P>      | The number of selected filenames in the ith selection window
<P>yasara.selection[i].filename[j]<P>    | The jth selected filename in the ith selection window
<T>

<H3> Object descriptors identify selected objects

Object descriptors are instances of the class obj_descriptor.
Typically, you loop over all object descriptors in the ith selection window:

<P>
for j in range(yasara.selection[i].objects):
  object=yasara.selection[i].object[j]
<P>

And then access various object properties:
<T>
<P>object.name<P> | The name of the object
<P>object.number.inyas<P> | The unique number/ID of the object in YASARA (a string, starting with 1)
<P>object.number.inall<P> | The sequential number of the object in the soup (a string, starting with 1)
<T>

You could then color the object red:
<P>
  yasara.ColorObj(object.number.inyas,"Red")
<P>

<H3> Molecule descriptors identify selected molecules

Molecule descriptors are instances of the class mol_descriptor.
Typically, you loop over all molecule descriptors in the ith selection window:

<P>
for j in range(yasara.selection[i].molecules):
  molecule=yasara.selection[i].molecule[j]
<P>

And then access various molecule properties:
<T>
<P>molecule.name<P>         | The name of the molecule (that's the chain name in the PDB file)
<P>molecule.number.inyas<P> | The unique number/ID of the molecule in YASARA (a string). {Becomes invalid if atoms are added or deleted<List>}.
<P>molecule.number.inall<P> | The sequential number of the molecule in the soup (a string, starting with 1)
<P>molecule.number.inobj<P> | The sequential number of the molecule in the object (a string, starting with 1)
<P>molecule.object<P>       | The <object descriptor> for the object the molecule belongs to
<T>

You could then display the molecule as sticks:
<P>
  yasara.StickMol(molecule.number.inyas)
<P>

Or delete the entire object containing this molecule:
<P>
  yasara.DelObj(molecule.object.number.inyas)
<P>

<H3> Residue descriptors identify selected residues

Residue descriptors are instances of the class res_descriptor.
Typically, you loop over all residue descriptors in the ith selection window:

<P>
for j in range(yasara.selection[i].residues):
  residue=yasara.selection[i].residue[j]
<P>

And then access various residue properties:
<T>
<P>residue.name3<P>        | The name of the residue in three letter code.
<P>residue.name1<P>        | The name of the residue in one letter code.
<P>residue.number.inyas<P> | The unique number/ID of the residue in YASARA (a string). {Becomes invalid if atoms are added or deleted<List>}.
<P>residue.number.inall<P> | The sequential number of the residue in the soup (a string, starting with 1).
<P>residue.number.inobj<P> | The sequential number of the residue in the object (a string, starting with 1).
<P>residue.number.inmol<P> | The sequential number of the residue in the molecule (a string, starting with 1).
<P>residue.number.inpdb<P> | The number of the residue in the PDB file (a string, last character may be the insertion code).
<P>residue.object<P>       | The <object descriptor> for the object the residue belongs to.
<P>residue.molecule<P>     | The <molecule descriptor> for the molecule the residue belongs to.
<T>

You could then color the residue yellow:
<P>
  yasara.ColorRes(residue.number.inyas,"Yellow")
<P>

Or display a ribbon for the entire molecule containing this residue:
<P>
  yasara.ShowSecMol(residue.molecule.number.inyas,"Ribbon")
<P>

<H3> Atom descriptors identify selected atoms

Atom descriptors are instances of the class atom_descriptor.
Typically, you loop over all atom descriptors in the ith selection window:

<P>
for j in range(yasara.selection[i].atoms):
  atom=yasara.selection[i].atom[j]
<P>

And then access various atom properties:
<T>
<P>atom.name<P>         | The name of the atom
<P>atom.namespaced<P>   | The name of the atom including spaces (always four characters)
<P>atom.altloc<P>       | The alternate location indicator of the atom
<P>atom.position<P>     | The position of the atom, a list with three cartesian coordinates
<P>atom.occupancy<P>    | The occupancy field of the atom in the original PDB file
<P>atom.bfactor<P>      | The B-factor of the atom
<P>atom.number.inyas<P> | The unique number/ID of the atom in YASARA (a string). {Becomes invalid if atoms are added or deleted<List>}.
<P>atom.number.inall<P> | The sequential number of the atom in the soup (a string, starting with 1, the same as .inyas above).
<P>atom.number.inobj<P> | The sequential number of the atom in the object (a string, starting with 1, usually the same number as in the PDB file).
<P>atom.number.inmol<P> | The sequential number of the atom in the molecule (a string, starting with 1).
<P>atom.number.inres<P> | The sequential number of the atom in the residue (a string, starting with 1).
<P>atom.object<P>       | The <object descriptor> for the object the atom belongs to.
<P>atom.molecule<P>     | The <molecule descriptor> for the molecule the atom belongs to.
<P>atom.residue<P>      | The <residue descriptor> for the residue the atom belongs to.
<T>

You could then color the atom green:
<P>
  yasara.ColorAtom(atom.number.inyas,"Green")
<P>

Or delete the entire residue the atom belongs to:
<P>
  yasara.DelRes(atom.residue.number.inyas)
<P>

<H2> Python plugins can access persistent storage in YASARA

If a Python plugin terminates {by calling yasara.plugin.end()<TlftrpdbPaY.html>}, the Python interpreter stops
executing the plugin and all variables are lost. Complex plugins may like to preserve certain variables
until the plugin is run again by the user (for example username and password for a database connection).
This can be achieved by using YASARA's persistent storage facility. As shown in the example below, you
only need to initialize the variable 'yasara.storage' (this name is fixed) when the plugin is run for the
first time, usually by assigning an instance of the trivial 'container' class. All data stored in this
container will then be preserved across calls to the plugin, until the user exits YASARA. If you want to preserve
data until YASARA is run again, then you need to save it to disk.

<P>
# YASARA PLUGIN
# DESCRIPTION: Click 'Options > Test plugin' multiple times to show a counter
""\"
MainMenu: Options
  PullDownMenu after Stop plugin: Test plugin
    Request: TestPlugin
""\"

import yasara,time
from python2to3 import *
from container import *

if (yasara.request=="TestPlugin"):
  if (yasara.storage==None):
    # Plugin is run for the first time, create a persistent storage container
    yasara.storage=container()
    # Store something
    yasara.storage.counter=1
  else:
    # Not the first time, increment counter in persistent storage container
    yasara.storage.counter+=1
  # Display the counter
  yasara.ShowMessage("Test plugin has been run %d times..."%yasara.storage.counter)
  time.sleep(3)
  yasara.HideMessage()
# This must always be the last command
yasara.plugin.end()
<P>

<H2> Yanaconda plugins can access a number of predefined variables

In addition to a large number of
{predefined variables that can be accessed by all Yanaconda macros<Ymcapv>},
the following additional variables are available to macros run as a plugin:

Note that (i) specifies the number of the selection window, counting starts
at 1 at each chain of selection windows leading to a 'Request' keyword.
(j) specifies the number of the selected item, counting starts at 1 in every
selection window.

<T>
<P>request<P>                 | The request string sent by YASARA to the plugin
<P>selection(i)<P>            | An atom to object selection string for atom to object selection windows and context menus
<P>selection(i)texts<P>       | The number of text input boxes in the ith selection window
<P>selection(i)text(j)<P>     | The text typed into the jth text input box in the ith selection window
<P>selection(i)numbers<P>     | The number of number input boxes in the ith selection window
<P>selection(i)number(j)<P>   | The number typed into the jth number input box in the ith selection window
<P>selection(i)checkboxes<P>  | The number of checkboxes in the ith selection window
<P>selection(i)checkbox(j)<P> | The state of the jth checkbox in the ith selection window (1=hooked, 0=not hooked)
<P>selection(i)radiobutton<P> | The number of the selected radiobutton in the ith selection window (1=first, 2=second..).
<P>selection(i)listentries<P> | The number of selected list entries in the ith selection window
<P>selection(i)list(j)<P>     | The jth selected list entry in the ith selection window
<P>selection(i)filenames<P>   | The number of selected filenames in the ith selection window
<P>selection(i)filename(j)<P> | The jth selected filename in the ith selection window
<T>

<H2> Plugins can create interactive user interfaces

In addition to the various selection windows that plugins can
{add to YASARA's user interface via a triple-quote comment<Tmsieiatc>},
they can also create interactive elements on the fly, while they
are running.

There are two different approaches:

*) Plugins can use the <ShowWin> command to open a window and obtain the
   selections made as a list of return values.

*) Plugins can create a custom user interface by {printing text<Print>},
   {drawing rectangles<FillRect>} and
   {showing clickable buttons<ShowButton>} at three different locations:
   In {the head-up display<PrintHUD>}, in {images<PrintImage>} (those
   {shown directly on screen<ShowImage>} and those
   {attached to 3D image objects<MakeImageObj>}), and in {a second window<PrintWin>}.

   When the user clicks on a button, the plugin is run again {with a request<TlftrpdbPaY>}
   that can be provided as the button's 'Action parameter'. Alternatively, the plugin
   can {wait until any button is pressed<Wait>} (which has the drawback that no
   other plugin can be run while the first is waiting).

   The following example Python plugin shows the details, it creates three buttons that perform
   various actions. To test the plugin, save it as
   'yasara/plg/buttontest.py' (don't change the name), restart YASARA and click
   Window > Head-up display > Test HUD buttons:

   <P>
   # YASARA PLUGIN
   # TOPIC:       Database interfaces
   # TITLE:       Test interactive buttons in the HUD
   # AUTHOR:      Elmar Krieger
   # LICENSE:     GPL
   # DESCRIPTION: This plugin shows text and some buttons, and handles the button clicks
   #
   ""\"
   MainMenu: Window
     PullDownMenu: Head-up display
       SubMenu after Off: Test HUD _b_uttons
         Request: ShowTestButtons
   ""\"

   import yasara
   from python2to3 import *

   # CREATE SOME TEST BUTTONS
   # ========================
   def ShowButtons():
     yasara.Font("Arial",height=25,color="White")
     yasara.PosText(x="50%",y=8,justify="center")
     yasara.Print("Button Test")
     yasara.Font(height=14)
     # Show a simple button, runs this plugin with request=="Showsidechains"
     yasara.ShowButton("Show sidechains",y=100,color="Red")
     # Show a button that opens a browser window
     yasara.ShowButton("Take me to YASARA.org",y=180,color="Green",
                       action="ShowURL http://www.yasara.org")
     # Show a complex button, runs this plugin with request=="ColorCYS" and a selection
     # of all cysteine residues in yasara.selection[0].residue
     yasara.ShowButton("Color cysteines yellow",y=260,color="Blue",
                       action="SavePLIRes CYS,Request=ColorCYS|RunPlugin buttontest.py")

   # MAIN PLUGIN
   # ===========
   if (yasara.request=="ShowTestButtons"):
     # Show example buttons in the HUD
     yasara.PrintHUD()
     ShowButtons()
     # Show example buttons in a moving image
     img=yasara.MakeImage("Buttons",width=512,height=512,topcol="None",bottomcol="None")
     yasara.ShowImage(img,x=-256,y=-128,width=1024,height=768,alpha=100,priority=0)
     yasara.AutoMoveImage(img,x=-256,y=250,width=1024,height=12,alpha=0,steps=400,cycle=1)
     yasara.PrintImage(img)
     ShowButtons()
     # Show example buttons in a 3d image object
     # We simply reuse image 'buttons', which means that button clicks will be visible in both
     obj=yasara.MakeImageObj("Buttons",img,width=40,height=40)
     yasara.AutoRotateObj(obj,y=0.3)
     yasara.MoveObj(obj,x=-20)
     # Direct printing back to console
     yasara.PrintCon()

   if (yasara.request=="Showsidechains"):
     # The 'Show sidechains' button has been clicked
     yasara.ShowAtom("Sidechain CA")

   if (yasara.request=="ColorCYS"):
     # The 'Color cysteines yellow' button has been clicked, the cysteine
     # residues have been selected via the 'SavePLIRes CYS' command
     if (yasara.selections):
       for i in range(yasara.selection[0].residues):
         yasara.ColorRes(yasara.selection[0].residue[i].number.inyas,"yellow")

   # This must always be the last command
   yasara.plugin.end()
   <P>


<H2> Python plugins run in a separate thread

While a Python plugin is running, you can continue using YASARA normally.
There are in fact two threads working in parallel: YASARA and the plugin.
When a plugin runs a YASARA command, this command is passed from the plugin
to YASARA and executed as soon as possible. <B>It is normally NOT guaranteed
that YASARA has finished a command when the function call in the plugin returns.<B>
This can lead to potential problems if there is a data dependency between YASARA
and the plugin, usually involving files on the hard disk accessed by both.

The solution is to let the plugin wait until YASARA has finished executing the command.
This can simply be achieved by using the return value (which can only be known after
YASARA finished the command). If you do not need the return value, consider putting
the command between brackets [..], which is a good way to indicate that synchronization
is requested. Here are three typical examples:

*) `The plugin reads a file created by YASARA`:
Since this is a common task, all YASARA commands that save data to the hard disk are
synchronized automatically. The only exception is the LogAs command:
<P>
# Log the output of the next command
yasara.LogAs("MyLog")
# List all hydrogen bonds, and assign the return value to a dummy
# variable, so that the plugin is forced to wait until YASARA finished:
dummy = yasara.ListHBoAtom("all","all")
# Or, alternatively with less typing:
[yasara.ListHBoAtom("all","all")]
# Read the log file in Python
log=open("MyLog").readlines()
<P>

*) `YASARA reads a file created by the plugin`:
This is normally not a problem, unless the file is a temporary one, and the
plugin decides to delete it. In this case, the plugin must wait for YASARA to
read the file before deleting it:
<P>
# Download a certain unofficial PDB file from the web
pdb=urllib2.urlopen(url).readlines()
# Save it temporarily
open(pdbfilename,"w").writelines(pdb)
# Read it in YASARA, and wait until YASARA has finished
[yasara.LoadPDB(pdbfilename)]
# Delete the temporary file only after it has been read by YASARA
os.path.remove(pdbfilename)
<P>
Instead of waiting for YASARA, one can also let YASARA delete the file, which
avoids synchronization issues:
<P>
# Read it in yasara
yasara.LoadPDB(pdbfilename)
# And delete
yasara.DelFile(pdbfilename)
<P>

*) `Catching a YASARA exception`:
Since the plugin does normally not wait until YASARA has finished executing
a command, any error YASARA encounters is shown on screen, but cannot be
reported back to the plugin. Again, the solution is to force synchronization
by using the command's return value or enclosing the command in brackets:
<P>
# Try to initialize force field parameters, forcing the plugin to wait for YASARA:
try:
  yasara.ShowMessage("Initializing simulation")
  [yasara.Sim("init")]
except:
  yasara.ShowMessage("Could not initialize simulation")
<P>

<H2> Plugins can be speeded up

Normally YASARA executes each command issued by the plugin just as if it had been
created via the graphical user interface. This includes an update of the graphics display
and potentially a {simulation step<TimeStep>} after each command. If the plugin issues hundreds of commands,
this approach may become too slow. In this case resort to the trick used by Yanaconda
macros to speed up execution: just switch off the <console>.

<P>
yasara.Console("Off")
<P>

See the <Console> command for more details and note that YASARA will neither redraw the screen
nor proceed a simulation unless you tell it to by {calling the Wait() function<Mcwfastouypab>},
and may thus appear frozen. So don't forget to enable the console
again with yasara.Console("Hidden") when leaving the performance critical section.

A common performance-critical example is building a large number of atoms. The following
example duplicates each atom of PDB file 5tim, at a rate of about 1000 atoms per second:

<P>
# Make sure that there are no unused objects between others
yasara.RenumberObj("all",1)
# Load the PDB file (becomes the last object), store the number of objects in 'objects'
objects=yasara.LoadPDB("/home/pdb/5tim",model=1)[0]
# Get the global coordinates and chemical elements of all the atoms
poslist=yasara.PosAtom("Obj %d"%objects,coordsys="global")
elementlist=yasara.ElementAtom("Obj %d"%objects)
# Speed up
yasara.Console("off")
for i in range(len(elementlist)):
  # Build a new atom and place it at the right spot
  obj=yasara.BuildAtom(elementlist[i])
  yasara.PosObj(obj,x=poslist[i*3],y=poslist[i*3+1],z=poslist[i*3+2])
  if (not i%100 or i==len(elementlist)-1):
    # As soon as 100 atoms have been built, join them (too many objects slow YASARA down,
    # note also that you need to use i%9 in YASARA View, which supports only 10 objects)
    yasara.JoinObj("not 1-%d"%(objects+1),objects+1)
yasara.Console("on")
<P>

<H2> Plugins can be run from the command line and in console mode

Plugins are normally linked to options in the user interface.
Sometimes, it may be helpful to run a plugin directly. This is achieved with the
<SavePLI> and <RunPlugin> commands:
<P>
# Save a PLugin Input (PLI) File containing a selection of Calpha atoms
# and the request 'MyRequest'
SavePLIAtom CA,MyRequest
# Run the plugin plg/MyPlugin.py
RunPlugin MyPlugin.py
<P>
You can put the code above into a macro, e.g. 'runplugin.mcr' and run it from the command line:
<P>
yasara runplugin.mcr
<P>
Note that the {RunPlugin command stops the currently running macro<RunPlugin>} (you cannot have both at the same time),
so any commands placed after RunPlugin will never be executed.

If no selections are required, the plugin can be run directly without a macro in between:
<P>
yasara MyPlugin.py MyRequest
<P>
If the plugin doesn't need user interaction, it can be run in {console- or plain text mode<RYwg>}:
<P>
yasara -con MyPlugin.py MyRequest
yasara -txt MyPlugin.py MyRequest
<P>

If you want to exit YASARA as soon as the plugin has finished, add this
line to the end of the plugin:
<P>
yasara.Exit()
<P>

<H2> Plugins can start additional programs that control YASARA, like a Python module

Some specialized applications may require to control YASARA from an external program.
For example, the 3DM system from Bio-Prodict.nl allows to control YASARA from a web
browser window. This is a non-trivial task that can be achieved with these steps:

1) Write a {Python module<Scripts>} that opens a socket and listens for
   YASARA control instructions, which it transforms into YASARA commands.

*) Use Java(-Script) on your webpage to check if this Python module is listening,
   connect to it if yes, and send YASARA control instructions that reflect what the
   user does in the browser. If the Python module is not listening, your webpage
   may start YASARA first, e.g. via the MIME-type setting if your browser's security
   settings don't allow to launch an external program.

*) To make sure that your {Python module<Scripts>} is started together with YASARA, save the
   module in the 'yasara/pym' folder and create a corresponding Python plugin (saved in the
   'yasara/plg' folder) that contains the following launch code:
   <P>
   if (yasara.request[:12]=="LaunchModule"):
     # YASARA requests to launch the Python module now. The Python module must be
     # placed in the yasara/pym folder. Since this is a Python plugin, we are currently
     # in the yasara/plg folder, so we need to prepend ../pym/ to the module name.
     # The yasara.request contains additional connection information at the end and
     # must be forwarded to the Python module as command line parameter.
     command='"'+sys.executable+'" ..'+os.sep+'pym'+os.sep+'3dmcommunicator.py '+yasara.request
     subprocess.Popen(command,shell=True)
     # If something went wrong launching, you could tell YASARA with a non-zero exitcode:
     # yasara.plugin.exitcode=1
   <P>
   When YASARA starts, it sends a 'LaunchModule' request to your plugin, which uses
   'subprocess.Popen' to launch your Python module, in this example
   'yasara/pym/3dmcommunicator.py'. Also note that 'yasara.request' needs to be
   passed to your Python module, in the example as the first command line parameter.

*) In your Python module (e.g. yasara/pym/3dmcommunicator.py) you need to connect
   to the YASARA instance that launched the module, so that you can send it YASARA
   commands. This is done with the following code:
   <P>
   # Import the YASARA Python module yasara/pym/yasara.py
   import yasara

   # Connect to the YASARA that launched us, which is identified via
   # its 'yasara.request' (passed here as command line parameter sys.argv[1])
   yasara.connect(sys.argv[1])
   <P>
   So to make sure that your Python module does not launch a new YASARA but instead
   communicates with the already running YASARA, you need to use the function
   'yasara.connect', providing the original yasara.request as argument.

   Then your Python module can already start to issue YASARA commands, e.g.
   <P>
   yasara.LoadPDB("1crn",download=1)
   while 1:
    for i in range(46):
      yasara.ColorRes(i+1,"blue")
      time.sleep(2)
   <P>

*) As a special service, YASARA kills your Python module when the user exits
   YASARA (since your Python module was started as a separate process with
   subprocess.Popen, it would normally continue running and crash eventually).

<H2> Debugging is done by adding temporary print commands

Programs contain errors, the same is true for plugins.
There are two types of errors in Python plugins:

*) Errors that occur during the initial plugin registration when YASARA starts up.
Most of the time these are simple syntax errors.
In Linux and MacOS, you see the error message in the console from where you started YASARA.
Windows can unfortunately not display the error message, but you know that something
went wrong because your plugin does not appear in YASARA's user interface. Open a command
prompt, go to the yasara\plg directory and run the plugin directly with the Python
interpreter to locate the problem:
<P>
c:\MyPythonInstallationPath\python.exe MyPlugin.py
<P>
This will show you a traceback. After correcting the error you have to restart YASARA.

*) Errors that occur while the plugin is running. YASARA displays the
main error message on screen, and a complete traceback in the console which you
can bring up by pressing <SPACE>. After correcting the error, you can simply rerun
the plugin, you DO NOT have to restart YASARA.

If you want to print debug statements to trace a problem, this is easily done using
<P>print "MyMessage"<P>
in Yanaconda and
<P>yasara.write(WhatEver)<P>
in Python plugins. 'WhatEver' does not have to be a string, but just anything you can
pass to Python's print function. DO NOT use Python's print function directly, because
this fails under Windows unless you also flush the output buffer with sys.stdout.flush()

If your Python plugin hangs in an infinite loop, click on Options > Stop plugin. This will terminate
your plugin as soon as it tries to print something or calls a YASARA command. If the plugin
does not do any of these things, YASARA will also hang until you kill the Python task manually
from the Windows Task Manager, with the Linux 'kill' command or with the MacOS
'Activity Monitor' (can be found in the Applications/Utilities folder).
"""

import sys,os,time,disk,socket,string,struct,stat
from python2to3 import *
from container import *

#  ======================================================================
#                         P L U G   I N   C L A S S
#  ======================================================================

class plg_in:
  """
  This class stores various methods used by the actual plugin
  """

  # INITIALIZE
  # ==========
  def __init__(self,name):
    self.exitcode=0
    self.name=name
    self.config={}
    # SEE IF THERE IS A CONFIG FILE
    configfilename=self.name[:-2]+"cnf"
    if (os.path.exists(configfilename)):
      # READ THE CONFIGURATION FILE
      for line in open(configfilename).readlines():
        line=line.strip()
        if (len(line)):
          # CHECK IF CURRENT LINE IS A COMMENT (STARTS WITH '#')
          if (line[0]!='#'):
            # LINE IS NOT A COMMENT, ALSO ADD EMPTY FIELDS TO AVOID PLUGIN CRASHES
            equalpos=line.find("=")
            if (equalpos>0):
              # ADD TO CONFIG DICTIONARY
              self.config[line[:equalpos].strip()]=line[equalpos+1:].strip()

  # END PLUGIN
  # ==========
  def end(self,errormessage=None):
    global request

    if (request!="CheckIfDisabled" and request[:12]!="LaunchModule"):
      if (errormessage):
        HideMessage()
        RaiseError(errormessage)
        Finish()
      # SAVE PERSISTENT STORAGE FOR NEXT TIME
      SaveStorage()
      # DONE
      StopPlugin()
      time.sleep(1)
    sys.exit(self.exitcode)

#  ======================================================================
#              N U M B E R   D E S C R I P T O R   C L A S S
#  ======================================================================

class num_descriptor:
  """
  This class stores any atom, residue, molecule and object number in
  various numbering schemes. All numbers are actually stored as strings,
  because that saves a lot of type casts later (and .inpdb and .inyas
  can contain characters).
  Contrary to Python conventions, all sequential numbers start at 1.

  .inyas - unique number in Yasara (always defined, may contain non-digits)
  .inall - sequential number in the soup (always defined),
  .inobj - sequential number in the object (defined for atoms, residues and molecules),
  .inmol - sequential number in the molecule (defined for atoms and residues),
  .inres - sequential number in the residue (defined for atoms).
  .inpdb - PDB residue number, five characters with insertion code (defined for residues).
  """
  def __init__(self,string):
    self.inyas=" ".join(string[0:13].strip().split())
    self.inall=string[14:22].strip()
    if (len(string)>23): self.inobj=string[23:31].strip()
    if (len(string)>32): self.inmol=string[32:40].strip()
    if (len(string)>41): self.inres=string[41:49].strip()
    self.inpdb=None

#  ======================================================================
#              O B J E C T   D E S C R I P T O R   C L A S S
#  ======================================================================

class obj_descriptor:
  """
  This class stores the identity of an object.
  """

  # INITIALIZE
  # ==========
  def __init__(self,string):
    # GET NAME
    self.name=string[0:12].strip()
    # GET THE NUMBER IN VARIOUS NUMBERING SCHEMES: inall, inobj
    self.number=num_descriptor(string[13:36])

#  ======================================================================
#             M O L E C U L E   D E S C R I P T O R   C L A S S
#  ======================================================================

class mol_descriptor:
  """
  This class stores the identity of a molecule.
  A molecule is a continuous stretch of atoms sharing the same chain name.
  """

  # INITIALIZE
  # ==========
  def __init__(self,str):
    # GET NAME
    self.name=str[0]
    # GET THE NUMBER IN VARIOUS NUMBERING SCHEMES: inall
    self.number=num_descriptor(str[2:34])
    # GET A DESCRIPTION OF THE OBJECT THE MOLECULE BELONGS TO
    self.object=obj_descriptor(str[34:])

#  ======================================================================
#             R E S I D U E   D E S C R I P T O R   C L A S S
#  ======================================================================

class res_descriptor:
  """
  This class stores the identity of a residue.
  """

  # INITIALIZE
  # ==========
  def __init__(self,string):
    # GET NAME IN THREE AND ONE LETTER CODE
    self.name3=string[0:3]
    self.name1=string[4]
    # GET THE NUMBER IN VARIOUS NUMBERING SCHEMES: inall, inobj, inmol
    self.number=num_descriptor(string[12:53])
    # AS A SPECIAL CASE, ADD THE NUMBER IN THE PDB FILE (INCLUDES INSERTION CODE)
    self.number.inpdb=string[6:11].strip()
    # GET A DESCRIPTION OF THE MOLECULE AND OBJECT THE RESIDUE BELONGS TO
    self.molecule=mol_descriptor(string[53:])
    self.object=self.molecule.object

#  ======================================================================
#                A T O M   D E S C R I P T O R   C L A S S
#  ======================================================================

class atom_descriptor:
  """
  This class stores the identity of an atom.
  """

  # INITIALIZE
  # ==========
  def __init__(self,str):
    # GET NAME, AND ALTLOC INDICATOR
    self.namespaced=str[0:4]
    self.name=self.namespaced.strip()
    self.altloc=str[5]
    # GET THE NUMBER IN VARIOUS NUMBERING SCHEMES: inall, inobj, inmol, inres
    self.number=num_descriptor(str[7:57])
    fmtoa=0.00001
    # GET ATOM PROPERTIES: POSITION, OCCUPANCY, B-FACTOR
    self.position=[int(str[57:68])*fmtoa,int(str[69:80])*fmtoa,int(str[81:92])*fmtoa]
    self.occupancy=float(str[93:104])
    self.bfactor=float(str[105:116])
    # GET A DESCRIPTION OF THE RESIDUE, MOLECULE AND OBJECT THE ATOM BELONGS TO
    self.residue=res_descriptor(str[117:])
    self.molecule=self.residue.molecule
    self.object=self.molecule.object

#  ======================================================================
#           S E L E C T I O N   D E S C R I P T O R   C L A S S
#  ======================================================================

class sel_descriptor:
  """
  This class stores an entire selection corresponding to the content of
  one YASARA selection window. Methods for adding to this selection are
  provided.
  """

  # INITIALIZE
  # ==========
  def __init__(self):
    # PREPARE STORAGE OF SELECTED UNITS
    self.atoms=0
    self.atom=[]
    self.atomlist=[]
    self.residues=0
    self.residue=[]
    self.residuelist=[]
    self.molecules=0
    self.molecule=[]
    self.moleculelist=[]
    self.objects=0
    self.object=[]
    self.objectlist=[]
    self.texts=0
    self.text=[]
    self.textlist=[]
    self.numbers=0
    self.number=[]
    self.numberlist=[]
    self.radiobutton=None
    self.radiobuttons=0
    # BACKWARDS COMPATIBILITY, OBSOLETE SINCE 11.10.17
    self.switchbox=None
    self.checkboxes=0
    self.checkbox=[]
    self.checkboxlist=[]
    self.listentries=0
    self.listentry=[]
    self.list=[]
    self.filenames=0
    self.filename=[]
    self.filenamelist=[]

  # PRINT CONTENT
  # =============
  def __repr__(self):
    return("A Yasara selection containing %d objects, %d molecules, "%(self.objects,self.molecules)+
           "%d residues, %d atoms and %d texts."%(self.residues,self.atoms,self.texts))

  # ADD AN OBJECT TO SELECTION
  # ==========================
  def addobject(self,string):
    self.object.append(obj_descriptor(string))
    self.objectlist=self.object
    self.objects+=1

  # ADD A MOLECULE TO SELECTION
  # ===========================
  def addmolecule(self,string):
    self.molecule.append(mol_descriptor(string))
    self.moleculelist=self.molecule
    self.molecules+=1

  # ADD A RESIDUE TO SELECTION
  # ==========================
  def addresidue(self,string):
    self.residue.append(res_descriptor(string))
    self.residuelist=self.residue
    self.residues+=1

  # ADD AN ATOM TO SELECTION
  # ========================
  def addatom(self,string):
    self.atom.append(atom_descriptor(string))
    self.atomlist=self.atom
    self.atoms+=1

  # ADD TEXT TO SELECTION
  # =====================
  def addtext(self,string):
    self.text=[string.strip()]+self.text
    self.textlist=self.text
    self.texts+=1

  # ADD NUMBER TO SELECTION
  # =======================
  def addnumber(self,number):
    if (int(number)==number): number=int(number)
    self.number=[number]+self.number
    self.numberlist=self.number
    self.numbers+=1

  # ADD CHECK BOX TO SELECTION
  # ==========================
  def addcheckbox(self,string):
    self.checkbox=[int(string)]+self.checkbox
    self.checkboxlist=self.checkbox
    self.checkboxes+=1

  # ADD RADIO BUTTON
  # ================
  def addradiobutton(self,string):
    if (self.radiobutton==None):
      self.radiobutton=int(string)
      # FOR BACKWARDS COMPATIBILITY, OBSOLETE SINCE VERSION 11.10.17, AND ALSO COUNTING
      # STARTED AT 0, WHICH IS NO LONGER POSSIBLE TO MATCH THE NEW ShowWin COMMAND.
      self.switchbox=self.radiobutton-1
    else:
      if (type(self.radiobutton)==type(1)): self.radiobutton=[self.radiobutton]
      self.radiobutton.append(int(string))
      self.radiobuttonlist=self.radiobutton
    self.radiobuttons+=1

  # ADD LIST ENTRY TO SELECTION
  # ===========================
  def addlistentry(self,string):
    self.list=[string]+self.list
    self.listentry=self.list
    self.listentries+=1

  # ADD FILENAME TO SELECTION
  # =========================
  def addfilename(self,string):
    self.filename=[string]+self.filename
    self.filenamelist=self.filename
    self.filenames+=1

#  ======================================================================
#           Y A S A R A   C O M M U N I C A T I O N   C L A S S
#  ======================================================================

class yasara_communicator:

  # INITIALIZE COMMUNICATION WITH YASARA
  # ====================================
  def __init__(self):
    # THE MESSAGE IDs AND OTHER PREDEFINED VALUES
    self.RESULT=0       # Result of a YASARA command
    self.ERROR=1        # Error raised by YASARA
    self.broken="Socket connection broken"
    port=socket.IPPORT_USERRESERVED
    while (1):
      self.srvsock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
      # FIND AND BLOCK A FREE PORT.
      # NOTE: AT LEAST WINDOWS ME WITH PYTHON 2.5 HAS A BUG WHERE SETTING SO_REUSEADDR
      # ALLOWS TO BIND TO PORT 5000, WHICH IS HOWEVER USED BY ANOTHER PROGRAM (ssdpsrv.exe).
      # (INSTEAD, SO_REUSEADDR SHOULD ONLY ALLOW TO BIND PORTS THAT ARE IN TIME_WAIT STATE
      # AFTER A PREVIOUS CONNECTION HAS ENDED, WAITING FOR LEFTOVER TCP PACKETS). AS A
      # RESULT, YASARA SENDS THE RESULTS TO WHOEVER OWNS PORT 5000, AND THE SCRIPT HANGS FOREVER.
      #self.srvsock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
      try:
        # SOCKET IS ONLY VISIBLE ON THE LOCAL MACHINE
        self.srvsock.bind(("",port))
        break
      except: port+=1
    self.srvsock.listen(1)
    self.sock=None
    self.port=port

  # ACCEPT A CONNECTION FROM YASARA
  # ===============================
  def accept(self):
    if (self.sock!=None): raise RuntimeError("Connection has already been accepted")
    (self.sock,ip)=self.srvsock.accept()

  # RECEIVE DATA FROM YASARA
  # ========================
  def receive(self,size):
    data=binary("")
    while (len(data)<size):
      # IF THE CONNECTION BREAKS, THIS RETURNS 0 IN LINUX,
      # BUT RAISES AN EXCEPTION (WHICH ONE??) IN SOME WINDOWS VERSIONS
      try: chunk=self.sock.recv(size-len(data))
      except KeyboardInterrupt: raise
      except: raise RuntimeError(self.broken)
      if (len(chunk)==0): raise RuntimeError(self.broken)
      data+=chunk
    return(data)

  # RECEIVE A MESSAGE FROM YASARA
  # =============================
  def receivemessage(self,expectedtype=None):
    (messagetype,datasize)=struct.unpack('ii',self.receive(8))
    data=self.receive(datasize)
    messagedata=pickle.loads(data)
    if (messagetype==self.ERROR):
      raise RuntimeError("YASARA raised error %d: %s"%(messagedata[0],messagedata[1]))
    if (expectedtype!=None and messagetype!=expectedtype):
      raise RuntimeError("Unexpected message type received")
    if (expectedtype==None): return((messagetype,messagedata))
    else: return(messagedata)

#  ======================================================================
#                 P L U G I N   F U N C T I O N   G R O U P
#  ======================================================================

# CONVERT VERSION STRING TO INTEGER
# =================================
def versionint(version):
  version=version.strip().split('.')
  return(int(version[0])*10000+int(version[1])*100+int(version[2]))

# CHECK IF THE RETURN VALUE OF THE CALLING FUNCTION IS USED
# =========================================================
def retvalused():
  # GET A TRACEBACK OBJECT
  try: raise ValueError
  except: tb=sys.exc_info()[2]
  # UNWIND THE CALL STACK
  frame=tb.tb_frame.f_back.f_back
  code=frame.f_code.co_code
  # byte(1) IS THE CODE 'POP_TOP', I.E. DO NOT USE RETURN VALUE
  return(code[frame.f_lasti+3]!=byte(1))

# RUN A YASARA COMMAND, POTENTIALLY RETURNING RESULTS
# ===================================================
def runretval(command,retvalused):
  global com,request, std_relay_service

  if (request=="CheckIfDisabled"): raise RuntimeError("You cannot run YASARA commands during the startup phase, when your plugin checks if it can be activated or should be disabled")
  if (not retvalused):
    # NO RETURN VALUE NEEDED, RETURN IMMEDIATELY
    std_relay_service.root.stdout_relay('Exec: '+command+'\n')
    return(None)
  else:
    # THE CALLER WANTS A RETURN VALUE, WAIT FOR YASARA RESULTS
    if (com==None):
      # BIND A SOCKET TO RECEIVE RESULTS FROM YASARA
      com=yasara_communicator()
      # SEND COMMAND AND REPLY PORT
      std_relay_service.root.stdout_relay('ExecRV%d: '%com.port+command+'\n')
      # ACCEPT CONNECTION
      com.accept()
    else:
      # SEND COMMAND ONLY
      std_relay_service.root.stdout_relay('ExecRV: '+command+'\n')
    return(com.receivemessage(com.RESULT))

# RUN A YASARA COMMAND
# ====================
def run(command):
  return(runretval(command,retvalused()))

def Run(command):
  return(runretval(command,retvalused()))

# WRITE DEBUGGING INFO TO CONSOLE
# ===============================
def write(info):
  print(info)
  sys.stdout.flush()

# CLEAN STRING
# ============
def cstr(text,quoted=0):
  text=str(text)
  text=text.replace("\n","\\n")
  text=text.replace("\r","\\r")
  text=text.replace("\t","\\t")
  if (quoted or text.find(',')!=-1):
    for quote in ['"',"'"]:
      if (text.find(quote)==-1): break
    else:
      quote='"'
      text=text.replace(quote,"'")
    text=quote+text+quote
  return(text)

# CONVERT SELECTION TO STRING
# ===========================
def selstr(selection):
  if (type(selection) in [type(""),type(u""),type(1),type(1.)]): selstr=cstr(selection)
  else:
    if (type(selection)!=type([])): selection=list(selection)
    selstr=""
    for i in range(len(selection)):
      if (i>0 and type(selection[i])==type("") and type(selection[i-1])==type("") and
          ((selection[i][:9]=="Res Atom " and selection[i-1][:9]=="Res Atom ") or
           (selection[i][:9]=="Mol Atom " and selection[i-1][:9]=="Mol Atom "))):
        # WE CAN COMPRESS THE UNIQUE RESIDUE/MOLECULE IDs (SEE DOCS OF List COMMAND)
        selstr+=cstr(selection[i][9:]+" ")
      else: selstr+=cstr(selection[i])+" "
  selstr=selstr.strip()
  if (selstr==""): selstr="none"
  return(selstr)

# CHECK FOR YASARA VERSION
# ========================
# THIS IS A REPLACEMENT FOR YASARA'S RequireVersion COMMAND
def RequireVersion(reqversion):
  # GET CURRENT VERSION
  curversionsplit=version.split(".")
  reqversionsplit=reqversion.split(".")
  for i in range(3):
    if (int(curversionsplit[i])>int(reqversionsplit[i])): break
    if (int(curversionsplit[i])<int(reqversionsplit[i])):
      plugin.end("This plugin reqires at least YASARA Version %s, but currently only version %s is installed"%(reqversion,version))

# SAVE PERSISTENT STORAGE FOR NEXT TIME
# =====================================
def SaveStorage():
  if (storage!=None):
    # USER ADDED PERSISTENT data, SEND TO YASARA (WHICH WILL DELETE THE FILE)
    filename=disk.tmpfilename("data")
    pickle.dump(storage,open(filename,"wb"))
    runretval("SaveStorage %s"%filename,0)

# WAIT FOR YASARA TO FINISH EXECUTION
# ===================================
def Finish():
  # USE THE RETURN VALUE OF A DUMMY COMMAND TO FORCE THE SYNCHRONIZATION
  result=CountObj("all")

# EXIT YASARA
# ===========
# WE CANNOT WAIT FOR A RESULT
def Exit():
  runretval("Exit",0)

# INITIALIZE THE PLUGIN
# =====================

# AA -- Nov 2021 -- 
# =================

# Previous initialisation as required here.
# STDERR is redirected to STDOUT
sys.__stderr__=sys.__stdout__
sys.stderr=sys.__stderr__


from rpyc.utils.registry import UDPRegistryServer
from rpyc import connect_by_service
from rpyc.utils.server import ThreadedServer

# Define the stdout relay service here

class YasaraStdoutRelayService(rpyc.Service):
    def exposed_stdout_relay(self, specific_command):
        # TODO: HIGH, Check specific_command for str type.
        sys.stdout.write(specific_command)
        sys.stdout.flush()

# Try to launch the registry server, if it is already running use it to discover the service.

try:
    reg_server = UDPRegistryServer()
    serv = ThreadedServer(YasaraStdoutRelayService)
    serv.start()
except OSError as net_error:
    pass
    
std_relay_service = rpyc.connect_by_service("YasaraStdoutRelay")        
    
    
# AA -- Nov 2021 -- 
# =================

# # STDERR is redirected to STDOUT
# sys.__stderr__=sys.__stdout__
# sys.stderr=sys.__stderr__

plugin=plg_in(os.path.basename(sys.argv[0]))
request=None
com=None
selection=[]
# GET OPERATING SYSTEM AND FILE EXTENSION OF APPLICATIONS
appext=""
if (os.name.lower()=="nt"):
  opsys="Windows"
  appext=".exe"
else:
  try:
    import platform
    opsys=platform.system()
    if (opsys=="Darwin"):
      opsys="MacOS"
      appext=".app"
  except:
    # platform MODULE DOES NOT YET EXIST (EARLY PYTHONS)
    if (os.path.exists("/Applications/Finder")):
      opsys="MacOS"
      appext=".app"
    else: opsys="Linux"
# GET YASARA PATH
os.chdir("..")
if (not os.path.exists("yasara.fof")):
  # USER TRIED TO RUN A PLUGIN OUTSIDE plg
  raise RuntimeError("Plugins must be placed in the yasara/plg folder. If you tried to run a Python plugin from the command line, check the user manual at 'Scripts - Use YASARA as a Python module' instead")
path=os.getcwd()
os.chdir("plg")
plugin.path=os.getcwd()
# GET PERMISSIONS OF THE yasara DIRECTORY, TO BE PROPAGATED IF PLUGIN UPDATES FILES
info=os.stat(path)
permissions=stat.S_IRWXU
if (opsys!="Windows"):
  if (info.st_mode&(stat.S_IRGRP|stat.S_IWGRP)): permissions|=stat.S_IRWXG
  if (info.st_mode&(stat.S_IROTH|stat.S_IWOTH)): permissions|=stat.S_IRWXO
# DO WE HAVE AN INPUT FILE? (sys.argv[1] IS THE YASARA PROCESS ID)
# IF NO INPUT FILE ID IS GIVEN, THE PLUGIN IS MOST LIKELY RUN MANUALLY TO CHECK FOR STARTUP ERRORS
request="CheckIfDisabled"
if (len(sys.argv)>=2):
  inputfilename=os.path.join(plugin.path,"dat"+os.sep+"input_"+sys.argv[1]+".txt")
  if (os.path.exists(inputfilename)):
    # PROCESS INPUT FILE
    input=open(inputfilename).readlines()
    for line in input:
      line=line.rstrip()
      if (line[:8]=="Request:"):
        # REMEMBER PLUGIN REQUEST
        request=line[9:]
      elif (line[:8]=="License:"):
        # REMEMBER LICENSE DATA
        line=line[9:].split()
        serialnumber=line[0]
        stage=line[3]
        # GET VERSION NUMBER, CONSIDERING ALSO yasara.ver TO AVOID PROBLEMS IF A HOTFIX WAS APPLIED
        version=line[2]
        versionfilename=".."+os.sep+"yasara.ver"
        if (os.path.exists(versionfilename)):
          version2=open(versionfilename).read().strip()
          pos=version2.find('_')
          if (pos!=-1): version2=version2[:pos]
          if (versionint(version2)<versionint(version)):
            version=version2
        # GET OWNER
        owner=container()
        owner.email=line[4]
        owner.firstname=line[5]
        if (len(line)==6): owner.familyname="Anonymous"
        else: owner.familyname=line[6]
      elif (line[:8]=="WorkDir:"):
        workdir=line[9:]
      elif (line[:10]=="Selection:"):
        # ADD A NEW SELECTION (SELECTIONS ARE STORED IN input.txt IN REVERSED ORDER)
        selection=[sel_descriptor()]+selection
      # ADD TO CURRENT SELECTION
      elif (line[:7]=="  Atom:"):
        selection[0].addatom(line[8:])
      elif (line[:10]=="  Residue:"):
        selection[0].addresidue(line[11:])
      elif (line[:11]=="  Molecule:"):
        selection[0].addmolecule(line[12:])
      elif (line[:9]=="  Object:"):
        selection[0].addobject(line[10:])
      elif (line[:7]=="  Text:"):
        selection[0].addtext(line[8:])
      elif (line[:9]=="  Number:"):
        selection[0].addnumber(float(line[10:]))
      elif (line[:8]=="  Color:"):
        selection[0].color=line[8:].strip()
      elif (line[:11]=="  CheckBox:"):
        selection[0].addcheckbox(line[12:])
      elif (line[:14]=="  RadioButton:"):
        selection[0].addradiobutton(line[15:])
      elif (line[:12]=="  ListEntry:"):
        selection[0].addlistentry(line[13:])
      elif (line[:11]=="  Filename:"):
        selection[0].addfilename(line[12:].strip())
    os.remove(inputfilename)
selections=len(selection)
# LOAD PERSISTENT yasara.storage FROM A PREVIOUS RUN
storage=None
if (request not in ["None","CheckIfDisabled"]): storage=runretval("LoadStorage",1)
# RETURN TO THE PLUGIN

# DEPRECATED COMMANDS, KEEP PYTHON WRAPPERS FOR BACKWARDS COMPATIBILITY:
# SINCE 2017-02:
def Renumber(first=None): Number(first=None)
def RenumberAll(first=None): NumberAll(first)
def RenumberObj(selection1, first=None): NumberObj(selection1, first)
def RenumberRes(selection1, first=None, inscode=None, increment=None): NumberRes(selection1, first, inscode, increment)
def RenumberAtom(selection1, first=None): NumberAtom(selection1, first)


#  ======================================================================
#                Y A S A R A   F U N C T I O N   G R O U P
#  ======================================================================

# SET/GET ACCELERATION OF ATOMS (ALL OR SELECTED)
# ===============================================
def Accel(x=None, y=None, z=None):
  command='Accel '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET ACCELERATION OF ATOMS (ALL)
# ===================================
def AccelAll(x=None, y=None, z=None):
  command='AccelAll '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET ACCELERATION OF ATOMS (OBJECT)
# ======================================
def AccelObj(selection1, x=None, y=None, z=None):
  command='AccelObj '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET ACCELERATION OF ATOMS (MOLECULE)
# ========================================
def AccelMol(selection1, x=None, y=None, z=None):
  command='AccelMol '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET ACCELERATION OF ATOMS (RESIDUE)
# =======================================
def AccelRes(selection1, x=None, y=None, z=None):
  command='AccelRes '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET ACCELERATION OF ATOMS (ATOM)
# ====================================
def AccelAtom(selection1, x=None, y=None, z=None):
  command='AccelAtom '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# ADD ANGLE TO FORCE FIELD
# ========================
def AddAngle(selection1, selection2, selection3, Min=None, bfc=None):
  command='AddAngle '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  command+=selstr(selection3)+','
  if (Min!=None): command+='Min='+cstr(Min)+','
  if (bfc!=None): command+='BFC='+cstr(bfc)+','
  return(runretval(command[:-1],retvalused()))

# ADD COVALENT BONDS
# ==================
def AddBond(selection1, selection2, order=None, update=None, lenmax=None):
  command='AddBond '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (order!=None): command+='Order='+cstr(order)+','
  if (update!=None): command+='Update='+cstr(update)+','
  if (lenmax!=None): command+='LenMax='+cstr(lenmax)+','
  return(runretval(command[:-1],retvalused()))

# ADD N/C-TERMINAL CAPPING GROUPS (ALL OR SELECTED)
# =================================================
def AddCap(Type=None, location=None):
  command='AddCap '
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (location!=None): command+='Location='+cstr(location)+','
  return(runretval(command[:-1],retvalused()))

# ADD N/C-TERMINAL CAPPING GROUPS (ALL)
# =====================================
def AddCapAll(Type=None, location=None):
  command='AddCapAll '
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (location!=None): command+='Location='+cstr(location)+','
  return(runretval(command[:-1],retvalused()))

# ADD N/C-TERMINAL CAPPING GROUPS (OBJECT)
# ========================================
def AddCapObj(selection1, Type=None, location=None):
  command='AddCapObj '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (location!=None): command+='Location='+cstr(location)+','
  return(runretval(command[:-1],retvalused()))

# ADD DIHEDRAL TO FORCE FIELD
# ===========================
def AddDihedral(selection1, selection2, selection3, selection4, barrier=None, period=None, phase=None):
  command='AddDihedral '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  command+=selstr(selection3)+','
  command+=selstr(selection4)+','
  if (barrier!=None): command+='Barrier='+cstr(barrier)+','
  if (period!=None): command+='Period='+cstr(period)+','
  if (phase!=None): command+='Phase='+cstr(phase)+','
  return(runretval(command[:-1],retvalused()))

# SUM ATOM DISPLACEMENTS TO CALCULATE CROSS-CORRELATION COEFFICIENTS (MOLECULE)
# =============================================================================
def AddDispMol(selection1, selection2):
  command='AddDispMol '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  return(runretval(command[:-1],retvalused()))

# SUM ATOM DISPLACEMENTS TO CALCULATE CROSS-CORRELATION COEFFICIENTS (RESIDUE)
# ============================================================================
def AddDispRes(selection1, selection2):
  command='AddDispRes '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  return(runretval(command[:-1],retvalused()))

# SUM ATOM DISPLACEMENTS TO CALCULATE CROSS-CORRELATION COEFFICIENTS (ATOM)
# =========================================================================
def AddDispAtom(selection1, selection2):
  command='AddDispAtom '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  return(runretval(command[:-1],retvalused()))

# ADD TO ENVIRONMENT FOR SURFACE CALCULATIONS (ALL OR SELECTED)
# =============================================================
def AddEnv():
  command='AddEnv '
  return(runretval(command[:-1],retvalused()))

# ADD TO ENVIRONMENT FOR SURFACE CALCULATIONS (ALL)
# =================================================
def AddEnvAll():
  command='AddEnvAll '
  return(runretval(command[:-1],retvalused()))

# ADD TO ENVIRONMENT FOR SURFACE CALCULATIONS (OBJECT)
# ====================================================
def AddEnvObj(selection1):
  command='AddEnvObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# ADD TO ENVIRONMENT FOR SURFACE CALCULATIONS (MOLECULE)
# ======================================================
def AddEnvMol(selection1):
  command='AddEnvMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# ADD TO ENVIRONMENT FOR SURFACE CALCULATIONS (RESIDUE)
# =====================================================
def AddEnvRes(selection1):
  command='AddEnvRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# ADD TO ENVIRONMENT FOR SURFACE CALCULATIONS (ATOM)
# ==================================================
def AddEnvAtom(selection1):
  command='AddEnvAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# ADD ELECTROSTATIC FIELD
# =======================
def AddESF(x=None, y=None, z=None):
  command='AddESF '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# ADD MISSING HYDROGENS (ALL OR SELECTED)
# =======================================
def AddHyd(number=None, update=None):
  command='AddHyd '
  if (number!=None): command+='Number='+cstr(number)+','
  if (update!=None): command+='Update='+cstr(update)+','
  return(runretval(command[:-1],retvalused()))

# ADD MISSING HYDROGENS (ALL)
# ===========================
def AddHydAll(number=None, update=None):
  command='AddHydAll '
  if (number!=None): command+='Number='+cstr(number)+','
  if (update!=None): command+='Update='+cstr(update)+','
  return(runretval(command[:-1],retvalused()))

# ADD MISSING HYDROGENS (OBJECT)
# ==============================
def AddHydObj(selection1, number=None, update=None):
  command='AddHydObj '
  command+=selstr(selection1)+','
  if (number!=None): command+='Number='+cstr(number)+','
  if (update!=None): command+='Update='+cstr(update)+','
  return(runretval(command[:-1],retvalused()))

# ADD MISSING HYDROGENS (MOLECULE)
# ================================
def AddHydMol(selection1, number=None, update=None):
  command='AddHydMol '
  command+=selstr(selection1)+','
  if (number!=None): command+='Number='+cstr(number)+','
  if (update!=None): command+='Update='+cstr(update)+','
  return(runretval(command[:-1],retvalused()))

# ADD MISSING HYDROGENS (RESIDUE)
# ===============================
def AddHydRes(selection1, number=None, update=None):
  command='AddHydRes '
  command+=selstr(selection1)+','
  if (number!=None): command+='Number='+cstr(number)+','
  if (update!=None): command+='Update='+cstr(update)+','
  return(runretval(command[:-1],retvalused()))

# ADD MISSING HYDROGENS (ATOM)
# ============================
def AddHydAtom(selection1, number=None, update=None):
  command='AddHydAtom '
  command+=selstr(selection1)+','
  if (number!=None): command+='Number='+cstr(number)+','
  if (update!=None): command+='Update='+cstr(update)+','
  return(runretval(command[:-1],retvalused()))

# SUM ATOM POSITIONS TO CALCULATE AVERAGE AND STANDARD DEVIATION (MOLECULE)
# =========================================================================
def AddPosMol(selection1):
  command='AddPosMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SUM ATOM POSITIONS TO CALCULATE AVERAGE AND STANDARD DEVIATION (RESIDUE)
# ========================================================================
def AddPosRes(selection1):
  command='AddPosRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SUM ATOM POSITIONS TO CALCULATE AVERAGE AND STANDARD DEVIATION (ATOM)
# =====================================================================
def AddPosAtom(selection1):
  command='AddPosAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# ADD TERMINAL RESIDUE
# ====================
def AddRes(name, selection1, omega=None, phi=None, psi=None, tau=None, end=None, isomer=None):
  command='AddRes '
  command+='Name='+cstr(name)+','
  command+=selstr(selection1)+','
  if (omega!=None): command+='Omega='+cstr(omega)+','
  if (phi!=None): command+='Phi='+cstr(phi)+','
  if (psi!=None): command+='Psi='+cstr(psi)+','
  if (tau!=None): command+='Tau='+cstr(tau)+','
  if (end!=None): command+='End='+cstr(end)+','
  if (isomer!=None): command+='Isomer='+cstr(isomer)+','
  return(runretval(command[:-1],retvalused()))

# ADD TERMINAL RESIDUE
# ====================
# THIS IS ALTERNATIVE 2, WITH DIFFERENT PARAMETERS
def AddRes2(name, selection1, epsilon=None, zeta=None, alpha=None, beta=None, gamma=None, end=None):
  command='AddRes '
  command+='Name='+cstr(name)+','
  command+=selstr(selection1)+','
  if (epsilon!=None): command+='Epsilon='+cstr(epsilon)+','
  if (zeta!=None): command+='Zeta='+cstr(zeta)+','
  if (alpha!=None): command+='Alpha='+cstr(alpha)+','
  if (beta!=None): command+='Beta='+cstr(beta)+','
  if (gamma!=None): command+='Gamma='+cstr(gamma)+','
  if (end!=None): command+='End='+cstr(end)+','
  return(runretval(command[:-1],retvalused()))

# ADD BOND OR POSITION RESTRAINT TO FORCE FIELD
# =============================================
def AddSpring(selection1, selection2, len=None, sfc=None):
  command='AddSpring '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (len!=None): command+='Len='+cstr(len)+','
  if (sfc!=None): command+='SFC='+cstr(sfc)+','
  return(runretval(command[:-1],retvalused()))

# ADD CELLS TO TABLE
# ==================
def Tabulate(value):
  command='Tabulate '
  command+='Value='+cstr(value)+','
  return(runretval(command[:-1],retvalused()))

# ADD C-TERMINAL OXYGENS (ALL OR SELECTED)
# ========================================
def AddTer():
  command='AddTer '
  return(runretval(command[:-1],retvalused()))

# ADD C-TERMINAL OXYGENS (ALL)
# ============================
def AddTerAll():
  command='AddTerAll '
  return(runretval(command[:-1],retvalused()))

# ADD C-TERMINAL OXYGENS (OBJECT)
# ===============================
def AddTerObj(selection1):
  command='AddTerObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# ADD OBJECTS TO THE SOUP (ALL OR SELECTED)
# =========================================
def Add():
  command='Add '
  return(runretval(command[:-1],retvalused()))

# ADD OBJECTS TO THE SOUP (ALL)
# =============================
def AddAll():
  command='AddAll '
  return(runretval(command[:-1],retvalused()))

# ADD OBJECTS TO THE SOUP (OBJECT)
# ================================
def AddObj(selection1):
  command='AddObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# ALIGN MULTIPLE OBJECTS (ALL OR SELECTED)
# ========================================
def AlignMulti(parameter=None):
  command='AlignMulti '
  if (parameter!=None): command+='Parameter='+cstr(parameter)+','
  return(runretval(command[:-1],retvalused()))

# ALIGN MULTIPLE OBJECTS (ALL)
# ============================
def AlignMultiAll(parameter=None):
  command='AlignMultiAll '
  if (parameter!=None): command+='Parameter='+cstr(parameter)+','
  return(runretval(command[:-1],retvalused()))

# ALIGN MULTIPLE OBJECTS (OBJECT)
# ===============================
def AlignMultiObj(selection1, parameter=None):
  command='AlignMultiObj '
  command+=selstr(selection1)+','
  if (parameter!=None): command+='Parameter='+cstr(parameter)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET ALIGNMENT PARAMETERS
# ============================
def AlignPar(dismax=None, anglemax=None, lenmin=None, gapopen=None, gapextend=None, overhang=None):
  command='AlignPar '
  if (dismax!=None): command+='DisMax='+cstr(dismax)+','
  if (anglemax!=None): command+='AngleMax='+cstr(anglemax)+','
  if (lenmin!=None): command+='LenMin='+cstr(lenmin)+','
  if (gapopen!=None): command+='GapOpen='+cstr(gapopen)+','
  if (gapextend!=None): command+='GapExtend='+cstr(gapextend)+','
  if (overhang!=None): command+='Overhang='+cstr(overhang)+','
  return(runretval(command[:-1],retvalused()))

# ALIGN SIMILAR PROTEINS FROM THE PDB
# ===================================
def AlignPDBMol(selection1, method=None, structures=None, coverage=None, seqidmax=None, filename=None, format=None):
  command='AlignPDBMol '
  command+=selstr(selection1)+','
  if (method!=None): command+='Method='+cstr(method)+','
  if (structures!=None): command+='Structures='+cstr(structures)+','
  if (coverage!=None): command+='Coverage='+cstr(coverage)+','
  if (seqidmax!=None): command+='SeqIdMax='+cstr(seqidmax)+','
  if (filename!=None): command+='Filename='+cstr(filename)+','
  if (format!=None): command+='Format='+cstr(format)+','
  return(runretval(command[:-1],retvalused()))

# ALIGN ATOMS
# ===========
def AlignAtom(selection1, selection2, method=None, matchelement=None, matchname=None, matchbonds=None, matchbondorders=None, matchsecstr=None, dismax=None):
  command='AlignAtom '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (method!=None): command+='Method='+cstr(method)+','
  if (matchelement!=None): command+='MatchElement='+cstr(matchelement)+','
  if (matchname!=None): command+='MatchName='+cstr(matchname)+','
  if (matchbonds!=None): command+='MatchBonds='+cstr(matchbonds)+','
  if (matchbondorders!=None): command+='MatchBondOrders='+cstr(matchbondorders)+','
  if (matchsecstr!=None): command+='MatchSecStr='+cstr(matchsecstr)+','
  if (dismax!=None): command+='DisMax='+cstr(dismax)+','
  return(runretval(command[:-1],retvalused()))

# ALIGN OBJECTS AND MOLECULES (OBJECT)
# ====================================
def AlignObj(selection1, selection2, method=None, parameter=None, results=None, copyresnum=None):
  command='AlignObj '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (method!=None): command+='Method='+cstr(method)+','
  if (parameter!=None): command+='Parameter='+cstr(parameter)+','
  if (results!=None): command+='Results='+cstr(results)+','
  if (copyresnum!=None): command+='CopyResNum='+cstr(copyresnum)+','
  return(runretval(command[:-1],retvalused()))

# ALIGN OBJECTS AND MOLECULES (MOLECULE)
# ======================================
def AlignMol(selection1, selection2, method=None, parameter=None, results=None, copyresnum=None):
  command='AlignMol '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (method!=None): command+='Method='+cstr(method)+','
  if (parameter!=None): command+='Parameter='+cstr(parameter)+','
  if (results!=None): command+='Results='+cstr(results)+','
  if (copyresnum!=None): command+='CopyResNum='+cstr(copyresnum)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET ANGLE BETWEEN ATOMS
# ===========================
def Angle(selection1, selection2, selection3, bound=None, set=None):
  command='Angle '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  command+=selstr(selection3)+','
  if (bound!=None): command+='bound='+cstr(bound)+','
  if (set!=None): command+='set='+cstr(set)+','
  return(runretval(command[:-1],retvalused()))

# GET ANGLE BETWEEN TWO VECTORS
# =============================
def AngleVec(x1=None, y1=None, z1=None, x2=None, y2=None, z2=None):
  command='AngleVec '
  if (x1!=None): command+='X1='+cstr(x1)+','
  if (y1!=None): command+='Y1='+cstr(y1)+','
  if (z1!=None): command+='Z1='+cstr(z1)+','
  if (x2!=None): command+='X2='+cstr(x2)+','
  if (y2!=None): command+='Y2='+cstr(y2)+','
  if (z2!=None): command+='Z2='+cstr(z2)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# ANIMATE APPEARANCE AND DISAPPEARANCE OF IMAGES
# ==============================================
def AnimateImage(selection1, enter=None, rest=None, leave=None, steps=None):
  command='AnimateImage '
  command+=selstr(selection1)+','
  if (enter!=None): command+='Enter='+cstr(enter)+','
  if (rest!=None): command+='Rest='+cstr(rest)+','
  if (leave!=None): command+='Leave='+cstr(leave)+','
  if (steps!=None): command+='Steps='+cstr(steps)+','
  return(runretval(command[:-1],retvalused()))

# ANIMATE WINDOWS
# ===============
def AnimateWin(Type):
  command='AnimateWin '
  command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# SET SIMULATED ANNEALING STEPS
# =============================
def AnnealSteps(number):
  command='AnnealSteps '
  command+='Number='+cstr(number)+','
  return(runretval(command[:-1],retvalused()))

# SWITCH ANTIALIASING ON/OFF
# ==========================
def Antialias(level):
  command='Antialias '
  command+='Level='+cstr(level)+','
  return(runretval(command[:-1],retvalused()))

# APPLY MACRO TO MULTIPLE TARGETS OR FILES
# ========================================
def ApplyMacro(filename, targets, remove=None, newextension=None):
  command='ApplyMacro '
  command+='Filename='+cstr(filename)+','
  command+='Targets='+cstr(targets)+','
  if (remove!=None): command+='Remove='+cstr(remove)+','
  if (newextension!=None): command+='NewExtension='+cstr(newextension)+','
  return(runretval(command[:-1],retvalused()))

# SWITCH PLASMA INSIDE ATOMS ON/OFF
# =================================
def AtomPlasma(flag):
  command='AtomPlasma '
  command+='Flag='+cstr(flag)+','
  return(runretval(command[:-1],retvalused()))

# SET SIZE OF ATOMS
# =================
def AtomSize(radius):
  command='AtomSize '
  command+='Radius='+cstr(radius)+','
  return(runretval(command[:-1],retvalused()))

# SWITCH ELEMENT SYMBOL INSIDE ATOMS ON/OFF
# =========================================
def AtomSymbol(flag):
  command='AtomSymbol '
  command+='Flag='+cstr(flag)+','
  return(runretval(command[:-1],retvalused()))

# SET TEXTURE STYLE OF ATOMS
# ==========================
def AtomTexture(Type):
  command='AtomTexture '
  command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# MOVE IMAGES AUTOMATICALLY
# =========================
def AutoMoveImage(selection1, x=None, y=None, width=None, height=None, alpha=None, steps=None, cycle=None, zoom3d=None):
  command='AutoMoveImage '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (width!=None): command+='Width='+cstr(width)+','
  if (height!=None): command+='Height='+cstr(height)+','
  if (alpha!=None): command+='Alpha='+cstr(alpha)+','
  if (steps!=None): command+='Steps='+cstr(steps)+','
  if (cycle!=None): command+='Cycle='+cstr(cycle)+','
  if (zoom3d!=None): command+='Zoom3D='+cstr(zoom3d)+','
  return(runretval(command[:-1],retvalused()))

# POSITION AND ORIENT OBJECTS OR SCENE AUTOMATICALLY IN A GIVEN NUMBER OF STEPS (ALL OR SELECTED)
# ===============================================================================================
def AutoPosOri(x, y, z, alpha, beta, gamma, steps=None, wait=None):
  command='AutoPosOri '
  command+='X='+cstr(x)+','
  command+='Y='+cstr(y)+','
  command+='Z='+cstr(z)+','
  command+='Alpha='+cstr(alpha)+','
  command+='Beta='+cstr(beta)+','
  command+='Gamma='+cstr(gamma)+','
  if (steps!=None): command+='Steps='+cstr(steps)+','
  if (wait!=None): command+='Wait='+cstr(wait)+','
  return(runretval(command[:-1],retvalused()))

# POSITION AND ORIENT OBJECTS OR SCENE AUTOMATICALLY IN A GIVEN NUMBER OF STEPS (ALL)
# ===================================================================================
def AutoPosOriAll(x, y, z, alpha, beta, gamma, steps=None, wait=None):
  command='AutoPosOriAll '
  command+='X='+cstr(x)+','
  command+='Y='+cstr(y)+','
  command+='Z='+cstr(z)+','
  command+='Alpha='+cstr(alpha)+','
  command+='Beta='+cstr(beta)+','
  command+='Gamma='+cstr(gamma)+','
  if (steps!=None): command+='Steps='+cstr(steps)+','
  if (wait!=None): command+='Wait='+cstr(wait)+','
  return(runretval(command[:-1],retvalused()))

# POSITION AND ORIENT OBJECTS OR SCENE AUTOMATICALLY IN A GIVEN NUMBER OF STEPS (OBJECT)
# ======================================================================================
def AutoPosOriObj(selection1, x, y, z, alpha, beta, gamma, steps=None, wait=None):
  command='AutoPosOriObj '
  command+=selstr(selection1)+','
  command+='X='+cstr(x)+','
  command+='Y='+cstr(y)+','
  command+='Z='+cstr(z)+','
  command+='Alpha='+cstr(alpha)+','
  command+='Beta='+cstr(beta)+','
  command+='Gamma='+cstr(gamma)+','
  if (steps!=None): command+='Steps='+cstr(steps)+','
  if (wait!=None): command+='Wait='+cstr(wait)+','
  return(runretval(command[:-1],retvalused()))

# POSITION OBJECTS OR SCENE AUTOMATICALLY IN A GIVEN NUMBER OF STEPS (ALL OR SELECTED)
# ====================================================================================
def AutoPos(x=None, y=None, z=None, steps=None, wait=None):
  command='AutoPos '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  if (steps!=None): command+='Steps='+cstr(steps)+','
  if (wait!=None): command+='Wait='+cstr(wait)+','
  return(runretval(command[:-1],retvalused()))

# POSITION OBJECTS OR SCENE AUTOMATICALLY IN A GIVEN NUMBER OF STEPS (ALL)
# ========================================================================
def AutoPosAll(x=None, y=None, z=None, steps=None, wait=None):
  command='AutoPosAll '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  if (steps!=None): command+='Steps='+cstr(steps)+','
  if (wait!=None): command+='Wait='+cstr(wait)+','
  return(runretval(command[:-1],retvalused()))

# POSITION OBJECTS OR SCENE AUTOMATICALLY IN A GIVEN NUMBER OF STEPS (OBJECT)
# ===========================================================================
def AutoPosObj(selection1, x=None, y=None, z=None, steps=None, wait=None):
  command='AutoPosObj '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  if (steps!=None): command+='Steps='+cstr(steps)+','
  if (wait!=None): command+='Wait='+cstr(wait)+','
  return(runretval(command[:-1],retvalused()))

# MOVE OBJECTS OR SCENE AUTOMATICALLY (ALL OR SELECTED)
# =====================================================
def AutoMove(x=None, y=None, z=None):
  command='AutoMove '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# MOVE OBJECTS OR SCENE AUTOMATICALLY (ALL)
# =========================================
def AutoMoveAll(x=None, y=None, z=None):
  command='AutoMoveAll '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# MOVE OBJECTS OR SCENE AUTOMATICALLY (OBJECT)
# ============================================
def AutoMoveObj(selection1, x=None, y=None, z=None):
  command='AutoMoveObj '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# ORIENT OBJECTS OR SCENE AUTOMATICALLY IN A GIVEN NUMBER OF STEPS (ALL OR SELECTED)
# ==================================================================================
def AutoOri(alpha, beta, gamma, steps=None, wait=None):
  command='AutoOri '
  command+='Alpha='+cstr(alpha)+','
  command+='Beta='+cstr(beta)+','
  command+='Gamma='+cstr(gamma)+','
  if (steps!=None): command+='Steps='+cstr(steps)+','
  if (wait!=None): command+='Wait='+cstr(wait)+','
  return(runretval(command[:-1],retvalused()))

# ORIENT OBJECTS OR SCENE AUTOMATICALLY IN A GIVEN NUMBER OF STEPS (ALL)
# ======================================================================
def AutoOriAll(alpha, beta, gamma, steps=None, wait=None):
  command='AutoOriAll '
  command+='Alpha='+cstr(alpha)+','
  command+='Beta='+cstr(beta)+','
  command+='Gamma='+cstr(gamma)+','
  if (steps!=None): command+='Steps='+cstr(steps)+','
  if (wait!=None): command+='Wait='+cstr(wait)+','
  return(runretval(command[:-1],retvalused()))

# ORIENT OBJECTS OR SCENE AUTOMATICALLY IN A GIVEN NUMBER OF STEPS (OBJECT)
# =========================================================================
def AutoOriObj(selection1, alpha, beta, gamma, steps=None, wait=None):
  command='AutoOriObj '
  command+=selstr(selection1)+','
  command+='Alpha='+cstr(alpha)+','
  command+='Beta='+cstr(beta)+','
  command+='Gamma='+cstr(gamma)+','
  if (steps!=None): command+='Steps='+cstr(steps)+','
  if (wait!=None): command+='Wait='+cstr(wait)+','
  return(runretval(command[:-1],retvalused()))

# ROTATE OBJECTS OR SCENE AUTOMATICALLY (ALL OR SELECTED)
# =======================================================
def AutoRotate(x=None, y=None, z=None):
  command='AutoRotate '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# ROTATE OBJECTS OR SCENE AUTOMATICALLY (ALL)
# ===========================================
def AutoRotateAll(x=None, y=None, z=None):
  command='AutoRotateAll '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# ROTATE OBJECTS OR SCENE AUTOMATICALLY (OBJECT)
# ==============================================
def AutoRotateObj(selection1, x=None, y=None, z=None):
  command='AutoRotateObj '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# AVERAGE ATOM POSITIONS (MOLECULE)
# =================================
def AveragePosMol(selection1):
  command='AveragePosMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# AVERAGE ATOM POSITIONS (RESIDUE)
# ================================
def AveragePosRes(selection1):
  command='AveragePosRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# AVERAGE ATOM POSITIONS (ATOM)
# =============================
def AveragePosAtom(selection1):
  command='AveragePosAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SET BALL AND STICK RADII IN BALLS&STICKS
# ========================================
def BallStickRadius(ball=None, stick=None):
  command='BallStickRadius '
  if (ball!=None): command+='Ball='+cstr(ball)+','
  if (stick!=None): command+='Stick='+cstr(stick)+','
  return(runretval(command[:-1],retvalused()))

# STYLE ATOMS AS BALLS&STICKS (ALL OR SELECTED)
# =============================================
def BallStick():
  command='BallStick '
  return(runretval(command[:-1],retvalused()))

# STYLE ATOMS AS BALLS&STICKS (ALL)
# =================================
def BallStickAll():
  command='BallStickAll '
  return(runretval(command[:-1],retvalused()))

# STYLE ATOMS AS BALLS&STICKS (OBJECT)
# ====================================
def BallStickObj(selection1):
  command='BallStickObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# STYLE ATOMS AS BALLS&STICKS (MOLECULE)
# ======================================
def BallStickMol(selection1):
  command='BallStickMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# STYLE ATOMS AS BALLS&STICKS (RESIDUE)
# =====================================
def BallStickRes(selection1):
  command='BallStickRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# STYLE ATOMS AS BALLS&STICKS (ATOM)
# ==================================
def BallStickAtom(selection1):
  command='BallStickAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# STYLE ATOMS AS BALLS (ALL OR SELECTED)
# ======================================
def Ball():
  command='Ball '
  return(runretval(command[:-1],retvalused()))

# STYLE ATOMS AS BALLS (ALL)
# ==========================
def BallAll():
  command='BallAll '
  return(runretval(command[:-1],retvalused()))

# STYLE ATOMS AS BALLS (OBJECT)
# =============================
def BallObj(selection1):
  command='BallObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# STYLE ATOMS AS BALLS (MOLECULE)
# ===============================
def BallMol(selection1):
  command='BallMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# STYLE ATOMS AS BALLS (RESIDUE)
# ==============================
def BallRes(selection1):
  command='BallRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# STYLE ATOMS AS BALLS (ATOM)
# ===========================
def BallAtom(selection1):
  command='BallAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE BINDING ENERGIES
# ==========================
def BindEnergyObj(selection1):
  command='BindEnergyObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE B-FACTOR (ALL OR SELECTED)
# ======================================
def BFactor(value=None):
  command='BFactor '
  if (value!=None): command+='value='+cstr(value)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE B-FACTOR (ALL)
# ==========================
def BFactorAll(value=None):
  command='BFactorAll '
  if (value!=None): command+='value='+cstr(value)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE B-FACTOR (OBJECT)
# =============================
def BFactorObj(selection1, value=None):
  command='BFactorObj '
  command+=selstr(selection1)+','
  if (value!=None): command+='value='+cstr(value)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE B-FACTOR (MOLECULE)
# ===============================
def BFactorMol(selection1, value=None):
  command='BFactorMol '
  command+=selstr(selection1)+','
  if (value!=None): command+='value='+cstr(value)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE B-FACTOR (RESIDUE)
# ==============================
def BFactorRes(selection1, value=None):
  command='BFactorRes '
  command+=selstr(selection1)+','
  if (value!=None): command+='value='+cstr(value)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE B-FACTOR (ATOM)
# ===========================
def BFactorAtom(selection1, value=None):
  command='BFactorAtom '
  command+=selstr(selection1)+','
  if (value!=None): command+='value='+cstr(value)+','
  return(runretval(command[:-1],retvalused()))

# SORT DISTANCES INTO BINS TO CALCULATE THE RADIAL DISTRIBUTION FUNCTION
# ======================================================================
def BinDistance(selection1, selection2, bins=None, binwidth=None):
  command='BinDistance '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (bins!=None): command+='Bins='+cstr(bins)+','
  if (binwidth!=None): command+='BinWidth='+cstr(binwidth)+','
  return(runretval(command[:-1],retvalused()))

# BLAST PROTEIN SEQUENCE (ALL OR SELECTED)
# ========================================
def BLAST(database=None, passes=None, evalue=None, hits=None, order=None, filename=None, format=None):
  command='BLAST '
  if (database!=None): command+='Database='+cstr(database)+','
  if (passes!=None): command+='Passes='+cstr(passes)+','
  if (evalue!=None): command+='EValue='+cstr(evalue)+','
  if (hits!=None): command+='Hits='+cstr(hits)+','
  if (order!=None): command+='Order='+cstr(order)+','
  if (filename!=None): command+='Filename='+cstr(filename)+','
  if (format!=None): command+='Format='+cstr(format)+','
  return(runretval(command[:-1],retvalused()))

# BLAST PROTEIN SEQUENCE (ALL)
# ============================
def BLASTAll(database=None, passes=None, evalue=None, hits=None, order=None, filename=None, format=None):
  command='BLASTAll '
  if (database!=None): command+='Database='+cstr(database)+','
  if (passes!=None): command+='Passes='+cstr(passes)+','
  if (evalue!=None): command+='EValue='+cstr(evalue)+','
  if (hits!=None): command+='Hits='+cstr(hits)+','
  if (order!=None): command+='Order='+cstr(order)+','
  if (filename!=None): command+='Filename='+cstr(filename)+','
  if (format!=None): command+='Format='+cstr(format)+','
  return(runretval(command[:-1],retvalused()))

# BLAST PROTEIN SEQUENCE (OBJECT)
# ===============================
def BLASTObj(selection1, database=None, passes=None, evalue=None, hits=None, order=None, filename=None, format=None):
  command='BLASTObj '
  command+=selstr(selection1)+','
  if (database!=None): command+='Database='+cstr(database)+','
  if (passes!=None): command+='Passes='+cstr(passes)+','
  if (evalue!=None): command+='EValue='+cstr(evalue)+','
  if (hits!=None): command+='Hits='+cstr(hits)+','
  if (order!=None): command+='Order='+cstr(order)+','
  if (filename!=None): command+='Filename='+cstr(filename)+','
  if (format!=None): command+='Format='+cstr(format)+','
  return(runretval(command[:-1],retvalused()))

# BLAST PROTEIN SEQUENCE (MOLECULE)
# =================================
def BLASTMol(selection1, database=None, passes=None, evalue=None, hits=None, order=None, filename=None, format=None):
  command='BLASTMol '
  command+=selstr(selection1)+','
  if (database!=None): command+='Database='+cstr(database)+','
  if (passes!=None): command+='Passes='+cstr(passes)+','
  if (evalue!=None): command+='EValue='+cstr(evalue)+','
  if (hits!=None): command+='Hits='+cstr(hits)+','
  if (order!=None): command+='Order='+cstr(order)+','
  if (filename!=None): command+='Filename='+cstr(filename)+','
  if (format!=None): command+='Format='+cstr(format)+','
  return(runretval(command[:-1],retvalused()))

# BLAST PROTEIN SEQUENCE (RESIDUE)
# ================================
def BLASTRes(selection1, database=None, passes=None, evalue=None, hits=None, order=None, filename=None, format=None):
  command='BLASTRes '
  command+=selstr(selection1)+','
  if (database!=None): command+='Database='+cstr(database)+','
  if (passes!=None): command+='Passes='+cstr(passes)+','
  if (evalue!=None): command+='EValue='+cstr(evalue)+','
  if (hits!=None): command+='Hits='+cstr(hits)+','
  if (order!=None): command+='Order='+cstr(order)+','
  if (filename!=None): command+='Filename='+cstr(filename)+','
  if (format!=None): command+='Format='+cstr(format)+','
  return(runretval(command[:-1],retvalused()))

# BOUND VALUE TO INTERVAL
# =======================
def Bound(value, Min=None, Max=None):
  command='Bound '
  command+='Value='+cstr(value)+','
  if (Min!=None): command+='Min='+cstr(Min)+','
  if (Max!=None): command+='Max='+cstr(Max)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SET/GET CELL BOUNDARY
# =====================
def Boundary(Type=None):
  command='Boundary '
  if (Type!=None): command+='Type='+cstr(Type)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SIMULATION BRAKE
# ================
def Brake(speed):
  command='Brake '
  command+='Speed='+cstr(speed)+','
  return(runretval(command[:-1],retvalused()))

# BUILD A BRIDGE BETWEEN TWO ATOMS
# ================================
def BridgeAtom(selection1, selection2, name):
  command='BridgeAtom '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# SET WEB BROWSER
# ===============
def Browser(com):
  command='Browser '
  command+='Command='+cstr(com)+','
  return(runretval(command[:-1],retvalused()))

# BUILD SINGLE ATOM
# =================
def BuildAtom(element, copies=None, selection1=None):
  command='BuildAtom '
  command+='Element='+cstr(element)+','
  if (copies!=None): command+='Copies='+cstr(copies)+','
  if (selection1!=None): command+=selstr(selection1)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# BUILD A GRID OF ATOMS
# =====================
def BuildGrid(element=None, x=None, y=None, z=None, spacing=None):
  command='BuildGrid '
  if (element!=None): command+='Element='+cstr(element)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  if (spacing!=None): command+='Spacing='+cstr(spacing)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# BUILD FUNCTIONAL GROUP
# ======================
def BuildGroup(name):
  command='BuildGroup '
  command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# BUILD CENTRAL OR TERMINAL LOOP
# ==============================
def BuildLoop(selection1, sequence, selection2, structures=None, mutate=None, bumpsum=None, secstr=None):
  command='BuildLoop '
  command+=selstr(selection1)+','
  command+='Sequence='+cstr(sequence)+','
  command+=selstr(selection2)+','
  if (structures!=None): command+='Structures='+cstr(structures)+','
  if (mutate!=None): command+='Mutate='+cstr(mutate)+','
  if (bumpsum!=None): command+='Bumpsum='+cstr(bumpsum)+','
  if (secstr!=None): command+='SecStr='+cstr(secstr)+','
  return(runretval(command[:-1],retvalused()))

# BUILD PEPTIDE OR NUCLEIC ACID CHAIN
# ===================================
def BuildMol(filename, sequence=None, Type=None):
  command='BuildMol '
  command+='Filename='+cstr(filename)+','
  if (sequence!=None): command+='Sequence='+cstr(sequence)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# BUILD SINGLE RESIDUE
# ====================
def BuildRes(name, psi=None, tau=None, center=None, isomer=None, useph=None):
  command='BuildRes '
  command+='Name='+cstr(name)+','
  if (psi!=None): command+='Psi='+cstr(psi)+','
  if (tau!=None): command+='Tau='+cstr(tau)+','
  if (center!=None): command+='Center='+cstr(center)+','
  if (isomer!=None): command+='Isomer='+cstr(isomer)+','
  if (useph!=None): command+='UsepH='+cstr(useph)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# BUILD SINGLE RESIDUE
# ====================
# THIS IS ALTERNATIVE 2, WITH DIFFERENT PARAMETERS
def BuildRes2(name, alpha=None, beta=None, gamma=None, center=None):
  command='BuildRes '
  command+='Name='+cstr(name)+','
  if (alpha!=None): command+='Alpha='+cstr(alpha)+','
  if (beta!=None): command+='Beta='+cstr(beta)+','
  if (gamma!=None): command+='Gamma='+cstr(gamma)+','
  if (center!=None): command+='Center='+cstr(center)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# BUILD MOLECULE FROM SMILES STRING
# =================================
def BuildSMILES(string, sort=None):
  command='BuildSMILES '
  command+='String='+cstr(string)+','
  if (sort!=None): command+='Sort='+cstr(sort)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# BUILD SYMMETRY RELATED RESIDUES
# ===============================
def BuildSymRes(selection1):
  command='BuildSymRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE CAVITY VOLUMES (ALL OR SELECTED)
# ==========================================
def CaviVol(Type=None):
  command='CaviVol '
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE CAVITY VOLUMES (ALL)
# ==============================
def CaviVolAll(Type=None):
  command='CaviVolAll '
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE CAVITY VOLUMES (OBJECT)
# =================================
def CaviVolObj(selection1, Type=None):
  command='CaviVolObj '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE CAVITY VOLUMES (MOLECULE)
# ===================================
def CaviVolMol(selection1, Type=None):
  command='CaviVolMol '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE CAVITY VOLUMES (RESIDUE)
# ==================================
def CaviVolRes(selection1, Type=None):
  command='CaviVolRes '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE CAVITY VOLUMES (ATOM)
# ===============================
def CaviVolAtom(selection1, Type=None):
  command='CaviVolAtom '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# CHANGE WORKING DIRECTORY
# ========================
def CD(noname1, onstartup=None):
  command='CD '
  command+=cstr(noname1)+','
  if (onstartup!=None): command+='OnStartUp='+cstr(onstartup)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET SIMULATION CELL DIMENSIONS
# ==================================
def Cell(x=None, y=None, z=None, alpha=None, beta=None, gamma=None, center=None):
  command='Cell '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  if (alpha!=None): command+='Alpha='+cstr(alpha)+','
  if (beta!=None): command+='Beta='+cstr(beta)+','
  if (gamma!=None): command+='Gamma='+cstr(gamma)+','
  if (center!=None): command+='Center='+cstr(center)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET SIMULATION CELL DIMENSIONS
# ==================================
# THIS IS ALTERNATIVE 2, WITH DIFFERENT PARAMETERS
def CellAuto(extension=None, shape=None, selection1=None):
  command='Cell Auto,'
  if (extension!=None): command+='Extension='+cstr(extension)+','
  if (shape!=None): command+='Shape='+cstr(shape)+','
  if (selection1!=None): command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET SIMULATION CELL DIMENSIONS
# ==================================
# THIS IS ALTERNATIVE 3, WITH DIFFERENT PARAMETERS
def CellCrystal(selection1):
  command='Cell Crystal,'
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# CENTER ATOMS OR POLYGON MESHES (ALL OR SELECTED)
# ================================================
def Center(coordsys=None):
  command='Center '
  if (coordsys!=None): command+='CoordSys='+cstr(coordsys)+','
  return(runretval(command[:-1],retvalused()))

# CENTER ATOMS OR POLYGON MESHES (ALL)
# ====================================
def CenterAll(coordsys=None):
  command='CenterAll '
  if (coordsys!=None): command+='CoordSys='+cstr(coordsys)+','
  return(runretval(command[:-1],retvalused()))

# CENTER ATOMS OR POLYGON MESHES (OBJECT)
# =======================================
def CenterObj(selection1, coordsys=None):
  command='CenterObj '
  command+=selstr(selection1)+','
  if (coordsys!=None): command+='CoordSys='+cstr(coordsys)+','
  return(runretval(command[:-1],retvalused()))

# CENTER ATOMS OR POLYGON MESHES (MOLECULE)
# =========================================
def CenterMol(selection1, coordsys=None):
  command='CenterMol '
  command+=selstr(selection1)+','
  if (coordsys!=None): command+='CoordSys='+cstr(coordsys)+','
  return(runretval(command[:-1],retvalused()))

# CENTER ATOMS OR POLYGON MESHES (RESIDUE)
# ========================================
def CenterRes(selection1, coordsys=None):
  command='CenterRes '
  command+=selstr(selection1)+','
  if (coordsys!=None): command+='CoordSys='+cstr(coordsys)+','
  return(runretval(command[:-1],retvalused()))

# CENTER ATOMS OR POLYGON MESHES (ATOM)
# =====================================
def CenterAtom(selection1, coordsys=None):
  command='CenterAtom '
  command+=selstr(selection1)+','
  if (coordsys!=None): command+='CoordSys='+cstr(coordsys)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE SUMMED UP CHARGE (ALL OR SELECTED)
# ==============================================
def Charge(e=None):
  command='Charge '
  if (e!=None): command+='e='+cstr(e)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE SUMMED UP CHARGE (ALL)
# ==================================
def ChargeAll(e=None):
  command='ChargeAll '
  if (e!=None): command+='e='+cstr(e)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE SUMMED UP CHARGE (OBJECT)
# =====================================
def ChargeObj(selection1, e=None):
  command='ChargeObj '
  command+=selstr(selection1)+','
  if (e!=None): command+='e='+cstr(e)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE SUMMED UP CHARGE (MOLECULE)
# =======================================
def ChargeMol(selection1, e=None):
  command='ChargeMol '
  command+=selstr(selection1)+','
  if (e!=None): command+='e='+cstr(e)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE SUMMED UP CHARGE (RESIDUE)
# ======================================
def ChargeRes(selection1, e=None):
  command='ChargeRes '
  command+=selstr(selection1)+','
  if (e!=None): command+='e='+cstr(e)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE SUMMED UP CHARGE (ATOM)
# ===================================
def ChargeAtom(selection1, e=None):
  command='ChargeAtom '
  command+=selstr(selection1)+','
  if (e!=None): command+='e='+cstr(e)+','
  return(runretval(command[:-1],retvalused()))

# CHECK STRUCTURE QUALITY (ALL OR SELECTED)
# =========================================
def Check(Type, filename=None):
  command='Check '
  command+='Type='+cstr(Type)+','
  if (filename!=None): command+='Filename='+cstr(filename)+','
  return(runretval(command[:-1],retvalused()))

# CHECK STRUCTURE QUALITY (ALL)
# =============================
def CheckAll(Type, filename=None):
  command='CheckAll '
  command+='Type='+cstr(Type)+','
  if (filename!=None): command+='Filename='+cstr(filename)+','
  return(runretval(command[:-1],retvalused()))

# CHECK STRUCTURE QUALITY (OBJECT)
# ================================
def CheckObj(selection1, Type, filename=None):
  command='CheckObj '
  command+=selstr(selection1)+','
  command+='Type='+cstr(Type)+','
  if (filename!=None): command+='Filename='+cstr(filename)+','
  return(runretval(command[:-1],retvalused()))

# CHECK STRUCTURE QUALITY (RESIDUE)
# =================================
def CheckRes(selection1, Type, filename=None):
  command='CheckRes '
  command+=selstr(selection1)+','
  command+='Type='+cstr(Type)+','
  if (filename!=None): command+='Filename='+cstr(filename)+','
  return(runretval(command[:-1],retvalused()))

# CHECK STRUCTURE QUALITY (ATOM)
# ==============================
def CheckAtom(selection1, Type, filename=None):
  command='CheckAtom '
  command+=selstr(selection1)+','
  command+='Type='+cstr(Type)+','
  if (filename!=None): command+='Filename='+cstr(filename)+','
  return(runretval(command[:-1],retvalused()))

# CLASSIFY RESTRAINTS (ALL OR SELECTED)
# =====================================
def ClassRest(Class, component, number, newclass):
  command='ClassRest '
  command+='Class='+cstr(Class)+','
  command+='Component='+cstr(component)+','
  command+='Number='+cstr(number)+','
  command+='NewClass='+cstr(newclass)+','
  return(runretval(command[:-1],retvalused()))

# CLASSIFY RESTRAINTS (ALL)
# =========================
def ClassRestAll(Class, component, number, newclass):
  command='ClassRestAll '
  command+='Class='+cstr(Class)+','
  command+='Component='+cstr(component)+','
  command+='Number='+cstr(number)+','
  command+='NewClass='+cstr(newclass)+','
  return(runretval(command[:-1],retvalused()))

# CLASSIFY RESTRAINTS (OBJECT)
# ============================
def ClassRestObj(selection1, Class, component, number, newclass):
  command='ClassRestObj '
  command+=selstr(selection1)+','
  command+='Class='+cstr(Class)+','
  command+='Component='+cstr(component)+','
  command+='Number='+cstr(number)+','
  command+='NewClass='+cstr(newclass)+','
  return(runretval(command[:-1],retvalused()))

# CLASSIFY RESTRAINTS (MOLECULE)
# ==============================
def ClassRestMol(selection1, Class, component, number, newclass):
  command='ClassRestMol '
  command+=selstr(selection1)+','
  command+='Class='+cstr(Class)+','
  command+='Component='+cstr(component)+','
  command+='Number='+cstr(number)+','
  command+='NewClass='+cstr(newclass)+','
  return(runretval(command[:-1],retvalused()))

# CLASSIFY RESTRAINTS (RESIDUE)
# =============================
def ClassRestRes(selection1, Class, component, number, newclass):
  command='ClassRestRes '
  command+=selstr(selection1)+','
  command+='Class='+cstr(Class)+','
  command+='Component='+cstr(component)+','
  command+='Number='+cstr(number)+','
  command+='NewClass='+cstr(newclass)+','
  return(runretval(command[:-1],retvalused()))

# CLASSIFY RESTRAINTS (ATOM)
# ==========================
def ClassRestAtom(selection1, Class, component, number, newclass):
  command='ClassRestAtom '
  command+=selstr(selection1)+','
  command+='Class='+cstr(Class)+','
  command+='Component='+cstr(component)+','
  command+='Number='+cstr(number)+','
  command+='NewClass='+cstr(newclass)+','
  return(runretval(command[:-1],retvalused()))

# CLEAN OBJECTS FOR MOLECULAR DYNAMICS SIMULATION (ALL OR SELECTED)
# =================================================================
def Clean(skip=None):
  command='Clean '
  if (skip!=None): command+='Skip='+cstr(skip)+','
  return(runretval(command[:-1],retvalused()))

# CLEAN OBJECTS FOR MOLECULAR DYNAMICS SIMULATION (ALL)
# =====================================================
def CleanAll(skip=None):
  command='CleanAll '
  if (skip!=None): command+='Skip='+cstr(skip)+','
  return(runretval(command[:-1],retvalused()))

# CLEAN OBJECTS FOR MOLECULAR DYNAMICS SIMULATION (OBJECT)
# ========================================================
def CleanObj(selection1, skip=None):
  command='CleanObj '
  command+=selstr(selection1)+','
  if (skip!=None): command+='Skip='+cstr(skip)+','
  return(runretval(command[:-1],retvalused()))

# CLEAR SCENE
# ===========
def Clear():
  command='Clear '
  return(runretval(command[:-1],retvalused()))

# COLOR BONDS
# ===========
def ColorBonds(color):
  command='ColorBonds '
  command+='Color='+cstr(color)+','
  return(runretval(command[:-1],retvalused()))

# COLOR BACKGROUND
# ================
def ColorBG(topleft, bottomleft=None, topright=None, bottomright=None):
  command='ColorBG '
  command+='TopLeft='+cstr(topleft)+','
  if (bottomleft!=None): command+='BottomLeft='+cstr(bottomleft)+','
  if (topright!=None): command+='TopRight='+cstr(topright)+','
  if (bottomright!=None): command+='BottomRight='+cstr(bottomright)+','
  return(runretval(command[:-1],retvalused()))

# SET OVERALL OBJECT INSTANCE COLORS AT A FAR DISTANCE (ALL OR SELECTED)
# ======================================================================
def ColorFar(Type, first, second=None):
  command='ColorFar '
  command+='Type='+cstr(Type)+','
  command+='First='+cstr(first)+','
  if (second!=None): command+='Second='+cstr(second)+','
  return(runretval(command[:-1],retvalused()))

# SET OVERALL OBJECT INSTANCE COLORS AT A FAR DISTANCE (ALL)
# ==========================================================
def ColorFarAll(Type, first, second=None):
  command='ColorFarAll '
  command+='Type='+cstr(Type)+','
  command+='First='+cstr(first)+','
  if (second!=None): command+='Second='+cstr(second)+','
  return(runretval(command[:-1],retvalused()))

# SET OVERALL OBJECT INSTANCE COLORS AT A FAR DISTANCE (OBJECT)
# =============================================================
def ColorFarObj(selection1, Type, first, second=None):
  command='ColorFarObj '
  command+=selstr(selection1)+','
  command+='Type='+cstr(Type)+','
  command+='First='+cstr(first)+','
  if (second!=None): command+='Second='+cstr(second)+','
  return(runretval(command[:-1],retvalused()))

# SET OVERALL OBJECT INSTANCE COLORS AT A FAR DISTANCE (MOLECULE)
# ===============================================================
def ColorFarMol(selection1, Type, first, second=None):
  command='ColorFarMol '
  command+=selstr(selection1)+','
  command+='Type='+cstr(Type)+','
  command+='First='+cstr(first)+','
  if (second!=None): command+='Second='+cstr(second)+','
  return(runretval(command[:-1],retvalused()))

# SET OVERALL OBJECT INSTANCE COLORS AT A FAR DISTANCE (RESIDUE)
# ==============================================================
def ColorFarRes(selection1, Type, first, second=None):
  command='ColorFarRes '
  command+=selstr(selection1)+','
  command+='Type='+cstr(Type)+','
  command+='First='+cstr(first)+','
  if (second!=None): command+='Second='+cstr(second)+','
  return(runretval(command[:-1],retvalused()))

# SET OVERALL OBJECT INSTANCE COLORS AT A FAR DISTANCE (ATOM)
# ===========================================================
def ColorFarAtom(selection1, Type, first, second=None):
  command='ColorFarAtom '
  command+=selstr(selection1)+','
  command+='Type='+cstr(Type)+','
  command+='First='+cstr(first)+','
  if (second!=None): command+='Second='+cstr(second)+','
  return(runretval(command[:-1],retvalused()))

# COLOR FOG
# =========
def ColorFog(color):
  command='ColorFog '
  command+='Color='+cstr(color)+','
  return(runretval(command[:-1],retvalused()))

# COLOR HYDROGEN BONDS
# ====================
def ColorHBo(color=None, alpha=None, inherit=None):
  command='ColorHBo '
  if (color!=None): command+='Color='+cstr(color)+','
  if (alpha!=None): command+='Alpha='+cstr(alpha)+','
  if (inherit!=None): command+='Inherit='+cstr(inherit)+','
  return(runretval(command[:-1],retvalused()))

# COLOR POLYGON MESH
# ==================
def ColorMesh(selection1, color=None):
  command='ColorMesh '
  command+=selstr(selection1)+','
  if (color!=None): command+='Color='+cstr(color)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET DEFAULT COLOR PARAMETERS
# ================================
def ColorPar(scheme, name=None, color=None, value=None):
  command='ColorPar '
  command+='Scheme='+cstr(scheme)+','
  if (name!=None): command+='Name='+cstr(name)+','
  if (color!=None): command+='Color='+cstr(color)+','
  if (value!=None): command+='Value='+cstr(value)+','
  return(runretval(command[:-1],retvalused()))

# COLOR SURFACE (ALL OR SELECTED)
# ===============================
def ColorSurf(Type=None, outcol=None, outalpha=None, incol=None, inalpha=None, specular=None):
  command='ColorSurf '
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (outcol!=None): command+='OutCol='+cstr(outcol)+','
  if (outalpha!=None): command+='OutAlpha='+cstr(outalpha)+','
  if (incol!=None): command+='InCol='+cstr(incol)+','
  if (inalpha!=None): command+='InAlpha='+cstr(inalpha)+','
  if (specular!=None): command+='Specular='+cstr(specular)+','
  return(runretval(command[:-1],retvalused()))

# COLOR SURFACE (ALL)
# ===================
def ColorSurfAll(Type=None, outcol=None, outalpha=None, incol=None, inalpha=None, specular=None):
  command='ColorSurfAll '
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (outcol!=None): command+='OutCol='+cstr(outcol)+','
  if (outalpha!=None): command+='OutAlpha='+cstr(outalpha)+','
  if (incol!=None): command+='InCol='+cstr(incol)+','
  if (inalpha!=None): command+='InAlpha='+cstr(inalpha)+','
  if (specular!=None): command+='Specular='+cstr(specular)+','
  return(runretval(command[:-1],retvalused()))

# COLOR SURFACE (OBJECT)
# ======================
def ColorSurfObj(selection1, Type=None, outcol=None, outalpha=None, incol=None, inalpha=None, specular=None):
  command='ColorSurfObj '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (outcol!=None): command+='OutCol='+cstr(outcol)+','
  if (outalpha!=None): command+='OutAlpha='+cstr(outalpha)+','
  if (incol!=None): command+='InCol='+cstr(incol)+','
  if (inalpha!=None): command+='InAlpha='+cstr(inalpha)+','
  if (specular!=None): command+='Specular='+cstr(specular)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET ATOM COLORS (ALL OR SELECTED)
# =====================================
def Color(first=None, second=None, segments=None, mapcons=None, filename=None, consmin=None):
  command='Color '
  if (first!=None): command+='first='+cstr(first)+','
  if (second!=None): command+='second='+cstr(second)+','
  if (segments!=None): command+='Segments='+cstr(segments)+','
  if (mapcons!=None): command+='MapCons='+cstr(mapcons)+','
  if (filename!=None): command+='Filename='+cstr(filename)+','
  if (consmin!=None): command+='ConsMin='+cstr(consmin)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET ATOM COLORS (ALL OR SELECTED)
# =====================================
# THIS IS ALTERNATIVE 2, WITH DIFFERENT PARAMETERS
def ColorFile(filename=None):
  command='Color File,'
  if (filename!=None): command+='Filename='+cstr(filename)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET ATOM COLORS (ALL)
# =========================
def ColorAll(first=None, second=None, segments=None, mapcons=None, filename=None, consmin=None):
  command='ColorAll '
  if (first!=None): command+='first='+cstr(first)+','
  if (second!=None): command+='second='+cstr(second)+','
  if (segments!=None): command+='Segments='+cstr(segments)+','
  if (mapcons!=None): command+='MapCons='+cstr(mapcons)+','
  if (filename!=None): command+='Filename='+cstr(filename)+','
  if (consmin!=None): command+='ConsMin='+cstr(consmin)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET ATOM COLORS (ALL)
# =========================
# THIS IS ALTERNATIVE 2, WITH DIFFERENT PARAMETERS
def ColorAllFile(filename=None):
  command='ColorAll File,'
  if (filename!=None): command+='Filename='+cstr(filename)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET ATOM COLORS (OBJECT)
# ============================
def ColorObj(selection1, first=None, second=None, segments=None, mapcons=None, filename=None, consmin=None):
  command='ColorObj '
  command+=selstr(selection1)+','
  if (first!=None): command+='first='+cstr(first)+','
  if (second!=None): command+='second='+cstr(second)+','
  if (segments!=None): command+='Segments='+cstr(segments)+','
  if (mapcons!=None): command+='MapCons='+cstr(mapcons)+','
  if (filename!=None): command+='Filename='+cstr(filename)+','
  if (consmin!=None): command+='ConsMin='+cstr(consmin)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET ATOM COLORS (OBJECT)
# ============================
# THIS IS ALTERNATIVE 2, WITH DIFFERENT PARAMETERS
def ColorObjFile(noname1=None, filename=None):
  command='ColorObj File,'
  if (noname1!=None): command+=cstr(noname1)+','
  if (filename!=None): command+='Filename='+cstr(filename)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET ATOM COLORS (MOLECULE)
# ==============================
def ColorMol(selection1, first=None, second=None, segments=None, mapcons=None, filename=None, consmin=None):
  command='ColorMol '
  command+=selstr(selection1)+','
  if (first!=None): command+='first='+cstr(first)+','
  if (second!=None): command+='second='+cstr(second)+','
  if (segments!=None): command+='Segments='+cstr(segments)+','
  if (mapcons!=None): command+='MapCons='+cstr(mapcons)+','
  if (filename!=None): command+='Filename='+cstr(filename)+','
  if (consmin!=None): command+='ConsMin='+cstr(consmin)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET ATOM COLORS (MOLECULE)
# ==============================
# THIS IS ALTERNATIVE 2, WITH DIFFERENT PARAMETERS
def ColorMolFile(noname1=None, filename=None):
  command='ColorMol File,'
  if (noname1!=None): command+=cstr(noname1)+','
  if (filename!=None): command+='Filename='+cstr(filename)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET ATOM COLORS (RESIDUE)
# =============================
def ColorRes(selection1, first=None, second=None, segments=None, mapcons=None, filename=None, consmin=None):
  command='ColorRes '
  command+=selstr(selection1)+','
  if (first!=None): command+='first='+cstr(first)+','
  if (second!=None): command+='second='+cstr(second)+','
  if (segments!=None): command+='Segments='+cstr(segments)+','
  if (mapcons!=None): command+='MapCons='+cstr(mapcons)+','
  if (filename!=None): command+='Filename='+cstr(filename)+','
  if (consmin!=None): command+='ConsMin='+cstr(consmin)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET ATOM COLORS (RESIDUE)
# =============================
# THIS IS ALTERNATIVE 2, WITH DIFFERENT PARAMETERS
def ColorResFile(noname1=None, filename=None):
  command='ColorRes File,'
  if (noname1!=None): command+=cstr(noname1)+','
  if (filename!=None): command+='Filename='+cstr(filename)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET ATOM COLORS (ATOM)
# ==========================
def ColorAtom(selection1, first=None, second=None, segments=None, mapcons=None, filename=None, consmin=None):
  command='ColorAtom '
  command+=selstr(selection1)+','
  if (first!=None): command+='first='+cstr(first)+','
  if (second!=None): command+='second='+cstr(second)+','
  if (segments!=None): command+='Segments='+cstr(segments)+','
  if (mapcons!=None): command+='MapCons='+cstr(mapcons)+','
  if (filename!=None): command+='Filename='+cstr(filename)+','
  if (consmin!=None): command+='ConsMin='+cstr(consmin)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET ATOM COLORS (ATOM)
# ==========================
# THIS IS ALTERNATIVE 2, WITH DIFFERENT PARAMETERS
def ColorAtomFile(noname1=None, filename=None):
  command='ColorAtom File,'
  if (noname1!=None): command+=cstr(noname1)+','
  if (filename!=None): command+='Filename='+cstr(filename)+','
  return(runretval(command[:-1],retvalused()))

# COMPARE BONDS
# =============
def CompareBond(selection1, selection2, selection3, selection4, checkmol=None):
  command='CompareBond '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  command+=selstr(selection3)+','
  command+=selstr(selection4)+','
  if (checkmol!=None): command+='CheckMol='+cstr(checkmol)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# COMPARE ATOMS AND RESIDUES (RESIDUE)
# ====================================
def CompareRes(selection1, selection2, checkmol=None):
  command='CompareRes '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (checkmol!=None): command+='CheckMol='+cstr(checkmol)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# COMPARE ATOMS AND RESIDUES (ATOM)
# =================================
def CompareAtom(selection1, selection2, checkmol=None):
  command='CompareAtom '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (checkmol!=None): command+='CheckMol='+cstr(checkmol)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SET/GET COMPOUND NAMES OF MOLECULES
# ===================================
def CompoundMol(selection1, name=None):
  command='CompoundMol '
  command+=selstr(selection1)+','
  if (name!=None): command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET CONSOLE MODE
# ====================
def Console(flag=None):
  command='Console '
  if (flag!=None): command+='Flag='+cstr(flag)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SET CONSOLE PARAMETERS
# ======================
def ConsolePar(font=None, height=None, antialias=None):
  command='ConsolePar '
  if (font!=None): command+='Font='+cstr(font)+','
  if (height!=None): command+='Height='+cstr(height)+','
  if (antialias!=None): command+='Antialias='+cstr(antialias)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET COORDINATE SYSTEM
# =========================
def CoordSys(handed=None):
  command='CoordSys '
  if (handed!=None): command+='handed='+cstr(handed)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# CALCULATE CONTACT SURFACE AREAS (OBJECT)
# ========================================
def ConSurfObj(selection1, selection2, cutoff=None, subtract=None, Type=None, unit=None):
  command='ConSurfObj '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (subtract!=None): command+='Subtract='+cstr(subtract)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE CONTACT SURFACE AREAS (MOLECULE)
# ==========================================
def ConSurfMol(selection1, selection2, cutoff=None, subtract=None, Type=None, unit=None):
  command='ConSurfMol '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (subtract!=None): command+='Subtract='+cstr(subtract)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE CONTACT SURFACE AREAS (RESIDUE)
# =========================================
def ConSurfRes(selection1, selection2, cutoff=None, subtract=None, Type=None, unit=None):
  command='ConSurfRes '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (subtract!=None): command+='Subtract='+cstr(subtract)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE CONTACT SURFACE AREAS (ATOM)
# ======================================
def ConSurfAtom(selection1, selection2, cutoff=None, subtract=None, Type=None, unit=None):
  command='ConSurfAtom '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (subtract!=None): command+='Subtract='+cstr(subtract)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# COPY FILE
# =========
def CopyFile(srcfilename=None, dstfilename=None, append=None):
  command='CopyFile '
  if (srcfilename!=None): command+='SrcFilename='+cstr(srcfilename)+','
  if (dstfilename!=None): command+='DstFilename='+cstr(dstfilename)+','
  if (append!=None): command+='append='+cstr(append)+','
  return(runretval(command[:-1],retvalused()))

# COPY VISUALIZATION STYLE BETWEEN OBJECTS
# ========================================
def CopyStyleObj(selection1, selection2, match=None):
  command='CopyStyleObj '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (match!=None): command+='Match='+cstr(match)+','
  return(runretval(command[:-1],retvalused()))

# CORRECT CIS-PEPTIDE BONDS DURING A SIMULATION
# =============================================
def CorrectCis(Type, old=None, proline=None):
  command='CorrectCis '
  command+='Type='+cstr(Type)+','
  if (old!=None): command+='Old='+cstr(old)+','
  if (proline!=None): command+='Proline='+cstr(proline)+','
  return(runretval(command[:-1],retvalused()))

# CORRECT NAMING CONVENTIONS DURING A SIMULATION
# ==============================================
def CorrectConv(flag):
  command='CorrectConv '
  command+='Flag='+cstr(flag)+','
  return(runretval(command[:-1],retvalused()))

# CORRECT SOLUTE DRIFT DURING A SIMULATION
# ========================================
def CorrectDrift(flag):
  command='CorrectDrift '
  command+='Flag='+cstr(flag)+','
  return(runretval(command[:-1],retvalused()))

# CORRECT WRONG ISOMERS DURING A SIMULATION
# =========================================
def CorrectIso(Type, old=None):
  command='CorrectIso '
  command+='Type='+cstr(Type)+','
  if (old!=None): command+='Old='+cstr(old)+','
  return(runretval(command[:-1],retvalused()))

# CORRECT KNOTS AND OTHER ENTANGLEMENTS DURING A SIMULATION
# =========================================================
def CorrectKnots(flag):
  command='CorrectKnots '
  command+='Flag='+cstr(flag)+','
  return(runretval(command[:-1],retvalused()))

# COUNT BONDS
# ===========
def CountBond(selection1, selection2, Type=None):
  command='CountBond '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# COUNT CONTACTS (OBJECT)
# =======================
def CountConObj(selection1, selection2, cutoff=None, subtract=None, energy=None, exclude=None, occluded=None, unit=None):
  command='CountConObj '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (subtract!=None): command+='Subtract='+cstr(subtract)+','
  if (energy!=None): command+='Energy='+cstr(energy)+','
  if (exclude!=None): command+='Exclude='+cstr(exclude)+','
  if (occluded!=None): command+='Occluded='+cstr(occluded)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# COUNT CONTACTS (MOLECULE)
# =========================
def CountConMol(selection1, selection2, cutoff=None, subtract=None, energy=None, exclude=None, occluded=None, unit=None):
  command='CountConMol '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (subtract!=None): command+='Subtract='+cstr(subtract)+','
  if (energy!=None): command+='Energy='+cstr(energy)+','
  if (exclude!=None): command+='Exclude='+cstr(exclude)+','
  if (occluded!=None): command+='Occluded='+cstr(occluded)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# COUNT CONTACTS (RESIDUE)
# ========================
def CountConRes(selection1, selection2, cutoff=None, subtract=None, energy=None, exclude=None, occluded=None, unit=None):
  command='CountConRes '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (subtract!=None): command+='Subtract='+cstr(subtract)+','
  if (energy!=None): command+='Energy='+cstr(energy)+','
  if (exclude!=None): command+='Exclude='+cstr(exclude)+','
  if (occluded!=None): command+='Occluded='+cstr(occluded)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# COUNT CONTACTS (ATOM)
# =====================
def CountConAtom(selection1, selection2, cutoff=None, subtract=None, energy=None, exclude=None, occluded=None, unit=None):
  command='CountConAtom '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (subtract!=None): command+='Subtract='+cstr(subtract)+','
  if (energy!=None): command+='Energy='+cstr(energy)+','
  if (exclude!=None): command+='Exclude='+cstr(exclude)+','
  if (occluded!=None): command+='Occluded='+cstr(occluded)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# COUNT SELECTED UNITS (OBJECT)
# =============================
def CountObj(selection1):
  command='CountObj '
  command+=selstr(selection1)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# COUNT SELECTED UNITS (MOLECULE)
# ===============================
def CountMol(selection1):
  command='CountMol '
  command+=selstr(selection1)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# COUNT SELECTED UNITS (RESIDUE)
# ==============================
def CountRes(selection1):
  command='CountRes '
  command+=selstr(selection1)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# COUNT SELECTED UNITS (ATOM)
# ===========================
def CountAtom(selection1):
  command='CountAtom '
  command+=selstr(selection1)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# CRYSTALLIZE OBJECTS TO FILL THE UNIT CELL (ALL OR SELECTED)
# ===========================================================
def Crystallize(center=None):
  command='Crystallize '
  if (center!=None): command+='Center='+cstr(center)+','
  return(runretval(command[:-1],retvalused()))

# CRYSTALLIZE OBJECTS TO FILL THE UNIT CELL (ALL)
# ===============================================
def CrystallizeAll(center=None):
  command='CrystallizeAll '
  if (center!=None): command+='Center='+cstr(center)+','
  return(runretval(command[:-1],retvalused()))

# CRYSTALLIZE OBJECTS TO FILL THE UNIT CELL (OBJECT)
# ==================================================
def CrystallizeObj(selection1, center=None):
  command='CrystallizeObj '
  command+=selstr(selection1)+','
  if (center!=None): command+='Center='+cstr(center)+','
  return(runretval(command[:-1],retvalused()))

# SET FORCE CUTOFF DISTANCE
# =========================
def Cutoff(distance):
  command='Cutoff '
  command+='Distance='+cstr(distance)+','
  return(runretval(command[:-1],retvalused()))

# CUT OBJECTS OPEN (ALL OR SELECTED)
# ==================================
def Cut(secstr=None):
  command='Cut '
  if (secstr!=None): command+='SecStr='+cstr(secstr)+','
  return(runretval(command[:-1],retvalused()))

# CUT OBJECTS OPEN (ALL)
# ======================
def CutAll(secstr=None):
  command='CutAll '
  if (secstr!=None): command+='SecStr='+cstr(secstr)+','
  return(runretval(command[:-1],retvalused()))

# CUT OBJECTS OPEN (OBJECT)
# =========================
def CutObj(selection1, secstr=None):
  command='CutObj '
  command+=selstr(selection1)+','
  if (secstr!=None): command+='SecStr='+cstr(secstr)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE CYSTEINE BRIDGE ENERGIES
# ==================================
def CysEnergyRes(selection1, selection2):
  command='CysEnergyRes '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE DYNAMIC CROSS-CORRELATION MATRIX
# ==========================================
def DCCM():
  command='DCCM '
  return(runretval(command[:-1],retvalused()))

# CONVERT 3D TO 2D COORDINATES, CREATING A FLAT STRUCTURAL FORMULA (ALL OR SELECTED)
# ==================================================================================
def Deflate(formulacol=None):
  command='Deflate '
  if (formulacol!=None): command+='FormulaCol='+cstr(formulacol)+','
  return(runretval(command[:-1],retvalused()))

# CONVERT 3D TO 2D COORDINATES, CREATING A FLAT STRUCTURAL FORMULA (ALL)
# ======================================================================
def DeflateAll(formulacol=None):
  command='DeflateAll '
  if (formulacol!=None): command+='FormulaCol='+cstr(formulacol)+','
  return(runretval(command[:-1],retvalused()))

# CONVERT 3D TO 2D COORDINATES, CREATING A FLAT STRUCTURAL FORMULA (OBJECT)
# =========================================================================
def DeflateObj(selection1, formulacol=None):
  command='DeflateObj '
  command+=selstr(selection1)+','
  if (formulacol!=None): command+='FormulaCol='+cstr(formulacol)+','
  return(runretval(command[:-1],retvalused()))

# CONVERT 3D TO 2D COORDINATES, CREATING A FLAT STRUCTURAL FORMULA (MOLECULE)
# ===========================================================================
def DeflateMol(selection1, formulacol=None):
  command='DeflateMol '
  command+=selstr(selection1)+','
  if (formulacol!=None): command+='FormulaCol='+cstr(formulacol)+','
  return(runretval(command[:-1],retvalused()))

# CONVERT 3D TO 2D COORDINATES, CREATING A FLAT STRUCTURAL FORMULA (RESIDUE)
# ==========================================================================
def DeflateRes(selection1, formulacol=None):
  command='DeflateRes '
  command+=selstr(selection1)+','
  if (formulacol!=None): command+='FormulaCol='+cstr(formulacol)+','
  return(runretval(command[:-1],retvalused()))

# CONVERT 3D TO 2D COORDINATES, CREATING A FLAT STRUCTURAL FORMULA (ATOM)
# =======================================================================
def DeflateAtom(selection1, formulacol=None):
  command='DeflateAtom '
  command+=selstr(selection1)+','
  if (formulacol!=None): command+='FormulaCol='+cstr(formulacol)+','
  return(runretval(command[:-1],retvalused()))

# GET DEGREES OF FREEDOM
# ======================
def DegFreedom():
  command='DegFreedom '
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# DELETE COVALENT BONDS
# =====================
def DelBond(selection1, selection2, lenmin=None):
  command='DelBond '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (lenmin!=None): command+='LenMin='+cstr(lenmin)+','
  return(runretval(command[:-1],retvalused()))

# DELETE FILE
# ===========
def DelFile(filename):
  command='DelFile '
  command+='Filename='+cstr(filename)+','
  return(runretval(command[:-1],retvalused()))

# DELETE ALL HYDROGENS (ALL OR SELECTED)
# ======================================
def DelHyd():
  command='DelHyd '
  return(runretval(command[:-1],retvalused()))

# DELETE ALL HYDROGENS (ALL)
# ==========================
def DelHydAll():
  command='DelHydAll '
  return(runretval(command[:-1],retvalused()))

# DELETE ALL HYDROGENS (OBJECT)
# =============================
def DelHydObj(selection1):
  command='DelHydObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# DELETE IMAGES
# =============
def DelImage(selection1):
  command='DelImage '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# DELETE RESTRAINTS (ALL OR SELECTED)
# ===================================
def DelRest(Class=None, component=None, number=None):
  command='DelRest '
  if (Class!=None): command+='Class='+cstr(Class)+','
  if (component!=None): command+='Component='+cstr(component)+','
  if (number!=None): command+='Number='+cstr(number)+','
  return(runretval(command[:-1],retvalused()))

# DELETE RESTRAINTS (ALL)
# =======================
def DelRestAll(Class=None, component=None, number=None):
  command='DelRestAll '
  if (Class!=None): command+='Class='+cstr(Class)+','
  if (component!=None): command+='Component='+cstr(component)+','
  if (number!=None): command+='Number='+cstr(number)+','
  return(runretval(command[:-1],retvalused()))

# DELETE RESTRAINTS (OBJECT)
# ==========================
def DelRestObj(selection1, Class=None, component=None, number=None):
  command='DelRestObj '
  command+=selstr(selection1)+','
  if (Class!=None): command+='Class='+cstr(Class)+','
  if (component!=None): command+='Component='+cstr(component)+','
  if (number!=None): command+='Number='+cstr(number)+','
  return(runretval(command[:-1],retvalused()))

# DELETE RESTRAINTS (MOLECULE)
# ============================
def DelRestMol(selection1, Class=None, component=None, number=None):
  command='DelRestMol '
  command+=selstr(selection1)+','
  if (Class!=None): command+='Class='+cstr(Class)+','
  if (component!=None): command+='Component='+cstr(component)+','
  if (number!=None): command+='Number='+cstr(number)+','
  return(runretval(command[:-1],retvalused()))

# DELETE RESTRAINTS (RESIDUE)
# ===========================
def DelRestRes(selection1, Class=None, component=None, number=None):
  command='DelRestRes '
  command+=selstr(selection1)+','
  if (Class!=None): command+='Class='+cstr(Class)+','
  if (component!=None): command+='Component='+cstr(component)+','
  if (number!=None): command+='Number='+cstr(number)+','
  return(runretval(command[:-1],retvalused()))

# DELETE RESTRAINTS (ATOM)
# ========================
def DelRestAtom(selection1, Class=None, component=None, number=None):
  command='DelRestAtom '
  command+=selstr(selection1)+','
  if (Class!=None): command+='Class='+cstr(Class)+','
  if (component!=None): command+='Component='+cstr(component)+','
  if (number!=None): command+='Number='+cstr(number)+','
  return(runretval(command[:-1],retvalused()))

# DELETE TABLES
# =============
def DelTab(selection1):
  command='DelTab '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# DELETE VIEW
# ===========
def DelView(selection1):
  command='DelView '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# DELETE ALL WATER MOLECULES (ALL OR SELECTED)
# ============================================
def DelWater():
  command='DelWater '
  return(runretval(command[:-1],retvalused()))

# DELETE ALL WATER MOLECULES (ALL)
# ================================
def DelWaterAll():
  command='DelWaterAll '
  return(runretval(command[:-1],retvalused()))

# DELETE ALL WATER MOLECULES (OBJECT)
# ===================================
def DelWaterObj(selection1):
  command='DelWaterObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# DELETE YANACONDA VARIABLE
# =========================
def DelVar(name, renumber=None, matchnum=None):
  command='DelVar '
  command+='Name='+cstr(name)+','
  if (renumber!=None): command+='Renumber='+cstr(renumber)+','
  if (matchnum!=None): command+='MatchNum='+cstr(matchnum)+','
  return(runretval(command[:-1],retvalused()))

# DELETE ATOMS AND OBJECTS (ALL OR SELECTED)
# ==========================================
def Del(center=None):
  command='Del '
  if (center!=None): command+='Center='+cstr(center)+','
  return(runretval(command[:-1],retvalused()))

# DELETE ATOMS AND OBJECTS (ALL)
# ==============================
def DelAll(center=None):
  command='DelAll '
  if (center!=None): command+='Center='+cstr(center)+','
  return(runretval(command[:-1],retvalused()))

# DELETE ATOMS AND OBJECTS (OBJECT)
# =================================
def DelObj(selection1, center=None):
  command='DelObj '
  command+=selstr(selection1)+','
  if (center!=None): command+='Center='+cstr(center)+','
  return(runretval(command[:-1],retvalused()))

# DELETE ATOMS AND OBJECTS (MOLECULE)
# ===================================
def DelMol(selection1, center=None):
  command='DelMol '
  command+=selstr(selection1)+','
  if (center!=None): command+='Center='+cstr(center)+','
  return(runretval(command[:-1],retvalused()))

# DELETE ATOMS AND OBJECTS (RESIDUE)
# ==================================
def DelRes(selection1, center=None):
  command='DelRes '
  command+=selstr(selection1)+','
  if (center!=None): command+='Center='+cstr(center)+','
  return(runretval(command[:-1],retvalused()))

# DELETE ATOMS AND OBJECTS (ATOM)
# ===============================
def DelAtom(selection1, center=None):
  command='DelAtom '
  command+=selstr(selection1)+','
  if (center!=None): command+='Center='+cstr(center)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET DIHEDRAL ANGLE BETWEEN ATOMS
# ====================================
def Dihedral(selection1, selection2, selection3, selection4, bound=None, set=None):
  command='Dihedral '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  command+=selstr(selection3)+','
  command+=selstr(selection4)+','
  if (bound!=None): command+='bound='+cstr(bound)+','
  if (set!=None): command+='set='+cstr(set)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE ELECTRIC DIPOLE MOMENTS (OBJECT)
# ==========================================
def DipoleObj(selection1):
  command='DipoleObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE ELECTRIC DIPOLE MOMENTS (MOLECULE)
# ============================================
def DipoleMol(selection1):
  command='DipoleMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE ELECTRIC DIPOLE MOMENTS (RESIDUE)
# ===========================================
def DipoleRes(selection1):
  command='DipoleRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE ELECTRIC DIPOLE MOMENTS (ATOM)
# ========================================
def DipoleAtom(selection1):
  command='DipoleAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET DISTANCE BETWEEN ATOMS
# ==============================
def Distance(selection1, selection2, bound=None, set=None):
  command='Distance '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (bound!=None): command+='bound='+cstr(bound)+','
  if (set!=None): command+='set='+cstr(set)+','
  return(runretval(command[:-1],retvalused()))

# DOWNLOAD FILE FROM INTERNET
# ===========================
def Download(url, filename):
  command='Download '
  command+='URL='+cstr(url)+','
  command+='Filename='+cstr(filename)+','
  return(runretval(command[:-1],retvalused()))

# DRAW A LINE
# ===========
def DrawLine(startx, starty, endx=None, endy=None, color=None, width=None, round=None):
  command='DrawLine '
  command+='StartX='+cstr(startx)+','
  command+='StartY='+cstr(starty)+','
  if (endx!=None): command+='EndX='+cstr(endx)+','
  if (endy!=None): command+='EndY='+cstr(endy)+','
  if (color!=None): command+='Color='+cstr(color)+','
  if (width!=None): command+='Width='+cstr(width)+','
  if (round!=None): command+='Round='+cstr(round)+','
  return(runretval(command[:-1],retvalused()))

# DUPLICATE VIEW
# ==============
def DuplicateView(selection1, name, hud=None):
  command='DuplicateView '
  command+=selstr(selection1)+','
  command+='Name='+cstr(name)+','
  if (hud!=None): command+='HUD='+cstr(hud)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# DUPLICATE OBJECTS (ALL OR SELECTED)
# ===================================
def Duplicate():
  command='Duplicate '
  return(runretval(command[:-1],retvalused()))

# DUPLICATE OBJECTS (ALL)
# =======================
def DuplicateAll():
  command='DuplicateAll '
  return(runretval(command[:-1],retvalused()))

# DUPLICATE OBJECTS (OBJECT)
# ==========================
def DuplicateObj(selection1):
  command='DuplicateObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# DUPLICATE OBJECTS (MOLECULE)
# ============================
def DuplicateMol(selection1):
  command='DuplicateMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# DUPLICATE OBJECTS (RESIDUE)
# ===========================
def DuplicateRes(selection1):
  command='DuplicateRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# DUPLICATE OBJECTS (ATOM)
# ========================
def DuplicateAtom(selection1):
  command='DuplicateAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# GET CHEMICAL ELEMENT
# ====================
def ElementAtom(selection1):
  command='ElementAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SET ENERGY UNIT
# ===============
def EnergyUnit(name):
  command='EnergyUnit '
  command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE FORCE FIELD ENERGIES (ALL OR SELECTED)
# ================================================
def Energy(component, *arglist2):
  command='Energy '
  command+='Component='+cstr(component)+','
  # ANY NUMBER OF VARIABLE ARGUMENTS CAN FOLLOW
  for arglist in arglist2:
    if (type(arglist)!=type([])): arglist=[arglist]
    for arg in arglist:
      command+=cstr(arg,quoted=(type(arg)!=type(1) and type(arg)!=type(1.)))+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE FORCE FIELD ENERGIES (ALL)
# ====================================
def EnergyAll(component, *arglist2):
  command='EnergyAll '
  command+='Component='+cstr(component)+','
  # ANY NUMBER OF VARIABLE ARGUMENTS CAN FOLLOW
  for arglist in arglist2:
    if (type(arglist)!=type([])): arglist=[arglist]
    for arg in arglist:
      command+=cstr(arg,quoted=(type(arg)!=type(1) and type(arg)!=type(1.)))+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE FORCE FIELD ENERGIES (OBJECT)
# =======================================
def EnergyObj(selection1, component, *arglist2):
  command='EnergyObj '
  command+=selstr(selection1)+','
  command+='Component='+cstr(component)+','
  # ANY NUMBER OF VARIABLE ARGUMENTS CAN FOLLOW
  for arglist in arglist2:
    if (type(arglist)!=type([])): arglist=[arglist]
    for arg in arglist:
      command+=cstr(arg,quoted=(type(arg)!=type(1) and type(arg)!=type(1.)))+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE FORCE FIELD ENERGIES (MOLECULE)
# =========================================
def EnergyMol(selection1, component, *arglist2):
  command='EnergyMol '
  command+=selstr(selection1)+','
  command+='Component='+cstr(component)+','
  # ANY NUMBER OF VARIABLE ARGUMENTS CAN FOLLOW
  for arglist in arglist2:
    if (type(arglist)!=type([])): arglist=[arglist]
    for arg in arglist:
      command+=cstr(arg,quoted=(type(arg)!=type(1) and type(arg)!=type(1.)))+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE FORCE FIELD ENERGIES (RESIDUE)
# ========================================
def EnergyRes(selection1, component, *arglist2):
  command='EnergyRes '
  command+=selstr(selection1)+','
  command+='Component='+cstr(component)+','
  # ANY NUMBER OF VARIABLE ARGUMENTS CAN FOLLOW
  for arglist in arglist2:
    if (type(arglist)!=type([])): arglist=[arglist]
    for arg in arglist:
      command+=cstr(arg,quoted=(type(arg)!=type(1) and type(arg)!=type(1.)))+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE FORCE FIELD ENERGIES (ATOM)
# =====================================
def EnergyAtom(selection1, component, *arglist2):
  command='EnergyAtom '
  command+=selstr(selection1)+','
  command+='Component='+cstr(component)+','
  # ANY NUMBER OF VARIABLE ARGUMENTS CAN FOLLOW
  for arglist in arglist2:
    if (type(arglist)!=type([])): arglist=[arglist]
    for arg in arglist:
      command+=cstr(arg,quoted=(type(arg)!=type(1) and type(arg)!=type(1.)))+','
  return(runretval(command[:-1],retvalused()))

# CHOOSE AND CONTROL EXPERIMENTS
# ==============================
def Experiment(noname1):
  command='Experiment '
  command+=cstr(noname1)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# CHOOSE AND CONTROL EXPERIMENTS
# ==============================
# THIS IS ALTERNATIVE 2, WITH DIFFERENT PARAMETERS
def ExperimentMinimization(convergence=None):
  command='Experiment Minimization\n'
  if (convergence!=None): command+='  convergence '+cstr(convergence)+'\n'
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# CHOOSE AND CONTROL EXPERIMENTS
# ==============================
# THIS IS ALTERNATIVE 3, WITH DIFFERENT PARAMETERS
def ExperimentNeutralization(waterdensity=None, nacl=None, ph=None, pkafile=None, speed=None, ions=None):
  command='Experiment Neutralization\n'
  if (waterdensity!=None): command+='  waterdensity '+cstr(waterdensity)+'\n'
  if (nacl!=None): command+='  nacl '+cstr(nacl)+'\n'
  if (ph!=None): command+='  ph '+cstr(ph)+'\n'
  if (pkafile!=None): command+='  pkafile '+cstr(pkafile)+'\n'
  if (speed!=None): command+='  speed '+cstr(speed)+'\n'
  if (ions!=None): command+='  ions '+cstr(ions)+'\n'
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# CHOOSE AND CONTROL EXPERIMENTS
# ==============================
# THIS IS ALTERNATIVE 4, WITH DIFFERENT PARAMETERS
def ExperimentMorphing(startobj=None, endobj=None, structures=None, structurefile=None, morphforce=None):
  command='Experiment Morphing\n'
  if (startobj!=None): command+='  startobj '+cstr(startobj)+'\n'
  if (endobj!=None): command+='  endobj '+cstr(endobj)+'\n'
  if (structures!=None): command+='  structures '+cstr(structures)+'\n'
  if (structurefile!=None): command+='  structurefile '+cstr(structurefile)+'\n'
  if (morphforce!=None): command+='  morphforce '+cstr(morphforce)+'\n'
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# CHOOSE AND CONTROL EXPERIMENTS
# ==============================
# THIS IS ALTERNATIVE 5, WITH DIFFERENT PARAMETERS
def ExperimentDocking(method=None, ligandobj=None, receptorobj=None, runs=None, clusterrmsd=None, resultfile=None, tmpfileid=None, gridparlist=None, dockparlist=None, setuponly=None):
  command='Experiment Docking\n'
  if (method!=None): command+='  method '+cstr(method)+'\n'
  if (ligandobj!=None): command+='  ligandobj '+cstr(ligandobj)+'\n'
  if (receptorobj!=None): command+='  receptorobj '+cstr(receptorobj)+'\n'
  if (runs!=None): command+='  runs '+cstr(runs)+'\n'
  if (clusterrmsd!=None): command+='  clusterrmsd '+cstr(clusterrmsd)+'\n'
  if (resultfile!=None): command+='  resultfile '+cstr(resultfile)+'\n'
  if (tmpfileid!=None): command+='  tmpfileid '+cstr(tmpfileid)+'\n'
  if (gridparlist!=None): 
    if (type(gridparlist)!=type([])): gridparlist=[gridparlist]
    for value in gridparlist:
      command+='  gridpar '+cstr(value)+'\n'
  if (dockparlist!=None): 
    if (type(dockparlist)!=type([])): dockparlist=[dockparlist]
    for value in dockparlist:
      command+='  dockpar '+cstr(value)+'\n'
  if (setuponly!=None): command+='  setuponly '+cstr(setuponly)+'\n'
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# CHOOSE AND CONTROL EXPERIMENTS
# ==============================
# THIS IS ALTERNATIVE 6, WITH DIFFERENT PARAMETERS
def ExperimentHomologyModeling(sequencefile=None, psiblasts=None, evalue=None, oligostate=None, templates=None, alignments=None, alignfile=None, templateobj=None, loopsamples=None, speed=None, animation=None, resultfile=None, termextension=None, residues=None, structprofile=None, fixmodelres=None, looplenmax=None):
  command='Experiment HomologyModeling\n'
  if (sequencefile!=None): command+='  sequencefile '+cstr(sequencefile)+'\n'
  if (psiblasts!=None): command+='  psiblasts '+cstr(psiblasts)+'\n'
  if (evalue!=None): command+='  evalue '+cstr(evalue)+'\n'
  if (oligostate!=None): command+='  oligostate '+cstr(oligostate)+'\n'
  if (templates!=None): command+='  templates '+cstr(templates)+'\n'
  if (alignments!=None): command+='  alignments '+cstr(alignments)+'\n'
  if (alignfile!=None): command+='  alignfile '+cstr(alignfile)+'\n'
  if (templateobj!=None): command+='  templateobj '+cstr(templateobj)+'\n'
  if (loopsamples!=None): command+='  loopsamples '+cstr(loopsamples)+'\n'
  if (speed!=None): command+='  speed '+cstr(speed)+'\n'
  if (animation!=None): command+='  animation '+cstr(animation)+'\n'
  if (resultfile!=None): command+='  resultfile '+cstr(resultfile)+'\n'
  if (termextension!=None): command+='  termextension '+cstr(termextension)+'\n'
  if (residues!=None): command+='  residues '+cstr(residues)+'\n'
  if (structprofile!=None): command+='  structprofile '+cstr(structprofile)+'\n'
  if (fixmodelres!=None): command+='  fixmodelres '+cstr(fixmodelres)+'\n'
  if (looplenmax!=None): command+='  looplenmax '+cstr(looplenmax)+'\n'
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# CHOOSE AND CONTROL EXPERIMENTS
# ==============================
# THIS IS ALTERNATIVE 7, WITH DIFFERENT PARAMETERS
def ExperimentNMRFolding(startobj=None, restrainfile=None, structures=None, structurefile=None):
  command='Experiment NMRFolding\n'
  if (startobj!=None): command+='  startobj '+cstr(startobj)+'\n'
  if (restrainfile!=None): command+='  restrainfile '+cstr(restrainfile)+'\n'
  if (structures!=None): command+='  structures '+cstr(structures)+'\n'
  if (structurefile!=None): command+='  structurefile '+cstr(structurefile)+'\n'
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# GET FILE SIZE
# =============
def FileSize(filename):
  command='FileSize '
  command+='Filename='+cstr(filename)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# FILL SIMULATION CELL WITH OBJECT
# ================================
def FillCellObj(selection1, copies=None, density=None, bumpsum=None, randomori=None, dismin=None):
  command='FillCellObj '
  command+=selstr(selection1)+','
  if (copies!=None): command+='Copies='+cstr(copies)+','
  if (density!=None): command+='Density='+cstr(density)+','
  if (bumpsum!=None): command+='BumpSum='+cstr(bumpsum)+','
  if (randomori!=None): command+='RandomOri='+cstr(randomori)+','
  if (dismin!=None): command+='DisMin='+cstr(dismin)+','
  return(runretval(command[:-1],retvalused()))

# FILL SIMULATION CELL WITH WATER
# ===============================
def FillCellWater(density=None, probe=None, bumpsum=None, dismax=None):
  command='FillCellWater '
  if (density!=None): command+='Density='+cstr(density)+','
  if (probe!=None): command+='Probe='+cstr(probe)+','
  if (bumpsum!=None): command+='BumpSum='+cstr(bumpsum)+','
  if (dismax!=None): command+='DisMax='+cstr(dismax)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# FILL OR CLEAR RECTANGULAR AREA
# ==============================
def FillRect(x=None, y=None, width=None, height=None, color=None):
  command='FillRect '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (width!=None): command+='Width='+cstr(width)+','
  if (height!=None): command+='Height='+cstr(height)+','
  if (color!=None): command+='Color='+cstr(color)+','
  return(runretval(command[:-1],retvalused()))

# GET FIRST ATOM OR RESIDUE FACING EACH CAVITY AND THE CAVITY VOLUME (RESIDUE)
# ============================================================================
def FirstCaviRes(selection1, Type=None):
  command='FirstCaviRes '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# GET FIRST ATOM OR RESIDUE FACING EACH CAVITY AND THE CAVITY VOLUME (ATOM)
# =========================================================================
def FirstCaviAtom(selection1, Type=None):
  command='FirstCaviAtom '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# GET FIRST ATOM OR RESIDUE FACING EACH SURFACE AND THE SURFACE AREA (RESIDUE)
# ============================================================================
def FirstSurfRes(selection1, Type=None):
  command='FirstSurfRes '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# GET FIRST ATOM OR RESIDUE FACING EACH SURFACE AND THE SURFACE AREA (ATOM)
# =========================================================================
def FirstSurfAtom(selection1, Type=None):
  command='FirstSurfAtom '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# CONSTRAIN BOND LENGTH DURING SIMULATION
# =======================================
def FixBond(selection1, selection2):
  command='FixBond '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  return(runretval(command[:-1],retvalused()))

# CONSTRAIN BOND ANGLE DURING SIMULATION
# ======================================
def FixAngle(selection1, selection2, selection3):
  command='FixAngle '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  command+=selstr(selection3)+','
  return(runretval(command[:-1],retvalused()))

# CONSTRAIN CRITICAL HYDROGEN BOND ANGLES DURING SIMULATION
# =========================================================
def FixHydAngle(selection1):
  command='FixHydAngle '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# FIX ATOMS DURING SIMULATION (ALL OR SELECTED)
# =============================================
def Fix():
  command='Fix '
  return(runretval(command[:-1],retvalused()))

# FIX ATOMS DURING SIMULATION (ALL)
# =================================
def FixAll():
  command='FixAll '
  return(runretval(command[:-1],retvalused()))

# FIX ATOMS DURING SIMULATION (OBJECT)
# ====================================
def FixObj(selection1):
  command='FixObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# FIX ATOMS DURING SIMULATION (MOLECULE)
# ======================================
def FixMol(selection1):
  command='FixMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# FIX ATOMS DURING SIMULATION (RESIDUE)
# =====================================
def FixRes(selection1):
  command='FixRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# FIX ATOMS DURING SIMULATION (ATOM)
# ==================================
def FixAtom(selection1):
  command='FixAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# FLIP TABLE AXES
# ===============
def FlipTab(selection1, firstdim, seconddim=None):
  command='FlipTab '
  command+=selstr(selection1)+','
  command+='FirstDim='+cstr(firstdim)+','
  if (seconddim!=None): command+='SecondDim='+cstr(seconddim)+','
  return(runretval(command[:-1],retvalused()))

# SET FOG DENSITY
# ===============
def Fog(density=None, Range=None, dismin=None, dismax=None):
  command='Fog '
  if (density!=None): command+='Density='+cstr(density)+','
  if (Range!=None): command+='Range='+cstr(Range)+','
  if (dismin!=None): command+='DisMin='+cstr(dismin)+','
  if (dismax!=None): command+='DisMax='+cstr(dismax)+','
  return(runretval(command[:-1],retvalused()))

# SET FONT FOR 3D LETTERS
# =======================
def Font(name=None, height=None, color=None, alpha=None, spacing=None, depth=None, depthcol=None, depthalpha=None):
  command='Font '
  if (name!=None): command+='Name='+cstr(name)+','
  if (height!=None): command+='Height='+cstr(height)+','
  if (color!=None): command+='Color='+cstr(color)+','
  if (alpha!=None): command+='Alpha='+cstr(alpha)+','
  if (spacing!=None): command+='Spacing='+cstr(spacing)+','
  if (depth!=None): command+='Depth='+cstr(depth)+','
  if (depthcol!=None): command+='DepthCol='+cstr(depthcol)+','
  if (depthalpha!=None): command+='DepthAlpha='+cstr(depthalpha)+','
  return(runretval(command[:-1],retvalused()))

# SWITCH FONT FOG ON/OFF
# ======================
def FontFog(flag):
  command='FontFog '
  command+='Flag='+cstr(flag)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET FORCE FIELD
# ===================
def ForceField(name=None, method=None, setpar=None):
  command='ForceField '
  if (name!=None): command+='Name='+cstr(name)+','
  if (method!=None): command+='Method='+cstr(method)+','
  if (setpar!=None): command+='SetPar='+cstr(setpar)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SET/GET FORCE ON ATOMS (ALL OR SELECTED)
# ========================================
def Force(x=None, y=None, z=None):
  command='Force '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET FORCE ON ATOMS (ALL)
# ============================
def ForceAll(x=None, y=None, z=None):
  command='ForceAll '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET FORCE ON ATOMS (OBJECT)
# ===============================
def ForceObj(selection1, x=None, y=None, z=None):
  command='ForceObj '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET FORCE ON ATOMS (MOLECULE)
# =================================
def ForceMol(selection1, x=None, y=None, z=None):
  command='ForceMol '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET FORCE ON ATOMS (RESIDUE)
# ================================
def ForceRes(selection1, x=None, y=None, z=None):
  command='ForceRes '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET FORCE ON ATOMS (ATOM)
# =============================
def ForceAtom(selection1, x=None, y=None, z=None):
  command='ForceAtom '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# FORMAT RESIDUE OUTPUT
# =====================
def FormatRes(output):
  command='FormatRes '
  command+='Output='+cstr(output)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE FORMATION ENERGIES (ALL OR SELECTED)
# ==============================================
def FormEnergy():
  command='FormEnergy '
  return(runretval(command[:-1],retvalused()))

# CALCULATE FORMATION ENERGIES (ALL)
# ==================================
def FormEnergyAll():
  command='FormEnergyAll '
  return(runretval(command[:-1],retvalused()))

# CALCULATE FORMATION ENERGIES (OBJECT)
# =====================================
def FormEnergyObj(selection1):
  command='FormEnergyObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE FORMATION ENERGIES (MOLECULE)
# =======================================
def FormEnergyMol(selection1):
  command='FormEnergyMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE FORMATION ENERGIES (RESIDUE)
# ======================================
def FormEnergyRes(selection1):
  command='FormEnergyRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE FORMATION ENERGIES (ATOM)
# ===================================
def FormEnergyAtom(selection1):
  command='FormEnergyAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SET SCREEN UPDATE FREQUENCY
# ===========================
def FramesPerSec(number, redrawidle=None):
  command='FramesPerSec '
  command+='Number='+cstr(number)+','
  if (redrawidle!=None): command+='RedrawIdle='+cstr(redrawidle)+','
  return(runretval(command[:-1],retvalused()))

# REMOVE BOND LENGTH CONSTRAINT DURING SIMULATION
# ===============================================
def FreeBond(selection1, selection2):
  command='FreeBond '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  return(runretval(command[:-1],retvalused()))

# FREE BOND ANGLE DURING SIMULATION
# =================================
def FreeAngle(selection1, selection2, selection3):
  command='FreeAngle '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  command+=selstr(selection3)+','
  return(runretval(command[:-1],retvalused()))

# FREE ATOMS DURING SIMULATION (ALL OR SELECTED)
# ==============================================
def Free():
  command='Free '
  return(runretval(command[:-1],retvalused()))

# FREE ATOMS DURING SIMULATION (ALL)
# ==================================
def FreeAll():
  command='FreeAll '
  return(runretval(command[:-1],retvalused()))

# FREE ATOMS DURING SIMULATION (OBJECT)
# =====================================
def FreeObj(selection1):
  command='FreeObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# FREE ATOMS DURING SIMULATION (MOLECULE)
# =======================================
def FreeMol(selection1):
  command='FreeMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# FREE ATOMS DURING SIMULATION (RESIDUE)
# ======================================
def FreeRes(selection1):
  command='FreeRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# FREE ATOMS DURING SIMULATION (ATOM)
# ===================================
def FreeAtom(selection1):
  command='FreeAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SWITCH FULLSCREEN MODE ON/OFF
# =============================
def FullScreen(flag):
  command='FullScreen '
  command+='Flag='+cstr(flag)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE GLOBAL DISTANCE TEST (OBJECT)
# =======================================
def GDTObj(selection1, selection2, cutoff=None, match=None):
  command='GDTObj '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (match!=None): command+='Match='+cstr(match)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE GLOBAL DISTANCE TEST (MOLECULE)
# =========================================
def GDTMol(selection1, selection2, cutoff=None, match=None):
  command='GDTMol '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (match!=None): command+='Match='+cstr(match)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE GLOBAL DISTANCE TEST (RESIDUE)
# ========================================
def GDTRes(selection1, selection2, cutoff=None, match=None):
  command='GDTRes '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (match!=None): command+='Match='+cstr(match)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE GLOBAL DISTANCE TEST (ATOM)
# =====================================
def GDTAtom(selection1, selection2, cutoff=None, match=None):
  command='GDTAtom '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (match!=None): command+='Match='+cstr(match)+','
  return(runretval(command[:-1],retvalused()))

# GRAB NEXT OBJECT FOR MOUSE MOVEMENT
# ===================================
def GrabNext():
  command='GrabNext '
  return(runretval(command[:-1],retvalused()))

# GRAB PREVIOUS OBJECT FOR MOUSE MOVEMENT
# =======================================
def GrabPrev():
  command='GrabPrev '
  return(runretval(command[:-1],retvalused()))

# GRAB OBJECT OR SCENE FOR MOUSE MOVEMENT (ALL OR SELECTED)
# =========================================================
def Grab():
  command='Grab '
  return(runretval(command[:-1],retvalused()))

# GRAB OBJECT OR SCENE FOR MOUSE MOVEMENT (ALL)
# =============================================
def GrabAll():
  command='GrabAll '
  return(runretval(command[:-1],retvalused()))

# GRAB OBJECT OR SCENE FOR MOUSE MOVEMENT (OBJECT)
# ================================================
def GrabObj(selection1):
  command='GrabObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE ANGLE BETWEEN TWO ATOM GROUPS
# =======================================
def GroupAngle(selection1, selection2, Range=None):
  command='GroupAngle '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (Range!=None): command+='Range='+cstr(Range)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# CALCULATE BOUNDING BOX AROUND ATOM GROUP
# ========================================
def GroupBox(selection1, Type=None, coordsys=None):
  command='GroupBox '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (coordsys!=None): command+='CoordSys='+cstr(coordsys)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE GEOMETRIC CENTER OR CENTER OF MASS
# ============================================
def GroupCenter(selection1, coordsys=None, Type=None):
  command='GroupCenter '
  command+=selstr(selection1)+','
  if (coordsys!=None): command+='CoordSys='+cstr(coordsys)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE DIHEDRAL ANGLE BETWEEN TWO ATOM GROUPS
# ================================================
def GroupDihedral(selection1, selection2):
  command='GroupDihedral '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# CALCULATE DISTANCE BETWEEN TWO ATOM GROUPS
# ==========================================
def GroupDistance(selection1, selection2, center=None):
  command='GroupDistance '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (center!=None): command+='Center='+cstr(center)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# CALCULATE OPTIMAL LINE THROUGH ATOM GROUP
# =========================================
def GroupLine(selection1, coordsys=None):
  command='GroupLine '
  command+=selstr(selection1)+','
  if (coordsys!=None): command+='CoordSys='+cstr(coordsys)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE OPTIMAL PLANE THROUGH ATOM GROUP
# ==========================================
def GroupPlane(selection1, coordsys=None):
  command='GroupPlane '
  command+=selstr(selection1)+','
  if (coordsys!=None): command+='CoordSys='+cstr(coordsys)+','
  return(runretval(command[:-1],retvalused()))

# ADD ATOMS TO GROUP (ALL OR SELECTED)
# ====================================
def Group(name):
  command='Group '
  command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# ADD ATOMS TO GROUP (ALL)
# ========================
def GroupAll(name):
  command='GroupAll '
  command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# ADD ATOMS TO GROUP (OBJECT)
# ===========================
def GroupObj(selection1, name):
  command='GroupObj '
  command+=selstr(selection1)+','
  command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# ADD ATOMS TO GROUP (MOLECULE)
# =============================
def GroupMol(selection1, name):
  command='GroupMol '
  command+=selstr(selection1)+','
  command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# ADD ATOMS TO GROUP (RESIDUE)
# ============================
def GroupRes(selection1, name):
  command='GroupRes '
  command+=selstr(selection1)+','
  command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# ADD ATOMS TO GROUP (ATOM)
# =========================
def GroupAtom(selection1, name):
  command='GroupAtom '
  command+=selstr(selection1)+','
  command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# HIDE ARROWS (ALL OR SELECTED)
# =============================
def HideArrow():
  command='HideArrow '
  return(runretval(command[:-1],retvalused()))

# HIDE ARROWS (ALL)
# =================
def HideArrowAll():
  command='HideArrowAll '
  return(runretval(command[:-1],retvalused()))

# HIDE ARROWS (OBJECT)
# ====================
def HideArrowObj(selection1):
  command='HideArrowObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# HIDE ARROWS (MOLECULE)
# ======================
def HideArrowMol(selection1):
  command='HideArrowMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# HIDE ARROWS (RESIDUE)
# =====================
def HideArrowRes(selection1):
  command='HideArrowRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# HIDE ARROWS (ATOM)
# ==================
def HideArrowAtom(selection1):
  command='HideArrowAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# HIDE HYDROGEN BONDS (ALL OR SELECTED)
# =====================================
def HideHBo():
  command='HideHBo '
  return(runretval(command[:-1],retvalused()))

# HIDE HYDROGEN BONDS (ALL)
# =========================
def HideHBoAll():
  command='HideHBoAll '
  return(runretval(command[:-1],retvalused()))

# HIDE HYDROGEN BONDS (OBJECT)
# ============================
def HideHBoObj(selection1):
  command='HideHBoObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# HIDE HYDROGEN BONDS (MOLECULE)
# ==============================
def HideHBoMol(selection1):
  command='HideHBoMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# HIDE HYDROGEN BONDS (RESIDUE)
# =============================
def HideHBoRes(selection1):
  command='HideHBoRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# HIDE HYDROGEN BONDS (ATOM)
# ==========================
def HideHBoAtom(selection1):
  command='HideHBoAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# HIDE IN HEAD-UP DISPLAY (MOLECULE)
# ==================================
def HideHUDMol(selection1):
  command='HideHUDMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# HIDE IN HEAD-UP DISPLAY (RESIDUE)
# =================================
def HideHUDRes(selection1):
  command='HideHUDRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# HIDE IN HEAD-UP DISPLAY (ATOM)
# ==============================
def HideHUDAtom(selection1):
  command='HideHUDAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# HIDE IMAGES
# ===========
def HideImage(selection1):
  command='HideImage '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# HIDE TEXT MESSAGE AT THE BOTTOM
# ===============================
def HideMessage():
  command='HideMessage '
  return(runretval(command[:-1],retvalused()))

# HIDE POLYGONS (ALL OR SELECTED)
# ===============================
def HidePolygon():
  command='HidePolygon '
  return(runretval(command[:-1],retvalused()))

# HIDE POLYGONS (ALL)
# ===================
def HidePolygonAll():
  command='HidePolygonAll '
  return(runretval(command[:-1],retvalused()))

# HIDE POLYGONS (OBJECT)
# ======================
def HidePolygonObj(selection1):
  command='HidePolygonObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# HIDE POLYGONS (MOLECULE)
# ========================
def HidePolygonMol(selection1):
  command='HidePolygonMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# HIDE POLYGONS (RESIDUE)
# =======================
def HidePolygonRes(selection1):
  command='HidePolygonRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# HIDE POLYGONS (ATOM)
# ====================
def HidePolygonAtom(selection1):
  command='HidePolygonAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# HIDE RESTRAINTS (ALL OR SELECTED)
# =================================
def HideRest(Class=None):
  command='HideRest '
  if (Class!=None): command+='Class='+cstr(Class)+','
  return(runretval(command[:-1],retvalused()))

# HIDE RESTRAINTS (ALL)
# =====================
def HideRestAll(Class=None):
  command='HideRestAll '
  if (Class!=None): command+='Class='+cstr(Class)+','
  return(runretval(command[:-1],retvalused()))

# HIDE RESTRAINTS (OBJECT)
# ========================
def HideRestObj(selection1, Class=None):
  command='HideRestObj '
  command+=selstr(selection1)+','
  if (Class!=None): command+='Class='+cstr(Class)+','
  return(runretval(command[:-1],retvalused()))

# HIDE RESTRAINTS (MOLECULE)
# ==========================
def HideRestMol(selection1, Class=None):
  command='HideRestMol '
  command+=selstr(selection1)+','
  if (Class!=None): command+='Class='+cstr(Class)+','
  return(runretval(command[:-1],retvalused()))

# HIDE RESTRAINTS (RESIDUE)
# =========================
def HideRestRes(selection1, Class=None):
  command='HideRestRes '
  command+=selstr(selection1)+','
  if (Class!=None): command+='Class='+cstr(Class)+','
  return(runretval(command[:-1],retvalused()))

# HIDE RESTRAINTS (ATOM)
# ======================
def HideRestAtom(selection1, Class=None):
  command='HideRestAtom '
  command+=selstr(selection1)+','
  if (Class!=None): command+='Class='+cstr(Class)+','
  return(runretval(command[:-1],retvalused()))

# HIDE SECONDARY STRUCTURE (ALL OR SELECTED)
# ==========================================
def HideSecStr(showatoms=None):
  command='HideSecStr '
  if (showatoms!=None): command+='ShowAtoms='+cstr(showatoms)+','
  return(runretval(command[:-1],retvalused()))

# HIDE SECONDARY STRUCTURE (ALL)
# ==============================
def HideSecStrAll(showatoms=None):
  command='HideSecStrAll '
  if (showatoms!=None): command+='ShowAtoms='+cstr(showatoms)+','
  return(runretval(command[:-1],retvalused()))

# HIDE SECONDARY STRUCTURE (OBJECT)
# =================================
def HideSecStrObj(selection1, showatoms=None):
  command='HideSecStrObj '
  command+=selstr(selection1)+','
  if (showatoms!=None): command+='ShowAtoms='+cstr(showatoms)+','
  return(runretval(command[:-1],retvalused()))

# HIDE SECONDARY STRUCTURE (MOLECULE)
# ===================================
def HideSecStrMol(selection1, showatoms=None):
  command='HideSecStrMol '
  command+=selstr(selection1)+','
  if (showatoms!=None): command+='ShowAtoms='+cstr(showatoms)+','
  return(runretval(command[:-1],retvalused()))

# HIDE SECONDARY STRUCTURE (RESIDUE)
# ==================================
def HideSecStrRes(selection1, showatoms=None):
  command='HideSecStrRes '
  command+=selstr(selection1)+','
  if (showatoms!=None): command+='ShowAtoms='+cstr(showatoms)+','
  return(runretval(command[:-1],retvalused()))

# HIDE SURFACE (ALL OR SELECTED)
# ==============================
def HideSurf(Type=None):
  command='HideSurf '
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# HIDE SURFACE (ALL)
# ==================
def HideSurfAll(Type=None):
  command='HideSurfAll '
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# HIDE SURFACE (OBJECT)
# =====================
def HideSurfObj(selection1, Type=None):
  command='HideSurfObj '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# HIDE SURFACE (MOLECULE)
# =======================
def HideSurfMol(selection1, Type=None):
  command='HideSurfMol '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# HIDE SURFACE (RESIDUE)
# ======================
def HideSurfRes(selection1, Type=None):
  command='HideSurfRes '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# HIDE SURFACE (ATOM)
# ===================
def HideSurfAtom(selection1, Type=None):
  command='HideSurfAtom '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# HIDE TRACE THROUGH ATOMS
# ========================
def HideTrace(selection1):
  command='HideTrace '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# HIDE ATOMS (ALL OR SELECTED)
# ============================
def Hide():
  command='Hide '
  return(runretval(command[:-1],retvalused()))

# HIDE ATOMS (ALL)
# ================
def HideAll():
  command='HideAll '
  return(runretval(command[:-1],retvalused()))

# HIDE ATOMS (OBJECT)
# ===================
def HideObj(selection1):
  command='HideObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# HIDE ATOMS (MOLECULE)
# =====================
def HideMol(selection1):
  command='HideMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# HIDE ATOMS (RESIDUE)
# ====================
def HideRes(selection1):
  command='HideRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# HIDE ATOMS (ATOM)
# =================
def HideAtom(selection1):
  command='HideAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SWITCH HEAD UP DISPLAY
# ======================
def HUD(show=None, antialias=None, fontsize=None):
  command='HUD '
  if (show!=None): command+='Show='+cstr(show)+','
  if (antialias!=None): command+='Antialias='+cstr(antialias)+','
  if (fontsize!=None): command+='FontSize='+cstr(fontsize)+','
  return(runretval(command[:-1],retvalused()))

# SWITCH IMAGE FOG ON/OFF
# =======================
def ImageFog(flag):
  command='ImageFog '
  command+='Flag='+cstr(flag)+','
  return(runretval(command[:-1],retvalused()))

# GENERATE 3D COORDINATES FOR FLAT OR DISTORTED MOLECULES (ALL OR SELECTED)
# =========================================================================
def Inflate():
  command='Inflate '
  return(runretval(command[:-1],retvalused()))

# GENERATE 3D COORDINATES FOR FLAT OR DISTORTED MOLECULES (ALL)
# =============================================================
def InflateAll():
  command='InflateAll '
  return(runretval(command[:-1],retvalused()))

# GENERATE 3D COORDINATES FOR FLAT OR DISTORTED MOLECULES (OBJECT)
# ================================================================
def InflateObj(selection1):
  command='InflateObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# GENERATE 3D COORDINATES FOR FLAT OR DISTORTED MOLECULES (MOLECULE)
# ==================================================================
def InflateMol(selection1):
  command='InflateMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# GENERATE 3D COORDINATES FOR FLAT OR DISTORTED MOLECULES (RESIDUE)
# =================================================================
def InflateRes(selection1):
  command='InflateRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# GENERATE 3D COORDINATES FOR FLAT OR DISTORTED MOLECULES (ATOM)
# ==============================================================
def InflateAtom(selection1):
  command='InflateAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# INSTALL ACCESSORY PROGRAM
# =========================
def Install(program, code):
  command='Install '
  command+='Program='+cstr(program)+','
  command+='Code='+cstr(code)+','
  return(runretval(command[:-1],retvalused()))

# CREATE OBJECT INSTANCES FOR VISUALIZATION (ALL OR SELECTED)
# ===========================================================
def Instance(copies=None, group=None, x=None, y=None, z=None, rx=None, ry=None, rz=None):
  command='Instance '
  if (copies!=None): command+='Copies='+cstr(copies)+','
  if (group!=None): command+='Group='+cstr(group)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  if (rx!=None): command+='RX='+cstr(rx)+','
  if (ry!=None): command+='RY='+cstr(ry)+','
  if (rz!=None): command+='RZ='+cstr(rz)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# CREATE OBJECT INSTANCES FOR VISUALIZATION (ALL)
# ===============================================
def InstanceAll(copies=None, group=None, x=None, y=None, z=None, rx=None, ry=None, rz=None):
  command='InstanceAll '
  if (copies!=None): command+='Copies='+cstr(copies)+','
  if (group!=None): command+='Group='+cstr(group)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  if (rx!=None): command+='RX='+cstr(rx)+','
  if (ry!=None): command+='RY='+cstr(ry)+','
  if (rz!=None): command+='RZ='+cstr(rz)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# CREATE OBJECT INSTANCES FOR VISUALIZATION (OBJECT)
# ==================================================
def InstanceObj(selection1, copies=None, group=None, x=None, y=None, z=None, rx=None, ry=None, rz=None):
  command='InstanceObj '
  command+=selstr(selection1)+','
  if (copies!=None): command+='Copies='+cstr(copies)+','
  if (group!=None): command+='Group='+cstr(group)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  if (rx!=None): command+='RX='+cstr(rx)+','
  if (ry!=None): command+='RY='+cstr(ry)+','
  if (rz!=None): command+='RZ='+cstr(rz)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SET FORCE FIELD TERMS
# =====================
def Interactions(Type):
  command='Interactions '
  command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# PERFORM COLLISION DETECTION TO FIND INTERSECTING OBJECTS
# ========================================================
def IntersectObj(selection1, radiusscale1, selection2, radiusscale2=None):
  command='IntersectObj '
  command+=selstr(selection1)+','
  command+='RadiusScale1='+cstr(radiusscale1)+','
  command+=selstr(selection2)+','
  if (radiusscale2!=None): command+='RadiusScale2='+cstr(radiusscale2)+','
  return(runretval(command[:-1],retvalused()))

# JOIN OBJECTS TO ONE FINAL OBJECT
# ================================
def JoinObj(selection1, selection2, center=None):
  command='JoinObj '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (center!=None): command+='Center='+cstr(center)+','
  return(runretval(command[:-1],retvalused()))

# DELETE SPLIT POINTS (MOLECULE)
# ==============================
def JoinMol(selection1):
  command='JoinMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# DELETE SPLIT POINTS (RESIDUE)
# =============================
def JoinRes(selection1):
  command='JoinRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# DELETE SPLIT POINTS (ATOM)
# ==========================
def JoinAtom(selection1):
  command='JoinAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# CONFIGURE VIRTUAL ON-SCREEN KEYBOARD
# ====================================
def Keyboard(state, layout, size, keysize, alpha, gapalpha, feedback):
  command='Keyboard '
  command+='State='+cstr(state)+','
  command+='Layout='+cstr(layout)+','
  command+='Size='+cstr(size)+','
  command+='KeySize='+cstr(keysize)+','
  command+='Alpha='+cstr(alpha)+','
  command+='GapAlpha='+cstr(gapalpha)+','
  command+='Feedback='+cstr(feedback)+','
  return(runretval(command[:-1],retvalused()))

# REMOVE FRACTIONAL BOND ORDERS
# =============================
def KekulizeBond(selection1, selection2):
  command='KekulizeBond '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE KINETIC ENERGY (ALL OR SELECTED)
# ==========================================
def KinEnergy(currenttime=None):
  command='KinEnergy '
  if (currenttime!=None): command+='CurrentTime='+cstr(currenttime)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE KINETIC ENERGY (ALL)
# ==============================
def KinEnergyAll(currenttime=None):
  command='KinEnergyAll '
  if (currenttime!=None): command+='CurrentTime='+cstr(currenttime)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE KINETIC ENERGY (OBJECT)
# =================================
def KinEnergyObj(selection1, currenttime=None):
  command='KinEnergyObj '
  command+=selstr(selection1)+','
  if (currenttime!=None): command+='CurrentTime='+cstr(currenttime)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE KINETIC ENERGY (MOLECULE)
# ===================================
def KinEnergyMol(selection1, currenttime=None):
  command='KinEnergyMol '
  command+=selstr(selection1)+','
  if (currenttime!=None): command+='CurrentTime='+cstr(currenttime)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE KINETIC ENERGY (RESIDUE)
# ==================================
def KinEnergyRes(selection1, currenttime=None):
  command='KinEnergyRes '
  command+=selstr(selection1)+','
  if (currenttime!=None): command+='CurrentTime='+cstr(currenttime)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE KINETIC ENERGY (ATOM)
# ===============================
def KinEnergyAtom(selection1, currenttime=None):
  command='KinEnergyAtom '
  command+=selstr(selection1)+','
  if (currenttime!=None): command+='CurrentTime='+cstr(currenttime)+','
  return(runretval(command[:-1],retvalused()))

# LABEL ATOM DISTANCES
# ====================
def LabelDis(selection1, selection2, format=None, height=None, color=None, x=None, y=None, z=None, bound=None, radius=None):
  command='LabelDis '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (format!=None): command+='Format='+cstr(format)+','
  if (height!=None): command+='Height='+cstr(height)+','
  if (color!=None): command+='Color='+cstr(color)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  if (bound!=None): command+='Bound='+cstr(bound)+','
  if (radius!=None): command+='Radius='+cstr(radius)+','
  return(runretval(command[:-1],retvalused()))

# SET LABEL PARAMETERS
# ====================
def LabelPar(font, height=None, color=None, ontop=None, shrink=None, fog=None):
  command='LabelPar '
  command+='Font='+cstr(font)+','
  if (height!=None): command+='Height='+cstr(height)+','
  if (color!=None): command+='Color='+cstr(color)+','
  if (ontop!=None): command+='OnTop='+cstr(ontop)+','
  if (shrink!=None): command+='Shrink='+cstr(shrink)+','
  if (fog!=None): command+='Fog='+cstr(fog)+','
  return(runretval(command[:-1],retvalused()))

# ADD LABELS (ALL OR SELECTED)
# ============================
def Label(format, height=None, color=None, x=None, y=None, z=None, convert=None):
  command='Label '
  command+='Format='+cstr(format)+','
  if (height!=None): command+='Height='+cstr(height)+','
  if (color!=None): command+='Color='+cstr(color)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  if (convert!=None): command+='Convert='+cstr(convert)+','
  return(runretval(command[:-1],retvalused()))

# ADD LABELS (ALL)
# ================
def LabelAll(format, height=None, color=None, x=None, y=None, z=None, convert=None):
  command='LabelAll '
  command+='Format='+cstr(format)+','
  if (height!=None): command+='Height='+cstr(height)+','
  if (color!=None): command+='Color='+cstr(color)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  if (convert!=None): command+='Convert='+cstr(convert)+','
  return(runretval(command[:-1],retvalused()))

# ADD LABELS (OBJECT)
# ===================
def LabelObj(selection1, format, height=None, color=None, x=None, y=None, z=None, convert=None):
  command='LabelObj '
  command+=selstr(selection1)+','
  command+='Format='+cstr(format)+','
  if (height!=None): command+='Height='+cstr(height)+','
  if (color!=None): command+='Color='+cstr(color)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  if (convert!=None): command+='Convert='+cstr(convert)+','
  return(runretval(command[:-1],retvalused()))

# ADD LABELS (MOLECULE)
# =====================
def LabelMol(selection1, format, height=None, color=None, x=None, y=None, z=None, convert=None):
  command='LabelMol '
  command+=selstr(selection1)+','
  command+='Format='+cstr(format)+','
  if (height!=None): command+='Height='+cstr(height)+','
  if (color!=None): command+='Color='+cstr(color)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  if (convert!=None): command+='Convert='+cstr(convert)+','
  return(runretval(command[:-1],retvalused()))

# ADD LABELS (SEGMENT)
# ====================
def LabelSeg(selection1, format, height=None, color=None, x=None, y=None, z=None, convert=None):
  command='LabelSeg '
  command+=selstr(selection1)+','
  command+='Format='+cstr(format)+','
  if (height!=None): command+='Height='+cstr(height)+','
  if (color!=None): command+='Color='+cstr(color)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  if (convert!=None): command+='Convert='+cstr(convert)+','
  return(runretval(command[:-1],retvalused()))

# ADD LABELS (RESIDUE)
# ====================
def LabelRes(selection1, format, height=None, color=None, x=None, y=None, z=None, convert=None):
  command='LabelRes '
  command+=selstr(selection1)+','
  command+='Format='+cstr(format)+','
  if (height!=None): command+='Height='+cstr(height)+','
  if (color!=None): command+='Color='+cstr(color)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  if (convert!=None): command+='Convert='+cstr(convert)+','
  return(runretval(command[:-1],retvalused()))

# ADD LABELS (ATOM)
# =================
def LabelAtom(selection1, format, height=None, color=None, x=None, y=None, z=None, convert=None):
  command='LabelAtom '
  command+=selstr(selection1)+','
  command+='Format='+cstr(format)+','
  if (height!=None): command+='Height='+cstr(height)+','
  if (color!=None): command+='Color='+cstr(color)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  if (convert!=None): command+='Convert='+cstr(convert)+','
  return(runretval(command[:-1],retvalused()))

# CONFIGURE THE LIGHT SOURCE
# ==========================
def LightSource(alpha=None, gamma=None, ambience=None, ambience2=None, shadow=None, shadowspeed=None, ambiencefps=None, softshadowfps=None, hardshadowfps=None, cellshadow=None):
  command='LightSource '
  if (alpha!=None): command+='Alpha='+cstr(alpha)+','
  if (gamma!=None): command+='Gamma='+cstr(gamma)+','
  if (ambience!=None): command+='Ambience='+cstr(ambience)+','
  if (ambience2!=None): command+='Ambience2='+cstr(ambience2)+','
  if (shadow!=None): command+='Shadow='+cstr(shadow)+','
  if (shadowspeed!=None): command+='ShadowSpeed='+cstr(shadowspeed)+','
  if (ambiencefps!=None): command+='AmbienceFPS='+cstr(ambiencefps)+','
  if (softshadowfps!=None): command+='SoftShadowFPS='+cstr(softshadowfps)+','
  if (hardshadowfps!=None): command+='HardShadowFPS='+cstr(hardshadowfps)+','
  if (cellshadow!=None): command+='CellShadow='+cstr(cellshadow)+','
  return(runretval(command[:-1],retvalused()))

# SET PER-ATOM LIGHTING (ALL OR SELECTED)
# =======================================
def Light(direction):
  command='Light '
  command+='Direction='+cstr(direction)+','
  return(runretval(command[:-1],retvalused()))

# SET PER-ATOM LIGHTING (ALL)
# ===========================
def LightAll(direction):
  command='LightAll '
  command+='Direction='+cstr(direction)+','
  return(runretval(command[:-1],retvalused()))

# SET PER-ATOM LIGHTING (OBJECT)
# ==============================
def LightObj(selection1, direction):
  command='LightObj '
  command+=selstr(selection1)+','
  command+='Direction='+cstr(direction)+','
  return(runretval(command[:-1],retvalused()))

# SET PER-ATOM LIGHTING (MOLECULE)
# ================================
def LightMol(selection1, direction):
  command='LightMol '
  command+=selstr(selection1)+','
  command+='Direction='+cstr(direction)+','
  return(runretval(command[:-1],retvalused()))

# SET PER-ATOM LIGHTING (RESIDUE)
# ===============================
def LightRes(selection1, direction):
  command='LightRes '
  command+=selstr(selection1)+','
  command+='Direction='+cstr(direction)+','
  return(runretval(command[:-1],retvalused()))

# SET PER-ATOM LIGHTING (ATOM)
# ============================
def LightAtom(selection1, direction):
  command='LightAtom '
  command+=selstr(selection1)+','
  command+='Direction='+cstr(direction)+','
  return(runretval(command[:-1],retvalused()))

# FIND BONDS AUTOMATICALLY (ALL OR SELECTED)
# ==========================================
def Link(deviation=None, Type=None):
  command='Link '
  if (deviation!=None): command+='Deviation='+cstr(deviation)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# FIND BONDS AUTOMATICALLY (ALL)
# ==============================
def LinkAll(deviation=None, Type=None):
  command='LinkAll '
  if (deviation!=None): command+='Deviation='+cstr(deviation)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# FIND BONDS AUTOMATICALLY (OBJECT)
# =================================
def LinkObj(selection1, deviation=None, Type=None):
  command='LinkObj '
  command+=selstr(selection1)+','
  if (deviation!=None): command+='Deviation='+cstr(deviation)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# FIND BONDS AUTOMATICALLY (MOLECULE)
# ===================================
def LinkMol(selection1, deviation=None, Type=None):
  command='LinkMol '
  command+=selstr(selection1)+','
  if (deviation!=None): command+='Deviation='+cstr(deviation)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# FIND BONDS AUTOMATICALLY (RESIDUE)
# ==================================
def LinkRes(selection1, deviation=None, Type=None):
  command='LinkRes '
  command+=selstr(selection1)+','
  if (deviation!=None): command+='Deviation='+cstr(deviation)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# FIND BONDS AUTOMATICALLY (ATOM)
# ===============================
def LinkAtom(selection1, deviation=None, Type=None):
  command='LinkAtom '
  command+=selstr(selection1)+','
  if (deviation!=None): command+='Deviation='+cstr(deviation)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# LIST CONTACTS (OBJECT)
# ======================
def ListConObj(selection1, selection2, cutoff=None, subtract=None, energy=None, exclude=None, occluded=None, sort=None, results=None):
  command='ListConObj '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (subtract!=None): command+='Subtract='+cstr(subtract)+','
  if (energy!=None): command+='Energy='+cstr(energy)+','
  if (exclude!=None): command+='Exclude='+cstr(exclude)+','
  if (occluded!=None): command+='Occluded='+cstr(occluded)+','
  if (sort!=None): command+='Sort='+cstr(sort)+','
  if (results!=None): command+='Results='+cstr(results)+','
  return(runretval(command[:-1],retvalused()))

# LIST CONTACTS (MOLECULE)
# ========================
def ListConMol(selection1, selection2, cutoff=None, subtract=None, energy=None, exclude=None, occluded=None, sort=None, results=None):
  command='ListConMol '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (subtract!=None): command+='Subtract='+cstr(subtract)+','
  if (energy!=None): command+='Energy='+cstr(energy)+','
  if (exclude!=None): command+='Exclude='+cstr(exclude)+','
  if (occluded!=None): command+='Occluded='+cstr(occluded)+','
  if (sort!=None): command+='Sort='+cstr(sort)+','
  if (results!=None): command+='Results='+cstr(results)+','
  return(runretval(command[:-1],retvalused()))

# LIST CONTACTS (RESIDUE)
# =======================
def ListConRes(selection1, selection2, cutoff=None, subtract=None, energy=None, exclude=None, occluded=None, sort=None, results=None):
  command='ListConRes '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (subtract!=None): command+='Subtract='+cstr(subtract)+','
  if (energy!=None): command+='Energy='+cstr(energy)+','
  if (exclude!=None): command+='Exclude='+cstr(exclude)+','
  if (occluded!=None): command+='Occluded='+cstr(occluded)+','
  if (sort!=None): command+='Sort='+cstr(sort)+','
  if (results!=None): command+='Results='+cstr(results)+','
  return(runretval(command[:-1],retvalused()))

# LIST CONTACTS (ATOM)
# ====================
def ListConAtom(selection1, selection2, cutoff=None, subtract=None, energy=None, exclude=None, occluded=None, sort=None, results=None):
  command='ListConAtom '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (subtract!=None): command+='Subtract='+cstr(subtract)+','
  if (energy!=None): command+='Energy='+cstr(energy)+','
  if (exclude!=None): command+='Exclude='+cstr(exclude)+','
  if (occluded!=None): command+='Occluded='+cstr(occluded)+','
  if (sort!=None): command+='Sort='+cstr(sort)+','
  if (results!=None): command+='Results='+cstr(results)+','
  return(runretval(command[:-1],retvalused()))

# LIST DIRECTORY CONTENT
# ======================
def ListDir(filename):
  command='ListDir '
  command+='Filename='+cstr(filename)+','
  return(runretval(command[:-1],retvalused()))

# LIST HYDROGEN BONDS (OBJECT)
# ============================
def ListHBoObj(selection1, selection2, Min=None, results=None):
  command='ListHBoObj '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (Min!=None): command+='Min='+cstr(Min)+','
  if (results!=None): command+='Results='+cstr(results)+','
  return(runretval(command[:-1],retvalused()))

# LIST HYDROGEN BONDS (MOLECULE)
# ==============================
def ListHBoMol(selection1, selection2, Min=None, results=None):
  command='ListHBoMol '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (Min!=None): command+='Min='+cstr(Min)+','
  if (results!=None): command+='Results='+cstr(results)+','
  return(runretval(command[:-1],retvalused()))

# LIST HYDROGEN BONDS (RESIDUE)
# =============================
def ListHBoRes(selection1, selection2, Min=None, results=None):
  command='ListHBoRes '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (Min!=None): command+='Min='+cstr(Min)+','
  if (results!=None): command+='Results='+cstr(results)+','
  return(runretval(command[:-1],retvalused()))

# LIST HYDROGEN BONDS (ATOM)
# ==========================
def ListHBoAtom(selection1, selection2, Min=None, results=None):
  command='ListHBoAtom '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (Min!=None): command+='Min='+cstr(Min)+','
  if (results!=None): command+='Results='+cstr(results)+','
  return(runretval(command[:-1],retvalused()))

# LIST INTERACTIONS (OBJECT)
# ==========================
def ListIntObj(selection1, selection2, Type, cutoff=None, exclude=None, occluded=None, sort=None, results=None):
  command='ListIntObj '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  command+='Type='+cstr(Type)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (exclude!=None): command+='Exclude='+cstr(exclude)+','
  if (occluded!=None): command+='Occluded='+cstr(occluded)+','
  if (sort!=None): command+='Sort='+cstr(sort)+','
  if (results!=None): command+='Results='+cstr(results)+','
  return(runretval(command[:-1],retvalused()))

# LIST INTERACTIONS (MOLECULE)
# ============================
def ListIntMol(selection1, selection2, Type, cutoff=None, exclude=None, occluded=None, sort=None, results=None):
  command='ListIntMol '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  command+='Type='+cstr(Type)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (exclude!=None): command+='Exclude='+cstr(exclude)+','
  if (occluded!=None): command+='Occluded='+cstr(occluded)+','
  if (sort!=None): command+='Sort='+cstr(sort)+','
  if (results!=None): command+='Results='+cstr(results)+','
  return(runretval(command[:-1],retvalused()))

# LIST INTERACTIONS (RESIDUE)
# ===========================
def ListIntRes(selection1, selection2, Type, cutoff=None, exclude=None, occluded=None, sort=None, results=None):
  command='ListIntRes '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  command+='Type='+cstr(Type)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (exclude!=None): command+='Exclude='+cstr(exclude)+','
  if (occluded!=None): command+='Occluded='+cstr(occluded)+','
  if (sort!=None): command+='Sort='+cstr(sort)+','
  if (results!=None): command+='Results='+cstr(results)+','
  return(runretval(command[:-1],retvalused()))

# LIST INTERACTIONS (ATOM)
# ========================
def ListIntAtom(selection1, selection2, Type, cutoff=None, exclude=None, occluded=None, sort=None, results=None):
  command='ListIntAtom '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  command+='Type='+cstr(Type)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (exclude!=None): command+='Exclude='+cstr(exclude)+','
  if (occluded!=None): command+='Occluded='+cstr(occluded)+','
  if (sort!=None): command+='Sort='+cstr(sort)+','
  if (results!=None): command+='Results='+cstr(results)+','
  return(runretval(command[:-1],retvalused()))

# LOAD IMAGE FROM BMP FILE
# ========================
def LoadBmp(filename, transcol=None):
  command='LoadBmp '
  command+='Filename='+cstr(filename)+','
  if (transcol!=None): command+='TransCol='+cstr(transcol)+','
  return(runretval(command[:-1],retvalused()))

# LOAD CIF OR MMCIF FILE
# ======================
def LoadCIF(filename, center=None, correct=None, model=None, missres=None):
  command='LoadCIF '
  command+='Filename='+cstr(filename)+','
  if (center!=None): command+='Center='+cstr(center)+','
  if (correct!=None): command+='Correct='+cstr(correct)+','
  if (model!=None): command+='Model='+cstr(model)+','
  if (missres!=None): command+='MissRes='+cstr(missres)+','
  return(runretval(command[:-1],retvalused()))

# LOAD AND VISUALIZE ELECTROSTATIC POTENTIAL
# ==========================================
def LoadESP(filename, style, Min=None, Max=None):
  command='LoadESP '
  command+='Filename='+cstr(filename)+','
  command+='Style='+cstr(style)+','
  if (Min!=None): command+='Min='+cstr(Min)+','
  if (Max!=None): command+='Max='+cstr(Max)+','
  return(runretval(command[:-1],retvalused()))

# LOAD AND VISUALIZE ELECTROSTATIC POTENTIAL
# ==========================================
# THIS IS ALTERNATIVE 2, WITH DIFFERENT PARAMETERS
def LoadESP2(filename, style, level=None):
  command='LoadESP '
  command+='Filename='+cstr(filename)+','
  command+='Style='+cstr(style)+','
  if (level!=None): command+='Level='+cstr(level)+','
  return(runretval(command[:-1],retvalused()))

# LOAD IMAGE FROM JPG FILE
# ========================
def LoadJPG(filename):
  command='LoadJPG '
  command+='Filename='+cstr(filename)+','
  return(runretval(command[:-1],retvalused()))

# LOAD SIMULATION SNAPSHOT IN MDCRD FORMAT (ALL OR SELECTED)
# ==========================================================
def LoadMDCrd(filename, snapshot=None, assignsec=None):
  command='LoadMDCrd '
  command+='Filename='+cstr(filename)+','
  if (snapshot!=None): command+='Snapshot='+cstr(snapshot)+','
  if (assignsec!=None): command+='assignSec='+cstr(assignsec)+','
  return(runretval(command[:-1],retvalused()))

# LOAD SIMULATION SNAPSHOT IN MDCRD FORMAT (ALL)
# ==============================================
def LoadMDCrdAll(filename, snapshot=None, assignsec=None):
  command='LoadMDCrdAll '
  command+='Filename='+cstr(filename)+','
  if (snapshot!=None): command+='Snapshot='+cstr(snapshot)+','
  if (assignsec!=None): command+='assignSec='+cstr(assignsec)+','
  return(runretval(command[:-1],retvalused()))

# LOAD SIMULATION SNAPSHOT IN MDCRD FORMAT (OBJECT)
# =================================================
def LoadMDCrdObj(selection1, filename, snapshot=None, assignsec=None):
  command='LoadMDCrdObj '
  command+=selstr(selection1)+','
  command+='Filename='+cstr(filename)+','
  if (snapshot!=None): command+='Snapshot='+cstr(snapshot)+','
  if (assignsec!=None): command+='assignSec='+cstr(assignsec)+','
  return(runretval(command[:-1],retvalused()))

# STREAM MOVIE FROM MPEG4 FILE
# ============================
def LoadMPG(filename, loop, selection1):
  command='LoadMPG '
  command+='Filename='+cstr(filename)+','
  command+='Loop='+cstr(loop)+','
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# LOAD DISTANCE, DIHEDRAL AND RDC RESTRAINTS IN NMR EXCHANGE FORMAT
# =================================================================
def LoadNEF(filename, selection1, Class, nameformat):
  command='LoadNEF '
  command+='Filename='+cstr(filename)+','
  command+=selstr(selection1)+','
  command+='Class='+cstr(Class)+','
  command+='NameFormat='+cstr(nameformat)+','
  return(runretval(command[:-1],retvalused()))

# LOAD PROTEIN DATA BANK FILE
# ===========================
def LoadPDB(filename, center=None, correct=None, model=None, download=None, seqres=None):
  command='LoadPDB '
  command+='Filename='+cstr(filename)+','
  if (center!=None): command+='Center='+cstr(center)+','
  if (correct!=None): command+='Correct='+cstr(correct)+','
  if (model!=None): command+='Model='+cstr(model)+','
  if (download!=None): command+='Download='+cstr(download)+','
  if (seqres!=None): command+='SeqRes='+cstr(seqres)+','
  return(runretval(command[:-1],retvalused()))

# LOAD IMAGE FROM PNG FILE
# ========================
def LoadPNG(filename, transcol, selection1):
  command='LoadPNG '
  command+='Filename='+cstr(filename)+','
  command+='TransCol='+cstr(transcol)+','
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# LOAD AMBER PREP TOPOLOGY
# ========================
def LoadPrep(filename, name=None):
  command='LoadPrep '
  command+='Filename='+cstr(filename)+','
  if (name!=None): command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# LOAD COMPLETE SCENE
# ===================
def LoadSce(filename, settings=None):
  command='LoadSce '
  command+='Filename='+cstr(filename)+','
  if (settings!=None): command+='Settings='+cstr(settings)+','
  return(runretval(command[:-1],retvalused()))

# LOAD SIMULATION SNAPSHOT IN SIM FORMAT
# ======================================
def LoadSim(filename, assignsec=None):
  command='LoadSim '
  command+='Filename='+cstr(filename)+','
  if (assignsec!=None): command+='assignSec='+cstr(assignsec)+','
  return(runretval(command[:-1],retvalused()))

# LOAD FORMATTED TABLE
# ====================
def LoadTab(filename, dimensions=None, columns=None, rows=None, pages=None):
  command='LoadTab '
  command+='Filename='+cstr(filename)+','
  if (dimensions!=None): command+='Dimensions='+cstr(dimensions)+','
  if (columns!=None): command+='Columns='+cstr(columns)+','
  if (rows!=None): command+='Rows='+cstr(rows)+','
  if (pages!=None): command+='Pages='+cstr(pages)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# LOAD DISTANCE, DIHEDRAL AND RDC RESTRAINTS IN XPLOR FORMAT
# ==========================================================
def LoadTbl(filename, selection1, Class=None, nameformat=None):
  command='LoadTbl '
  command+='Filename='+cstr(filename)+','
  command+=selstr(selection1)+','
  if (Class!=None): command+='Class='+cstr(Class)+','
  if (nameformat!=None): command+='NameFormat='+cstr(nameformat)+','
  return(runretval(command[:-1],retvalused()))

# LOAD SIMULATION SNAPSHOT IN XTC FORMAT (ALL OR SELECTED)
# ========================================================
def LoadXTC(filename, snapshot=None, assignsec=None):
  command='LoadXTC '
  command+='Filename='+cstr(filename)+','
  if (snapshot!=None): command+='Snapshot='+cstr(snapshot)+','
  if (assignsec!=None): command+='assignSec='+cstr(assignsec)+','
  return(runretval(command[:-1],retvalused()))

# LOAD SIMULATION SNAPSHOT IN XTC FORMAT (ALL)
# ============================================
def LoadXTCAll(filename, snapshot=None, assignsec=None):
  command='LoadXTCAll '
  command+='Filename='+cstr(filename)+','
  if (snapshot!=None): command+='Snapshot='+cstr(snapshot)+','
  if (assignsec!=None): command+='assignSec='+cstr(assignsec)+','
  return(runretval(command[:-1],retvalused()))

# LOAD SIMULATION SNAPSHOT IN XTC FORMAT (OBJECT)
# ===============================================
def LoadXTCObj(selection1, filename, snapshot=None, assignsec=None):
  command='LoadXTCObj '
  command+=selstr(selection1)+','
  command+='Filename='+cstr(filename)+','
  if (snapshot!=None): command+='Snapshot='+cstr(snapshot)+','
  if (assignsec!=None): command+='assignSec='+cstr(assignsec)+','
  return(runretval(command[:-1],retvalused()))

# LOAD YASARA OBJECT
# ==================
def LoadYOb(filename):
  command='LoadYOb '
  command+='Filename='+cstr(filename)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# IMPORT FILE WITH OPENBABEL
# ==========================
def Load(format, filename, center=None, resonate=None, model=None):
  command='Load '
  command=command[:-1]+cstr(format)+' '
  command+='Filename='+cstr(filename)+','
  if (center!=None): command+='Center='+cstr(center)+','
  if (resonate!=None): command+='Resonate='+cstr(resonate)+','
  if (model!=None): command+='Model='+cstr(model)+','
  return(runretval(command[:-1],retvalused()))

# LOG OUTPUT OF NEXT COMMAND
# ==========================
def LogAs(filename, append=None):
  command='LogAs '
  command+='Filename='+cstr(filename)+','
  if (append!=None): command+='append='+cstr(append)+','
  return(runretval(command[:-1],retvalused()))

# LOG OUTPUT OF NEXT COMMAND
# ==========================
# THIS IS ALTERNATIVE 2, WITH DIFFERENT PARAMETERS
def LogAs2(filename, append, noname1):
  command='LogAs '
  command+='Filename='+cstr(filename)+','
  command+='append='+cstr(append)+','
  command+=cstr(noname1)+','
  return(runretval(command[:-1],retvalused()))

# LIST BONDS
# ==========
def ListBond(selection1, selection2, results=None, lenmin=None):
  command='ListBond '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (results!=None): command+='Results='+cstr(results)+','
  if (lenmin!=None): command+='LenMin='+cstr(lenmin)+','
  return(runretval(command[:-1],retvalused()))

# LIST FLOATING ASSIGNMENTS (ALL OR SELECTED)
# ===========================================
def ListFloat(Type=None, format=None):
  command='ListFloat '
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (format!=None): command+='Format='+cstr(format)+','
  return(runretval(command[:-1],retvalused()))

# LIST FLOATING ASSIGNMENTS (ALL)
# ===============================
def ListFloatAll(Type=None, format=None):
  command='ListFloatAll '
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (format!=None): command+='Format='+cstr(format)+','
  return(runretval(command[:-1],retvalused()))

# LIST FLOATING ASSIGNMENTS (OBJECT)
# ==================================
def ListFloatObj(selection1, Type=None, format=None):
  command='ListFloatObj '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (format!=None): command+='Format='+cstr(format)+','
  return(runretval(command[:-1],retvalused()))

# LIST IMAGES
# ===========
def ListImage(selection1):
  command='ListImage '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# LIST RESTRAINTS AND ENERGIES (ALL OR SELECTED)
# ==============================================
def ListRest(Class=None, component=None, format=None, sort=None, dismin=None, dihmin=None, rdcmin=None, objectsmin=None):
  command='ListRest '
  if (Class!=None): command+='Class='+cstr(Class)+','
  if (component!=None): command+='Component='+cstr(component)+','
  if (format!=None): command+='Format='+cstr(format)+','
  if (sort!=None): command+='Sort='+cstr(sort)+','
  if (dismin!=None): command+='DisMin='+cstr(dismin)+','
  if (dihmin!=None): command+='DihMin='+cstr(dihmin)+','
  if (rdcmin!=None): command+='RDCMin='+cstr(rdcmin)+','
  if (objectsmin!=None): command+='ObjectsMin='+cstr(objectsmin)+','
  return(runretval(command[:-1],retvalused()))

# LIST RESTRAINTS AND ENERGIES (ALL)
# ==================================
def ListRestAll(Class=None, component=None, format=None, sort=None, dismin=None, dihmin=None, rdcmin=None, objectsmin=None):
  command='ListRestAll '
  if (Class!=None): command+='Class='+cstr(Class)+','
  if (component!=None): command+='Component='+cstr(component)+','
  if (format!=None): command+='Format='+cstr(format)+','
  if (sort!=None): command+='Sort='+cstr(sort)+','
  if (dismin!=None): command+='DisMin='+cstr(dismin)+','
  if (dihmin!=None): command+='DihMin='+cstr(dihmin)+','
  if (rdcmin!=None): command+='RDCMin='+cstr(rdcmin)+','
  if (objectsmin!=None): command+='ObjectsMin='+cstr(objectsmin)+','
  return(runretval(command[:-1],retvalused()))

# LIST RESTRAINTS AND ENERGIES (OBJECT)
# =====================================
def ListRestObj(selection1, Class=None, component=None, format=None, sort=None, dismin=None, dihmin=None, rdcmin=None, objectsmin=None):
  command='ListRestObj '
  command+=selstr(selection1)+','
  if (Class!=None): command+='Class='+cstr(Class)+','
  if (component!=None): command+='Component='+cstr(component)+','
  if (format!=None): command+='Format='+cstr(format)+','
  if (sort!=None): command+='Sort='+cstr(sort)+','
  if (dismin!=None): command+='DisMin='+cstr(dismin)+','
  if (dihmin!=None): command+='DihMin='+cstr(dihmin)+','
  if (rdcmin!=None): command+='RDCMin='+cstr(rdcmin)+','
  if (objectsmin!=None): command+='ObjectsMin='+cstr(objectsmin)+','
  return(runretval(command[:-1],retvalused()))

# LIST RESTRAINTS AND ENERGIES (MOLECULE)
# =======================================
def ListRestMol(selection1, Class=None, component=None, format=None, sort=None, dismin=None, dihmin=None, rdcmin=None, objectsmin=None):
  command='ListRestMol '
  command+=selstr(selection1)+','
  if (Class!=None): command+='Class='+cstr(Class)+','
  if (component!=None): command+='Component='+cstr(component)+','
  if (format!=None): command+='Format='+cstr(format)+','
  if (sort!=None): command+='Sort='+cstr(sort)+','
  if (dismin!=None): command+='DisMin='+cstr(dismin)+','
  if (dihmin!=None): command+='DihMin='+cstr(dihmin)+','
  if (rdcmin!=None): command+='RDCMin='+cstr(rdcmin)+','
  if (objectsmin!=None): command+='ObjectsMin='+cstr(objectsmin)+','
  return(runretval(command[:-1],retvalused()))

# LIST RESTRAINTS AND ENERGIES (RESIDUE)
# ======================================
def ListRestRes(selection1, Class=None, component=None, format=None, sort=None, dismin=None, dihmin=None, rdcmin=None, objectsmin=None):
  command='ListRestRes '
  command+=selstr(selection1)+','
  if (Class!=None): command+='Class='+cstr(Class)+','
  if (component!=None): command+='Component='+cstr(component)+','
  if (format!=None): command+='Format='+cstr(format)+','
  if (sort!=None): command+='Sort='+cstr(sort)+','
  if (dismin!=None): command+='DisMin='+cstr(dismin)+','
  if (dihmin!=None): command+='DihMin='+cstr(dihmin)+','
  if (rdcmin!=None): command+='RDCMin='+cstr(rdcmin)+','
  if (objectsmin!=None): command+='ObjectsMin='+cstr(objectsmin)+','
  return(runretval(command[:-1],retvalused()))

# LIST RESTRAINTS AND ENERGIES (ATOM)
# ===================================
def ListRestAtom(selection1, Class=None, component=None, format=None, sort=None, dismin=None, dihmin=None, rdcmin=None, objectsmin=None):
  command='ListRestAtom '
  command+=selstr(selection1)+','
  if (Class!=None): command+='Class='+cstr(Class)+','
  if (component!=None): command+='Component='+cstr(component)+','
  if (format!=None): command+='Format='+cstr(format)+','
  if (sort!=None): command+='Sort='+cstr(sort)+','
  if (dismin!=None): command+='DisMin='+cstr(dismin)+','
  if (dihmin!=None): command+='DihMin='+cstr(dihmin)+','
  if (rdcmin!=None): command+='RDCMin='+cstr(rdcmin)+','
  if (objectsmin!=None): command+='ObjectsMin='+cstr(objectsmin)+','
  return(runretval(command[:-1],retvalused()))

# LIST ATOMS MATCHING SMARTS STRING
# =================================
def ListSMARTS(string, selection1=None):
  command='ListSMARTS '
  command+='String='+cstr(string)+','
  if (selection1!=None): command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# LIST ATOMS MATCHING SMILES STRING
# =================================
def ListSMILES(string, selection1=None):
  command='ListSMILES '
  command+='String='+cstr(string)+','
  if (selection1!=None): command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# LIST SELECTION (OBJECT)
# =======================
def ListObj(selection1, format=None, compress=None):
  command='ListObj '
  command+=selstr(selection1)+','
  if (format!=None): command+='Format='+cstr(format)+','
  if (compress!=None): command+='Compress='+cstr(compress)+','
  return(runretval(command[:-1],retvalused()))

# LIST SELECTION (MOLECULE)
# =========================
def ListMol(selection1, format=None, compress=None):
  command='ListMol '
  command+=selstr(selection1)+','
  if (format!=None): command+='Format='+cstr(format)+','
  if (compress!=None): command+='Compress='+cstr(compress)+','
  return(runretval(command[:-1],retvalused()))

# LIST SELECTION (RESIDUE)
# ========================
def ListRes(selection1, format=None, compress=None):
  command='ListRes '
  command+=selstr(selection1)+','
  if (format!=None): command+='Format='+cstr(format)+','
  if (compress!=None): command+='Compress='+cstr(compress)+','
  return(runretval(command[:-1],retvalused()))

# LIST SELECTION (ATOM)
# =====================
def ListAtom(selection1, format=None, compress=None):
  command='ListAtom '
  command+=selstr(selection1)+','
  if (format!=None): command+='Format='+cstr(format)+','
  if (compress!=None): command+='Compress='+cstr(compress)+','
  return(runretval(command[:-1],retvalused()))

# SET LONG RANGE INTERACTIONS
# ===========================
def Longrange(Type):
  command='Longrange '
  command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# CREATE EMPTY IMAGE
# ==================
def MakeImage(name, width=None, height=None, topcol=None, bottomcol=None):
  command='MakeImage '
  command+='Name='+cstr(name)+','
  if (width!=None): command+='Width='+cstr(width)+','
  if (height!=None): command+='Height='+cstr(height)+','
  if (topcol!=None): command+='TopCol='+cstr(topcol)+','
  if (bottomcol!=None): command+='BottomCol='+cstr(bottomcol)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# CREATE OBJECT WITH ATTACHED IMAGE
# =================================
def MakeImageObj(name, selection1, width=None, height=None, depth=None):
  command='MakeImageObj '
  command+='Name='+cstr(name)+','
  command+=selstr(selection1)+','
  if (width!=None): command+='Width='+cstr(width)+','
  if (height!=None): command+='Height='+cstr(height)+','
  if (depth!=None): command+='Depth='+cstr(depth)+','
  return(runretval(command[:-1],retvalused()))

# MAKE A TABLE
# ============
def MakeTab(name, dimensions=None, columns=None, rows=None, pages=None):
  command='MakeTab '
  command+='Name='+cstr(name)+','
  if (dimensions!=None): command+='Dimensions='+cstr(dimensions)+','
  if (columns!=None): command+='Columns='+cstr(columns)+','
  if (rows!=None): command+='Rows='+cstr(rows)+','
  if (pages!=None): command+='Pages='+cstr(pages)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# MAKE TEXT OBJECT TO PRINT 3D LETTERS
# ====================================
def MakeTextObj(name=None, width=None, height=None):
  command='MakeTextObj '
  if (name!=None): command+='Name='+cstr(name)+','
  if (width!=None): command+='Width='+cstr(width)+','
  if (height!=None): command+='Height='+cstr(height)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# CREATE AN EMPTY SECONDARY WINDOW
# ================================
def MakeWin(width=None, height=None, screen=None, fullscreen=None, topcol=None, bottomcol=None):
  command='MakeWin '
  if (width!=None): command+='Width='+cstr(width)+','
  if (height!=None): command+='Height='+cstr(height)+','
  if (screen!=None): command+='Screen='+cstr(screen)+','
  if (fullscreen!=None): command+='FullScreen='+cstr(fullscreen)+','
  if (topcol!=None): command+='TopCol='+cstr(topcol)+','
  if (bottomcol!=None): command+='BottomCol='+cstr(bottomcol)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET ATOMS MARKED WITH FIREFLIES
# ===================================
def MarkAtom(selection1=None, selection2=None, selection3=None, selection4=None, zoom=None):
  command='MarkAtom '
  if (selection1!=None): command+=selstr(selection1)+','
  if (selection2!=None): command+=selstr(selection2)+','
  if (selection3!=None): command+=selstr(selection3)+','
  if (selection4!=None): command+=selstr(selection4)+','
  if (zoom!=None): command+='Zoom='+cstr(zoom)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET ATOMS MARKED WITH FIREFLIES
# ===================================
# THIS IS ALTERNATIVE 2, WITH DIFFERENT PARAMETERS
def MarkAtomNone():
  command='MarkAtom None,'
  return(runretval(command[:-1],retvalused()))

# CALCULATE MASS (ALL OR SELECTED)
# ================================
def Mass():
  command='Mass '
  return(runretval(command[:-1],retvalused()))

# CALCULATE MASS (ALL)
# ====================
def MassAll():
  command='MassAll '
  return(runretval(command[:-1],retvalused()))

# CALCULATE MASS (OBJECT)
# =======================
def MassObj(selection1):
  command='MassObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE MASS (MOLECULE)
# =========================
def MassMol(selection1):
  command='MassMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE MASS (RESIDUE)
# ========================
def MassRes(selection1):
  command='MassRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE MASS (ATOM)
# =====================
def MassAtom(selection1):
  command='MassAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SET MEMORY USAGE AND EXIT
# =========================
def Memory(size):
  command='Memory '
  command+='Size='+cstr(size)+','
  return(runretval(command[:-1],retvalused()))

# SWITCH MENU ON/OFF
# ==================
def Menu(flag):
  command='Menu '
  command+='Flag='+cstr(flag)+','
  return(runretval(command[:-1],retvalused()))

# MOVE POLYGON MESH
# =================
def MoveMesh(selection1, x=None, y=None, z=None):
  command='MoveMesh '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# MOVE ATOMS, OBJECTS OR THE SCENE (ALL OR SELECTED)
# ==================================================
def Move(x=None, y=None, z=None):
  command='Move '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# MOVE ATOMS, OBJECTS OR THE SCENE (ALL)
# ======================================
def MoveAll(x=None, y=None, z=None):
  command='MoveAll '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# MOVE ATOMS, OBJECTS OR THE SCENE (OBJECT)
# =========================================
def MoveObj(selection1, x=None, y=None, z=None):
  command='MoveObj '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# MOVE ATOMS, OBJECTS OR THE SCENE (MOLECULE)
# ===========================================
def MoveMol(selection1, x=None, y=None, z=None):
  command='MoveMol '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# MOVE ATOMS, OBJECTS OR THE SCENE (RESIDUE)
# ==========================================
def MoveRes(selection1, x=None, y=None, z=None):
  command='MoveRes '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# MOVE ATOMS, OBJECTS OR THE SCENE (ATOM)
# =======================================
def MoveAtom(selection1, x=None, y=None, z=None):
  command='MoveAtom '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# SET ENERGY MINIMIZATION STEP
# ============================
def MinStep(size):
  command='MinStep '
  command+='Size='+cstr(size)+','
  return(runretval(command[:-1],retvalused()))

# CONVERT RESIDUE NAMES FROM 1- TO 3-LETTER CODE
# ==============================================
def Name3(sequence):
  command='Name3 '
  command+='Sequence='+cstr(sequence)+','
  return(runretval(command[:-1],retvalused()))

# RENAME FILE
# ===========
def RenameFile(srcfilename=None, dstfilename=None, overwrite=None):
  command='RenameFile '
  if (srcfilename!=None): command+='SrcFilename='+cstr(srcfilename)+','
  if (dstfilename!=None): command+='DstFilename='+cstr(dstfilename)+','
  if (overwrite!=None): command+='Overwrite='+cstr(overwrite)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET NAMES OF OBJECTS, SEGMENTS, MOLECULES, RESIDUES AND ATOMS (OBJECT)
# ==========================================================================
def NameObj(selection1, name=None):
  command='NameObj '
  command+=selstr(selection1)+','
  if (name!=None): command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET NAMES OF OBJECTS, SEGMENTS, MOLECULES, RESIDUES AND ATOMS (MOLECULE)
# ============================================================================
def NameMol(selection1, name=None):
  command='NameMol '
  command+=selstr(selection1)+','
  if (name!=None): command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET NAMES OF OBJECTS, SEGMENTS, MOLECULES, RESIDUES AND ATOMS (SEGMENT)
# ===========================================================================
def NameSeg(selection1, name=None):
  command='NameSeg '
  command+=selstr(selection1)+','
  if (name!=None): command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET NAMES OF OBJECTS, SEGMENTS, MOLECULES, RESIDUES AND ATOMS (RESIDUE)
# ===========================================================================
def NameRes(selection1, name=None):
  command='NameRes '
  command+=selstr(selection1)+','
  if (name!=None): command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET NAMES OF OBJECTS, SEGMENTS, MOLECULES, RESIDUES AND ATOMS (ATOM)
# ========================================================================
def NameAtom(selection1, name=None):
  command='NameAtom '
  command+=selstr(selection1)+','
  if (name!=None): command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# ORIENT OBJECTS NICELY (ALL OR SELECTED)
# =======================================
def NiceOri(axis1=None, axis2=None):
  command='NiceOri '
  if (axis1!=None): command+='Axis1='+cstr(axis1)+','
  if (axis2!=None): command+='Axis2='+cstr(axis2)+','
  return(runretval(command[:-1],retvalused()))

# ORIENT OBJECTS NICELY (ALL)
# ===========================
def NiceOriAll(axis1=None, axis2=None):
  command='NiceOriAll '
  if (axis1!=None): command+='Axis1='+cstr(axis1)+','
  if (axis2!=None): command+='Axis2='+cstr(axis2)+','
  return(runretval(command[:-1],retvalused()))

# ORIENT OBJECTS NICELY (OBJECT)
# ==============================
def NiceOriObj(selection1, axis1=None, axis2=None):
  command='NiceOriObj '
  command+=selstr(selection1)+','
  if (axis1!=None): command+='Axis1='+cstr(axis1)+','
  if (axis2!=None): command+='Axis2='+cstr(axis2)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE OCCUPANCY (ALL OR SELECTED)
# =======================================
def Occup(value=None):
  command='Occup '
  if (value!=None): command+='Value='+cstr(value)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE OCCUPANCY (ALL)
# ===========================
def OccupAll(value=None):
  command='OccupAll '
  if (value!=None): command+='Value='+cstr(value)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE OCCUPANCY (OBJECT)
# ==============================
def OccupObj(selection1, value=None):
  command='OccupObj '
  command+=selstr(selection1)+','
  if (value!=None): command+='Value='+cstr(value)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE OCCUPANCY (MOLECULE)
# ================================
def OccupMol(selection1, value=None):
  command='OccupMol '
  command+=selstr(selection1)+','
  if (value!=None): command+='Value='+cstr(value)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE OCCUPANCY (RESIDUE)
# ===============================
def OccupRes(selection1, value=None):
  command='OccupRes '
  command+=selstr(selection1)+','
  if (value!=None): command+='Value='+cstr(value)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE OCCUPANCY (ATOM)
# ============================
def OccupAtom(selection1, value=None):
  command='OccupAtom '
  command+=selstr(selection1)+','
  if (value!=None): command+='Value='+cstr(value)+','
  return(runretval(command[:-1],retvalused()))

# OLIGOMERIZE OBJECTS TO GENERATE THE BIOLOGICALLY ACTIVE FORM (ALL OR SELECTED)
# ==============================================================================
def Oligomerize(center=None, instance=None):
  command='Oligomerize '
  if (center!=None): command+='Center='+cstr(center)+','
  if (instance!=None): command+='Instance='+cstr(instance)+','
  return(runretval(command[:-1],retvalused()))

# OLIGOMERIZE OBJECTS TO GENERATE THE BIOLOGICALLY ACTIVE FORM (ALL)
# ==================================================================
def OligomerizeAll(center=None, instance=None):
  command='OligomerizeAll '
  if (center!=None): command+='Center='+cstr(center)+','
  if (instance!=None): command+='Instance='+cstr(instance)+','
  return(runretval(command[:-1],retvalused()))

# OLIGOMERIZE OBJECTS TO GENERATE THE BIOLOGICALLY ACTIVE FORM (OBJECT)
# =====================================================================
def OligomerizeObj(selection1, center=None, instance=None):
  command='OligomerizeObj '
  command+=selstr(selection1)+','
  if (center!=None): command+='Center='+cstr(center)+','
  if (instance!=None): command+='Instance='+cstr(instance)+','
  return(runretval(command[:-1],retvalused()))

# SET ERROR ACTION
# ================
def OnError(action):
  command='OnError '
  command+='Action='+cstr(action)+','
  return(runretval(command[:-1],retvalused()))

# OPTIMIZE HYDROGEN BONDING NETWORK (ALL OR SELECTED)
# ===================================================
def OptHyd(method):
  command='OptHyd '
  command+='Method='+cstr(method)+','
  return(runretval(command[:-1],retvalused()))

# OPTIMIZE HYDROGEN BONDING NETWORK (ALL)
# =======================================
def OptHydAll(method):
  command='OptHydAll '
  command+='Method='+cstr(method)+','
  return(runretval(command[:-1],retvalused()))

# OPTIMIZE HYDROGEN BONDING NETWORK (OBJECT)
# ==========================================
def OptHydObj(selection1, method):
  command='OptHydObj '
  command+=selstr(selection1)+','
  command+='Method='+cstr(method)+','
  return(runretval(command[:-1],retvalused()))

# OPTIMIZE CENTRAL OR TERMINAL LOOP
# =================================
def OptimizeLoop(selection1, selection2, samples=None, secstr=None):
  command='OptimizeLoop '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (samples!=None): command+='Samples='+cstr(samples)+','
  if (secstr!=None): command+='SecStr='+cstr(secstr)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# OPTIMIZE MOLECULAR GEOMETRY (ALL OR SELECTED)
# =============================================
def Optimize(method=None, structures=None):
  command='Optimize '
  if (method!=None): command+='Method='+cstr(method)+','
  if (structures!=None): command+='Structures='+cstr(structures)+','
  return(runretval(command[:-1],retvalused()))

# OPTIMIZE MOLECULAR GEOMETRY (ALL)
# =================================
def OptimizeAll(method=None, structures=None):
  command='OptimizeAll '
  if (method!=None): command+='Method='+cstr(method)+','
  if (structures!=None): command+='Structures='+cstr(structures)+','
  return(runretval(command[:-1],retvalused()))

# OPTIMIZE MOLECULAR GEOMETRY (OBJECT)
# ====================================
def OptimizeObj(selection1, method=None, structures=None):
  command='OptimizeObj '
  command+=selstr(selection1)+','
  if (method!=None): command+='Method='+cstr(method)+','
  if (structures!=None): command+='Structures='+cstr(structures)+','
  return(runretval(command[:-1],retvalused()))

# OPTIMIZE MOLECULAR GEOMETRY (MOLECULE)
# ======================================
def OptimizeMol(selection1, method=None, structures=None):
  command='OptimizeMol '
  command+=selstr(selection1)+','
  if (method!=None): command+='Method='+cstr(method)+','
  if (structures!=None): command+='Structures='+cstr(structures)+','
  return(runretval(command[:-1],retvalused()))

# OPTIMIZE MOLECULAR GEOMETRY (RESIDUE)
# =====================================
def OptimizeRes(selection1, method=None, structures=None):
  command='OptimizeRes '
  command+=selstr(selection1)+','
  if (method!=None): command+='Method='+cstr(method)+','
  if (structures!=None): command+='Structures='+cstr(structures)+','
  return(runretval(command[:-1],retvalused()))

# GET VECTOR ORIENTATION
# ======================
def OriVec(x1=None, y1=None, z1=None, x2=None, y2=None, z2=None):
  command='OriVec '
  if (x1!=None): command+='X1='+cstr(x1)+','
  if (y1!=None): command+='Y1='+cstr(y1)+','
  if (z1!=None): command+='Z1='+cstr(z1)+','
  if (x2!=None): command+='X2='+cstr(x2)+','
  if (y2!=None): command+='Y2='+cstr(y2)+','
  if (z2!=None): command+='Z2='+cstr(z2)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET OBJECT OR SCENE ORIENTATION (ALL OR SELECTED)
# =====================================================
def Ori(alpha=None, beta=None, gamma=None):
  command='Ori '
  if (alpha!=None): command+='Alpha='+cstr(alpha)+','
  if (beta!=None): command+='Beta='+cstr(beta)+','
  if (gamma!=None): command+='Gamma='+cstr(gamma)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET OBJECT OR SCENE ORIENTATION (ALL)
# =========================================
def OriAll(alpha=None, beta=None, gamma=None):
  command='OriAll '
  if (alpha!=None): command+='Alpha='+cstr(alpha)+','
  if (beta!=None): command+='Beta='+cstr(beta)+','
  if (gamma!=None): command+='Gamma='+cstr(gamma)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET OBJECT OR SCENE ORIENTATION (OBJECT)
# ============================================
def OriObj(selection1, alpha=None, beta=None, gamma=None):
  command='OriObj '
  command+=selstr(selection1)+','
  if (alpha!=None): command+='Alpha='+cstr(alpha)+','
  if (beta!=None): command+='Beta='+cstr(beta)+','
  if (gamma!=None): command+='Gamma='+cstr(gamma)+','
  return(runretval(command[:-1],retvalused()))

# SET PERMISSIONS OF THE YASARA INSTALL DIRECTORY
# ===============================================
def PermitAccess():
  command='PermitAccess '
  return(runretval(command[:-1],retvalused()))

# SET/GET DEFAULT PH
# ==================
def pH(value=None, update=None):
  command='pH '
  if (value!=None): command+='Value='+cstr(value)+','
  if (update!=None): command+='update='+cstr(update)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SET/GET RESIDUE PKA
# ===================
def pKaRes(selection1, value=None):
  command='pKaRes '
  command+=selstr(selection1)+','
  if (value!=None): command+='value='+cstr(value)+','
  return(runretval(command[:-1],retvalused()))

# PLAY BACK MACRO
# ===============
def PlayMacro(filename, label, onstartup=None):
  command='PlayMacro '
  command+='Filename='+cstr(filename)+','
  command+='Label='+cstr(label)+','
  if (onstartup!=None): command+='OnStartup='+cstr(onstartup)+','
  return(runretval(command[:-1],retvalused()))

# SET STYLE OF MOUSE POINTER
# ==========================
def PointerStyle(Type=None):
  command='PointerStyle '
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# SET POINT AND LINE RADIUS AND PLASTICITY IN WIRE FRAMES
# =======================================================
def PointPar(radius=None, plastic=None):
  command='PointPar '
  if (radius!=None): command+='Radius='+cstr(radius)+','
  if (plastic!=None): command+='plastic='+cstr(plastic)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET POLYGON SMOOTHNESS AND REFLECTIVITY
# ===========================================
def PolygonPar(smoothness=None, reflection=None):
  command='PolygonPar '
  if (smoothness!=None): command+='Smoothness='+cstr(smoothness)+','
  if (reflection!=None): command+='Reflection='+cstr(reflection)+','
  return(runretval(command[:-1],retvalused()))

# POLYMERIZE OBJECTS
# ==================
def Polymerize(selection1, selection2, copies=None, dihedral=None):
  command='Polymerize '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (copies!=None): command+='Copies='+cstr(copies)+','
  if (dihedral!=None): command+='Dihedral='+cstr(dihedral)+','
  return(runretval(command[:-1],retvalused()))

# POSITION AND JUSTIFY TEXT
# =========================
def PosText(x=None, y=None, justify=None):
  command='PosText '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (justify!=None): command+='justify='+cstr(justify)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET ATOM POSITIONS (MOLECULE)
# =================================
def PosMol(selection1, x=None, y=None, z=None, coordsys=None, mean=None):
  command='PosMol '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  if (coordsys!=None): command+='CoordSys='+cstr(coordsys)+','
  if (mean!=None): command+='Mean='+cstr(mean)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET ATOM POSITIONS (RESIDUE)
# ================================
def PosRes(selection1, x=None, y=None, z=None, coordsys=None, mean=None):
  command='PosRes '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  if (coordsys!=None): command+='CoordSys='+cstr(coordsys)+','
  if (mean!=None): command+='Mean='+cstr(mean)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET ATOM POSITIONS (ATOM)
# =============================
def PosAtom(selection1, x=None, y=None, z=None, coordsys=None, mean=None):
  command='PosAtom '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  if (coordsys!=None): command+='CoordSys='+cstr(coordsys)+','
  if (mean!=None): command+='Mean='+cstr(mean)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET OBJECT OR SCENE POSITION AND ORIENTATION (ALL OR SELECTED)
# ==================================================================
def PosOri(x=None, y=None, z=None, alpha=None, beta=None, gamma=None):
  command='PosOri '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  if (alpha!=None): command+='Alpha='+cstr(alpha)+','
  if (beta!=None): command+='Beta='+cstr(beta)+','
  if (gamma!=None): command+='Gamma='+cstr(gamma)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET OBJECT OR SCENE POSITION AND ORIENTATION (ALL)
# ======================================================
def PosOriAll(x=None, y=None, z=None, alpha=None, beta=None, gamma=None):
  command='PosOriAll '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  if (alpha!=None): command+='Alpha='+cstr(alpha)+','
  if (beta!=None): command+='Beta='+cstr(beta)+','
  if (gamma!=None): command+='Gamma='+cstr(gamma)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET OBJECT OR SCENE POSITION AND ORIENTATION (OBJECT)
# =========================================================
def PosOriObj(selection1, x=None, y=None, z=None, alpha=None, beta=None, gamma=None):
  command='PosOriObj '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  if (alpha!=None): command+='Alpha='+cstr(alpha)+','
  if (beta!=None): command+='Beta='+cstr(beta)+','
  if (gamma!=None): command+='Gamma='+cstr(gamma)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET OBJECT OR SCENE POSITION (ALL OR SELECTED)
# ==================================================
def Pos(x=None, y=None, z=None):
  command='Pos '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET OBJECT OR SCENE POSITION (ALL)
# ======================================
def PosAll(x=None, y=None, z=None):
  command='PosAll '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET OBJECT OR SCENE POSITION (OBJECT)
# =========================================
def PosObj(selection1, x=None, y=None, z=None):
  command='PosObj '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# SET PRESSURE CONTROL
# ====================
def PressureCtrl(Type, pressure=None, name=None, density=None, axis=None):
  command='PressureCtrl '
  command+='Type='+cstr(Type)+','
  if (pressure!=None): command+='Pressure='+cstr(pressure)+','
  if (name!=None): command+='Name='+cstr(name)+','
  if (density!=None): command+='Density='+cstr(density)+','
  if (axis!=None): command+='Axis='+cstr(axis)+','
  return(runretval(command[:-1],retvalused()))

# PRINT TEXT
# ==========
def Print(text, convert=None):
  command='Print '
  command+='Text='+cstr(text,1)+','
  if (convert!=None): command+='Convert='+cstr(convert)+','
  return(runretval(command[:-1],retvalused()))

# PRINT TO CONSOLE
# ================
def PrintCon():
  command='PrintCon '
  return(runretval(command[:-1],retvalused()))

# PRINT TO HEAD UP DISPLAY
# ========================
def PrintHUD():
  command='PrintHUD '
  return(runretval(command[:-1],retvalused()))

# PRINT TO IMAGE
# ==============
def PrintImage(selection1):
  command='PrintImage '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# PRINT TO TEXT OBJECT
# ====================
def PrintObj(selection1):
  command='PrintObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# PRINT TO SECONDARY WINDOW
# =========================
def PrintWin():
  command='PrintWin '
  return(runretval(command[:-1],retvalused()))

# SET/GET NUMBER OF PROCESSORS TO USE
# ===================================
def Processors(cputhreads=None, gpu=None):
  command='Processors '
  if (cputhreads!=None): command+='CPUThreads='+cstr(cputhreads)+','
  if (gpu!=None): command+='GPU='+cstr(gpu)+','
  return(runretval(command[:-1],retvalused()))

# SET PERSPECTIVE OR PARALLEL PROJECTION
# ======================================
def Projection(Type):
  command='Projection '
  command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE PROPERTY VALUE (ALL OR SELECTED)
# ============================================
def Prop(value=None):
  command='Prop '
  if (value!=None): command+='value='+cstr(value)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE PROPERTY VALUE (ALL)
# ================================
def PropAll(value=None):
  command='PropAll '
  if (value!=None): command+='value='+cstr(value)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE PROPERTY VALUE (OBJECT)
# ===================================
def PropObj(selection1, value=None):
  command='PropObj '
  command+=selstr(selection1)+','
  if (value!=None): command+='value='+cstr(value)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE PROPERTY VALUE (MOLECULE)
# =====================================
def PropMol(selection1, value=None):
  command='PropMol '
  command+=selstr(selection1)+','
  if (value!=None): command+='value='+cstr(value)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE PROPERTY VALUE (RESIDUE)
# ====================================
def PropRes(selection1, value=None):
  command='PropRes '
  command+=selstr(selection1)+','
  if (value!=None): command+='value='+cstr(value)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE PROPERTY VALUE (ATOM)
# =================================
def PropAtom(selection1, value=None):
  command='PropAtom '
  command+=selstr(selection1)+','
  if (value!=None): command+='value='+cstr(value)+','
  return(runretval(command[:-1],retvalused()))

# PRINT WORKING DIRECTORY
# =======================
def PWD():
  command='PWD '
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SET QUANTUM MECHANICS METHOD
# ============================
def QuantumMechanics(method):
  command='QuantumMechanics '
  command+='Method='+cstr(method)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE THE RADIUS (ALL OR SELECTED)
# ======================================
def Radius(center=None, Type=None):
  command='Radius '
  if (center!=None): command+='Center='+cstr(center)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE THE RADIUS (ALL)
# ==========================
def RadiusAll(center=None, Type=None):
  command='RadiusAll '
  if (center!=None): command+='Center='+cstr(center)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE THE RADIUS (OBJECT)
# =============================
def RadiusObj(selection1, center=None, Type=None):
  command='RadiusObj '
  command+=selstr(selection1)+','
  if (center!=None): command+='Center='+cstr(center)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE THE RADIUS (MOLECULE)
# ===============================
def RadiusMol(selection1, center=None, Type=None):
  command='RadiusMol '
  command+=selstr(selection1)+','
  if (center!=None): command+='Center='+cstr(center)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE THE RADIUS (RESIDUE)
# ==============================
def RadiusRes(selection1, center=None, Type=None):
  command='RadiusRes '
  command+=selstr(selection1)+','
  if (center!=None): command+='Center='+cstr(center)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE THE RADIUS (ATOM)
# ===========================
def RadiusAtom(selection1, center=None, Type=None):
  command='RadiusAtom '
  command+=selstr(selection1)+','
  if (center!=None): command+='Center='+cstr(center)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# DISPLAY ERROR MESSAGE
# =====================
def RaiseError(text=None):
  command='RaiseError '
  if (text!=None): command+='Text='+cstr(text,1)+','
  return(runretval(command[:-1],retvalused()))

# CREATE RAYTRACED SCREENSHOT USING POVRAY
# ========================================
def RayTrace(filename, x=None, y=None, zoom=None, atoms=None, labelshadow=None, secalpha=None, display=None, outline=None, background=None):
  command='RayTrace '
  command+='Filename='+cstr(filename)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (zoom!=None): command+='zoom='+cstr(zoom)+','
  if (atoms!=None): command+='Atoms='+cstr(atoms)+','
  if (labelshadow!=None): command+='LabelShadow='+cstr(labelshadow)+','
  if (secalpha!=None): command+='SecAlpha='+cstr(secalpha)+','
  if (display!=None): command+='Display='+cstr(display)+','
  if (outline!=None): command+='Outline='+cstr(outline)+','
  if (background!=None): command+='Background='+cstr(background)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# CALCULATE RADIAL DISTRIBUTION FUNCTION
# ======================================
def RDF(normbins=None):
  command='RDF '
  if (normbins!=None): command+='NormBins='+cstr(normbins)+','
  return(runretval(command[:-1],retvalused()))

# RECORD ALL CONSOLE OUTPUT IN A LOG FILE
# =======================================
def RecordLog(filename, append=None):
  command='RecordLog '
  command+='Filename='+cstr(filename)+','
  if (append!=None): command+='append='+cstr(append)+','
  return(runretval(command[:-1],retvalused()))

# REGULARIZE COVALENT GEOMETRY (ALL OR SELECTED)
# ==============================================
def Regularize(sigmas=None):
  command='Regularize '
  if (sigmas!=None): command+='Sigmas='+cstr(sigmas)+','
  return(runretval(command[:-1],retvalused()))

# REGULARIZE COVALENT GEOMETRY (ALL)
# ==================================
def RegularizeAll(sigmas=None):
  command='RegularizeAll '
  if (sigmas!=None): command+='Sigmas='+cstr(sigmas)+','
  return(runretval(command[:-1],retvalused()))

# REGULARIZE COVALENT GEOMETRY (OBJECT)
# =====================================
def RegularizeObj(selection1, sigmas=None):
  command='RegularizeObj '
  command+=selstr(selection1)+','
  if (sigmas!=None): command+='Sigmas='+cstr(sigmas)+','
  return(runretval(command[:-1],retvalused()))

# REMOVE FROM ENVIRONMENT FOR SURFACE CALCULATIONS (ALL OR SELECTED)
# ==================================================================
def RemoveEnv():
  command='RemoveEnv '
  return(runretval(command[:-1],retvalused()))

# REMOVE FROM ENVIRONMENT FOR SURFACE CALCULATIONS (ALL)
# ======================================================
def RemoveEnvAll():
  command='RemoveEnvAll '
  return(runretval(command[:-1],retvalused()))

# REMOVE FROM ENVIRONMENT FOR SURFACE CALCULATIONS (OBJECT)
# =========================================================
def RemoveEnvObj(selection1):
  command='RemoveEnvObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# REMOVE FROM ENVIRONMENT FOR SURFACE CALCULATIONS (MOLECULE)
# ===========================================================
def RemoveEnvMol(selection1):
  command='RemoveEnvMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# REMOVE FROM ENVIRONMENT FOR SURFACE CALCULATIONS (RESIDUE)
# ==========================================================
def RemoveEnvRes(selection1):
  command='RemoveEnvRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# REMOVE FROM ENVIRONMENT FOR SURFACE CALCULATIONS (ATOM)
# =======================================================
def RemoveEnvAtom(selection1):
  command='RemoveEnvAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# REMOVE OBJECTS FROM THE SOUP (ALL OR SELECTED)
# ==============================================
def Remove():
  command='Remove '
  return(runretval(command[:-1],retvalused()))

# REMOVE OBJECTS FROM THE SOUP (ALL)
# ==================================
def RemoveAll():
  command='RemoveAll '
  return(runretval(command[:-1],retvalused()))

# REMOVE OBJECTS FROM THE SOUP (OBJECT)
# =====================================
def RemoveObj(selection1):
  command='RemoveObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# PREDICT SECONDARY STRUCTURE (ALL OR SELECTED)
# =============================================
def PredSecStr(method=None):
  command='PredSecStr '
  if (method!=None): command+='Method='+cstr(method)+','
  return(runretval(command[:-1],retvalused()))

# PREDICT SECONDARY STRUCTURE (ALL)
# =================================
def PredSecStrAll(method=None):
  command='PredSecStrAll '
  if (method!=None): command+='Method='+cstr(method)+','
  return(runretval(command[:-1],retvalused()))

# PREDICT SECONDARY STRUCTURE (OBJECT)
# ====================================
def PredSecStrObj(selection1, method=None):
  command='PredSecStrObj '
  command+=selstr(selection1)+','
  if (method!=None): command+='Method='+cstr(method)+','
  return(runretval(command[:-1],retvalused()))

# PREDICT SECONDARY STRUCTURE (MOLECULE)
# ======================================
def PredSecStrMol(selection1, method=None):
  command='PredSecStrMol '
  command+=selstr(selection1)+','
  if (method!=None): command+='Method='+cstr(method)+','
  return(runretval(command[:-1],retvalused()))

# PREDICT SECONDARY STRUCTURE (RESIDUE)
# =====================================
def PredSecStrRes(selection1, method=None):
  command='PredSecStrRes '
  command+=selstr(selection1)+','
  if (method!=None): command+='Method='+cstr(method)+','
  return(runretval(command[:-1],retvalused()))

# SET YANACONDA RANDOM NUMBER SEED
# ================================
def RandomSeed(number):
  command='RandomSeed '
  command+='Number='+cstr(number)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SET/GET RENDERING LIBRARY AND GPU
# =================================
def Renderer(library=None, gpu=None):
  command='Renderer '
  if (library!=None): command+='Library='+cstr(library)+','
  if (gpu!=None): command+='GPU='+cstr(gpu)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# NUMBER OBJECTS (ALL OR SELECTED)
# ================================
def Number(first=None):
  command='Number '
  if (first!=None): command+='first='+cstr(first)+','
  return(runretval(command[:-1],retvalused()))

# NUMBER OBJECTS (ALL)
# ====================
def NumberAll(first=None):
  command='NumberAll '
  if (first!=None): command+='first='+cstr(first)+','
  return(runretval(command[:-1],retvalused()))

# NUMBER OBJECTS (OBJECT)
# =======================
def NumberObj(selection1, first=None):
  command='NumberObj '
  command+=selstr(selection1)+','
  if (first!=None): command+='first='+cstr(first)+','
  return(runretval(command[:-1],retvalused()))

# NUMBER RESIDUES
# ===============
def NumberRes(selection1, first=None, inscode=None, increment=None):
  command='NumberRes '
  command+=selstr(selection1)+','
  if (first!=None): command+='First='+cstr(first)+','
  if (inscode!=None): command+='InsCode='+cstr(inscode)+','
  if (increment!=None): command+='Increment='+cstr(increment)+','
  return(runretval(command[:-1],retvalused()))

# NUMBER ATOMS
# ============
def NumberAtom(selection1, first=None):
  command='NumberAtom '
  command+=selstr(selection1)+','
  if (first!=None): command+='First='+cstr(first)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET KEYBOARD REPEAT RATE
# ============================
def RepeatKey(delay=None, interval=None):
  command='RepeatKey '
  if (delay!=None): command+='Delay='+cstr(delay)+','
  if (interval!=None): command+='Interval='+cstr(interval)+','
  return(runretval(command[:-1],retvalused()))

# REPLACE RESIDUES
# ================
def ReplaceRes(selection1, selection2, superpose=None, addbonds=None, renumberres=None, renamemol=None):
  command='ReplaceRes '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (superpose!=None): command+='Superpose='+cstr(superpose)+','
  if (addbonds!=None): command+='AddBonds='+cstr(addbonds)+','
  if (renumberres!=None): command+='RenumberRes='+cstr(renumberres)+','
  if (renamemol!=None): command+='RenameMol='+cstr(renamemol)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET OBJECT X-RAY RESOLUTION (ALL OR SELECTED)
# =================================================
def Resolution(value=None):
  command='Resolution '
  if (value!=None): command+='Value='+cstr(value)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET OBJECT X-RAY RESOLUTION (ALL)
# =====================================
def ResolutionAll(value=None):
  command='ResolutionAll '
  if (value!=None): command+='Value='+cstr(value)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET OBJECT X-RAY RESOLUTION (OBJECT)
# ========================================
def ResolutionObj(selection1, value=None):
  command='ResolutionObj '
  command+=selstr(selection1)+','
  if (value!=None): command+='Value='+cstr(value)+','
  return(runretval(command[:-1],retvalused()))

# INTRODUCE FRACTIONAL BOND ORDERS
# ================================
def ResonateBond(selection1, selection2):
  command='ResonateBond '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE RESTRAINT ENERGIES (ALL OR SELECTED)
# ==============================================
def RestEnergy(component=None):
  command='RestEnergy '
  if (component!=None): command+='Component='+cstr(component)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE RESTRAINT ENERGIES (ALL)
# ==================================
def RestEnergyAll(component=None):
  command='RestEnergyAll '
  if (component!=None): command+='Component='+cstr(component)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE RESTRAINT ENERGIES (OBJECT)
# =====================================
def RestEnergyObj(selection1, component=None):
  command='RestEnergyObj '
  command+=selstr(selection1)+','
  if (component!=None): command+='Component='+cstr(component)+','
  return(runretval(command[:-1],retvalused()))

# GET RESTRAINT VIOLATION STATISTICS (ALL OR SELECTED)
# ====================================================
def RestViol():
  command='RestViol '
  return(runretval(command[:-1],retvalused()))

# GET RESTRAINT VIOLATION STATISTICS (ALL)
# ========================================
def RestViolAll():
  command='RestViolAll '
  return(runretval(command[:-1],retvalused()))

# GET RESTRAINT VIOLATION STATISTICS (OBJECT)
# ===========================================
def RestViolObj(selection1):
  command='RestViolObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# RESTRAIN DISTANCE
# =================
def RestrainDis(selection1, selection2, Class, d, dminus, dplus):
  command='RestrainDis '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  command+='Class='+cstr(Class)+','
  command+='d='+cstr(d)+','
  command+='dminus='+cstr(dminus)+','
  command+='dplus='+cstr(dplus)+','
  return(runretval(command[:-1],retvalused()))

# RESTRAIN DIHEDRAL ANGLE
# =======================
def RestrainDih(selection1, selection2, selection3, selection4, Class, c, equil, delta, exponent=None):
  command='RestrainDih '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  command+=selstr(selection3)+','
  command+=selstr(selection4)+','
  command+='Class='+cstr(Class)+','
  command+='C='+cstr(c)+','
  command+='Equil='+cstr(equil)+','
  command+='Delta='+cstr(delta)+','
  if (exponent!=None): command+='Exponent='+cstr(exponent)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET RESTRAINING PARAMETERS
# ==============================
def RestrainPar(average=None, ceil=None, dismin=None, monomers=None, joindis=None, floatgroups=None, showamb=None, periodic=None):
  command='RestrainPar '
  if (average!=None): command+='Average='+cstr(average)+','
  if (ceil!=None): command+='Ceil='+cstr(ceil)+','
  if (dismin!=None): command+='DisMin='+cstr(dismin)+','
  if (monomers!=None): command+='Monomers='+cstr(monomers)+','
  if (joindis!=None): command+='JoinDis='+cstr(joindis)+','
  if (floatgroups!=None): command+='FloatGroups='+cstr(floatgroups)+','
  if (showamb!=None): command+='ShowAmb='+cstr(showamb)+','
  if (periodic!=None): command+='Periodic='+cstr(periodic)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET RESTRAINING POTENTIAL FUNCTIONS
# =======================================
def RestrainPot(name=None, sqconstant=None, sqoffset=None, sqexponent=None, rswitch=None, soexponent=None, asymptote=None, gamma=None, rdcforceconst=None, rdcerrorscale=None, update=None):
  command='RestrainPot '
  if (name!=None): command+='Name='+cstr(name)+','
  if (sqconstant!=None): command+='SqConstant='+cstr(sqconstant)+','
  if (sqoffset!=None): command+='SqOffset='+cstr(sqoffset)+','
  if (sqexponent!=None): command+='SqExponent='+cstr(sqexponent)+','
  if (rswitch!=None): command+='rSwitch='+cstr(rswitch)+','
  if (soexponent!=None): command+='SoExponent='+cstr(soexponent)+','
  if (asymptote!=None): command+='Asymptote='+cstr(asymptote)+','
  if (gamma!=None): command+='Gamma='+cstr(gamma)+','
  if (rdcforceconst!=None): command+='RDCForceConst='+cstr(rdcforceconst)+','
  if (rdcerrorscale!=None): command+='RDCErrorScale='+cstr(rdcerrorscale)+','
  if (update!=None): command+='Update='+cstr(update)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE ROOT MEAN SQUARE FLUCTUATIONS AND B-FACTORS (MOLECULE)
# ================================================================
def RMSFMol(selection1, unit=None):
  command='RMSFMol '
  command+=selstr(selection1)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE ROOT MEAN SQUARE FLUCTUATIONS AND B-FACTORS (RESIDUE)
# ===============================================================
def RMSFRes(selection1, unit=None):
  command='RMSFRes '
  command+=selstr(selection1)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE ROOT MEAN SQUARE FLUCTUATIONS AND B-FACTORS (ATOM)
# ============================================================
def RMSFAtom(selection1, unit=None):
  command='RMSFAtom '
  command+=selstr(selection1)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE RMSDS (OBJECT)
# ========================
def RMSDObj(selection1, selection2, match=None, flip=None, unit=None):
  command='RMSDObj '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (match!=None): command+='Match='+cstr(match)+','
  if (flip!=None): command+='Flip='+cstr(flip)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE RMSDS (MOLECULE)
# ==========================
def RMSDMol(selection1, selection2, match=None, flip=None, unit=None):
  command='RMSDMol '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (match!=None): command+='Match='+cstr(match)+','
  if (flip!=None): command+='Flip='+cstr(flip)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE RMSDS (RESIDUE)
# =========================
def RMSDRes(selection1, selection2, match=None, flip=None, unit=None):
  command='RMSDRes '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (match!=None): command+='Match='+cstr(match)+','
  if (flip!=None): command+='Flip='+cstr(flip)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE RMSDS (ATOM)
# ======================
def RMSDAtom(selection1, selection2, match=None, flip=None, unit=None):
  command='RMSDAtom '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (match!=None): command+='Match='+cstr(match)+','
  if (flip!=None): command+='Flip='+cstr(flip)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# ROTATE ATOMS, OBJECTS OR THE SCENE (ALL OR SELECTED)
# ====================================================
def Rotate(x=None, y=None, z=None):
  command='Rotate '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# ROTATE ATOMS, OBJECTS OR THE SCENE (ALL)
# ========================================
def RotateAll(x=None, y=None, z=None):
  command='RotateAll '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# ROTATE ATOMS, OBJECTS OR THE SCENE (OBJECT)
# ===========================================
def RotateObj(selection1, x=None, y=None, z=None):
  command='RotateObj '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# ROTATE ATOMS, OBJECTS OR THE SCENE (MOLECULE)
# =============================================
def RotateMol(selection1, x=None, y=None, z=None):
  command='RotateMol '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# ROTATE ATOMS, OBJECTS OR THE SCENE (RESIDUE)
# ============================================
def RotateRes(selection1, x=None, y=None, z=None):
  command='RotateRes '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# ROTATE ATOMS, OBJECTS OR THE SCENE (ATOM)
# =========================================
def RotateAtom(selection1, x=None, y=None, z=None):
  command='RotateAtom '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# ROTATE ATOMS ABOUT A SPECIFIED AXIS (ALL OR SELECTED)
# =====================================================
def RotAxis(px, py, pz, dx, dy, dz, angle):
  command='RotAxis '
  command+='PX='+cstr(px)+','
  command+='PY='+cstr(py)+','
  command+='PZ='+cstr(pz)+','
  command+='DX='+cstr(dx)+','
  command+='DY='+cstr(dy)+','
  command+='DZ='+cstr(dz)+','
  command+='Angle='+cstr(angle)+','
  return(runretval(command[:-1],retvalused()))

# ROTATE ATOMS ABOUT A SPECIFIED AXIS (ALL)
# =========================================
def RotAxisAll(px, py, pz, dx, dy, dz, angle):
  command='RotAxisAll '
  command+='PX='+cstr(px)+','
  command+='PY='+cstr(py)+','
  command+='PZ='+cstr(pz)+','
  command+='DX='+cstr(dx)+','
  command+='DY='+cstr(dy)+','
  command+='DZ='+cstr(dz)+','
  command+='Angle='+cstr(angle)+','
  return(runretval(command[:-1],retvalused()))

# ROTATE ATOMS ABOUT A SPECIFIED AXIS (OBJECT)
# ============================================
def RotAxisObj(selection1, px, py, pz, dx, dy, dz, angle):
  command='RotAxisObj '
  command+=selstr(selection1)+','
  command+='PX='+cstr(px)+','
  command+='PY='+cstr(py)+','
  command+='PZ='+cstr(pz)+','
  command+='DX='+cstr(dx)+','
  command+='DY='+cstr(dy)+','
  command+='DZ='+cstr(dz)+','
  command+='Angle='+cstr(angle)+','
  return(runretval(command[:-1],retvalused()))

# ROTATE ATOMS ABOUT A SPECIFIED AXIS (MOLECULE)
# ==============================================
def RotAxisMol(selection1, px, py, pz, dx, dy, dz, angle):
  command='RotAxisMol '
  command+=selstr(selection1)+','
  command+='PX='+cstr(px)+','
  command+='PY='+cstr(py)+','
  command+='PZ='+cstr(pz)+','
  command+='DX='+cstr(dx)+','
  command+='DY='+cstr(dy)+','
  command+='DZ='+cstr(dz)+','
  command+='Angle='+cstr(angle)+','
  return(runretval(command[:-1],retvalused()))

# ROTATE ATOMS ABOUT A SPECIFIED AXIS (RESIDUE)
# =============================================
def RotAxisRes(selection1, px, py, pz, dx, dy, dz, angle):
  command='RotAxisRes '
  command+=selstr(selection1)+','
  command+='PX='+cstr(px)+','
  command+='PY='+cstr(py)+','
  command+='PZ='+cstr(pz)+','
  command+='DX='+cstr(dx)+','
  command+='DY='+cstr(dy)+','
  command+='DZ='+cstr(dz)+','
  command+='Angle='+cstr(angle)+','
  return(runretval(command[:-1],retvalused()))

# ROTATE ATOMS ABOUT A SPECIFIED AXIS (ATOM)
# ==========================================
def RotAxisAtom(selection1, px, py, pz, dx, dy, dz, angle):
  command='RotAxisAtom '
  command+=selstr(selection1)+','
  command+='PX='+cstr(px)+','
  command+='PY='+cstr(py)+','
  command+='PZ='+cstr(pz)+','
  command+='DX='+cstr(dx)+','
  command+='DY='+cstr(dy)+','
  command+='DZ='+cstr(dz)+','
  command+='Angle='+cstr(angle)+','
  return(runretval(command[:-1],retvalused()))

# RUN MOPAC FOR CUSTOM CALCULATION (ALL OR SELECTED)
# ==================================================
def RunMOPAC(keywords):
  command='RunMOPAC '
  command+='Keywords='+cstr(keywords)+','
  return(runretval(command[:-1],retvalused()))

# RUN MOPAC FOR CUSTOM CALCULATION (ALL)
# ======================================
def RunMOPACAll(keywords):
  command='RunMOPACAll '
  command+='Keywords='+cstr(keywords)+','
  return(runretval(command[:-1],retvalused()))

# RUN MOPAC FOR CUSTOM CALCULATION (OBJECT)
# =========================================
def RunMOPACObj(selection1, keywords):
  command='RunMOPACObj '
  command+=selstr(selection1)+','
  command+='Keywords='+cstr(keywords)+','
  return(runretval(command[:-1],retvalused()))

# RUN MOPAC FOR CUSTOM CALCULATION (MOLECULE)
# ===========================================
def RunMOPACMol(selection1, keywords):
  command='RunMOPACMol '
  command+=selstr(selection1)+','
  command+='Keywords='+cstr(keywords)+','
  return(runretval(command[:-1],retvalused()))

# RUN MOPAC FOR CUSTOM CALCULATION (RESIDUE)
# ==========================================
def RunMOPACRes(selection1, keywords):
  command='RunMOPACRes '
  command+=selstr(selection1)+','
  command+='Keywords='+cstr(keywords)+','
  return(runretval(command[:-1],retvalused()))

# RUN MOPAC FOR CUSTOM CALCULATION (ATOM)
# =======================================
def RunMOPACAtom(selection1, keywords):
  command='RunMOPACAtom '
  command+=selstr(selection1)+','
  command+='Keywords='+cstr(keywords)+','
  return(runretval(command[:-1],retvalused()))

# SAMPLE DIHEDRAL ANGLES
# ======================
def SampleDih(selection1, method=None, structures=None, dihedrals=None, bumpsum=None, scaffold=None, devmax=None, devbins=None):
  command='SampleDih '
  command+=selstr(selection1)+','
  if (method!=None): command+='Method='+cstr(method)+','
  if (structures!=None): command+='Structures='+cstr(structures)+','
  if (dihedrals!=None): command+='Dihedrals='+cstr(dihedrals)+','
  if (bumpsum!=None): command+='Bumpsum='+cstr(bumpsum)+','
  if (scaffold!=None): command+='Scaffold='+cstr(scaffold)+','
  if (devmax!=None): command+='DevMax='+cstr(devmax)+','
  if (devbins!=None): command+='DevBins='+cstr(devbins)+','
  return(runretval(command[:-1],retvalused()))

# SAMPLE CENTRAL OR TERMINAL LOOP
# ===============================
def SampleLoop(selection1, selection2, structures=None, bumpsum=None, secstr=None):
  command='SampleLoop '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (structures!=None): command+='Structures='+cstr(structures)+','
  if (bumpsum!=None): command+='Bumpsum='+cstr(bumpsum)+','
  if (secstr!=None): command+='SecStr='+cstr(secstr)+','
  return(runretval(command[:-1],retvalused()))

# SAVE ALIGNMENT BETWEEN OBJECTS
# ==============================
def SaveAli(selection1, selection2, method=None, filename=None, format=None):
  command='SaveAli '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (method!=None): command+='Method='+cstr(method)+','
  if (filename!=None): command+='Filename='+cstr(filename)+','
  if (format!=None): command+='Format='+cstr(format)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# SAVE SCREENSHOT AS UNCOMPRESSED WINDOWS BITMAP
# ==============================================
def SaveBmp(filename, menu=None, depthmap=None):
  command='SaveBmp '
  command+='Filename='+cstr(filename)+','
  if (menu!=None): command+='Menu='+cstr(menu)+','
  if (depthmap!=None): command+='DepthMap='+cstr(depthmap)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# SAVE CIF OR MMCIF FILE
# ======================
def SaveCIF(selection1, filename, format=None, transform=None):
  command='SaveCIF '
  command+=selstr(selection1)+','
  command+='Filename='+cstr(filename)+','
  if (format!=None): command+='Format='+cstr(format)+','
  if (transform!=None): command+='Transform='+cstr(transform)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# SAVE ELECTROSTATIC POTENTIAL MAP
# ================================
def SaveESP(filename, method=None):
  command='SaveESP '
  command+='Filename='+cstr(filename)+','
  if (method!=None): command+='Method='+cstr(method)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# SAVE A MACRO TO RESTORE THE CURRENT STATE
# =========================================
def SaveMacro(filename, component):
  command='SaveMacro '
  command+='Filename='+cstr(filename)+','
  command+='Component='+cstr(component)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# SAVE SIMULATION SNAPSHOTS IN MDCRD FORMAT
# =========================================
def SaveMDCrd(filename, steps, selection1):
  command='SaveMDCrd '
  command+='Filename='+cstr(filename)+','
  command+='Steps='+cstr(steps)+','
  command+=selstr(selection1)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# SAVE MPEG4 VIDEO
# ================
def SaveMPG(filename, x=None, y=None, fps=None, quality=None, skip=None, raytrace=None, menu=None, justmacro=None, frames=None):
  command='SaveMPG '
  command+='Filename='+cstr(filename)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (fps!=None): command+='FPS='+cstr(fps)+','
  if (quality!=None): command+='Quality='+cstr(quality)+','
  if (skip!=None): command+='Skip='+cstr(skip)+','
  if (raytrace!=None): command+='RayTrace='+cstr(raytrace)+','
  if (menu!=None): command+='Menu='+cstr(menu)+','
  if (justmacro!=None): command+='justMacro='+cstr(justmacro)+','
  if (frames!=None): command+='Frames='+cstr(frames)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  result=runretval(command[:-1],1)
  if (result!=None and len(result)): return(result[0])
  return(result)

# SAVE DISTANCE, DIHEDRAL AND RDC RESTRAINTS IN NMR EXCHANGE FORMAT
# =================================================================
def SaveNEF(selection1, filename, component=None):
  command='SaveNEF '
  command+=selstr(selection1)+','
  command+='Filename='+cstr(filename)+','
  if (component!=None): command+='Component='+cstr(component)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# SAVE PROTEIN DATA BANK FILE
# ===========================
def SavePDB(selection1, filename, format=None, transform=None, usecif=None):
  command='SavePDB '
  command+=selstr(selection1)+','
  command+='Filename='+cstr(filename)+','
  if (format!=None): command+='Format='+cstr(format)+','
  if (transform!=None): command+='Transform='+cstr(transform)+','
  if (usecif!=None): command+='UseCIF='+cstr(usecif)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# SAVE PLOT
# =========
def SavePlot(filename, selection1, width, height, title, Type, xcolumn, ycolumn, ycolumns, xlabel, ylabel, legendpos, graphname, *arglist2):
  command='SavePlot '
  command+='Filename='+cstr(filename)+','
  command+=selstr(selection1)+','
  command+='Width='+cstr(width)+','
  command+='Height='+cstr(height)+','
  command+='Title='+cstr(title)+','
  command+='Type='+cstr(Type)+','
  command+='XColumn='+cstr(xcolumn)+','
  command+='YColumn='+cstr(ycolumn)+','
  command+='YColumns='+cstr(ycolumns)+','
  command+='XLabel='+cstr(xlabel)+','
  command+='YLabel='+cstr(ylabel)+','
  command+='LegendPos='+cstr(legendpos)+','
  command+='Graphname='+cstr(graphname)+','
  # ANY NUMBER OF VARIABLE ARGUMENTS CAN FOLLOW
  for arglist in arglist2:
    if (type(arglist)!=type([])): arglist=[arglist]
    for arg in arglist:
      command+=cstr(arg,quoted=(type(arg)!=type(1) and type(arg)!=type(1.)))+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# SAVE SCREENSHOT AS COMPRESSED PNG BITMAP
# ========================================
def SavePNG(filename, menu=None, depthmap=None):
  command='SavePNG '
  command+='Filename='+cstr(filename)+','
  if (menu!=None): command+='Menu='+cstr(menu)+','
  if (depthmap!=None): command+='DepthMap='+cstr(depthmap)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# SAVE POVRAY SCENE DESCRIPTION
# =============================
def SavePOV(filename, zoom=None, atoms=None, labelshadow=None, secalpha=None):
  command='SavePOV '
  command+='Filename='+cstr(filename)+','
  if (zoom!=None): command+='Zoom='+cstr(zoom)+','
  if (atoms!=None): command+='Atoms='+cstr(atoms)+','
  if (labelshadow!=None): command+='LabelShadow='+cstr(labelshadow)+','
  if (secalpha!=None): command+='SecAlpha='+cstr(secalpha)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# SAVE AMBER PREP TOPOLOGY (ALL OR SELECTED)
# ==========================================
def SavePrep(filename, hydnumbers=None, reorder=None):
  command='SavePrep '
  command+='Filename='+cstr(filename)+','
  if (hydnumbers!=None): command+='HydNumbers='+cstr(hydnumbers)+','
  if (reorder!=None): command+='Reorder='+cstr(reorder)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# SAVE AMBER PREP TOPOLOGY (ALL)
# ==============================
def SavePrepAll(filename, hydnumbers=None, reorder=None):
  command='SavePrepAll '
  command+='Filename='+cstr(filename)+','
  if (hydnumbers!=None): command+='HydNumbers='+cstr(hydnumbers)+','
  if (reorder!=None): command+='Reorder='+cstr(reorder)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# SAVE AMBER PREP TOPOLOGY (OBJECT)
# =================================
def SavePrepObj(selection1, filename, hydnumbers=None, reorder=None):
  command='SavePrepObj '
  command+=selstr(selection1)+','
  command+='Filename='+cstr(filename)+','
  if (hydnumbers!=None): command+='HydNumbers='+cstr(hydnumbers)+','
  if (reorder!=None): command+='Reorder='+cstr(reorder)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# SAVE AMBER PREP TOPOLOGY (MOLECULE)
# ===================================
def SavePrepMol(selection1, filename, hydnumbers=None, reorder=None):
  command='SavePrepMol '
  command+=selstr(selection1)+','
  command+='Filename='+cstr(filename)+','
  if (hydnumbers!=None): command+='HydNumbers='+cstr(hydnumbers)+','
  if (reorder!=None): command+='Reorder='+cstr(reorder)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# SAVE AMBER PREP TOPOLOGY (RESIDUE)
# ==================================
def SavePrepRes(selection1, filename, hydnumbers=None, reorder=None):
  command='SavePrepRes '
  command+=selstr(selection1)+','
  command+='Filename='+cstr(filename)+','
  if (hydnumbers!=None): command+='HydNumbers='+cstr(hydnumbers)+','
  if (reorder!=None): command+='Reorder='+cstr(reorder)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# SAVE COMPLETE SCENE
# ===================
def SaveSce(filename):
  command='SaveSce '
  command+='Filename='+cstr(filename)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# SAVE RESIDUE SEQUENCE (OBJECT)
# ==============================
def SaveSeqObj(selection1, filename, join=None):
  command='SaveSeqObj '
  command+=selstr(selection1)+','
  command+='Filename='+cstr(filename)+','
  if (join!=None): command+='Join='+cstr(join)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# SAVE RESIDUE SEQUENCE (MOLECULE)
# ================================
def SaveSeqMol(selection1, filename, join=None):
  command='SaveSeqMol '
  command+=selstr(selection1)+','
  command+='Filename='+cstr(filename)+','
  if (join!=None): command+='Join='+cstr(join)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# SAVE RESIDUE SEQUENCE (RESIDUE)
# ===============================
def SaveSeqRes(selection1, filename, join=None):
  command='SaveSeqRes '
  command+=selstr(selection1)+','
  command+='Filename='+cstr(filename)+','
  if (join!=None): command+='Join='+cstr(join)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# SAVE SIMULATION SNAPSHOTS IN SIM FORMAT
# =======================================
def SaveSim(filename, steps=None, number=None):
  command='SaveSim '
  command+='Filename='+cstr(filename)+','
  if (steps!=None): command+='Steps='+cstr(steps)+','
  if (number!=None): command+='Number='+cstr(number)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# SAVE FORMATTED TABLE
# ====================
def SaveTab(selection1, filename, format, columns, numformat, header):
  command='SaveTab '
  command+=selstr(selection1)+','
  command+='Filename='+cstr(filename)+','
  command+='Format='+cstr(format)+','
  command+='Columns='+cstr(columns)+','
  command+='NumFormat='+cstr(numformat)+','
  command+='Header='+cstr(header)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# SAVE DISTANCE, DIHEDRAL AND RDC RESTRAINTS IN XPLOR FORMAT
# ==========================================================
def SaveTbl(selection1, filename, component=None, nameformat=None):
  command='SaveTbl '
  command+=selstr(selection1)+','
  command+='Filename='+cstr(filename)+','
  if (component!=None): command+='Component='+cstr(component)+','
  if (nameformat!=None): command+='NameFormat='+cstr(nameformat)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# SAVE ALIAS/WAVEFRONT OBJECT
# ===========================
def SaveWOb(selection1, filename, interpolcol=None, level=None, ballzoom=None):
  command='SaveWOb '
  command+=selstr(selection1)+','
  command+='Filename='+cstr(filename)+','
  if (interpolcol!=None): command+='InterpolCol='+cstr(interpolcol)+','
  if (level!=None): command+='Level='+cstr(level)+','
  if (ballzoom!=None): command+='BallZoom='+cstr(ballzoom)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# SAVE SIMULATION SNAPSHOTS IN XTC FORMAT
# =======================================
def SaveXTC(filename, steps, selection1):
  command='SaveXTC '
  command+='Filename='+cstr(filename)+','
  command+='Steps='+cstr(steps)+','
  command+=selstr(selection1)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# SAVE YASARA OBJECT
# ==================
def SaveYOb(selection1, filename):
  command='SaveYOb '
  command+=selstr(selection1)+','
  command+='Filename='+cstr(filename)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# EXPORT FILE WITH OPENBABEL
# ==========================
def Save(format, selection1, filename, nameformat=None, transform=None):
  command='Save '
  command=command[:-1]+cstr(format)+' '
  command+=selstr(selection1)+','
  command+='Filename='+cstr(filename)+','
  if (nameformat!=None): command+='NameFormat='+cstr(nameformat)+','
  if (transform!=None): command+='Transform='+cstr(transform)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# SET/GET FORCE SCALING FACTORS
# =============================
def ScaleForce(component=None, factor=None):
  command='ScaleForce '
  if (component!=None): command+='Component='+cstr(component)+','
  if (factor!=None): command+='Factor='+cstr(factor)+','
  return(runretval(command[:-1],retvalused()))

# SCALE RESTRAINTS (ALL OR SELECTED)
# ==================================
def ScaleRest(Class=None, distance=None, dihedral=None, rdc=None):
  command='ScaleRest '
  if (Class!=None): command+='Class='+cstr(Class)+','
  if (distance!=None): command+='Distance='+cstr(distance)+','
  if (dihedral!=None): command+='Dihedral='+cstr(dihedral)+','
  if (rdc!=None): command+='RDC='+cstr(rdc)+','
  return(runretval(command[:-1],retvalused()))

# SCALE RESTRAINTS (ALL)
# ======================
def ScaleRestAll(Class=None, distance=None, dihedral=None, rdc=None):
  command='ScaleRestAll '
  if (Class!=None): command+='Class='+cstr(Class)+','
  if (distance!=None): command+='Distance='+cstr(distance)+','
  if (dihedral!=None): command+='Dihedral='+cstr(dihedral)+','
  if (rdc!=None): command+='RDC='+cstr(rdc)+','
  return(runretval(command[:-1],retvalused()))

# SCALE RESTRAINTS (OBJECT)
# =========================
def ScaleRestObj(selection1, Class=None, distance=None, dihedral=None, rdc=None):
  command='ScaleRestObj '
  command+=selstr(selection1)+','
  if (Class!=None): command+='Class='+cstr(Class)+','
  if (distance!=None): command+='Distance='+cstr(distance)+','
  if (dihedral!=None): command+='Dihedral='+cstr(dihedral)+','
  if (rdc!=None): command+='RDC='+cstr(rdc)+','
  return(runretval(command[:-1],retvalused()))

# SCALE RESTRAINTS (MOLECULE)
# ===========================
def ScaleRestMol(selection1, Class=None, distance=None, dihedral=None, rdc=None):
  command='ScaleRestMol '
  command+=selstr(selection1)+','
  if (Class!=None): command+='Class='+cstr(Class)+','
  if (distance!=None): command+='Distance='+cstr(distance)+','
  if (dihedral!=None): command+='Dihedral='+cstr(dihedral)+','
  if (rdc!=None): command+='RDC='+cstr(rdc)+','
  return(runretval(command[:-1],retvalused()))

# SCALE RESTRAINTS (RESIDUE)
# ==========================
def ScaleRestRes(selection1, Class=None, distance=None, dihedral=None, rdc=None):
  command='ScaleRestRes '
  command+=selstr(selection1)+','
  if (Class!=None): command+='Class='+cstr(Class)+','
  if (distance!=None): command+='Distance='+cstr(distance)+','
  if (dihedral!=None): command+='Dihedral='+cstr(dihedral)+','
  if (rdc!=None): command+='RDC='+cstr(rdc)+','
  return(runretval(command[:-1],retvalused()))

# SCALE RESTRAINTS (ATOM)
# =======================
def ScaleRestAtom(selection1, Class=None, distance=None, dihedral=None, rdc=None):
  command='ScaleRestAtom '
  command+=selstr(selection1)+','
  if (Class!=None): command+='Class='+cstr(Class)+','
  if (distance!=None): command+='Distance='+cstr(distance)+','
  if (dihedral!=None): command+='Dihedral='+cstr(dihedral)+','
  if (rdc!=None): command+='RDC='+cstr(rdc)+','
  return(runretval(command[:-1],retvalused()))

# SCALE ATOM POSITIONS AND POLYGON MESHES (ALL OR SELECTED)
# =========================================================
def Scale(x=None, y=None, z=None):
  command='Scale '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# SCALE ATOM POSITIONS AND POLYGON MESHES (ALL)
# =============================================
def ScaleAll(x=None, y=None, z=None):
  command='ScaleAll '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# SCALE ATOM POSITIONS AND POLYGON MESHES (OBJECT)
# ================================================
def ScaleObj(selection1, x=None, y=None, z=None):
  command='ScaleObj '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# SCALE ATOM POSITIONS AND POLYGON MESHES (MOLECULE)
# ==================================================
def ScaleMol(selection1, x=None, y=None, z=None):
  command='ScaleMol '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# SCALE ATOM POSITIONS AND POLYGON MESHES (RESIDUE)
# =================================================
def ScaleRes(selection1, x=None, y=None, z=None):
  command='ScaleRes '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# SCALE ATOM POSITIONS AND POLYGON MESHES (ATOM)
# ==============================================
def ScaleAtom(selection1, x=None, y=None, z=None):
  command='ScaleAtom '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# FIX YASARA WINDOW ON A CERTAIN SCREEN
# =====================================
def Screen(number):
  command='Screen '
  command+='Number='+cstr(number)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET WINDOW AND FULLSCREEN SIZE
# ==================================
def ScreenSize(x=None, y=None, scale=None):
  command='ScreenSize '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (scale!=None): command+='Scale='+cstr(scale)+','
  return(runretval(command[:-1],retvalused()))

# SET SECONDARY STRUCTURE DISPLAY PARAMETERS
# ==========================================
def SecStrPar(strandwidth, strandheight, strandslope, arrowheight, strandperf, helixwidth, helixheight, helixslope, helixperf, helixsection, tuberadius, tubeellip, gaps, coltrans):
  command='SecStrPar '
  command+='StrandWidth='+cstr(strandwidth)+','
  command+='StrandHeight='+cstr(strandheight)+','
  command+='StrandSlope='+cstr(strandslope)+','
  command+='ArrowHeight='+cstr(arrowheight)+','
  command+='StrandPerf='+cstr(strandperf)+','
  command+='HelixWidth='+cstr(helixwidth)+','
  command+='HelixHeight='+cstr(helixheight)+','
  command+='HelixSlope='+cstr(helixslope)+','
  command+='HelixPerf='+cstr(helixperf)+','
  command+='HelixSection='+cstr(helixsection)+','
  command+='TubeRadius='+cstr(tuberadius)+','
  command+='TubeEllip='+cstr(tubeellip)+','
  command+='Gaps='+cstr(gaps)+','
  command+='ColTrans='+cstr(coltrans)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET SECONDARY STRUCTURE (ALL OR SELECTED)
# =============================================
def SecStr(Type=None):
  command='SecStr '
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET SECONDARY STRUCTURE (ALL)
# =================================
def SecStrAll(Type=None):
  command='SecStrAll '
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET SECONDARY STRUCTURE (OBJECT)
# ====================================
def SecStrObj(selection1, Type=None):
  command='SecStrObj '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET SECONDARY STRUCTURE (MOLECULE)
# ======================================
def SecStrMol(selection1, Type=None):
  command='SecStrMol '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET SECONDARY STRUCTURE (RESIDUE)
# =====================================
def SecStrRes(selection1, Type=None):
  command='SecStrRes '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE SEGMENT NAME (ALL OR SELECTED)
# ==========================================
def Seg(name=None):
  command='Seg '
  if (name!=None): command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE SEGMENT NAME (ALL)
# ==============================
def SegAll(name=None):
  command='SegAll '
  if (name!=None): command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE SEGMENT NAME (OBJECT)
# =================================
def SegObj(selection1, name=None):
  command='SegObj '
  command+=selstr(selection1)+','
  if (name!=None): command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE SEGMENT NAME (MOLECULE)
# ===================================
def SegMol(selection1, name=None):
  command='SegMol '
  command+=selstr(selection1)+','
  if (name!=None): command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE SEGMENT NAME (RESIDUE)
# ==================================
def SegRes(selection1, name=None):
  command='SegRes '
  command+=selstr(selection1)+','
  if (name!=None): command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET THE SEGMENT NAME (ATOM)
# ===============================
def SegAtom(selection1, name=None):
  command='SegAtom '
  command+=selstr(selection1)+','
  if (name!=None): command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# INTERACTIVELY SELECT ATOMS WITHIN AN ARBITRARY AREA (OBJECT)
# ============================================================
def SelectAreaObj():
  command='SelectAreaObj '
  return(runretval(command[:-1],retvalused()))

# INTERACTIVELY SELECT ATOMS WITHIN AN ARBITRARY AREA (MOLECULE)
# ==============================================================
def SelectAreaMol():
  command='SelectAreaMol '
  return(runretval(command[:-1],retvalused()))

# INTERACTIVELY SELECT ATOMS WITHIN AN ARBITRARY AREA (RESIDUE)
# =============================================================
def SelectAreaRes():
  command='SelectAreaRes '
  return(runretval(command[:-1],retvalused()))

# INTERACTIVELY SELECT ATOMS WITHIN AN ARBITRARY AREA (ATOM)
# ==========================================================
def SelectAreaAtom():
  command='SelectAreaAtom '
  return(runretval(command[:-1],retvalused()))

# INTERACTIVELY SELECT ATOMS WITHIN A RECTANGULAR BOX (OBJECT)
# ============================================================
def SelectBoxObj():
  command='SelectBoxObj '
  return(runretval(command[:-1],retvalused()))

# INTERACTIVELY SELECT ATOMS WITHIN A RECTANGULAR BOX (MOLECULE)
# ==============================================================
def SelectBoxMol():
  command='SelectBoxMol '
  return(runretval(command[:-1],retvalused()))

# INTERACTIVELY SELECT ATOMS WITHIN A RECTANGULAR BOX (RESIDUE)
# =============================================================
def SelectBoxRes():
  command='SelectBoxRes '
  return(runretval(command[:-1],retvalused()))

# INTERACTIVELY SELECT ATOMS WITHIN A RECTANGULAR BOX (ATOM)
# ==========================================================
def SelectBoxAtom():
  command='SelectBoxAtom '
  return(runretval(command[:-1],retvalused()))

# INTERACTIVELY SELECT ATOMS WITHIN A SPHERE AROUND OTHER ATOMS (OBJECT)
# ======================================================================
def SelectSphereObj(selection1):
  command='SelectSphereObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# INTERACTIVELY SELECT ATOMS WITHIN A SPHERE AROUND OTHER ATOMS (MOLECULE)
# ========================================================================
def SelectSphereMol(selection1):
  command='SelectSphereMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# INTERACTIVELY SELECT ATOMS WITHIN A SPHERE AROUND OTHER ATOMS (RESIDUE)
# =======================================================================
def SelectSphereRes(selection1):
  command='SelectSphereRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# INTERACTIVELY SELECT ATOMS WITHIN A SPHERE AROUND OTHER ATOMS (ATOM)
# ====================================================================
def SelectSphereAtom(selection1):
  command='SelectSphereAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SELECT TABLE TO ADD CELLS
# =========================
def SelectTab(selection1):
  command='SelectTab '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SELECT ATOMS (ALL OR SELECTED)
# ==============================
def Select(mode=None):
  command='Select '
  if (mode!=None): command+='Mode='+cstr(mode)+','
  return(runretval(command[:-1],retvalused()))

# SELECT ATOMS (ALL)
# ==================
def SelectAll(mode=None):
  command='SelectAll '
  if (mode!=None): command+='Mode='+cstr(mode)+','
  return(runretval(command[:-1],retvalused()))

# SELECT ATOMS (OBJECT)
# =====================
def SelectObj(selection1, mode=None):
  command='SelectObj '
  command+=selstr(selection1)+','
  if (mode!=None): command+='Mode='+cstr(mode)+','
  return(runretval(command[:-1],retvalused()))

# SELECT ATOMS (MOLECULE)
# =======================
def SelectMol(selection1, mode=None):
  command='SelectMol '
  command+=selstr(selection1)+','
  if (mode!=None): command+='Mode='+cstr(mode)+','
  return(runretval(command[:-1],retvalused()))

# SELECT ATOMS (RESIDUE)
# ======================
def SelectRes(selection1, mode=None):
  command='SelectRes '
  command+=selstr(selection1)+','
  if (mode!=None): command+='Mode='+cstr(mode)+','
  return(runretval(command[:-1],retvalused()))

# SELECT ATOMS (ATOM)
# ===================
def SelectAtom(selection1, mode=None):
  command='SelectAtom '
  command+=selstr(selection1)+','
  if (mode!=None): command+='Mode='+cstr(mode)+','
  return(runretval(command[:-1],retvalused()))

# SWITCH SEQUENCE SELECTOR ON/OFF
# ===============================
def SeqSelector(flag):
  command='SeqSelector '
  command+='Flag='+cstr(flag)+','
  return(runretval(command[:-1],retvalused()))

# GET RESIDUE SEQUENCE (ALL OR SELECTED)
# ======================================
def Sequence(join=None):
  command='Sequence '
  if (join!=None): command+='Join='+cstr(join)+','
  return(runretval(command[:-1],retvalused()))

# GET RESIDUE SEQUENCE (ALL)
# ==========================
def SequenceAll(join=None):
  command='SequenceAll '
  if (join!=None): command+='Join='+cstr(join)+','
  return(runretval(command[:-1],retvalused()))

# GET RESIDUE SEQUENCE (OBJECT)
# =============================
def SequenceObj(selection1, join=None):
  command='SequenceObj '
  command+=selstr(selection1)+','
  if (join!=None): command+='Join='+cstr(join)+','
  return(runretval(command[:-1],retvalused()))

# GET RESIDUE SEQUENCE (MOLECULE)
# ===============================
def SequenceMol(selection1, join=None):
  command='SequenceMol '
  command+=selstr(selection1)+','
  if (join!=None): command+='Join='+cstr(join)+','
  return(runretval(command[:-1],retvalused()))

# GET RESIDUE SEQUENCE (RESIDUE)
# ==============================
def SequenceRes(selection1, join=None):
  command='SequenceRes '
  command+=selstr(selection1)+','
  if (join!=None): command+='Join='+cstr(join)+','
  return(runretval(command[:-1],retvalused()))

# SHIFT ATOM COLORS (ALL OR SELECTED)
# ===================================
def ShiftColor(color, shift=None):
  command='ShiftColor '
  command+='color='+cstr(color)+','
  if (shift!=None): command+='Shift='+cstr(shift)+','
  return(runretval(command[:-1],retvalused()))

# SHIFT ATOM COLORS (ALL)
# =======================
def ShiftColorAll(color, shift=None):
  command='ShiftColorAll '
  command+='color='+cstr(color)+','
  if (shift!=None): command+='Shift='+cstr(shift)+','
  return(runretval(command[:-1],retvalused()))

# SHIFT ATOM COLORS (OBJECT)
# ==========================
def ShiftColorObj(selection1, color, shift=None):
  command='ShiftColorObj '
  command+=selstr(selection1)+','
  command+='color='+cstr(color)+','
  if (shift!=None): command+='Shift='+cstr(shift)+','
  return(runretval(command[:-1],retvalused()))

# SHIFT ATOM COLORS (MOLECULE)
# ============================
def ShiftColorMol(selection1, color, shift=None):
  command='ShiftColorMol '
  command+=selstr(selection1)+','
  command+='color='+cstr(color)+','
  if (shift!=None): command+='Shift='+cstr(shift)+','
  return(runretval(command[:-1],retvalused()))

# SHIFT ATOM COLORS (RESIDUE)
# ===========================
def ShiftColorRes(selection1, color, shift=None):
  command='ShiftColorRes '
  command+=selstr(selection1)+','
  command+='color='+cstr(color)+','
  if (shift!=None): command+='Shift='+cstr(shift)+','
  return(runretval(command[:-1],retvalused()))

# SHIFT ATOM COLORS (ATOM)
# ========================
def ShiftColorAtom(selection1, color, shift=None):
  command='ShiftColorAtom '
  command+=selstr(selection1)+','
  command+='color='+cstr(color)+','
  if (shift!=None): command+='Shift='+cstr(shift)+','
  return(runretval(command[:-1],retvalused()))

# SHOW ARROWS BETWEEN ATOMS OR POINTS
# ===================================
def ShowArrow(start, selection1, end, selection2, radius=None, heads=None, color=None, dismax=None, visualize=None):
  command='ShowArrow '
  command+='Start='+cstr(start)+','
  command+=selstr(selection1)+','
  command+='End='+cstr(end)+','
  command+=selstr(selection2)+','
  if (radius!=None): command+='Radius='+cstr(radius)+','
  if (heads!=None): command+='Heads='+cstr(heads)+','
  if (color!=None): command+='Color='+cstr(color)+','
  if (dismax!=None): command+='DisMax='+cstr(dismax)+','
  if (visualize!=None): command+='Visualize='+cstr(visualize)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SHOW ARROWS BETWEEN ATOMS OR POINTS
# ===================================
# THIS IS ALTERNATIVE 2, WITH DIFFERENT PARAMETERS
def ShowArrow2(start, x, y, z, end, x2=None, y2=None, z2=None, radius=None, heads=None, color=None):
  command='ShowArrow '
  command+='Start='+cstr(start)+','
  command+='X='+cstr(x)+','
  command+='Y='+cstr(y)+','
  command+='Z='+cstr(z)+','
  command+='End='+cstr(end)+','
  if (x2!=None): command+='X='+cstr(x2)+','
  if (y2!=None): command+='Y='+cstr(y2)+','
  if (z2!=None): command+='Z='+cstr(z2)+','
  if (radius!=None): command+='Radius='+cstr(radius)+','
  if (heads!=None): command+='Heads='+cstr(heads)+','
  if (color!=None): command+='Color='+cstr(color)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SHOW ARROWS BETWEEN ATOMS OR POINTS
# ===================================
# THIS IS ALTERNATIVE 3, WITH DIFFERENT PARAMETERS
def ShowArrow3(start, selection1, x, y, z, end, selection2, x2=None, y2=None, z2=None, radius=None, heads=None, color=None, dismax=None):
  command='ShowArrow '
  command+='Start='+cstr(start)+','
  command+=selstr(selection1)+','
  command+='X='+cstr(x)+','
  command+='Y='+cstr(y)+','
  command+='Z='+cstr(z)+','
  command+='End='+cstr(end)+','
  command+=selstr(selection2)+','
  if (x2!=None): command+='X='+cstr(x2)+','
  if (y2!=None): command+='Y='+cstr(y2)+','
  if (z2!=None): command+='Z='+cstr(z2)+','
  if (radius!=None): command+='Radius='+cstr(radius)+','
  if (heads!=None): command+='Heads='+cstr(heads)+','
  if (color!=None): command+='Color='+cstr(color)+','
  if (dismax!=None): command+='DisMax='+cstr(dismax)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SHOW ARROWS BETWEEN ATOMS OR POINTS
# ===================================
# THIS IS ALTERNATIVE 4, WITH DIFFERENT PARAMETERS
def ShowArrow4(start, selection1, dis, end, selection2, dis2=None, radius=None, heads=None, color=None, dismax=None):
  command='ShowArrow '
  command+='Start='+cstr(start)+','
  command+=selstr(selection1)+','
  command+='Dis='+cstr(dis)+','
  command+='End='+cstr(end)+','
  command+=selstr(selection2)+','
  if (dis2!=None): command+='Dis='+cstr(dis2)+','
  if (radius!=None): command+='Radius='+cstr(radius)+','
  if (heads!=None): command+='Heads='+cstr(heads)+','
  if (color!=None): command+='Color='+cstr(color)+','
  if (dismax!=None): command+='DisMax='+cstr(dismax)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SHOW A RECTANGULAR BOX
# ======================
def ShowBox(width=None, height=None, depth=None, leftcol=None, rightcol=None, bottomcol=None, topcol=None, frontcol=None, backcol=None):
  command='ShowBox '
  if (width!=None): command+='Width='+cstr(width)+','
  if (height!=None): command+='Height='+cstr(height)+','
  if (depth!=None): command+='Depth='+cstr(depth)+','
  if (leftcol!=None): command+='LeftCol='+cstr(leftcol)+','
  if (rightcol!=None): command+='RightCol='+cstr(rightcol)+','
  if (bottomcol!=None): command+='BottomCol='+cstr(bottomcol)+','
  if (topcol!=None): command+='TopCol='+cstr(topcol)+','
  if (frontcol!=None): command+='FrontCol='+cstr(frontcol)+','
  if (backcol!=None): command+='BackCol='+cstr(backcol)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SHOW CLICKABLE BUTTON
# =====================
def ShowButton(text, x=None, y=None, width=None, height=None, border=None, color=None, action=None):
  command='ShowButton '
  command+='Text='+cstr(text,1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (width!=None): command+='Width='+cstr(width)+','
  if (height!=None): command+='Height='+cstr(height)+','
  if (border!=None): command+='Border='+cstr(border)+','
  if (color!=None): command+='Color='+cstr(color)+','
  if (action!=None): command+='Action='+cstr(action)+','
  return(runretval(command[:-1],retvalused()))

# SHOW CAVITIES (ALL OR SELECTED)
# ===============================
def ShowCavi(Type=None, outcol=None, outalpha=None, incol=None, inalpha=None, specular=None):
  command='ShowCavi '
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (outcol!=None): command+='OutCol='+cstr(outcol)+','
  if (outalpha!=None): command+='OutAlpha='+cstr(outalpha)+','
  if (incol!=None): command+='InCol='+cstr(incol)+','
  if (inalpha!=None): command+='InAlpha='+cstr(inalpha)+','
  if (specular!=None): command+='Specular='+cstr(specular)+','
  return(runretval(command[:-1],retvalused()))

# SHOW CAVITIES (ALL)
# ===================
def ShowCaviAll(Type=None, outcol=None, outalpha=None, incol=None, inalpha=None, specular=None):
  command='ShowCaviAll '
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (outcol!=None): command+='OutCol='+cstr(outcol)+','
  if (outalpha!=None): command+='OutAlpha='+cstr(outalpha)+','
  if (incol!=None): command+='InCol='+cstr(incol)+','
  if (inalpha!=None): command+='InAlpha='+cstr(inalpha)+','
  if (specular!=None): command+='Specular='+cstr(specular)+','
  return(runretval(command[:-1],retvalused()))

# SHOW CAVITIES (OBJECT)
# ======================
def ShowCaviObj(selection1, Type=None, outcol=None, outalpha=None, incol=None, inalpha=None, specular=None):
  command='ShowCaviObj '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (outcol!=None): command+='OutCol='+cstr(outcol)+','
  if (outalpha!=None): command+='OutAlpha='+cstr(outalpha)+','
  if (incol!=None): command+='InCol='+cstr(incol)+','
  if (inalpha!=None): command+='InAlpha='+cstr(inalpha)+','
  if (specular!=None): command+='Specular='+cstr(specular)+','
  return(runretval(command[:-1],retvalused()))

# SHOW CAVITIES (MOLECULE)
# ========================
def ShowCaviMol(selection1, Type=None, outcol=None, outalpha=None, incol=None, inalpha=None, specular=None):
  command='ShowCaviMol '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (outcol!=None): command+='OutCol='+cstr(outcol)+','
  if (outalpha!=None): command+='OutAlpha='+cstr(outalpha)+','
  if (incol!=None): command+='InCol='+cstr(incol)+','
  if (inalpha!=None): command+='InAlpha='+cstr(inalpha)+','
  if (specular!=None): command+='Specular='+cstr(specular)+','
  return(runretval(command[:-1],retvalused()))

# SHOW CAVITIES (RESIDUE)
# =======================
def ShowCaviRes(selection1, Type=None, outcol=None, outalpha=None, incol=None, inalpha=None, specular=None):
  command='ShowCaviRes '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (outcol!=None): command+='OutCol='+cstr(outcol)+','
  if (outalpha!=None): command+='OutAlpha='+cstr(outalpha)+','
  if (incol!=None): command+='InCol='+cstr(incol)+','
  if (inalpha!=None): command+='InAlpha='+cstr(inalpha)+','
  if (specular!=None): command+='Specular='+cstr(specular)+','
  return(runretval(command[:-1],retvalused()))

# SHOW CAVITIES (ATOM)
# ====================
def ShowCaviAtom(selection1, Type=None, outcol=None, outalpha=None, incol=None, inalpha=None, specular=None):
  command='ShowCaviAtom '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (outcol!=None): command+='OutCol='+cstr(outcol)+','
  if (outalpha!=None): command+='OutAlpha='+cstr(outalpha)+','
  if (incol!=None): command+='InCol='+cstr(incol)+','
  if (inalpha!=None): command+='InAlpha='+cstr(inalpha)+','
  if (specular!=None): command+='Specular='+cstr(specular)+','
  return(runretval(command[:-1],retvalused()))

# SHOW A CONE, CYLINDER, PYRAMID OR PRISM
# =======================================
def ShowCone(bottomradius=None, topradius=None, height=None, edges=None, bottomcol=None, topcol=None, sidecol=None, alpha=None, smooth=None):
  command='ShowCone '
  if (bottomradius!=None): command+='BottomRadius='+cstr(bottomradius)+','
  if (topradius!=None): command+='TopRadius='+cstr(topradius)+','
  if (height!=None): command+='Height='+cstr(height)+','
  if (edges!=None): command+='Edges='+cstr(edges)+','
  if (bottomcol!=None): command+='BottomCol='+cstr(bottomcol)+','
  if (topcol!=None): command+='TopCol='+cstr(topcol)+','
  if (sidecol!=None): command+='SideCol='+cstr(sidecol)+','
  if (alpha!=None): command+='Alpha='+cstr(alpha)+','
  if (smooth!=None): command+='Smooth='+cstr(smooth)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SHOW CONTACT SURFACE (OBJECT)
# =============================
def ShowConSurfObj(selection1, selection2, cutoff=None, subtract=None, Type=None, outcol=None, outalpha=None, incol=None, inalpha=None, specular=None):
  command='ShowConSurfObj '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (subtract!=None): command+='Subtract='+cstr(subtract)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (outcol!=None): command+='OutCol='+cstr(outcol)+','
  if (outalpha!=None): command+='OutAlpha='+cstr(outalpha)+','
  if (incol!=None): command+='InCol='+cstr(incol)+','
  if (inalpha!=None): command+='InAlpha='+cstr(inalpha)+','
  if (specular!=None): command+='Specular='+cstr(specular)+','
  return(runretval(command[:-1],retvalused()))

# SHOW CONTACT SURFACE (MOLECULE)
# ===============================
def ShowConSurfMol(selection1, selection2, cutoff=None, subtract=None, Type=None, outcol=None, outalpha=None, incol=None, inalpha=None, specular=None):
  command='ShowConSurfMol '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (subtract!=None): command+='Subtract='+cstr(subtract)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (outcol!=None): command+='OutCol='+cstr(outcol)+','
  if (outalpha!=None): command+='OutAlpha='+cstr(outalpha)+','
  if (incol!=None): command+='InCol='+cstr(incol)+','
  if (inalpha!=None): command+='InAlpha='+cstr(inalpha)+','
  if (specular!=None): command+='Specular='+cstr(specular)+','
  return(runretval(command[:-1],retvalused()))

# SHOW CONTACT SURFACE (RESIDUE)
# ==============================
def ShowConSurfRes(selection1, selection2, cutoff=None, subtract=None, Type=None, outcol=None, outalpha=None, incol=None, inalpha=None, specular=None):
  command='ShowConSurfRes '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (subtract!=None): command+='Subtract='+cstr(subtract)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (outcol!=None): command+='OutCol='+cstr(outcol)+','
  if (outalpha!=None): command+='OutAlpha='+cstr(outalpha)+','
  if (incol!=None): command+='InCol='+cstr(incol)+','
  if (inalpha!=None): command+='InAlpha='+cstr(inalpha)+','
  if (specular!=None): command+='Specular='+cstr(specular)+','
  return(runretval(command[:-1],retvalused()))

# SHOW CONTACT SURFACE (ATOM)
# ===========================
def ShowConSurfAtom(selection1, selection2, cutoff=None, subtract=None, Type=None, outcol=None, outalpha=None, incol=None, inalpha=None, specular=None):
  command='ShowConSurfAtom '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (subtract!=None): command+='Subtract='+cstr(subtract)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (outcol!=None): command+='OutCol='+cstr(outcol)+','
  if (outalpha!=None): command+='OutAlpha='+cstr(outalpha)+','
  if (incol!=None): command+='InCol='+cstr(incol)+','
  if (inalpha!=None): command+='InAlpha='+cstr(inalpha)+','
  if (specular!=None): command+='Specular='+cstr(specular)+','
  return(runretval(command[:-1],retvalused()))

# SHOW CONTACTS (OBJECT)
# ======================
def ShowConObj(selection1, selection2, cutoff=None, subtract=None, energy=None, exclude=None, occluded=None):
  command='ShowConObj '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (subtract!=None): command+='Subtract='+cstr(subtract)+','
  if (energy!=None): command+='Energy='+cstr(energy)+','
  if (exclude!=None): command+='Exclude='+cstr(exclude)+','
  if (occluded!=None): command+='Occluded='+cstr(occluded)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SHOW CONTACTS (MOLECULE)
# ========================
def ShowConMol(selection1, selection2, cutoff=None, subtract=None, energy=None, exclude=None, occluded=None):
  command='ShowConMol '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (subtract!=None): command+='Subtract='+cstr(subtract)+','
  if (energy!=None): command+='Energy='+cstr(energy)+','
  if (exclude!=None): command+='Exclude='+cstr(exclude)+','
  if (occluded!=None): command+='Occluded='+cstr(occluded)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SHOW CONTACTS (RESIDUE)
# =======================
def ShowConRes(selection1, selection2, cutoff=None, subtract=None, energy=None, exclude=None, occluded=None):
  command='ShowConRes '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (subtract!=None): command+='Subtract='+cstr(subtract)+','
  if (energy!=None): command+='Energy='+cstr(energy)+','
  if (exclude!=None): command+='Exclude='+cstr(exclude)+','
  if (occluded!=None): command+='Occluded='+cstr(occluded)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SHOW CONTACTS (ATOM)
# ====================
def ShowConAtom(selection1, selection2, cutoff=None, subtract=None, energy=None, exclude=None, occluded=None):
  command='ShowConAtom '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (subtract!=None): command+='Subtract='+cstr(subtract)+','
  if (energy!=None): command+='Energy='+cstr(energy)+','
  if (exclude!=None): command+='Exclude='+cstr(exclude)+','
  if (occluded!=None): command+='Occluded='+cstr(occluded)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SHOW ELECTROSTATIC POTENTIAL
# ============================
def ShowESP():
  RaiseError('This command is only available with extensions Points,Density,Contour in Python')

# SHOW ELECTROSTATIC POTENTIAL
# ============================
# THIS IS ALTERNATIVE 1, WITH DIFFERENT PARAMETERS
def ShowESPPoints(method=None, resolution=None, Min=None, Max=None):
  command='ShowESP Points,'
  if (method!=None): command+='Method='+cstr(method)+','
  if (resolution!=None): command+='Resolution='+cstr(resolution)+','
  if (Min!=None): command+='Min='+cstr(Min)+','
  if (Max!=None): command+='Max='+cstr(Max)+','
  return(runretval(command[:-1],retvalused()))

# SHOW ELECTROSTATIC POTENTIAL
# ============================
# THIS IS ALTERNATIVE 2, WITH DIFFERENT PARAMETERS
def ShowESPDensity(method=None, resolution=None, Min=None, Max=None):
  command='ShowESP Density,'
  if (method!=None): command+='Method='+cstr(method)+','
  if (resolution!=None): command+='Resolution='+cstr(resolution)+','
  if (Min!=None): command+='Min='+cstr(Min)+','
  if (Max!=None): command+='Max='+cstr(Max)+','
  return(runretval(command[:-1],retvalused()))

# SHOW ELECTROSTATIC POTENTIAL
# ============================
# THIS IS ALTERNATIVE 3, WITH DIFFERENT PARAMETERS
def ShowESPContour(method=None, resolution=None, level=None):
  command='ShowESP Contour,'
  if (method!=None): command+='Method='+cstr(method)+','
  if (resolution!=None): command+='Resolution='+cstr(resolution)+','
  if (level!=None): command+='Level='+cstr(level)+','
  return(runretval(command[:-1],retvalused()))

# SHOW HYDROGEN BONDS (ALL OR SELECTED)
# =====================================
def ShowHBo(extend=None):
  command='ShowHBo '
  if (extend!=None): command+='Extend='+cstr(extend)+','
  return(runretval(command[:-1],retvalused()))

# SHOW HYDROGEN BONDS (ALL)
# =========================
def ShowHBoAll(extend=None):
  command='ShowHBoAll '
  if (extend!=None): command+='Extend='+cstr(extend)+','
  return(runretval(command[:-1],retvalused()))

# SHOW HYDROGEN BONDS (OBJECT)
# ============================
def ShowHBoObj(selection1, extend=None):
  command='ShowHBoObj '
  command+=selstr(selection1)+','
  if (extend!=None): command+='Extend='+cstr(extend)+','
  return(runretval(command[:-1],retvalused()))

# SHOW HYDROGEN BONDS (MOLECULE)
# ==============================
def ShowHBoMol(selection1, extend=None):
  command='ShowHBoMol '
  command+=selstr(selection1)+','
  if (extend!=None): command+='Extend='+cstr(extend)+','
  return(runretval(command[:-1],retvalused()))

# SHOW HYDROGEN BONDS (RESIDUE)
# =============================
def ShowHBoRes(selection1, extend=None):
  command='ShowHBoRes '
  command+=selstr(selection1)+','
  if (extend!=None): command+='Extend='+cstr(extend)+','
  return(runretval(command[:-1],retvalused()))

# SHOW HYDROGEN BONDS (ATOM)
# ==========================
def ShowHBoAtom(selection1, extend=None):
  command='ShowHBoAtom '
  command+=selstr(selection1)+','
  if (extend!=None): command+='Extend='+cstr(extend)+','
  return(runretval(command[:-1],retvalused()))

# SHOW IN HEAD-UP DISPLAY (MOLECULE)
# ==================================
def ShowHUDMol(selection1):
  command='ShowHUDMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SHOW IN HEAD-UP DISPLAY (RESIDUE)
# =================================
def ShowHUDRes(selection1):
  command='ShowHUDRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SHOW IN HEAD-UP DISPLAY (ATOM)
# ==============================
def ShowHUDAtom(selection1):
  command='ShowHUDAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SHOW IMAGES
# ===========
def ShowImage(selection1, x=None, y=None, width=None, height=None, alpha=None, priority=None):
  command='ShowImage '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (width!=None): command+='Width='+cstr(width)+','
  if (height!=None): command+='Height='+cstr(height)+','
  if (alpha!=None): command+='Alpha='+cstr(alpha)+','
  if (priority!=None): command+='Priority='+cstr(priority)+','
  return(runretval(command[:-1],retvalused()))

# SHOW INTERACTIONS (OBJECT)
# ==========================
def ShowIntObj(selection1, selection2, Type, cutoff=None, exclude=None, occluded=None):
  command='ShowIntObj '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  command+='Type='+cstr(Type)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (exclude!=None): command+='Exclude='+cstr(exclude)+','
  if (occluded!=None): command+='Occluded='+cstr(occluded)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SHOW INTERACTIONS (MOLECULE)
# ============================
def ShowIntMol(selection1, selection2, Type, cutoff=None, exclude=None, occluded=None):
  command='ShowIntMol '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  command+='Type='+cstr(Type)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (exclude!=None): command+='Exclude='+cstr(exclude)+','
  if (occluded!=None): command+='Occluded='+cstr(occluded)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SHOW INTERACTIONS (RESIDUE)
# ===========================
def ShowIntRes(selection1, selection2, Type, cutoff=None, exclude=None, occluded=None):
  command='ShowIntRes '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  command+='Type='+cstr(Type)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (exclude!=None): command+='Exclude='+cstr(exclude)+','
  if (occluded!=None): command+='Occluded='+cstr(occluded)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SHOW INTERACTIONS (ATOM)
# ========================
def ShowIntAtom(selection1, selection2, Type, cutoff=None, exclude=None, occluded=None):
  command='ShowIntAtom '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  command+='Type='+cstr(Type)+','
  if (cutoff!=None): command+='Cutoff='+cstr(cutoff)+','
  if (exclude!=None): command+='Exclude='+cstr(exclude)+','
  if (occluded!=None): command+='Occluded='+cstr(occluded)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SHOW ION BINDING SITES (ALL OR SELECTED)
# ========================================
def ShowIonSites(ion):
  command='ShowIonSites '
  command+='Ion='+cstr(ion)+','
  return(runretval(command[:-1],retvalused()))

# SHOW ION BINDING SITES (ALL)
# ============================
def ShowIonSitesAll(ion):
  command='ShowIonSitesAll '
  command+='Ion='+cstr(ion)+','
  return(runretval(command[:-1],retvalused()))

# SHOW ION BINDING SITES (OBJECT)
# ===============================
def ShowIonSitesObj(selection1, ion):
  command='ShowIonSitesObj '
  command+=selstr(selection1)+','
  command+='Ion='+cstr(ion)+','
  return(runretval(command[:-1],retvalused()))

# SHOW KNOWLEDGE-BASED POTENTIAL
# ==============================
def ShowKBP(selection1, selection2, name=None, Type=None, size=None):
  command='ShowKBP '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (name!=None): command+='Name='+cstr(name)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (size!=None): command+='Size='+cstr(size)+','
  return(runretval(command[:-1],retvalused()))

# SHOW TEXT MESSAGE AT THE BOTTOM
# ===============================
def ShowMessage(text):
  command='ShowMessage '
  command+='Text='+cstr(text,1)+','
  return(runretval(command[:-1],retvalused()))

# SHOW RESTRAINTS (ALL OR SELECTED)
# =================================
def ShowRest(Class=None):
  command='ShowRest '
  if (Class!=None): command+='Class='+cstr(Class)+','
  return(runretval(command[:-1],retvalused()))

# SHOW RESTRAINTS (ALL)
# =====================
def ShowRestAll(Class=None):
  command='ShowRestAll '
  if (Class!=None): command+='Class='+cstr(Class)+','
  return(runretval(command[:-1],retvalused()))

# SHOW RESTRAINTS (OBJECT)
# ========================
def ShowRestObj(selection1, Class=None):
  command='ShowRestObj '
  command+=selstr(selection1)+','
  if (Class!=None): command+='Class='+cstr(Class)+','
  return(runretval(command[:-1],retvalused()))

# SHOW RESTRAINTS (MOLECULE)
# ==========================
def ShowRestMol(selection1, Class=None):
  command='ShowRestMol '
  command+=selstr(selection1)+','
  if (Class!=None): command+='Class='+cstr(Class)+','
  return(runretval(command[:-1],retvalused()))

# SHOW RESTRAINTS (RESIDUE)
# =========================
def ShowRestRes(selection1, Class=None):
  command='ShowRestRes '
  command+=selstr(selection1)+','
  if (Class!=None): command+='Class='+cstr(Class)+','
  return(runretval(command[:-1],retvalused()))

# SHOW RESTRAINTS (ATOM)
# ======================
def ShowRestAtom(selection1, Class=None):
  command='ShowRestAtom '
  command+=selstr(selection1)+','
  if (Class!=None): command+='Class='+cstr(Class)+','
  return(runretval(command[:-1],retvalused()))

# SHOW SIDE-CHAIN ROTAMERS (ALL OR SELECTED)
# ==========================================
def ShowRota():
  command='ShowRota '
  return(runretval(command[:-1],retvalused()))

# SHOW SIDE-CHAIN ROTAMERS (ALL)
# ==============================
def ShowRotaAll():
  command='ShowRotaAll '
  return(runretval(command[:-1],retvalused()))

# SHOW SIDE-CHAIN ROTAMERS (OBJECT)
# =================================
def ShowRotaObj(selection1):
  command='ShowRotaObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SHOW SIDE-CHAIN ROTAMERS (MOLECULE)
# ===================================
def ShowRotaMol(selection1):
  command='ShowRotaMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SHOW SIDE-CHAIN ROTAMERS (RESIDUE)
# ==================================
def ShowRotaRes(selection1):
  command='ShowRotaRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SHOW SECONDARY STRUCTURE (ALL OR SELECTED)
# ==========================================
def ShowSecStr(style=None, hideatoms=None):
  command='ShowSecStr '
  if (style!=None): command+='Style='+cstr(style)+','
  if (hideatoms!=None): command+='HideAtoms='+cstr(hideatoms)+','
  return(runretval(command[:-1],retvalused()))

# SHOW SECONDARY STRUCTURE (ALL)
# ==============================
def ShowSecStrAll(style=None, hideatoms=None):
  command='ShowSecStrAll '
  if (style!=None): command+='Style='+cstr(style)+','
  if (hideatoms!=None): command+='HideAtoms='+cstr(hideatoms)+','
  return(runretval(command[:-1],retvalused()))

# SHOW SECONDARY STRUCTURE (OBJECT)
# =================================
def ShowSecStrObj(selection1, style=None, hideatoms=None):
  command='ShowSecStrObj '
  command+=selstr(selection1)+','
  if (style!=None): command+='Style='+cstr(style)+','
  if (hideatoms!=None): command+='HideAtoms='+cstr(hideatoms)+','
  return(runretval(command[:-1],retvalused()))

# SHOW SECONDARY STRUCTURE (MOLECULE)
# ===================================
def ShowSecStrMol(selection1, style=None, hideatoms=None):
  command='ShowSecStrMol '
  command+=selstr(selection1)+','
  if (style!=None): command+='Style='+cstr(style)+','
  if (hideatoms!=None): command+='HideAtoms='+cstr(hideatoms)+','
  return(runretval(command[:-1],retvalused()))

# SHOW SECONDARY STRUCTURE (RESIDUE)
# ==================================
def ShowSecStrRes(selection1, style=None, hideatoms=None):
  command='ShowSecStrRes '
  command+=selstr(selection1)+','
  if (style!=None): command+='Style='+cstr(style)+','
  if (hideatoms!=None): command+='HideAtoms='+cstr(hideatoms)+','
  return(runretval(command[:-1],retvalused()))

# CREATE A SIMULATION CELL OBJECT TO VISUALIZE NEIGHBORING CELLS
# ==============================================================
def ShowCell(x=None, y=None, z=None, alpha=None, beta=None, gamma=None):
  command='ShowCell '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  if (alpha!=None): command+='Alpha='+cstr(alpha)+','
  if (beta!=None): command+='Beta='+cstr(beta)+','
  if (gamma!=None): command+='Gamma='+cstr(gamma)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SHOW SIMULATION NEIGHBOR SEARCH GRID
# ====================================
def ShowGrid(Type=None, center=None, color=None):
  command='ShowGrid '
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (center!=None): command+='Center='+cstr(center)+','
  if (color!=None): command+='Color='+cstr(color)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SHOW A SPHERE OR ELLIPSOID
# ==========================
def ShowSphere(radius=None, color=None, alpha=None, level=None, scaley=None, scalez=None):
  command='ShowSphere '
  if (radius!=None): command+='Radius='+cstr(radius)+','
  if (color!=None): command+='Color='+cstr(color)+','
  if (alpha!=None): command+='Alpha='+cstr(alpha)+','
  if (level!=None): command+='Level='+cstr(level)+','
  if (scaley!=None): command+='ScaleY='+cstr(scaley)+','
  if (scalez!=None): command+='ScaleZ='+cstr(scalez)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SHOW POLYGON BETWEEN ATOMS OR POINTS
# ====================================
def ShowPolygon():
  RaiseError('This command is only available with extensions Atoms,Points in Python')

# SHOW POLYGON BETWEEN ATOMS OR POINTS
# ====================================
# THIS IS ALTERNATIVE 1, WITH DIFFERENT PARAMETERS
def ShowPolygonAtoms(color, alpha, vertices, selection1, selection2, selection3, selection4=None, selection5=None, selection6=None, selection7=None, selection8=None):
  command='ShowPolygon Atoms,'
  command+='Color='+cstr(color)+','
  command+='Alpha='+cstr(alpha)+','
  command+='Vertices='+cstr(vertices)+','
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  command+=selstr(selection3)+','
  if (selection4!=None): command+=selstr(selection4)+','
  if (selection5!=None): command+=selstr(selection5)+','
  if (selection6!=None): command+=selstr(selection6)+','
  if (selection7!=None): command+=selstr(selection7)+','
  if (selection8!=None): command+=selstr(selection8)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SHOW POLYGON BETWEEN ATOMS OR POINTS
# ====================================
# THIS IS ALTERNATIVE 2, WITH DIFFERENT PARAMETERS
def ShowPolygonPoints(color, alpha, vertices, x1, y1, z1, x2=None, y2=None, z2=None, x3=None, y3=None, z3=None, x4=None, y4=None, z4=None, x5=None, y5=None, z5=None, x6=None, y6=None, z6=None, x7=None, y7=None, z7=None, x8=None, y8=None, z8=None):
  command='ShowPolygon Points,'
  command+='Color='+cstr(color)+','
  command+='Alpha='+cstr(alpha)+','
  command+='Vertices='+cstr(vertices)+','
  command+='X1='+cstr(x1)+','
  command+='Y1='+cstr(y1)+','
  command+='Z1='+cstr(z1)+','
  if (x2!=None): command+='X2='+cstr(x2)+','
  if (y2!=None): command+='Y2='+cstr(y2)+','
  if (z2!=None): command+='Z2='+cstr(z2)+','
  if (x3!=None): command+='X3='+cstr(x3)+','
  if (y3!=None): command+='Y3='+cstr(y3)+','
  if (z3!=None): command+='Z3='+cstr(z3)+','
  if (x4!=None): command+='X4='+cstr(x4)+','
  if (y4!=None): command+='Y4='+cstr(y4)+','
  if (z4!=None): command+='Z4='+cstr(z4)+','
  if (x5!=None): command+='X5='+cstr(x5)+','
  if (y5!=None): command+='Y5='+cstr(y5)+','
  if (z5!=None): command+='Z5='+cstr(z5)+','
  if (x6!=None): command+='X6='+cstr(x6)+','
  if (y6!=None): command+='Y6='+cstr(y6)+','
  if (z6!=None): command+='Z6='+cstr(z6)+','
  if (x7!=None): command+='X7='+cstr(x7)+','
  if (y7!=None): command+='Y7='+cstr(y7)+','
  if (z7!=None): command+='Z7='+cstr(z7)+','
  if (x8!=None): command+='X8='+cstr(x8)+','
  if (y8!=None): command+='Y8='+cstr(y8)+','
  if (z8!=None): command+='Z8='+cstr(z8)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SHOW POLYGON INSIDE RING (ALL OR SELECTED)
# ==========================================
def ShowRing(color=None, alpha=None):
  command='ShowRing '
  if (color!=None): command+='Color='+cstr(color)+','
  if (alpha!=None): command+='Alpha='+cstr(alpha)+','
  return(runretval(command[:-1],retvalused()))

# SHOW POLYGON INSIDE RING (ALL)
# ==============================
def ShowRingAll(color=None, alpha=None):
  command='ShowRingAll '
  if (color!=None): command+='Color='+cstr(color)+','
  if (alpha!=None): command+='Alpha='+cstr(alpha)+','
  return(runretval(command[:-1],retvalused()))

# SHOW POLYGON INSIDE RING (OBJECT)
# =================================
def ShowRingObj(selection1, color=None, alpha=None):
  command='ShowRingObj '
  command+=selstr(selection1)+','
  if (color!=None): command+='Color='+cstr(color)+','
  if (alpha!=None): command+='Alpha='+cstr(alpha)+','
  return(runretval(command[:-1],retvalused()))

# SHOW POLYGON INSIDE RING (MOLECULE)
# ===================================
def ShowRingMol(selection1, color=None, alpha=None):
  command='ShowRingMol '
  command+=selstr(selection1)+','
  if (color!=None): command+='Color='+cstr(color)+','
  if (alpha!=None): command+='Alpha='+cstr(alpha)+','
  return(runretval(command[:-1],retvalused()))

# SHOW POLYGON INSIDE RING (RESIDUE)
# ==================================
def ShowRingRes(selection1, color=None, alpha=None):
  command='ShowRingRes '
  command+=selstr(selection1)+','
  if (color!=None): command+='Color='+cstr(color)+','
  if (alpha!=None): command+='Alpha='+cstr(alpha)+','
  return(runretval(command[:-1],retvalused()))

# SHOW POLYGON INSIDE RING (ATOM)
# ===============================
def ShowRingAtom(selection1, color=None, alpha=None):
  command='ShowRingAtom '
  command+=selstr(selection1)+','
  if (color!=None): command+='Color='+cstr(color)+','
  if (alpha!=None): command+='Alpha='+cstr(alpha)+','
  return(runretval(command[:-1],retvalused()))

# SHOW A SPHERICAL ENVIRONMENT
# ============================
def ShowSkySphere(filename):
  command='ShowSkySphere '
  command+='Filename='+cstr(filename)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SHOW SURFACE (ALL OR SELECTED)
# ==============================
def ShowSurf(Type=None, update=None, outcol=None, outalpha=None, incol=None, inalpha=None, specular=None):
  command='ShowSurf '
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (update!=None): command+='Update='+cstr(update)+','
  if (outcol!=None): command+='OutCol='+cstr(outcol)+','
  if (outalpha!=None): command+='OutAlpha='+cstr(outalpha)+','
  if (incol!=None): command+='InCol='+cstr(incol)+','
  if (inalpha!=None): command+='InAlpha='+cstr(inalpha)+','
  if (specular!=None): command+='Specular='+cstr(specular)+','
  return(runretval(command[:-1],retvalused()))

# SHOW SURFACE (ALL)
# ==================
def ShowSurfAll(Type=None, update=None, outcol=None, outalpha=None, incol=None, inalpha=None, specular=None):
  command='ShowSurfAll '
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (update!=None): command+='Update='+cstr(update)+','
  if (outcol!=None): command+='OutCol='+cstr(outcol)+','
  if (outalpha!=None): command+='OutAlpha='+cstr(outalpha)+','
  if (incol!=None): command+='InCol='+cstr(incol)+','
  if (inalpha!=None): command+='InAlpha='+cstr(inalpha)+','
  if (specular!=None): command+='Specular='+cstr(specular)+','
  return(runretval(command[:-1],retvalused()))

# SHOW SURFACE (OBJECT)
# =====================
def ShowSurfObj(selection1, Type=None, update=None, outcol=None, outalpha=None, incol=None, inalpha=None, specular=None):
  command='ShowSurfObj '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (update!=None): command+='Update='+cstr(update)+','
  if (outcol!=None): command+='OutCol='+cstr(outcol)+','
  if (outalpha!=None): command+='OutAlpha='+cstr(outalpha)+','
  if (incol!=None): command+='InCol='+cstr(incol)+','
  if (inalpha!=None): command+='InAlpha='+cstr(inalpha)+','
  if (specular!=None): command+='Specular='+cstr(specular)+','
  return(runretval(command[:-1],retvalused()))

# SHOW SURFACE (MOLECULE)
# =======================
def ShowSurfMol(selection1, Type=None, update=None, outcol=None, outalpha=None, incol=None, inalpha=None, specular=None):
  command='ShowSurfMol '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (update!=None): command+='Update='+cstr(update)+','
  if (outcol!=None): command+='OutCol='+cstr(outcol)+','
  if (outalpha!=None): command+='OutAlpha='+cstr(outalpha)+','
  if (incol!=None): command+='InCol='+cstr(incol)+','
  if (inalpha!=None): command+='InAlpha='+cstr(inalpha)+','
  if (specular!=None): command+='Specular='+cstr(specular)+','
  return(runretval(command[:-1],retvalused()))

# SHOW SURFACE (RESIDUE)
# ======================
def ShowSurfRes(selection1, Type=None, update=None, outcol=None, outalpha=None, incol=None, inalpha=None, specular=None):
  command='ShowSurfRes '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (update!=None): command+='Update='+cstr(update)+','
  if (outcol!=None): command+='OutCol='+cstr(outcol)+','
  if (outalpha!=None): command+='OutAlpha='+cstr(outalpha)+','
  if (incol!=None): command+='InCol='+cstr(incol)+','
  if (inalpha!=None): command+='InAlpha='+cstr(inalpha)+','
  if (specular!=None): command+='Specular='+cstr(specular)+','
  return(runretval(command[:-1],retvalused()))

# SHOW SURFACE (ATOM)
# ===================
def ShowSurfAtom(selection1, Type=None, update=None, outcol=None, outalpha=None, incol=None, inalpha=None, specular=None):
  command='ShowSurfAtom '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (update!=None): command+='Update='+cstr(update)+','
  if (outcol!=None): command+='OutCol='+cstr(outcol)+','
  if (outalpha!=None): command+='OutAlpha='+cstr(outalpha)+','
  if (incol!=None): command+='InCol='+cstr(incol)+','
  if (inalpha!=None): command+='InAlpha='+cstr(inalpha)+','
  if (specular!=None): command+='Specular='+cstr(specular)+','
  return(runretval(command[:-1],retvalused()))

# SHOW TABLE DATA AS 3D OBJECT
# ============================
def ShowTab(selection1, width=None, Range=None, Min=None, mincol=None, Max=None, maxcol=None, style=None):
  command='ShowTab '
  command+=selstr(selection1)+','
  if (width!=None): command+='Width='+cstr(width)+','
  if (Range!=None): command+='Range='+cstr(Range)+','
  if (Min!=None): command+='Min='+cstr(Min)+','
  if (mincol!=None): command+='MinCol='+cstr(mincol)+','
  if (Max!=None): command+='Max='+cstr(Max)+','
  if (maxcol!=None): command+='MaxCol='+cstr(maxcol)+','
  if (style!=None): command+='Style='+cstr(style)+','
  return(runretval(command[:-1],retvalused()))

# SHOW A TORUS
# ============
def ShowTorus(largeradius=None, largeedges=None, smallradius=None, smalledges=None, color=None, alpha=None):
  command='ShowTorus '
  if (largeradius!=None): command+='LargeRadius='+cstr(largeradius)+','
  if (largeedges!=None): command+='LargeEdges='+cstr(largeedges)+','
  if (smallradius!=None): command+='SmallRadius='+cstr(smallradius)+','
  if (smalledges!=None): command+='SmallEdges='+cstr(smalledges)+','
  if (color!=None): command+='Color='+cstr(color)+','
  if (alpha!=None): command+='Alpha='+cstr(alpha)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SHOW TRACE THROUGH ATOMS
# ========================
def ShowTrace(selection1):
  command='ShowTrace '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# OPEN A FILE IN THE WEB BROWSER
# ==============================
def ShowURL(name):
  command='ShowURL '
  command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# SHOW VIEW
# =========
def ShowView(selection1):
  command='ShowView '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SHOW A USER INTERFACE WINDOW AND OBTAIN THE INPUT MADE
# ======================================================
def ShowWin(Type, title, *arglist2):
  command='ShowWin '
  command+='Type='+cstr(Type)+','
  command+='Title='+cstr(title)+','
  # ANY NUMBER OF VARIABLE ARGUMENTS CAN FOLLOW
  for arglist in arglist2:
    if (type(arglist)!=type([])): arglist=[arglist]
    for arg in arglist:
      command+=cstr(arg,quoted=(type(arg)!=type(1) and type(arg)!=type(1.)))+','
  return(runretval(command[:-1],retvalused()))

# SHOW POLYGON MESH AS WIRE FRAME (ALL OR SELECTED)
# =================================================
def ShowWire(update=None, mesh=None, side=None):
  command='ShowWire '
  if (update!=None): command+='Update='+cstr(update)+','
  if (mesh!=None): command+='Mesh='+cstr(mesh)+','
  if (side!=None): command+='Side='+cstr(side)+','
  return(runretval(command[:-1],retvalused()))

# SHOW POLYGON MESH AS WIRE FRAME (ALL)
# =====================================
def ShowWireAll(update=None, mesh=None, side=None):
  command='ShowWireAll '
  if (update!=None): command+='Update='+cstr(update)+','
  if (mesh!=None): command+='Mesh='+cstr(mesh)+','
  if (side!=None): command+='Side='+cstr(side)+','
  return(runretval(command[:-1],retvalused()))

# SHOW POLYGON MESH AS WIRE FRAME (OBJECT)
# ========================================
def ShowWireObj(selection1, update=None, mesh=None, side=None):
  command='ShowWireObj '
  command+=selstr(selection1)+','
  if (update!=None): command+='Update='+cstr(update)+','
  if (mesh!=None): command+='Mesh='+cstr(mesh)+','
  if (side!=None): command+='Side='+cstr(side)+','
  return(runretval(command[:-1],retvalused()))

# SHOW ATOMS (ALL OR SELECTED)
# ============================
def Show():
  command='Show '
  return(runretval(command[:-1],retvalused()))

# SHOW ATOMS (ALL)
# ================
def ShowAll():
  command='ShowAll '
  return(runretval(command[:-1],retvalused()))

# SHOW ATOMS (OBJECT)
# ===================
def ShowObj(selection1):
  command='ShowObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SHOW ATOMS (MOLECULE)
# =====================
def ShowMol(selection1):
  command='ShowMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SHOW ATOMS (RESIDUE)
# ====================
def ShowRes(selection1):
  command='ShowRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SHOW ATOMS (ATOM)
# =================
def ShowAtom(selection1):
  command='ShowAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET SIMULATION STATE
# ========================
def Sim(control=None, In=None):
  command='Sim '
  if (control!=None): command+='Control='+cstr(control)+','
  if (In!=None): command+='in='+cstr(In)+','
  return(runretval(command[:-1],retvalused()))

# SET SIMULATION SPEED
# ====================
def SimSpeed(Type):
  command='SimSpeed '
  command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET NUMBER OF SIMULATION STEPS PER SCREEN AND PAIRLIST UPDATE
# =================================================================
def SimSteps(screen=None, pairlist=None):
  command='SimSteps '
  if (screen!=None): command+='Screen='+cstr(screen)+','
  if (pairlist!=None): command+='Pairlist='+cstr(pairlist)+','
  return(runretval(command[:-1],retvalused()))

# GET SOLVENT DENSITY IN SIMULATION CELL
# ======================================
def SolvDensity(name=None):
  command='SolvDensity '
  if (name!=None): command+='Name='+cstr(name)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# CALCULATE SOLVATION ENERGY (ALL OR SELECTED)
# ============================================
def SolvEnergy(method=None):
  command='SolvEnergy '
  if (method!=None): command+='Method='+cstr(method)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE SOLVATION ENERGY (ALL)
# ================================
def SolvEnergyAll(method=None):
  command='SolvEnergyAll '
  if (method!=None): command+='Method='+cstr(method)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE SOLVATION ENERGY (OBJECT)
# ===================================
def SolvEnergyObj(selection1, method=None):
  command='SolvEnergyObj '
  command+=selstr(selection1)+','
  if (method!=None): command+='Method='+cstr(method)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE SOLVATION ENERGY (MOLECULE)
# =====================================
def SolvEnergyMol(selection1, method=None):
  command='SolvEnergyMol '
  command+=selstr(selection1)+','
  if (method!=None): command+='Method='+cstr(method)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE SOLVATION ENERGY (RESIDUE)
# ====================================
def SolvEnergyRes(selection1, method=None):
  command='SolvEnergyRes '
  command+=selstr(selection1)+','
  if (method!=None): command+='Method='+cstr(method)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE SOLVATION ENERGY (ATOM)
# =================================
def SolvEnergyAtom(selection1, method=None):
  command='SolvEnergyAtom '
  command+=selstr(selection1)+','
  if (method!=None): command+='Method='+cstr(method)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET SOLVATION PARAMETERS
# ============================
def SolvPar(esolute=None, esolvent=None, resolution=None, ioncon=None):
  command='SolvPar '
  if (esolute!=None): command+='eSolute='+cstr(esolute)+','
  if (esolvent!=None): command+='eSolvent='+cstr(esolvent)+','
  if (resolution!=None): command+='Resolution='+cstr(resolution)+','
  if (ioncon!=None): command+='IonCon='+cstr(ioncon)+','
  return(runretval(command[:-1],retvalused()))

# ASSIGN COMMAND TO SPACEBALL BUTTON
# ==================================
def SpaceballButton(number, com):
  command='SpaceballButton '
  command+='Number='+cstr(number)+','
  command+='Command='+cstr(com)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SET SPACEBALL PARAMETERS
# ========================
def SpaceballPar(mode=None, movescale=None, rotatescale=None):
  command='SpaceballPar '
  if (mode!=None): command+='Mode='+cstr(mode)+','
  if (movescale!=None): command+='MoveScale='+cstr(movescale)+','
  if (rotatescale!=None): command+='RotateScale='+cstr(rotatescale)+','
  return(runretval(command[:-1],retvalused()))

# DETERMINE FIRST AND LAST UNIT SPANNING A SELECTION (OBJECT)
# ===========================================================
def SpanObj(selection1):
  command='SpanObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# DETERMINE FIRST AND LAST UNIT SPANNING A SELECTION (RESIDUE)
# ============================================================
def SpanRes(selection1):
  command='SpanRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# DETERMINE FIRST AND LAST UNIT SPANNING A SELECTION (ATOM)
# =========================================================
def SpanAtom(selection1):
  command='SpanAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SPEED UP MOVEMENTS WHEN GRAPHICS ARE SLOW
# =========================================
def SpeedUp(status=None):
  command='SpeedUp '
  if (status!=None): command+='Status='+cstr(status)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET SPEED AND VELOCITY OF ATOMS (ALL OR SELECTED)
# =====================================================
def Speed(x=None, y=None, z=None):
  command='Speed '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET SPEED AND VELOCITY OF ATOMS (ALL)
# =========================================
def SpeedAll(x=None, y=None, z=None):
  command='SpeedAll '
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET SPEED AND VELOCITY OF ATOMS (OBJECT)
# ============================================
def SpeedObj(selection1, x=None, y=None, z=None):
  command='SpeedObj '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET SPEED AND VELOCITY OF ATOMS (MOLECULE)
# ==============================================
def SpeedMol(selection1, x=None, y=None, z=None):
  command='SpeedMol '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET SPEED AND VELOCITY OF ATOMS (RESIDUE)
# =============================================
def SpeedRes(selection1, x=None, y=None, z=None):
  command='SpeedRes '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET SPEED AND VELOCITY OF ATOMS (ATOM)
# ==========================================
def SpeedAtom(selection1, x=None, y=None, z=None):
  command='SpeedAtom '
  command+=selstr(selection1)+','
  if (x!=None): command+='X='+cstr(x)+','
  if (y!=None): command+='Y='+cstr(y)+','
  if (z!=None): command+='Z='+cstr(z)+','
  return(runretval(command[:-1],retvalused()))

# SPLIT OBJECTS AT SPLIT POINTS (ALL OR SELECTED)
# ===============================================
def Split(center=None, selection1=None, keep=None):
  command='Split '
  if (center!=None): command+='Center='+cstr(center)+','
  if (selection1!=None): command+=selstr(selection1)+','
  if (keep!=None): command+='Keep='+cstr(keep)+','
  return(runretval(command[:-1],retvalused()))

# SPLIT OBJECTS AT SPLIT POINTS (ALL)
# ===================================
def SplitAll(center=None, selection1=None, keep=None):
  command='SplitAll '
  if (center!=None): command+='Center='+cstr(center)+','
  if (selection1!=None): command+=selstr(selection1)+','
  if (keep!=None): command+='Keep='+cstr(keep)+','
  return(runretval(command[:-1],retvalused()))

# SPLIT OBJECTS AT SPLIT POINTS (OBJECT)
# ======================================
def SplitObj(selection1, center=None, selection2=None, keep=None):
  command='SplitObj '
  command+=selstr(selection1)+','
  if (center!=None): command+='Center='+cstr(center)+','
  if (selection2!=None): command+=selstr(selection2)+','
  if (keep!=None): command+='Keep='+cstr(keep)+','
  return(runretval(command[:-1],retvalused()))

# INTRODUCE SPLIT POINTS (MOLECULE)
# =================================
def SplitMol(selection1):
  command='SplitMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# INTRODUCE SPLIT POINTS (RESIDUE)
# ================================
def SplitRes(selection1):
  command='SplitRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# INTRODUCE SPLIT POINTS (ATOM)
# =============================
def SplitAtom(selection1):
  command='SplitAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SET STEREO MODE
# ===============
def Stereo(mode):
  command='Stereo '
  command+='Mode='+cstr(mode)+','
  return(runretval(command[:-1],retvalused()))

# SET STEREO PARAMETERS
# =====================
def StereoPar(eyedis=None, protru=None):
  command='StereoPar '
  if (eyedis!=None): command+='EyeDis='+cstr(eyedis)+','
  if (protru!=None): command+='ProTru='+cstr(protru)+','
  return(runretval(command[:-1],retvalused()))

# SET STICK RADIUS
# ================
def StickRadius(percent):
  command='StickRadius '
  command+='percent='+cstr(percent)+','
  return(runretval(command[:-1],retvalused()))

# STYLE ATOMS AS STICKS (ALL OR SELECTED)
# =======================================
def Stick():
  command='Stick '
  return(runretval(command[:-1],retvalused()))

# STYLE ATOMS AS STICKS (ALL)
# ===========================
def StickAll():
  command='StickAll '
  return(runretval(command[:-1],retvalused()))

# STYLE ATOMS AS STICKS (OBJECT)
# ==============================
def StickObj(selection1):
  command='StickObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# STYLE ATOMS AS STICKS (MOLECULE)
# ================================
def StickMol(selection1):
  command='StickMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# STYLE ATOMS AS STICKS (RESIDUE)
# ===============================
def StickRes(selection1):
  command='StickRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# STYLE ATOMS AS STICKS (ATOM)
# ============================
def StickAtom(selection1):
  command='StickAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# STOP LOG RECORDER
# =================
def StopLog():
  command='StopLog '
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  return(runretval(command[:-1],1))

# STOP RUNNING PLUGIN
# ===================
def StopPlugin():
  global std_relay_service, reg_server
  
  # Shutdown the "service"
  std_relay_service.close()
  # Shutdown the registry
  reg_server.close()
  
    
  command='StopPlugin '
  return(runretval(command[:-1],retvalused()))

# SET GENERAL DISPLAY STYLE
# =========================
def Style(backbone=None, sidechain=None, hetgroup=None, save=None):
  command='Style '
  if (backbone!=None): command+='Backbone='+cstr(backbone)+','
  if (sidechain!=None): command+='Sidechain='+cstr(sidechain)+','
  if (hetgroup!=None): command+='Hetgroup='+cstr(hetgroup)+','
  if (save!=None): command+='Save='+cstr(save)+','
  return(runretval(command[:-1],retvalused()))

# STYLE WINDOWS
# =============
def StyleWin(Type):
  command='StyleWin '
  command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# SUPERPOSE MULTIPLE OBJECTS (OBJECT)
# ===================================
def SupMultiObj(selection1, method=None, match=None, flip=None, unit=None):
  command='SupMultiObj '
  command+=selstr(selection1)+','
  if (method!=None): command+='Method='+cstr(method)+','
  if (match!=None): command+='Match='+cstr(match)+','
  if (flip!=None): command+='Flip='+cstr(flip)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# SUPERPOSE MULTIPLE OBJECTS (MOLECULE)
# =====================================
def SupMultiMol(selection1, method=None, match=None, flip=None, unit=None):
  command='SupMultiMol '
  command+=selstr(selection1)+','
  if (method!=None): command+='Method='+cstr(method)+','
  if (match!=None): command+='Match='+cstr(match)+','
  if (flip!=None): command+='Flip='+cstr(flip)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# SUPERPOSE MULTIPLE OBJECTS (RESIDUE)
# ====================================
def SupMultiRes(selection1, method=None, match=None, flip=None, unit=None):
  command='SupMultiRes '
  command+=selstr(selection1)+','
  if (method!=None): command+='Method='+cstr(method)+','
  if (match!=None): command+='Match='+cstr(match)+','
  if (flip!=None): command+='Flip='+cstr(flip)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# SUPERPOSE MULTIPLE OBJECTS (ATOM)
# =================================
def SupMultiAtom(selection1, method=None, match=None, flip=None, unit=None):
  command='SupMultiAtom '
  command+=selstr(selection1)+','
  if (method!=None): command+='Method='+cstr(method)+','
  if (match!=None): command+='Match='+cstr(match)+','
  if (flip!=None): command+='Flip='+cstr(flip)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# SUPERPOSE OBJECTS ON ORDERED UNITS (MOLECULE)
# =============================================
def SupOrderedMol(selection1, selection2, selection3, selection4, selection5, selection6, *arglist2):
  command='SupOrderedMol '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  command+=selstr(selection3)+','
  command+=selstr(selection4)+','
  command+=selstr(selection5)+','
  command+=selstr(selection6)+','
  # ANY NUMBER OF VARIABLE ARGUMENTS CAN FOLLOW
  for arglist in arglist2:
    if (type(arglist)!=type([])): arglist=[arglist]
    for arg in arglist:
      command+=cstr(arg,quoted=(type(arg)!=type(1) and type(arg)!=type(1.)))+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SUPERPOSE OBJECTS ON ORDERED UNITS (RESIDUE)
# ============================================
def SupOrderedRes(selection1, selection2, selection3, selection4, selection5, selection6, *arglist2):
  command='SupOrderedRes '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  command+=selstr(selection3)+','
  command+=selstr(selection4)+','
  command+=selstr(selection5)+','
  command+=selstr(selection6)+','
  # ANY NUMBER OF VARIABLE ARGUMENTS CAN FOLLOW
  for arglist in arglist2:
    if (type(arglist)!=type([])): arglist=[arglist]
    for arg in arglist:
      command+=cstr(arg,quoted=(type(arg)!=type(1) and type(arg)!=type(1.)))+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SUPERPOSE OBJECTS ON ORDERED UNITS (ATOM)
# =========================================
def SupOrderedAtom(selection1, selection2, selection3, selection4, selection5, selection6, *arglist2):
  command='SupOrderedAtom '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  command+=selstr(selection3)+','
  command+=selstr(selection4)+','
  command+=selstr(selection5)+','
  command+=selstr(selection6)+','
  # ANY NUMBER OF VARIABLE ARGUMENTS CAN FOLLOW
  for arglist in arglist2:
    if (type(arglist)!=type([])): arglist=[arglist]
    for arg in arglist:
      command+=cstr(arg,quoted=(type(arg)!=type(1) and type(arg)!=type(1.)))+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SUPERPOSE OBJECTS (OBJECT)
# ==========================
def SupObj(selection1, selection2, match=None, flip=None, unit=None):
  command='SupObj '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (match!=None): command+='Match='+cstr(match)+','
  if (flip!=None): command+='Flip='+cstr(flip)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# SUPERPOSE OBJECTS (MOLECULE)
# ============================
def SupMol(selection1, selection2, match=None, flip=None, unit=None):
  command='SupMol '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (match!=None): command+='Match='+cstr(match)+','
  if (flip!=None): command+='Flip='+cstr(flip)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# SUPERPOSE OBJECTS (RESIDUE)
# ===========================
def SupRes(selection1, selection2, match=None, flip=None, unit=None):
  command='SupRes '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (match!=None): command+='Match='+cstr(match)+','
  if (flip!=None): command+='Flip='+cstr(flip)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# SUPERPOSE OBJECTS (ATOM)
# ========================
def SupAtom(selection1, selection2, match=None, flip=None, unit=None):
  command='SupAtom '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (match!=None): command+='Match='+cstr(match)+','
  if (flip!=None): command+='Flip='+cstr(flip)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET SURFACE PARAMETERS
# ==========================
def SurfPar(probe=None, resolution=None, molecular=None, espmax=None, smoothcut=None, radii=None, unite=None):
  command='SurfPar '
  if (probe!=None): command+='Probe='+cstr(probe)+','
  if (resolution!=None): command+='Resolution='+cstr(resolution)+','
  if (molecular!=None): command+='Molecular='+cstr(molecular)+','
  if (espmax!=None): command+='ESPMax='+cstr(espmax)+','
  if (smoothcut!=None): command+='SmoothCut='+cstr(smoothcut)+','
  if (radii!=None): command+='Radii='+cstr(radii)+','
  if (unite!=None): command+='Unite='+cstr(unite)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE DISTANCE FROM SURFACE (OBJECT)
# ========================================
def SurfDisObj(selection1, Type, results=None):
  command='SurfDisObj '
  command+=selstr(selection1)+','
  command+='Type='+cstr(Type)+','
  if (results!=None): command+='Results='+cstr(results)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE DISTANCE FROM SURFACE (MOLECULE)
# ==========================================
def SurfDisMol(selection1, Type, results=None):
  command='SurfDisMol '
  command+=selstr(selection1)+','
  command+='Type='+cstr(Type)+','
  if (results!=None): command+='Results='+cstr(results)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE DISTANCE FROM SURFACE (RESIDUE)
# =========================================
def SurfDisRes(selection1, Type, results=None):
  command='SurfDisRes '
  command+=selstr(selection1)+','
  command+='Type='+cstr(Type)+','
  if (results!=None): command+='Results='+cstr(results)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE DISTANCE FROM SURFACE (ATOM)
# ======================================
def SurfDisAtom(selection1, Type, results=None):
  command='SurfDisAtom '
  command+=selstr(selection1)+','
  command+='Type='+cstr(Type)+','
  if (results!=None): command+='Results='+cstr(results)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE ELECTROSTATIC SURFACE POTENTIALS (ALL OR SELECTED)
# ============================================================
def SurfESP(Type=None, method=None, unit=None):
  command='SurfESP '
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (method!=None): command+='Method='+cstr(method)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE ELECTROSTATIC SURFACE POTENTIALS (ALL)
# ================================================
def SurfESPAll(Type=None, method=None, unit=None):
  command='SurfESPAll '
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (method!=None): command+='Method='+cstr(method)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE ELECTROSTATIC SURFACE POTENTIALS (OBJECT)
# ===================================================
def SurfESPObj(selection1, Type=None, method=None, unit=None):
  command='SurfESPObj '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (method!=None): command+='Method='+cstr(method)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE ELECTROSTATIC SURFACE POTENTIALS (MOLECULE)
# =====================================================
def SurfESPMol(selection1, Type=None, method=None, unit=None):
  command='SurfESPMol '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (method!=None): command+='Method='+cstr(method)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE ELECTROSTATIC SURFACE POTENTIALS (RESIDUE)
# ====================================================
def SurfESPRes(selection1, Type=None, method=None, unit=None):
  command='SurfESPRes '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (method!=None): command+='Method='+cstr(method)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE ELECTROSTATIC SURFACE POTENTIALS (ATOM)
# =================================================
def SurfESPAtom(selection1, Type=None, method=None, unit=None):
  command='SurfESPAtom '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (method!=None): command+='Method='+cstr(method)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE SURFACE AREAS (ALL OR SELECTED)
# =========================================
def Surf(Type=None, unit=None):
  command='Surf '
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE SURFACE AREAS (ALL)
# =============================
def SurfAll(Type=None, unit=None):
  command='SurfAll '
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE SURFACE AREAS (OBJECT)
# ================================
def SurfObj(selection1, Type=None, unit=None):
  command='SurfObj '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE SURFACE AREAS (MOLECULE)
# ==================================
def SurfMol(selection1, Type=None, unit=None):
  command='SurfMol '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE SURFACE AREAS (RESIDUE)
# =================================
def SurfRes(selection1, Type=None, unit=None):
  command='SurfRes '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE SURFACE AREAS (ATOM)
# ==============================
def SurfAtom(selection1, Type=None, unit=None):
  command='SurfAtom '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  return(runretval(command[:-1],retvalused()))

# CHANGE CHEMICAL ELEMENT OR ADD FUNCTIONAL GROUP
# ===============================================
def SwapAtom(selection1, element, updatebonds=None, updatehyd=None, rename=None, attachpoint=None):
  command='SwapAtom '
  command+=selstr(selection1)+','
  command+='Element='+cstr(element)+','
  if (updatebonds!=None): command+='UpdateBonds='+cstr(updatebonds)+','
  if (updatehyd!=None): command+='UpdateHyd='+cstr(updatehyd)+','
  if (rename!=None): command+='Rename='+cstr(rename)+','
  if (attachpoint!=None): command+='AttachPoint='+cstr(attachpoint)+','
  return(runretval(command[:-1],retvalused()))

# SWAP ORDER OF COVALENT BONDS
# ============================
def SwapBond(selection1, selection2, order=None, update=None):
  command='SwapBond '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (order!=None): command+='Order='+cstr(order)+','
  if (update!=None): command+='Update='+cstr(update)+','
  return(runretval(command[:-1],retvalused()))

# SWAP HYDROGEN ORDERING IN RESIDUES (ALL OR SELECTED)
# ====================================================
def SwapHyd(order):
  command='SwapHyd '
  command+='Order='+cstr(order)+','
  return(runretval(command[:-1],retvalused()))

# SWAP HYDROGEN ORDERING IN RESIDUES (ALL)
# ========================================
def SwapHydAll(order):
  command='SwapHydAll '
  command+='Order='+cstr(order)+','
  return(runretval(command[:-1],retvalused()))

# SWAP HYDROGEN ORDERING IN RESIDUES (OBJECT)
# ===========================================
def SwapHydObj(selection1, order):
  command='SwapHydObj '
  command+=selstr(selection1)+','
  command+='Order='+cstr(order)+','
  return(runretval(command[:-1],retvalused()))

# SWAP IMAGES
# ===========
def SwapImage(selection1, selection2):
  command='SwapImage '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  return(runretval(command[:-1],retvalused()))

# SWAP TWO OBJECTS IN THE LIST
# ============================
def SwapObj(selection1, selection2):
  command='SwapObj '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  return(runretval(command[:-1],retvalused()))

# SWAP ATOM POSITIONS
# ===================
def SwapPosAtom(selection1, selection2, bound=None):
  command='SwapPosAtom '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (bound!=None): command+='Bound='+cstr(bound)+','
  return(runretval(command[:-1],retvalused()))

# SWAP RESIDUE SIDE-CHAINS
# ========================
def SwapRes(selection1, new, isomer=None):
  command='SwapRes '
  command+=selstr(selection1)+','
  command+='new='+cstr(new)+','
  if (isomer!=None): command+='Isomer='+cstr(isomer)+','
  return(runretval(command[:-1],retvalused()))

# SWITCH OBJECTS ON/OFF (ALL OR SELECTED)
# =======================================
def Switch(visibility=None, wait=None):
  command='Switch '
  if (visibility!=None): command+='Visibility='+cstr(visibility)+','
  if (wait!=None): command+='Wait='+cstr(wait)+','
  return(runretval(command[:-1],retvalused()))

# SWITCH OBJECTS ON/OFF (ALL)
# ===========================
def SwitchAll(visibility=None, wait=None):
  command='SwitchAll '
  if (visibility!=None): command+='Visibility='+cstr(visibility)+','
  if (wait!=None): command+='Wait='+cstr(wait)+','
  return(runretval(command[:-1],retvalused()))

# SWITCH OBJECTS ON/OFF (OBJECT)
# ==============================
def SwitchObj(selection1, visibility=None, wait=None):
  command='SwitchObj '
  command+=selstr(selection1)+','
  if (visibility!=None): command+='Visibility='+cstr(visibility)+','
  if (wait!=None): command+='Wait='+cstr(wait)+','
  return(runretval(command[:-1],retvalused()))

# GET SYSTEM TIME
# ===============
def SystemTime():
  command='SystemTime '
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SET/GET TABLE CELLS
# ===================
def Tab(selection1, column=None, row=None, page=None, set=None, numformat=None):
  command='Tab '
  command+=selstr(selection1)+','
  if (column!=None): command+='Column='+cstr(column)+','
  if (row!=None): command+='Row='+cstr(row)+','
  if (page!=None): command+='Page='+cstr(page)+','
  if (set!=None): command+='Set='+cstr(set)+','
  if (numformat!=None): command+='NumFormat='+cstr(numformat)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET SIMULATION TEMPERATURE
# ==============================
def Temp(degrees=None, reassign=None):
  command='Temp '
  if (degrees!=None): command+='degrees='+cstr(degrees)+','
  if (reassign!=None): command+='Reassign='+cstr(reassign)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SET TEMPERATURE CONTROL
# =======================
def TempCtrl(Type):
  command='TempCtrl '
  command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# SET/GET SIMULATION TIME
# =======================
def Time(fs=None):
  command='Time '
  if (fs!=None): command+='FS='+cstr(fs)+','
  result=runretval(command[:-1],retvalused())
  if (result!=None and len(result)): return(result[0])
  return(result)

# SET SIMULATION TIMESTEP
# =======================
def TimeStep(inter=None, intra=None):
  command='TimeStep '
  if (inter!=None): command+='Inter='+cstr(inter)+','
  if (intra!=None): command+='Intra='+cstr(intra)+','
  return(runretval(command[:-1],retvalused()))

# TRANSFER OBJECTS INTO ANOTHER COORDINATE SYSTEM (ALL OR SELECTED)
# =================================================================
def Transfer(selection1, local=None):
  command='Transfer '
  command+=selstr(selection1)+','
  if (local!=None): command+='Local='+cstr(local)+','
  return(runretval(command[:-1],retvalused()))

# TRANSFER OBJECTS INTO ANOTHER COORDINATE SYSTEM (ALL)
# =====================================================
def TransferAll(selection1, local=None):
  command='TransferAll '
  command+=selstr(selection1)+','
  if (local!=None): command+='Local='+cstr(local)+','
  return(runretval(command[:-1],retvalused()))

# TRANSFER OBJECTS INTO ANOTHER COORDINATE SYSTEM (OBJECT)
# ========================================================
def TransferObj(selection1, selection2, local=None):
  command='TransferObj '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (local!=None): command+='Local='+cstr(local)+','
  return(runretval(command[:-1],retvalused()))

# GET PREVIOUSLY APPLIED TRANSFORMATIONS
# ======================================
def Transformation(Type=None, number=None):
  command='Transformation '
  if (Type!=None): command+='Type='+cstr(Type)+','
  if (number!=None): command+='Number='+cstr(number)+','
  return(runretval(command[:-1],retvalused()))

# TRANSFORM OBJECTS (ALL OR SELECTED)
# ===================================
def Transform(keeppos=None):
  command='Transform '
  if (keeppos!=None): command+='KeepPos='+cstr(keeppos)+','
  return(runretval(command[:-1],retvalused()))

# TRANSFORM OBJECTS (ALL)
# =======================
def TransformAll(keeppos=None):
  command='TransformAll '
  if (keeppos!=None): command+='KeepPos='+cstr(keeppos)+','
  return(runretval(command[:-1],retvalused()))

# TRANSFORM OBJECTS (OBJECT)
# ==========================
def TransformObj(selection1, keeppos=None):
  command='TransformObj '
  command+=selstr(selection1)+','
  if (keeppos!=None): command+='KeepPos='+cstr(keeppos)+','
  return(runretval(command[:-1],retvalused()))

# TWIST OBJECTS TO IMPROVE STRUCTURAL ALIGNMENT (OBJECT)
# ======================================================
def TwistObj(selection1, selection2, strength=None, structures=None):
  command='TwistObj '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (strength!=None): command+='Strength='+cstr(strength)+','
  if (structures!=None): command+='Structures='+cstr(structures)+','
  return(runretval(command[:-1],retvalused()))

# TWIST OBJECTS TO IMPROVE STRUCTURAL ALIGNMENT (MOLECULE)
# ========================================================
def TwistMol(selection1, selection2, strength=None, structures=None):
  command='TwistMol '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (strength!=None): command+='Strength='+cstr(strength)+','
  if (structures!=None): command+='Structures='+cstr(structures)+','
  return(runretval(command[:-1],retvalused()))

# GET THE ATOM TYPE
# =================
def TypeAtom(selection1, method=None):
  command='TypeAtom '
  command+=selstr(selection1)+','
  if (method!=None): command+='Method='+cstr(method)+','
  return(runretval(command[:-1],retvalused()))

# ASSIGN BOND ORDERS AUTOMATICALLY
# ================================
def TypeBond(selection1, selection2, usetopo=None, kekulize=None, hydmissing=None):
  command='TypeBond '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (usetopo!=None): command+='useTopo='+cstr(usetopo)+','
  if (kekulize!=None): command+='Kekulize='+cstr(kekulize)+','
  if (hydmissing!=None): command+='HydMissing='+cstr(hydmissing)+','
  return(runretval(command[:-1],retvalused()))

# SET NUMBER OF UNDO LEVELS
# =========================
def UndoLevels(number):
  command='UndoLevels '
  command+='Number='+cstr(number)+','
  return(runretval(command[:-1],retvalused()))

# REMOVE ATOMS FROM GROUP (ALL OR SELECTED)
# =========================================
def Ungroup(name):
  command='Ungroup '
  command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# REMOVE ATOMS FROM GROUP (ALL)
# =============================
def UngroupAll(name):
  command='UngroupAll '
  command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# REMOVE ATOMS FROM GROUP (OBJECT)
# ================================
def UngroupObj(selection1, name):
  command='UngroupObj '
  command+=selstr(selection1)+','
  command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# REMOVE ATOMS FROM GROUP (MOLECULE)
# ==================================
def UngroupMol(selection1, name):
  command='UngroupMol '
  command+=selstr(selection1)+','
  command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# REMOVE ATOMS FROM GROUP (RESIDUE)
# =================================
def UngroupRes(selection1, name):
  command='UngroupRes '
  command+=selstr(selection1)+','
  command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# REMOVE ATOMS FROM GROUP (ATOM)
# ==============================
def UngroupAtom(selection1, name):
  command='UngroupAtom '
  command+=selstr(selection1)+','
  command+='Name='+cstr(name)+','
  return(runretval(command[:-1],retvalused()))

# DELETE DISTANCES LABELS
# =======================
def UnlabelDis(selection1, selection2, bound=None):
  command='UnlabelDis '
  command+=selstr(selection1)+','
  command+=selstr(selection2)+','
  if (bound!=None): command+='bound='+cstr(bound)+','
  return(runretval(command[:-1],retvalused()))

# DELETE LABELS (ALL OR SELECTED)
# ===============================
def Unlabel():
  command='Unlabel '
  return(runretval(command[:-1],retvalused()))

# DELETE LABELS (ALL)
# ===================
def UnlabelAll():
  command='UnlabelAll '
  return(runretval(command[:-1],retvalused()))

# DELETE LABELS (OBJECT)
# ======================
def UnlabelObj(selection1):
  command='UnlabelObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# DELETE LABELS (MOLECULE)
# ========================
def UnlabelMol(selection1):
  command='UnlabelMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# DELETE LABELS (SEGMENT)
# =======================
def UnlabelSeg(selection1):
  command='UnlabelSeg '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# DELETE LABELS (RESIDUE)
# =======================
def UnlabelRes(selection1):
  command='UnlabelRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# DELETE LABELS (ATOM)
# ====================
def UnlabelAtom(selection1):
  command='UnlabelAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# LET ANIMATED IMAGE DISAPPEAR
# ============================
def UnrestImage(selection1):
  command='UnrestImage '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# UNSELECT ATOMS (ALL OR SELECTED)
# ================================
def Unselect():
  command='Unselect '
  return(runretval(command[:-1],retvalused()))

# UNSELECT ATOMS (ALL)
# ====================
def UnselectAll():
  command='UnselectAll '
  return(runretval(command[:-1],retvalused()))

# UNSELECT ATOMS (OBJECT)
# =======================
def UnselectObj(selection1):
  command='UnselectObj '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# UNSELECT ATOMS (MOLECULE)
# =========================
def UnselectMol(selection1):
  command='UnselectMol '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# UNSELECT ATOMS (RESIDUE)
# ========================
def UnselectRes(selection1):
  command='UnselectRes '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# UNSELECT ATOMS (ATOM)
# =====================
def UnselectAtom(selection1):
  command='UnselectAtom '
  command+=selstr(selection1)+','
  return(runretval(command[:-1],retvalused()))

# SET USER INPUT
# ==============
def UserInput(status=None):
  command='UserInput '
  if (status!=None): command+='Status='+cstr(status)+','
  return(runretval(command[:-1],retvalused()))

# GET ORIENTATION VECTORS
# =======================
def VecOri(alpha, beta, gamma):
  command='VecOri '
  command+='Alpha='+cstr(alpha)+','
  command+='Beta='+cstr(beta)+','
  command+='Gamma='+cstr(gamma)+','
  return(runretval(command[:-1],retvalused()))

# WAIT FOR CERTAIN TIME PERIOD OR CONDITION
# =========================================
def Wait(steps, unit=None):
  command='Wait '
  command+=cstr(steps)+','
  if (unit!=None): command+='Unit='+cstr(unit)+','
  # ALWAYS GET A RETURN VALUE TO SYNCHRONIZE THREADS
  result=runretval(command[:-1],1)
  if (result!=None and len(result)): return(result[0])
  return(result)

# TREAT WARNINGS AS ERRORS
# ========================
def WarnIsError(flag):
  command='WarnIsError '
  command+='Flag='+cstr(flag)+','
  return(runretval(command[:-1],retvalused()))

# SET TIMEOUT FOR INTERNET CONNECTIONS
# ====================================
def WebTimeout(seconds=None):
  command='WebTimeout '
  if (seconds!=None): command+='Seconds='+cstr(seconds)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE VOLUMES (ALL OR SELECTED)
# ===================================
def Volume(Type=None):
  command='Volume '
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE VOLUMES (ALL)
# =======================
def VolumeAll(Type=None):
  command='VolumeAll '
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE VOLUMES (OBJECT)
# ==========================
def VolumeObj(selection1, Type=None):
  command='VolumeObj '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE VOLUMES (MOLECULE)
# ============================
def VolumeMol(selection1, Type=None):
  command='VolumeMol '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE VOLUMES (RESIDUE)
# ===========================
def VolumeRes(selection1, Type=None):
  command='VolumeRes '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# CALCULATE VOLUMES (ATOM)
# ========================
def VolumeAtom(selection1, Type=None):
  command='VolumeAtom '
  command+=selstr(selection1)+','
  if (Type!=None): command+='Type='+cstr(Type)+','
  return(runretval(command[:-1],retvalused()))

# SET WINDOW FONT
# ===============
def WinFont(location, name=None, height=None):
  command='WinFont '
  command+='Location='+cstr(location)+','
  if (name!=None): command+='Name='+cstr(name)+','
  if (height!=None): command+='Height='+cstr(height)+','
  return(runretval(command[:-1],retvalused()))

# SET WINDOW BACKGROUND TEXTURE
# =============================
def WinTexture(number):
  command='WinTexture '
  command+='Number='+cstr(number)+','
  return(runretval(command[:-1],retvalused()))

# WRITE HTML REPORT
# =================
def WriteReport():
  RaiseError('This command is only available with extensions Title,Heading,Paragraph,Table,Plot,Image,End in Python')

# WRITE HTML REPORT
# =================
# THIS IS ALTERNATIVE 1, WITH DIFFERENT PARAMETERS
def WriteReportTitle(filename, text):
  command='WriteReport Title,'
  command+='Filename='+cstr(filename)+','
  command+='Text='+cstr(text,1)+','
  return(runretval(command[:-1],retvalused()))

# WRITE HTML REPORT
# =================
# THIS IS ALTERNATIVE 2, WITH DIFFERENT PARAMETERS
def WriteReportHeading(level, text):
  command='WriteReport Heading,'
  command+='Level='+cstr(level)+','
  command+='Text='+cstr(text,1)+','
  return(runretval(command[:-1],retvalused()))

# WRITE HTML REPORT
# =================
# THIS IS ALTERNATIVE 3, WITH DIFFERENT PARAMETERS
def WriteReportParagraph(text):
  command='WriteReport Paragraph,'
  command+='Text='+cstr(text,1)+','
  return(runretval(command[:-1],retvalused()))

# WRITE HTML REPORT
# =================
# THIS IS ALTERNATIVE 4, WITH DIFFERENT PARAMETERS
def WriteReportTable(selection1, caption=None, numformat=None, rowsmax=None, infocolumn=None, datacolumn=None, datacolumns=None, *arglist2):
  command='WriteReport Table,'
  command+=selstr(selection1)+','
  if (caption!=None): command+='Caption='+cstr(caption)+','
  if (numformat!=None): command+='NumFormat='+cstr(numformat)+','
  if (rowsmax!=None): command+='RowsMax='+cstr(rowsmax)+','
  if (infocolumn!=None): command+='InfoColumn='+cstr(infocolumn)+','
  if (datacolumn!=None): command+='DataColumn='+cstr(datacolumn)+','
  if (datacolumns!=None): command+='DataColumns='+cstr(datacolumns)+','
  # ANY NUMBER OF VARIABLE ARGUMENTS CAN FOLLOW
  for arglist in arglist2:
    if (type(arglist)!=type([])): arglist=[arglist]
    for arg in arglist:
      command+=cstr(arg,quoted=(type(arg)!=type(1) and type(arg)!=type(1.)))+','
  return(runretval(command[:-1],retvalused()))

# WRITE HTML REPORT
# =================
# THIS IS ALTERNATIVE 5, WITH DIFFERENT PARAMETERS
def WriteReportPlot(caption, selection1, width, height, title, Type, xcolumn, ycolumn, ycolumns, xlabel, ylabel, legendpos, graphname, *arglist2):
  command='WriteReport Plot,'
  command+='Caption='+cstr(caption)+','
  command+=selstr(selection1)+','
  command+='Width='+cstr(width)+','
  command+='Height='+cstr(height)+','
  command+='Title='+cstr(title)+','
  command+='Type='+cstr(Type)+','
  command+='XColumn='+cstr(xcolumn)+','
  command+='YColumn='+cstr(ycolumn)+','
  command+='YColumns='+cstr(ycolumns)+','
  command+='XLabel='+cstr(xlabel)+','
  command+='YLabel='+cstr(ylabel)+','
  command+='LegendPos='+cstr(legendpos)+','
  command+='GraphName='+cstr(graphname)+','
  # ANY NUMBER OF VARIABLE ARGUMENTS CAN FOLLOW
  for arglist in arglist2:
    if (type(arglist)!=type([])): arglist=[arglist]
    for arg in arglist:
      command+=cstr(arg,quoted=(type(arg)!=type(1) and type(arg)!=type(1.)))+','
  return(runretval(command[:-1],retvalused()))

# WRITE HTML REPORT
# =================
# THIS IS ALTERNATIVE 6, WITH DIFFERENT PARAMETERS
def WriteReportImage(filename, style=None, caption=None, width=None, height=None, name=None, delete=None):
  command='WriteReport Image,'
  command+='Filename='+cstr(filename)+','
  if (style!=None): command+='Style='+cstr(style)+','
  if (caption!=None): command+='Caption='+cstr(caption)+','
  if (width!=None): command+='Width='+cstr(width)+','
  if (height!=None): command+='Height='+cstr(height)+','
  if (name!=None): command+='Name='+cstr(name)+','
  if (delete!=None): command+='Delete='+cstr(delete)+','
  return(runretval(command[:-1],retvalused()))

# WRITE HTML REPORT
# =================
# THIS IS ALTERNATIVE 7, WITH DIFFERENT PARAMETERS
def WriteReportEnd():
  command='WriteReport End,'
  return(runretval(command[:-1],retvalused()))

# ZOOM IN ON ATOMS (ALL OR SELECTED)
# ==================================
def Zoom(steps=None, wait=None):
  command='Zoom '
  if (steps!=None): command+='Steps='+cstr(steps)+','
  if (wait!=None): command+='Wait='+cstr(wait)+','
  return(runretval(command[:-1],retvalused()))

# ZOOM IN ON ATOMS (ALL)
# ======================
def ZoomAll(steps=None, wait=None):
  command='ZoomAll '
  if (steps!=None): command+='Steps='+cstr(steps)+','
  if (wait!=None): command+='Wait='+cstr(wait)+','
  return(runretval(command[:-1],retvalused()))

# ZOOM IN ON ATOMS (OBJECT)
# =========================
def ZoomObj(selection1, steps=None, wait=None):
  command='ZoomObj '
  command+=selstr(selection1)+','
  if (steps!=None): command+='Steps='+cstr(steps)+','
  if (wait!=None): command+='Wait='+cstr(wait)+','
  return(runretval(command[:-1],retvalused()))

# ZOOM IN ON ATOMS (MOLECULE)
# ===========================
def ZoomMol(selection1, steps=None, wait=None):
  command='ZoomMol '
  command+=selstr(selection1)+','
  if (steps!=None): command+='Steps='+cstr(steps)+','
  if (wait!=None): command+='Wait='+cstr(wait)+','
  return(runretval(command[:-1],retvalused()))

# ZOOM IN ON ATOMS (RESIDUE)
# ==========================
def ZoomRes(selection1, steps=None, wait=None):
  command='ZoomRes '
  command+=selstr(selection1)+','
  if (steps!=None): command+='Steps='+cstr(steps)+','
  if (wait!=None): command+='Wait='+cstr(wait)+','
  return(runretval(command[:-1],retvalused()))

# ZOOM IN ON ATOMS (ATOM)
# =======================
def ZoomAtom(selection1, steps=None, wait=None):
  command='ZoomAtom '
  command+=selstr(selection1)+','
  if (steps!=None): command+='Steps='+cstr(steps)+','
  if (wait!=None): command+='Wait='+cstr(wait)+','
  return(runretval(command[:-1],retvalused()))


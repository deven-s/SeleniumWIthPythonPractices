
from pywinauto import Application
from pywinauto.keyboard import send_keys, KeySequenceError
name = "chris"


app = Application(backend="uia").start("Notepad.exe")
app.UntitledNotepad.dump_tree()
writer_app = app.UntitledNotepad.child_window(title="Text Editor", auto_id="15", control_type="Edit").wrapper_object()
writer_app.type_keys("hi " + name +\
                     "{ENTER}"
                     "bye", with_spaces=True)

# Make the scroll bar visible by moving some lines down
for i in range(25):
    writer_app.type_keys("{ENTER}")


# Scroll up by clicking on the scroll bar up button
app.UntitledNotepad.UpButton.wait("ready", 4, 1).click_input()

app.UntitledNotepad.File.click_input()

# Try to save the file
app.UntitledNotepad.child_window(title_re="Save", control_type="MenuItem").click_input()


app.UntitledNotepad.dump_tree()
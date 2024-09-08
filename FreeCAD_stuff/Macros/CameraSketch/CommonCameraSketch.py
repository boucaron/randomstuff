import FreeCAD
import FreeCADGui

# Get Action is True restore from the hashtable otherwise False then set the camera for the sketch in the hashtable
def SetOrGetCameraSketch(sketch, getAction):
    FreeCAD.Console.PrintMessage("ListSketches.FCMacro start\n")
    doc = FreeCAD.ActiveDocument

    keyToSearch = ""
    # Define a global variable
    if not hasattr(FreeCAD, "SketchesCamera"):
        FreeCAD.SketchesCamera = {}

    if not sketch:
        FreeCAD.Console.PrintMessage("No ActiveSketch skipping\n")
    else:
        keyToSearch = sketch.FullName

    if doc is None:
        FreeCAD.Console.PrintError("No active document found!\n")
    else:
        # Get the active view (helps to determine if a sketch is being edited)
        active_view = FreeCADGui.ActiveDocument.ActiveView
        currentCamera = active_view.getCamera()
        FreeCAD.Console.PrintMessage(f"Current Camera: {currentCamera}\n")
        # Action is either a get or a set
        if getAction:
            FreeCAD.Console.PrintMessage("Restore the camera from sketch's camera\n")
            # Get from Hashtable Camera -  if not found write an error
            getValue = FreeCAD.SketchesCamera.get(keyToSearch)
            if getValue is not None:
                FreeCAD.Console.PrintMessage("Camera found, restoring\n")
                FreeCAD.Console.PrintMessage(f"KeyToSearch: {keyToSearch}\n")
                active_view.setCamera(getValue)
            else:
                FreeCAD.Console.PrintMessage("Camera not found\n")
        else:
            FreeCAD.Console.PrintMessage("Save the current camera for the sketch\n")
            FreeCAD.Console.PrintMessage(f"KeyToSearch: {keyToSearch}\n")
            # Set in Hashtable the Camera
            FreeCAD.SketchesCamera[keyToSearch] = currentCamera
        
        

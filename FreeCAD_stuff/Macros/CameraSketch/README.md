# Proof of Concept: Preserve Matrix Transformation When Editing Sketches

This repository provides a proof of concept for the feature request discussed on the FreeCAD forum: [Preserve Matrix Transformation When Editing Sketches](https://forum.freecad.org/viewtopic.php?p=780832#p780832).

## Overview

This PoC includes two macros designed to help preserve and restore the camera view while editing sketches in FreeCAD.

### How It Works

1. **Setting the Camera**:
   - When you edit a sketch, run the `SetCameraFromSketch` macro. This macro will save the current camera view.

2. **Restoring the Camera**:
   - After making changes to your sketch and wanting to return to your previous view, run the `GetCameraFromSketch` macro. This will restore the camera view that was saved earlier.

### Installation

1. **Download**:
   - Download the provided macros (with the associated python file) into your FreeCAD macros directory. This is typically located in your FreeCAD user directory.

2. **Run the Macros**:
   - Use FreeCAD’s macro dialog to run the `SetCameraFromSketch` and `GetCameraFromSketch` macros as needed.

### Notes

- **Data Persistence**:
  - The camera settings are stored only in memory during runtime and are not saved within the FreeCAD file. 

For more details and discussions about this feature, visit the [FreeCAD Forum thread](https://forum.freecad.org/viewtopic.php?p=780832#p780832).




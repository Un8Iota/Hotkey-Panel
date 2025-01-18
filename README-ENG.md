# **Hotkey Panels** Add-on – Experimental Version

## Overview

Hotkey Panels is an add-on designed to streamline your workflow in Blender by allowing you to display add-on panels as contextual (pop-up) menus.

It automatically detects these panels and enables you to create shortcuts for quick access to your favorite features, without constantly digging through the sidebar. This helps you save valuable time and maintain a more organized workspace.

> **Note**: Only the experimental version is provided here, which may lead to compatibility or stability issues. It is therefore recommended to use it on non-critical projects or make regular backups of your work.
>
> **Important**: If certain add-ons do not include the code required to be managed by Hotkey Panels, I unfortunately cannot remedy that.
>
> Some panels are only visible if the conditions set by their original add-on are met (for example, having a specific object selected, being in Edit mode, or having an armature, etc.). If a panel you expect to see does not appear, please check that those conditions are satisfied in your scene.

---

## Installation

1. **Download the add-on** (the `.py` file).
2. Open Blender, then go to **`Edit > Preferences > Add-ons`**.
3. Click **`Install`** and select the downloaded `.py` file.
4. Then enable the plugin from the Add-ons list.

---

## Key Features

- **Custom Keyboard Shortcuts**  
  Assign single keys (or key combinations) to instantly display panels extracted from your favorite add-ons.

- **Flexible Shortcut Management**  
  Quickly enable or disable a shortcut in the add-on preferences. You can also easily duplicate or remove a shortcut.

- **Automatic Panel Organization**  
  Panels are categorized by the add-on they come from, which makes it easier to locate them (using each add-on’s HEADER).

- **Customizable Icons and Names**  
  Give each panel its own name and icon for faster recognition.

- **Shortcut Import/Export**  
  Lets you copy a Hotkey Panel’s configuration to your clipboard, then import it with a single click—whether into another Hotkey Panel or even another Blender version.  
  Save your configuration or share it with other users effortlessly.

---

## Panel Display Modes

- **Standard (Stable)**  
  Displays a traditional context menu when you use the shortcut. You then choose the panel you want from those associated with it.

- **Pop-up (Experimental)**  
  Immediately shows panels in a pop-up menu, positioned according to the settings defined for each panel in the corresponding Hotkey Panel.  
  > **Note**: This feature is experimental and may present stability or compatibility issues depending on your setup and Blender version.  
  > It generally works without too many bugs on versions prior to 3.5, but can be unstable from Blender 3.6 and above.

- **Pie Menu (Stable)**  
  Provides a circular menu featuring multiple panels. This setup is ideal for quickly browsing different categories, with a pagination system if you have more panels than can be displayed at once.

---

## Quick Start

1. In the **Add-on Preferences**, create a new shortcut by clicking on **“Add Hotkey Panel”**.
2. Select your desired keys (e.g., `Q` with optional `Ctrl/Alt/Shift`).
3. Choose the **Execution Mode** among:
   - **Standard**
   - **Pop Up**
   - **Pie Menu**
4. Select one or more panels to associate with the shortcut, then optionally customize their names, icons, or margins (if you’re using **Pop Up**).
5. Close the preferences and test your shortcut in the 3D View.

---

## Important Notes and Limitations

> **Note**: This feature is experimental and may present stability or compatibility issues depending on your setup and Blender version.  
> It generally works fine with versions prior to 3.5, but can be unstable from Blender 3.6 and above.

> **Note**: Only the experimental version is provided here, so it may exhibit compatibility and stability problems. It’s recommended for non-critical projects or frequent backups.

> **Important**: If certain add-ons do not have the code necessary for Hotkey Panels to manage them, unfortunately I cannot fix that.

> Some panels are only visible if the conditions from their original add-on are met (for example, having a specific object selected, being in Edit mode, having an armature, etc.). If a panel that should appear is not showing, please make sure you have fulfilled those conditions in your scene.

---

## Support and Community

- **Blender Artists Forum**: Share your feedback or bug reports on the [dedicated thread](https://blenderartists.org/t/hotkey-panels-feedback/1542369?u=soee).  
- **Video Tutorials**: Check out upcoming YouTube videos for a step-by-step demonstration.  
- **Other Links**: Find all official resources and links on my [Linktree].

---

Feel free to share your feedback and report any issues. Your input helps the add-on continue to evolve and become more stable.

---

**Created by**: Soee  
**Version**: 2.5 (Experimental)  
**License**: Community  

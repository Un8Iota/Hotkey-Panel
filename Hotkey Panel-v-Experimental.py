import bpy
from bpy.types import Operator, AddonPreferences, PropertyGroup, UIList, Menu
from bpy.props import StringProperty, EnumProperty, BoolProperty, PointerProperty, CollectionProperty, IntProperty

bl_info = {
    "name": "Hotkey Panels",
    "blender": (3, 4, 0),
    "category": "Interface",
    "location": "Blender preferences > Add-ons",
    "author": "Soee",
    "version": (2, 5),
    "description": "Add-on to create hotkeys for quickly displaying selected panels in the 3D Viewport",
    "wiki_url": "",
    "tracker_url": "https://blenderartists.org/t/hotkey-panels-feedback/1542369?u=soee",
    "support": "COMMUNITY",
    "doc_url": "https://iotasoee.gumroad.com/l/HotkeyPanels",
}


def update_category_items(self, context):
    """Update the category items for the EnumProperty dynamically."""
    search_text = self.search_filter.lower()
    categories = {}
    for cls in bpy.types.Panel.__subclasses__():
        if hasattr(cls, 'bl_idname') and cls.bl_idname:
            category = cls.bl_category if hasattr(cls, 'bl_category') else "Uncategorized"
            if search_text in cls.bl_label.lower() or search_text in cls.bl_idname.lower() or search_text in category.lower():
                if category not in categories:
                    categories[category] = []
                categories[category].append((cls.bl_idname, cls.bl_label, ""))
    organized_panels = []
    for category, panels in sorted(categories.items()):
        organized_panels.append((f"HEADER_{category}", f"-- {category} --", ""))
        organized_panels.extend(panels)
    return organized_panels


class PanelItem(PropertyGroup):
    name: StringProperty()
    display_name: StringProperty(
        name="Display Name",
        description="Friendly name to display for the panel",
        default=""
    ) # type: ignore
    icon: StringProperty(
        name="Icon",
        description="Icon for the panel",
        default='NONE'
    ) # type: ignore
    f_mp_x_padding: IntProperty(
        name="Horizontal Padding (F-MPADDING X)",
        description="Adjust the horizontal padding (X axis) of this panel",
        default=0,
        min=-500,
        max=500
    ) # type: ignore
    f_mp_y_padding: IntProperty(
        name="Vertical Padding (F-MPADDING Y)",
        description="Adjust the vertical padding (Y axis) of this panel",
        default=0,
        min=-500,
        max=500
    ) # type: ignore
    is_active: BoolProperty(
        name="Active",
        description="Enable or disable this panel",
        default=True
    ) # type: ignore


class HotkeyPanelShortcut(PropertyGroup):
    user_name: StringProperty(
        name="Hotkey Panel Name",
        description="Name of the hotkey panel shortcut for display purposes",
        default="Hotkey Panel Name"
    ) # type: ignore
    internal_name: StringProperty(
        name="Internal Name",
        description="Internal name of the hotkey panel shortcut",
        default="Hotkey Panel"
    ) # type: ignore
    panels: CollectionProperty(type=PanelItem)
    active_panel_index: IntProperty()
    search_filter: StringProperty(
        name="Search Filter",
        description="Filter panels by name or category",
        default=""
    ) # type: ignore
    panel: EnumProperty(
        name="Select Panel",
        description="Select the panel to display",
        items=update_category_items,
        update=lambda self, context: self.update_selected_panel(context)
    ) # type: ignore
    keymap: EnumProperty(
        name="Key",
        description="Key or mouse button to open the panel",
        items=[
            # Standard Keys
            ('A', 'A', ''), ('B', 'B', ''), ('C', 'C', ''), ('D', 'D', ''), ('E', 'E', ''),
            ('F', 'F', ''), ('G', 'G', ''), ('H', 'H', ''), ('I', 'I', ''), ('J', 'J', ''),
            ('K', 'K', ''), ('L', 'L', ''), ('M', 'M', ''), ('N', 'N', ''), ('O', 'O', ''),
            ('P', 'P', ''), ('Q', 'Q', ''), ('R', 'R', ''), ('S', 'S', ''), ('T', 'T', ''),
            ('U', 'U', ''), ('V', 'V', ''), ('W', 'W', ''), ('X', 'X', ''), ('Y', 'Y', ''),
            ('Z', 'Z', ''),
            # Numbers
            ('ONE', '1', ''), ('TWO', '2', ''), ('THREE', '3', ''), ('FOUR', '4', ''),
            ('FIVE', '5', ''), ('SIX', '6', ''), ('SEVEN', '7', ''), ('EIGHT', '8', ''), ('NINE', '9', ''), ('ZERO', '0', ''),
            # Function Keys
            ('F1', 'F1', ''), ('F2', 'F2', ''), ('F3', 'F3', ''), ('F4', 'F4', ''),
            ('F5', 'F5', ''), ('F6', 'F6', ''), ('F7', 'F7', ''), ('F8', 'F8', ''), ('F9', 'F9', ''),
            ('F10', 'F10', ''), ('F11', 'F11', ''), ('F12', 'F12', ''),
            # Mouse Buttons
            ('LEFTMOUSE', 'Left Mouse', ''), ('MIDDLEMOUSE', 'Middle Mouse', ''), ('RIGHTMOUSE', 'Right Mouse', ''),
            ('BUTTON4MOUSE', 'Button 4 Mouse', ''), ('BUTTON5MOUSE', 'Button 5 Mouse', ''),
            ('WHEELUPMOUSE', 'Mouse Wheel Up', ''), ('WHEELDOWNMOUSE', 'Mouse Wheel Down', ''),
            ('WHEELINMOUSE', 'Mouse Wheel In', ''), ('WHEELOUTMOUSE', 'Mouse Wheel Out', ''),
            # Special Characters for French Keyboard
            ('AMPERSAND', '&', 'Ampersand'), ('E_ACUTE', 'é', 'E acute'), ('QUOTATION', '"', 'Quotation mark'),
            ('APOSTROPHE', '\'', 'Apostrophe'), ('LEFT_PAREN', '(', 'Left parenthesis'), ('HYPHEN', '-', 'Hyphen'),
            ('E_GRAVE', 'è', 'E grave'), ('UNDERSCORE', '_', 'Underscore'), ('C_CEDILLA', 'ç', 'C cedilla'),
            ('A_GRAVE', 'à', 'A grave'), ('RIGHT_PAREN', ')', 'Right parenthesis'), ('EQUALS', '=', 'Equals sign'),
            # Add other keys as needed
        ],
        default='Q',
        update=lambda self, context: update_shortcut(self, context)
    ) # type: ignore
    event_value: EnumProperty(
        name="Event Value",
        description="Type of event",
        items=[
            ('ANY', 'Any', ''),
            ('PRESS', 'Press', ''),
            ('RELEASE', 'Release', ''),
            ('CLICK', 'Click', ''),
            ('DOUBLE_CLICK', 'Double Click', ''),
            ('CLICK_DRAG', 'Click Drag', ''),
            ('NOTHING', 'Nothing', '')
        ],
        default='PRESS',
        update=lambda self, context: update_shortcut(self, context)
    ) # type: ignore
    ctrl: BoolProperty(
        name="Ctrl",
        description="Press Ctrl",
        default=False,
        update=lambda self, context: update_shortcut(self, context)
    ) # type: ignore
    shift: BoolProperty(
        name="Shift",
        description="Press Shift",
        default=False,
        update=lambda self, context: update_shortcut(self, context)
    ) # type: ignore
    alt: BoolProperty(
        name="Alt",
        description="Press Alt",
        default=False,
        update=lambda self, context: update_shortcut(self, context)
    ) # type: ignore

    is_enabled: BoolProperty(
        name="Enabled",
        description="Enable or disable this Hotkey Panel",
        default=True,
        update=lambda self, context: update_shortcut(self, context)
    ) # type: ignore

    execution_mode: EnumProperty(
        name="Execution Mode",
        description="Choose how the panels are displayed for this hotkey",
        items=[
            ('STANDARD', "Standard", "Standard version with popup menu"),
            ('POPUP', "Pop Up", "Activate panels directly under cursor"),
            ('PIE_MENU', "Pie Menu", "Display panels using a pie menu"),
        ],
        default='STANDARD',
    ) # type: ignore

    def update_selected_panel(self, context):
        pass


class PANEL_UL_panel_list(UIList):
    def draw(self, context):
        layout = self.layout
        data = self.list_id  # data is the HotkeyPanelShortcut
        execution_mode = data.execution_mode  # Access execution_mode from the shortcut

        collection = getattr(data, self.list_propname)
        index = getattr(data, self.active_propname)

        shortcut = data  # data is the HotkeyPanelShortcut
        active_panels = [p for p in shortcut.panels if p.is_active]

        panels_per_page = 6

        last_page_number = None

        for i, item in enumerate(collection):
            if execution_mode == 'PIE_MENU' and item.is_active:
                active_index = active_panels.index(item)
                page_number = active_index // panels_per_page + 1
            else:
                page_number = None

            if execution_mode == 'PIE_MENU' and item.is_active:
                if page_number != last_page_number:
                    # Insert page label
                    layout.label(text=f"Page {page_number}", icon='NONE')
                    last_page_number = page_number
            elif execution_mode == 'PIE_MENU' and not item.is_active:
                if last_page_number != "Inactive":
                    layout.label(text="Inactive Panels", icon='NONE')
                    last_page_number = "Inactive"
            else:
                if last_page_number != "Panels":
                    layout.label(text="Panels", icon='NONE')
                    last_page_number = "Panels"

            # Draw the item
            self.draw_item(context, layout, data, item, 0, data, self.active_propname, i)

    def draw_item(self, context, layout, data, item, icon, active_data, active_propname, index):
        execution_mode = data.execution_mode  # Access execution_mode from data

        row = layout.row(align=True)
        # Toggle button to activate/deactivate panel
        row.prop(item, "is_active", text="", icon='CHECKBOX_HLT' if item.is_active else 'CHECKBOX_DEHLT', emboss=False)
        row.prop(item, "name", text="", emboss=False, icon='BLENDER' if item.name else 'ERROR')
        row.prop(item, "display_name", text="Display Name", emboss=False, icon=item.icon if item.icon else 'NONE')

        # Display padding options if execution_mode is 'POPUP'
        if execution_mode == 'POPUP':
            row.prop(item, "f_mp_x_padding", text="X Padding", slider=True)
            row.prop(item, "f_mp_y_padding", text="Y Padding", slider=True)


class HotkeyPanelPreferences(AddonPreferences):
    bl_idname = __name__

    tabs: EnumProperty(
        name="Tabs",
        description="Choose a tab",
        items=[
            ('HOTKEY', "Hotkey Map", ""),
        ],
        default='HOTKEY'
    ) # type: ignore

    shortcuts: CollectionProperty(type=HotkeyPanelShortcut)
    active_shortcut_index: IntProperty(default=-1)

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.prop(self, "tabs", expand=True)

        box = layout.box()

        if self.tabs == 'HOTKEY':
            self.draw_hotkey_map(box)

    def draw_hotkey_map(self, layout):
        col = layout.column()

        # Add shortcut button
        row = layout.row()
        row.operator("hotkey_panel.add_shortcut", icon='ADD')

        for i, shortcut in enumerate(self.shortcuts):
            box = col.box()

            # Creating a hierarchical layout like in the keymap UI
            row = box.row(align=True)
            row.prop(shortcut, "is_enabled", text="", icon='CHECKBOX_HLT' if shortcut.is_enabled else 'CHECKBOX_DEHLT')

            # Use dynamic split for better space allocation
            split = row.split(factor=0.2)
            split.prop(shortcut, "user_name", text="")

            row = split.row(align=True)
            row.scale_x = 1
            row.alignment = 'RIGHT'
            row.prop(shortcut, "execution_mode", text="", expand=False)

            # Operators aligned to the right
            sub = row.row(align=True)
            row.scale_x = 1
            sub.alignment = 'RIGHT'
            sub.operator("hotkey_panel.duplicate_shortcut", icon='DUPLICATE', text="").index = i
            sub.operator("hotkey_panel.remove_shortcut", icon='REMOVE', text="").index = i

            # Align properties in the middle using dynamic layout
            split = box.split(factor=0.33)
            row = split.row(align=True)
            row.alignment = 'CENTER'
            row.prop(shortcut, "panel", text="Select Panel")

            row = split.row(align=True)
            row.alignment = 'CENTER'
            row.prop(shortcut, "keymap", text="Key")

            row = split.row(align=True)
            row.alignment = 'CENTER'
            row.prop(shortcut, "event_value", text="Event Value")

            # Styled toggle buttons for "Ctrl", "Shift", "Alt"
            row = box.row(align=True)
            row.alignment = 'CENTER'
            row.prop(shortcut, "ctrl", text="Ctrl", toggle=True)
            row.prop(shortcut, "shift", text="Shift", toggle=True)
            row.prop(shortcut, "alt", text="Alt", toggle=True)


            # Panel management section
            row = box.row()
            row.template_list("PANEL_UL_panel_list", "", shortcut, "panels", shortcut, "active_panel_index", rows=6)
            col_sub = row.column(align=True)
            col_sub.operator("hotkey_panel.add_panel", icon='ADD', text="").index = i
            col_sub.operator("hotkey_panel.remove_panel", icon='REMOVE', text="").index = i
            col_sub.separator()  # Adds space between buttons
            col_sub.operator("hotkey_panel.move_panel_up", icon='TRIA_UP', text="").index = i
            col_sub.operator("hotkey_panel.move_panel_down", icon='TRIA_DOWN', text="").index = i

            # Button to select icon for the panel
            col_sub.separator()
            col_sub.operator("hotkey_panel.select_icon", text="", icon='COLOR').index = i

            # Button to export data
            col_sub.operator("hotkey_panel.export_data", text="", icon='FILE_TICK').index = i

            # Button to import data
            col_sub.operator("hotkey_panel.import_data", text="", icon='FILE_FOLDER').index = i


class HOTKEYPANEL_OT_add_shortcut(Operator):
    bl_idname = "hotkey_panel.add_shortcut"
    bl_label = "Add Hotkey Panel"

    def execute(self, context):
        prefs = context.preferences.addons[__name__].preferences
        shortcut = prefs.shortcuts.add()
        shortcut.internal_name = "HotkeyPanel_" + str(len(prefs.shortcuts))
        update_shortcut(self, context)  # Update keymap
        return {'FINISHED'}


class HOTKEYPANEL_OT_remove_shortcut(Operator):
    bl_idname = "hotkey_panel.remove_shortcut"
    bl_label = "Remove Hotkey Panel Shortcut"
    index: IntProperty()

    def execute(self, context):
        prefs = context.preferences.addons[__name__].preferences
        prefs.shortcuts.remove(self.index)
        update_shortcut(self, context)  # Update keymap
        return {'FINISHED'}


class HOTKEYPANEL_OT_duplicate_shortcut(Operator):
    bl_idname = "hotkey_panel.duplicate_shortcut"
    bl_label = "Duplicate Hotkey Panel Shortcut"
    index: IntProperty()

    def execute(self, context):
        prefs = context.preferences.addons[__name__].preferences
        original_shortcut = prefs.shortcuts[self.index]
        new_shortcut = prefs.shortcuts.add()
        new_shortcut.user_name = original_shortcut.user_name + " (Copy)"
        new_shortcut.internal_name = "HotkeyPanel_" + str(len(prefs.shortcuts))
        new_shortcut.keymap = original_shortcut.keymap
        new_shortcut.event_value = original_shortcut.event_value
        new_shortcut.ctrl = original_shortcut.ctrl
        new_shortcut.shift = original_shortcut.shift
        new_shortcut.alt = original_shortcut.alt
        new_shortcut.is_enabled = original_shortcut.is_enabled
        new_shortcut.execution_mode = original_shortcut.execution_mode
        for panel in original_shortcut.panels:
            panel_item = new_shortcut.panels.add()
            panel_item.name = panel.name
            panel_item.display_name = panel.display_name
            panel_item.icon = panel.icon
            panel_item.f_mp_x_padding = panel.f_mp_x_padding
            panel_item.f_mp_y_padding = panel.f_mp_y_padding
            panel_item.is_active = panel.is_active
        update_shortcut(self, context)  # Update keymap
        return {'FINISHED'}


class HOTKEYPANEL_OT_add_panel(Operator):
    bl_idname = "hotkey_panel.add_panel"
    bl_label = "Add Panel"
    index: IntProperty()

    def execute(self, context):
        prefs = context.preferences.addons[__name__].preferences
        shortcut = prefs.shortcuts[self.index]
        selected_panel = shortcut.panel

        if selected_panel.startswith("HEADER_"):
            # If a header is selected, add all panels in that category
            category = selected_panel.split("HEADER_")[1]
            existing_panel_ids = {panel.name for panel in shortcut.panels}

            for cls in bpy.types.Panel.__subclasses__():
                if hasattr(cls, 'bl_idname') and cls.bl_idname:
                    panel_category = cls.bl_category if hasattr(cls, 'bl_category') else "Uncategorized"
                    if panel_category == category and cls.bl_idname not in existing_panel_ids:
                        panel_item = shortcut.panels.add()
                        panel_item.name = cls.bl_idname
                        panel_item.display_name = cls.bl_label
                        existing_panel_ids.add(cls.bl_idname)  # Prevent duplicates

        else:
            # Add a single panel
            panel_item = shortcut.panels.add()
            panel_item.name = selected_panel
            panel_item.display_name = selected_panel

        return {'FINISHED'}


class HOTKEYPANEL_OT_remove_panel(Operator):
    bl_idname = "hotkey_panel.remove_panel"
    bl_label = "Remove Panel"
    index: IntProperty()

    def execute(self, context):
        prefs = context.preferences.addons[__name__].preferences
        shortcut = prefs.shortcuts[self.index]
        if shortcut.panels:
            shortcut.panels.remove(shortcut.active_panel_index)
        return {'FINISHED'}


class HOTKEYPANEL_OT_move_panel_up(Operator):
    bl_idname = "hotkey_panel.move_panel_up"
    bl_label = "Move Panel Up"
    index: IntProperty()

    def execute(self, context):
        prefs = context.preferences.addons[__name__].preferences
        shortcut = prefs.shortcuts[self.index]
        if shortcut.active_panel_index > 0:
            shortcut.panels.move(shortcut.active_panel_index, shortcut.active_panel_index - 1)
            shortcut.active_panel_index -= 1
        return {'FINISHED'}


class HOTKEYPANEL_OT_move_panel_down(Operator):
    bl_idname = "hotkey_panel.move_panel_down"
    bl_label = "Move Panel Down"
    index: IntProperty()

    def execute(self, context):
        prefs = context.preferences.addons[__name__].preferences
        shortcut = prefs.shortcuts[self.index]
        if shortcut.active_panel_index < len(shortcut.panels) - 1:
            shortcut.panels.move(shortcut.active_panel_index, shortcut.active_panel_index + 1)
            shortcut.active_panel_index += 1
        return {'FINISHED'}


class HOTKEYPANEL_OT_display_panels(Operator):
    bl_idname = "hotkey_panel.display_panels"
    bl_label = "Display Panels"
    shortcut_name: StringProperty()

    def execute(self, context):
        prefs = context.preferences.addons[__name__].preferences

        # Retrieve the shortcut corresponding to the given name
        shortcut = next(
            (s for s in prefs.shortcuts if s.internal_name == self.shortcut_name and s.is_enabled), None)
        if not shortcut:
            self.show_error_popup(context, "No valid Hotkey Panel shortcut found or not enabled.")
            return {'CANCELLED'}

        # Get active panels
        active_panels = [panel for panel in shortcut.panels if panel.is_active]
        if not active_panels:
            message = f"No active panels in the '{shortcut.user_name}'."
            self.show_error_popup(context, message)
            return {'CANCELLED'}

        if shortcut.execution_mode == 'PIE_MENU':
            self.execute_pie_menu(context, shortcut, active_panels)
        elif shortcut.execution_mode == 'POPUP':
            self.execute_popup(context, shortcut, active_panels)
        else:
            # STANDARD
            self.draw_popup(context)

        return {'FINISHED'}

    def execute_pie_menu(self, context, shortcut, active_panels):
        wm = context.window_manager
        wm.hotkey_panel_current_shortcut = shortcut.internal_name
        wm.hotkey_panel_current_page = 0  # Initialize page

        bpy.ops.wm.call_menu_pie(name="HOTKEYPANEL_MT_pie_menu")

    def execute_popup(self, context, shortcut, active_panels):
        # "Pop Up" functionality: Activate panels directly under cursor with padding
        for panel in active_panels:
            if hasattr(bpy.types, panel.name):  # Check if the panel exists
                panel_class = getattr(bpy.types, panel.name)
                area_type = panel_class.bl_space_type
                region_type = panel_class.bl_region_type

                # Find the area and region matching the panel's requirements
                area = next((area for area in context.window.screen.areas if area.type == area_type), None)
                if area:
                    region = next((region for region in area.regions if region.type == region_type), None)
                    if region:
                        # Adjust mouse position by padding
                        adjusted_mouse_x = self.initial_mouse_x + panel.f_mp_x_padding
                        adjusted_mouse_y = self.initial_mouse_y + panel.f_mp_y_padding

                        # Warp cursor to adjusted position
                        context.window.cursor_warp(adjusted_mouse_x, adjusted_mouse_y)

                        # Create an override context
                        override_context = context.copy()
                        override_context.update({
                            'window': context.window,
                            'screen': context.screen,
                            'area': area,
                            'region': region,
                            'region_data': region.data,
                            'scene': context.scene,
                            'active_object': context.active_object,
                            'selected_objects': context.selected_objects,
                            'edit_object': context.edit_object,
                        })

                        # Call the panel operator with the override context
                        try:
                            result = bpy.ops.wm.call_panel(override_context, name=panel.name, keep_open=True)
                            print(f"Called panel '{panel.name}' with result: {result}")
                        except Exception as e:
                            self.report({'ERROR'}, f"Error calling panel '{panel.name}': {e}")
                            print(f"Error calling panel '{panel.name}': {e}")

                        # Restore cursor position
                        context.window.cursor_warp(self.initial_mouse_x, self.initial_mouse_y)
                    else:
                        self.report({'WARNING'}, f"No region '{region_type}' found for panel '{panel.name}'.")
                else:
                    self.report({'WARNING'}, f"No area '{area_type}' found for panel '{panel.name}'.")
            else:
                self.report({'WARNING'}, f"Panel '{panel.name}' not found.")

    def invoke(self, context, event):
        # Store initial mouse position
        self.initial_mouse_x = event.mouse_x
        self.initial_mouse_y = event.mouse_y

        prefs = context.preferences.addons[__name__].preferences

        # Retrieve the shortcut corresponding to the given name
        shortcut = next(
            (s for s in prefs.shortcuts if s.internal_name == self.shortcut_name and s.is_enabled), None)

        if not shortcut:
            self.show_error_popup(context, "No valid Hotkey Panel shortcut found or not enabled.")
            return {'CANCELLED'}

        if shortcut.execution_mode in {'POPUP', 'PIE_MENU'}:
            return self.execute(context)
        else:
            self.draw_popup(context)
            return {'RUNNING_MODAL'}

    def draw_popup(self, context):
        prefs = context.preferences.addons[__name__].preferences
        shortcut = next(
            (s for s in prefs.shortcuts if s.internal_name == self.shortcut_name), None)

        if shortcut:
            active_panels = [panel for panel in shortcut.panels if panel.is_active]
            if not active_panels:
                self.show_error_popup(context, f"No active panels in the '{shortcut.user_name}'.")
                return

            # If there is a user-defined name, display it instead of the default "Select a Panel"
            title = shortcut.user_name if shortcut and shortcut.user_name else "Select a Panel"

            context.window_manager.popup_menu(self.draw_panels, title=title, icon='INFO')

    def draw_panels(self, menu, context):
        prefs = context.preferences.addons[__name__].preferences
        layout = menu.layout
        shortcut = next(
            (s for s in prefs.shortcuts if s.internal_name == self.shortcut_name), None)
        if shortcut:
            active_panels = [panel for panel in shortcut.panels if panel.is_active]
            for panel in active_panels:
                display_name = panel.display_name if panel.display_name else panel.name
                layout.operator("wm.call_panel", text=display_name, icon=panel.icon).name = panel.name

    def show_error_popup(self, context, message):
        """Display an error message in a pop-up menu."""
        def draw(self, context):
            layout = self.layout
            layout.label(text=message, icon='ERROR')

        context.window_manager.popup_menu(draw)


class HOTKEYPANEL_MT_pie_menu(Menu):
    bl_label = "Hotkey Panel Pie Menu"
    bl_idname = "HOTKEYPANEL_MT_pie_menu"

    def draw(self, context):
        layout = self.layout
        pie = layout.menu_pie()

        wm = context.window_manager
        prefs = context.preferences.addons[__name__].preferences

        # Retrieve the shortcut corresponding to the given name
        shortcut_name = wm.hotkey_panel_current_shortcut
        current_page = wm.get('hotkey_panel_current_page', 0)
        shortcut = next(
            (s for s in prefs.shortcuts if s.internal_name == shortcut_name and s.is_enabled), None)

        if shortcut:
            active_panels = [panel for panel in shortcut.panels if panel.is_active]
            total_panels = len(active_panels)
            panels_per_page = 6
            total_pages = (total_panels - 1) // panels_per_page + 1

            # Clamp current_page
            current_page = max(0, min(current_page, total_pages - 1))
            # Update the wm property
            wm.hotkey_panel_current_page = current_page

            # Get panels for current page
            start_index = current_page * panels_per_page
            end_index = start_index + panels_per_page
            page_panels = active_panels[start_index:end_index]

            # Now, build the Pie menu

            # Slot 1
            if len(page_panels) > 0:
                panel = page_panels[0]
                display_name = panel.display_name if panel.display_name else panel.name
                icon = panel.icon if panel.icon else 'NONE'
                pie.operator("hotkey_panel.call_panel", text=display_name, icon=icon).panel_name = panel.name
            else:
                pie.separator()

            # Slot 2
            if len(page_panels) > 1:
                panel = page_panels[1]
                display_name = panel.display_name if panel.display_name else panel.name
                icon = panel.icon if panel.icon else 'NONE'
                pie.operator("hotkey_panel.call_panel", text=display_name, icon=icon).panel_name = panel.name
            else:
                pie.separator()

            # Slot 3
            if len(page_panels) > 2:
                panel = page_panels[2]
                display_name = panel.display_name if panel.display_name else panel.name
                icon = panel.icon if panel.icon else 'NONE'
                pie.operator("hotkey_panel.call_panel", text=display_name, icon=icon).panel_name = panel.name
            else:
                pie.separator()

            # Slot 4
            if len(page_panels) > 3:
                panel = page_panels[3]
                display_name = panel.display_name if panel.display_name else panel.name
                icon = panel.icon if panel.icon else 'NONE'
                pie.operator("hotkey_panel.call_panel", text=display_name, icon=icon).panel_name = panel.name
            else:
                pie.separator()

            # Slot 5
            if len(page_panels) > 4:
                panel = page_panels[4]
                display_name = panel.display_name if panel.display_name else panel.name
                icon = panel.icon if panel.icon else 'NONE'
                pie.operator("hotkey_panel.call_panel", text=display_name, icon=icon).panel_name = panel.name
            else:
                pie.separator()

            # Slot 6
            if len(page_panels) > 5:
                panel = page_panels[5]
                display_name = panel.display_name if panel.display_name else panel.name
                icon = panel.icon if panel.icon else 'NONE'
                pie.operator("hotkey_panel.call_panel", text=display_name, icon=icon).panel_name = panel.name
            else:
                pie.separator()

            # Slot 7 - Previous
            if total_pages > 1 and current_page > 0:
                pie.operator("hotkey_panel.pie_menu_previous_page", text="Previous Page", icon='TRIA_LEFT')
            else:
                pie.separator()

            # Slot 8 - Next
            if total_pages > 1 and current_page < total_pages - 1:
                pie.operator("hotkey_panel.pie_menu_next_page", text="Next Page", icon='TRIA_RIGHT')
            else:
                pie.separator()


class HOTKEYPANEL_OT_pie_menu_next_page(Operator):
    bl_idname = "hotkey_panel.pie_menu_next_page"
    bl_label = "Next Page"

    def execute(self, context):
        wm = context.window_manager
        current_page = wm.get('hotkey_panel_current_page', 0)
        wm.hotkey_panel_current_page = current_page + 1
        # Re-open the Pie menu
        bpy.ops.wm.call_menu_pie(name="HOTKEYPANEL_MT_pie_menu")
        return {'FINISHED'}


class HOTKEYPANEL_OT_pie_menu_previous_page(Operator):
    bl_idname = "hotkey_panel.pie_menu_previous_page"
    bl_label = "Previous Page"

    def execute(self, context):
        wm = context.window_manager
        current_page = wm.get('hotkey_panel_current_page', 0)
        wm.hotkey_panel_current_page = current_page - 1
        # Re-open the Pie menu
        bpy.ops.wm.call_menu_pie(name="HOTKEYPANEL_MT_pie_menu")
        return {'FINISHED'}


class HOTKEYPANEL_OT_call_panel(Operator):
    bl_idname = "hotkey_panel.call_panel"
    bl_label = "Call Panel"

    panel_name: StringProperty()

    def execute(self, context):
        panel_name = self.panel_name
        panel_class = getattr(bpy.types, panel_name, None)
        if panel_class:
            area_type = panel_class.bl_space_type
            region_type = panel_class.bl_region_type

            # Find the area and region matching the panel's requirements
            area = next((area for area in context.window.screen.areas if area.type == area_type), None)
            if area:
                region = next((region for region in area.regions if region.type == region_type), None)
                if region:
                    # Create an override context
                    override_context = context.copy()
                    override_context.update({
                        'window': context.window,
                        'screen': context.screen,
                        'area': area,
                        'region': region,
                        'region_data': region.data,
                        'scene': context.scene,
                        'active_object': context.active_object,
                        'selected_objects': context.selected_objects,
                        'edit_object': context.edit_object,
                    })

                    # Call the panel operator with the override context
                    try:
                        result = bpy.ops.wm.call_panel(override_context, name=panel_name, keep_open=True)
                        print(f"Called panel '{panel_name}' with result: {result}")
                    except Exception as e:
                        self.report({'ERROR'}, f"Error calling panel '{panel_name}': {e}")
                        print(f"Error calling panel '{panel_name}': {e}")

                else:
                    self.report({'WARNING'}, f"No region '{region_type}' found for panel '{panel_name}'.")
            else:
                self.report({'WARNING'}, f"No area '{area_type}' found for panel '{panel_name}'.")
        else:
            self.report({'WARNING'}, f"Panel '{panel_name}' not found.")

        return {'FINISHED'}


class HOTKEYPANEL_OT_select_icon(Operator):
    bl_idname = "hotkey_panel.select_icon"
    bl_label = "Select Icon"
    index: IntProperty()

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_popup(self)

    def draw(self, context):
        layout = self.layout
        layout.label(text="Choose an Icon:")
        icons = bpy.types.UILayout.bl_rna.functions["prop"].parameters["icon"].enum_items
        for i, icon in enumerate(icons):
            if i % 10 == 0:
                row = layout.row()
            row.operator("hotkey_panel.icon_select_action", text="", icon=icon.identifier).icon_name = icon.identifier

    def execute(self, context):
        return {'FINISHED'}


class HOTKEYPANEL_OT_icon_select_action(Operator):
    bl_idname = "hotkey_panel.icon_select_action"
    bl_label = "Icon Select Action"
    icon_name: StringProperty()

    def execute(self, context):
        wm = context.window_manager
        prefs = context.preferences.addons[__name__].preferences
        shortcut = prefs.shortcuts[prefs.active_shortcut_index]
        panel = shortcut.panels[shortcut.active_panel_index]
        panel.icon = self.icon_name
        return {'FINISHED'}


class HOTKEYPANEL_OT_export_data(Operator):
    bl_idname = "hotkey_panel.export_data"
    bl_label = "Export Hotkey Panel Data"
    index: IntProperty()

    def execute(self, context):
        prefs = context.preferences.addons[__name__].preferences
        shortcut = prefs.shortcuts[self.index]

        # Collect data from Hotkey Panel
        shortcut_data = f"Hotkey Panel Name: {shortcut.user_name}\n"
        shortcut_data += f"Internal Name: {shortcut.internal_name}\n"
        shortcut_data += f"Keymap: {shortcut.keymap}\n"
        shortcut_data += f"Event Value: {shortcut.event_value}\n"
        shortcut_data += f"Ctrl: {shortcut.ctrl}\n"
        shortcut_data += f"Shift: {shortcut.shift}\n"
        shortcut_data += f"Alt: {shortcut.alt}\n"
        shortcut_data += f"Is Enabled: {shortcut.is_enabled}\n"
        shortcut_data += f"Execution Mode: {shortcut.execution_mode}\n"
        shortcut_data += f"Search Filter: {shortcut.search_filter}\n"
        shortcut_data += f"Selected Panel: {shortcut.panel}\n"

        # Export panels information
        shortcut_data += "Panels:\n"
        for panel in shortcut.panels:
            shortcut_data += f"  - Name: {panel.name}\n"
            shortcut_data += f"    Display Name: {panel.display_name}\n"
            shortcut_data += f"    Icon: {panel.icon}\n"
            shortcut_data += f"    X Padding: {panel.f_mp_x_padding}\n"
            shortcut_data += f"    Y Padding: {panel.f_mp_y_padding}\n"
            shortcut_data += f"    Active: {panel.is_active}\n"  # Include active state

        # Copy the data to clipboard
        context.window_manager.clipboard = shortcut_data

        self.report({'INFO'}, "Hotkey Panel data copied to clipboard.")
        return {'FINISHED'}


class HOTKEYPANEL_OT_import_data(Operator):
    bl_idname = "hotkey_panel.import_data"
    bl_label = "Import Hotkey Panel Data"
    index: IntProperty()

    def execute(self, context):
        prefs = context.preferences.addons[__name__].preferences
        shortcut = prefs.shortcuts[self.index]

        # Get data from the clipboard
        import_text = context.window_manager.clipboard
        lines = import_text.split('\n')

        # Clear existing panels
        shortcut.panels.clear()

        # Process each line and update the properties of the Hotkey Panel
        current_panel = None
        for line in lines:
            if line.startswith("Hotkey Panel Name:"):
                shortcut.user_name = line.split(":", 1)[1].strip()
            elif line.startswith("Internal Name:"):
                shortcut.internal_name = line.split(":", 1)[1].strip()
            elif line.startswith("Keymap:"):
                shortcut.keymap = line.split(":", 1)[1].strip()
            elif line.startswith("Event Value:"):
                shortcut.event_value = line.split(":", 1)[1].strip()
            elif line.startswith("Ctrl:"):
                shortcut.ctrl = line.split(":", 1)[1].strip() == 'True'
            elif line.startswith("Shift:"):
                shortcut.shift = line.split(":", 1)[1].strip() == 'True'
            elif line.startswith("Alt:"):
                shortcut.alt = line.split(":", 1)[1].strip() == 'True'
            elif line.startswith("Is Enabled:"):
                shortcut.is_enabled = line.split(":", 1)[1].strip() == 'True'
            elif line.startswith("Execution Mode:"):
                shortcut.execution_mode = line.split(":", 1)[1].strip()
            elif line.startswith("Search Filter:"):
                shortcut.search_filter = line.split(":", 1)[1].strip()
            elif line.startswith("Selected Panel:"):
                shortcut.panel = line.split(":", 1)[1].strip()
            elif line.startswith("  - Name:"):
                current_panel = shortcut.panels.add()
                current_panel.name = line.split(":", 1)[1].strip()
            elif line.startswith("    Display Name:") and current_panel:
                current_panel.display_name = line.split(":", 1)[1].strip()
            elif line.startswith("    Icon:") and current_panel:
                current_panel.icon = line.split(":", 1)[1].strip()
            elif line.startswith("    X Padding:") and current_panel:
                current_panel.f_mp_x_padding = int(line.split(":", 1)[1].strip())
            elif line.startswith("    Y Padding:") and current_panel:
                current_panel.f_mp_y_padding = int(line.split(":", 1)[1].strip())
            elif line.startswith("    Active:") and current_panel:
                current_panel.is_active = line.split(":", 1)[1].strip() == 'True'  # Import active state

        self.report({'INFO'}, "Hotkey Panel data imported from clipboard.")
        return {'FINISHED'}


addon_keymaps = []


def register_keymaps():
    prefs = bpy.context.preferences.addons[__name__].preferences
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon

    unregister_keymaps()

    if kc:
        for shortcut in prefs.shortcuts:
            if shortcut.is_enabled and shortcut.keymap and shortcut.keymap != 'NONE':
                km = kc.keymaps.new(name='3D View', space_type='VIEW_3D')
                kmi = km.keymap_items.new(
                    idname='hotkey_panel.display_panels',
                    type=shortcut.keymap,
                    value=shortcut.event_value,
                    ctrl=shortcut.ctrl,
                    shift=shortcut.shift,
                    alt=shortcut.alt
                )
                kmi.properties.shortcut_name = shortcut.internal_name
                addon_keymaps.append((km, kmi))


def unregister_keymaps():
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


def update_shortcut(self, context):
    unregister_keymaps()
    register_keymaps()


def register():
    bpy.utils.register_class(PanelItem)
    bpy.utils.register_class(HotkeyPanelShortcut)
    bpy.utils.register_class(HotkeyPanelPreferences)
    bpy.utils.register_class(HOTKEYPANEL_OT_add_shortcut)
    bpy.utils.register_class(HOTKEYPANEL_OT_remove_shortcut)
    bpy.utils.register_class(HOTKEYPANEL_OT_duplicate_shortcut)
    bpy.utils.register_class(HOTKEYPANEL_OT_add_panel)
    bpy.utils.register_class(HOTKEYPANEL_OT_remove_panel)
    bpy.utils.register_class(HOTKEYPANEL_OT_move_panel_up)
    bpy.utils.register_class(HOTKEYPANEL_OT_move_panel_down)
    bpy.utils.register_class(HOTKEYPANEL_OT_display_panels)
    bpy.utils.register_class(PANEL_UL_panel_list)
    bpy.utils.register_class(HOTKEYPANEL_OT_select_icon)
    bpy.utils.register_class(HOTKEYPANEL_OT_icon_select_action)
    bpy.utils.register_class(HOTKEYPANEL_OT_export_data)
    bpy.utils.register_class(HOTKEYPANEL_OT_import_data)
    bpy.utils.register_class(HOTKEYPANEL_MT_pie_menu)  # Register the pie menu
    bpy.utils.register_class(HOTKEYPANEL_OT_call_panel)  # Register the call panel operator
    bpy.utils.register_class(HOTKEYPANEL_OT_pie_menu_next_page)  # Register Next Page operator
    bpy.utils.register_class(HOTKEYPANEL_OT_pie_menu_previous_page)  # Register Previous Page operator

    bpy.types.WindowManager.hotkey_panel_shortcuts = PointerProperty(type=HotkeyPanelShortcut)
    bpy.types.WindowManager.hotkey_panel_current_shortcut = StringProperty()
    bpy.types.WindowManager.hotkey_panel_current_page = IntProperty()

    register_keymaps()


def unregister():
    unregister_keymaps()
    bpy.utils.unregister_class(PanelItem)
    bpy.utils.unregister_class(HotkeyPanelShortcut)
    bpy.utils.unregister_class(HotkeyPanelPreferences)
    bpy.utils.unregister_class(HOTKEYPANEL_OT_add_shortcut)
    bpy.utils.unregister_class(HOTKEYPANEL_OT_remove_shortcut)
    bpy.utils.unregister_class(HOTKEYPANEL_OT_duplicate_shortcut)
    bpy.utils.unregister_class(HOTKEYPANEL_OT_add_panel)
    bpy.utils.unregister_class(HOTKEYPANEL_OT_remove_panel)
    bpy.utils.unregister_class(HOTKEYPANEL_OT_move_panel_up)
    bpy.utils.unregister_class(HOTKEYPANEL_OT_move_panel_down)
    bpy.utils.unregister_class(HOTKEYPANEL_OT_display_panels)
    bpy.utils.unregister_class(PANEL_UL_panel_list)
    bpy.utils.unregister_class(HOTKEYPANEL_OT_select_icon)
    bpy.utils.unregister_class(HOTKEYPANEL_OT_icon_select_action)
    bpy.utils.unregister_class(HOTKEYPANEL_OT_export_data)
    bpy.utils.unregister_class(HOTKEYPANEL_OT_import_data)
    bpy.utils.unregister_class(HOTKEYPANEL_MT_pie_menu)
    bpy.utils.unregister_class(HOTKEYPANEL_OT_call_panel)
    bpy.utils.unregister_class(HOTKEYPANEL_OT_pie_menu_next_page)
    bpy.utils.unregister_class(HOTKEYPANEL_OT_pie_menu_previous_page)

    del bpy.types.WindowManager.hotkey_panel_shortcuts
    del bpy.types.WindowManager.hotkey_panel_current_shortcut
    del bpy.types.WindowManager.hotkey_panel_current_page


if __name__ == "__main__":
    register()

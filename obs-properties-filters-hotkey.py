import obspython as obs

def script_description():
    return """Add hotkeys to open source properties and filters."""


class Hotkey:
    def __init__(self, callback, obs_settings, _id):
        self.obs_data = obs_settings
        self.hotkey_id = obs.OBS_INVALID_HOTKEY_ID
        self.hotkey_saved_key = None
        self.callback = callback
        self._id = _id

        self.load_hotkey()
        self.register_hotkey()
        self.save_hotkey()

    def register_hotkey(self):
        description = str(self._id)
        self.hotkey_id = obs.obs_hotkey_register_frontend(
            "htk_id" + str(self._id), description, self.callback
        )
        obs.obs_hotkey_load(self.hotkey_id, self.hotkey_saved_key)

    def load_hotkey(self):
        self.hotkey_saved_key = obs.obs_data_get_array(
            self.obs_data, "htk_id" + str(self._id)
        )
        obs.obs_data_array_release(self.hotkey_saved_key)

    def save_hotkey(self):
        self.hotkey_saved_key = obs.obs_hotkey_save(self.hotkey_id)
        obs.obs_data_set_array(
            self.obs_data, "htk_id" + str(self._id), self.hotkey_saved_key
        )
        obs.obs_data_array_release(self.hotkey_saved_key)


class h:
    htk_copy = None  # this attribute will hold instance of Hotkey

hk_properties = h()
hk_filters = h()


def script_properties():
    properties = obs.obs_properties_create()
    p = []
    return properties


def script_load(settings):
    hk_properties.htk_copy = Hotkey(open_properties, settings, "Open source properties")
    hk_filters.htk_copy = Hotkey(open_filters, settings, "Open source filters")
    print("hotkey helper loaded")

def script_update(settings):
    print("hotkey helper updated")

def script_unload():
    obs.obs_hotkey_unregister(source_setter)
    print("hotkey helper unloaded")

def script_save(settings):
    hk_properties.htk_copy.save_hotkey()
    hk_filters.htk_copy.save_hotkey()


def open_properties(pressed):
    if(pressed):
        source_setter("properties")

def open_filters(pressed):
    if(pressed):
        source_setter("filters")



def source_setter(test):
    studio_mode = obs.obs_frontend_preview_program_mode_active()
    current_scene = ''
    if not studio_mode:
        current_scene = obs.obs_frontend_get_current_scene()
    else:
        current_scene = obs.obs_frontend_get_current_preview_scene()
    scene_source = obs.obs_scene_from_source(current_scene)
    scene_items = obs.obs_scene_enum_items(scene_source)
    for item in scene_items:
        select_getter = obs.obs_sceneitem_selected(item)
        if select_getter:
            if test == "properties":
                source = obs.obs_sceneitem_get_source(item)
                obs.obs_frontend_open_source_properties(source)
            elif test == "filters":
                source = obs.obs_sceneitem_get_source(item)
                obs.obs_frontend_open_source_filters(source)

    obs.sceneitem_list_release(scene_items)
    obs.obs_source_release(current_scene)

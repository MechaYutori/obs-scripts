import obspython as obs

def script_description():
    return """Set selected font to new text source automatically."""

selected_font = ''

def script_properties():
    properties = obs.obs_properties_create()
    obs.obs_properties_add_font(properties, "_font", "Select font")
    return properties

def script_update(settings):
    global selected_font
    selected_font = obs.obs_data_get_obj(settings, "_font")
    print("font setter updated")

def script_load(settings):
    global selected_font
    selected_font = obs.obs_data_get_obj(settings, "_font")
    handler = obs.obs_get_signal_handler()
    obs.signal_handler_connect(handler, "source_create", font_setter)
    print("font setter loaded")

def script_unload():
    print("font setter unloaded")

def font_setter(trigger):
    global selected_font
    source = obs.calldata_source(trigger, "source")
    current_scene = obs.obs_frontend_get_current_scene()
    source_name = obs.obs_source_get_name(source)
    scene_name = obs.obs_source_get_name(current_scene)
    if (obs.obs_source_get_id(source) == "text_gdiplus_v2"):
        if scene_name != None:
            settings = obs.obs_data_create()
            obs.obs_data_set_obj(settings, "font", selected_font)
            obs.obs_source_update(source, settings)
            obs.obs_data_release(settings)
            print(f"font set! {source_name}")

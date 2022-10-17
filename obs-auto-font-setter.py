import obspython as obs

def script_description():
    return """Set selected font to new text source automaticaly."""

source_identifier = 'uninitialized'
selected_font = ''

def script_properties():
    properties = obs.obs_properties_create()
    obs.obs_properties_add_font(properties, "_font", "Select font")
    return properties

def script_update(settings):
    global selected_font
    obs.timer_remove(font_setter)
    selected_font = obs.obs_data_get_obj(settings, "_font")
    obs.timer_add(font_setter, 1000)
    print("font setter updated")

def script_load(settings):
    global selected_font
    selected_font = obs.obs_data_get_obj(settings, "_font")
    print("font setter loaded")

def script_unload():
    obs.timer_remove(font_setter)
    print("font setter unloaded")

def font_setter():
    global selected_font
    global source_identifier
    source_ids = []
    sources = obs.obs_enum_sources()
    
    if source_identifier == 'uninitialized':
        for source in sources:
            if (obs.obs_source_get_id(source) == "text_gdiplus_v2"):
                id = obs.obs_source_get_name(source)
                source_ids.append(id)
                print("it has " + id)
    else:
        for source in sources:
            if (obs.obs_source_get_id(source) == "text_gdiplus_v2"):
                id = obs.obs_source_get_name(source)
                source_ids.append(id)
                if not(id in source_identifier):
                    settings = obs.obs_data_create()
                    obs.obs_data_set_obj(settings, "font", selected_font)
                    obs.obs_source_update(source, settings)
                    obs.obs_data_release(settings)
                    print("font set!")


    source_identifier = source_ids
    obs.source_list_release(sources)

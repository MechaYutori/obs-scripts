import obspython as obs

def script_description():
    return """Set selected scale filter to new source automatically"""

initialized = False
item_identifier = []
set_scale = ''
old_scene = ''

def script_properties():
    properties = obs.obs_properties_create()
    list = obs.obs_properties_add_list(properties, "_scale", "Scaling Filter", obs.OBS_COMBO_TYPE_LIST , obs.OBS_COMBO_FORMAT_INT)
    obs.obs_property_list_add_int(list, "Disable", obs.OBS_SCALE_DISABLE)
    obs.obs_property_list_add_int(list, "Point", obs.OBS_SCALE_POINT)
    obs.obs_property_list_add_int(list, "Bilinear", obs.OBS_SCALE_BILINEAR)
    obs.obs_property_list_add_int(list, "Bicubic", obs.OBS_SCALE_BICUBIC)
    obs.obs_property_list_add_int(list, "Lanczos", obs.OBS_SCALE_LANCZOS)
    obs.obs_property_list_add_int(list, "Area", obs.OBS_SCALE_AREA)
    return properties

def script_update(settings):
    global set_scale
    obs.timer_remove(scale_setter)
    set_scale = obs.obs_data_get_int(settings, "_scale")
    obs.timer_add(scale_setter, 1000)
    print("auto scale filter updated")

def script_load(settings):
    global set_scale
    set_scale = obs.obs_data_get_int(settings, "_scale")
    print("auto scale filter loaded")

def script_unload():
    obs.timer_remove(scale_setter)
    print("auto scale filter unloaded")

def scale_setter():
    global set_scale
    global item_identifier
    global old_scene
    global initialized

    studio_mode = obs.obs_frontend_preview_program_mode_active()
    current_scene = ''

    if not studio_mode:
        current_scene = obs.obs_frontend_get_current_scene()
    else:
        current_scene = obs.obs_frontend_get_current_preview_scene()
        
    scene_source = obs.obs_scene_from_source(current_scene)
    scene_items = obs.obs_scene_enum_items(scene_source)
    scene_name = obs.obs_source_get_name(current_scene)
    item_ids = []
    
    if initialized == False or scene_name != old_scene:
        for item in scene_items:
            id = obs.obs_sceneitem_get_id(item)
            item_ids.append(id)
            initialized = True
    else:
        for item in scene_items:
            id = obs.obs_sceneitem_get_id(item)
            if not(id in item_identifier):
                obs.obs_sceneitem_set_scale_filter(item, set_scale)
                print("scale filter set!")
            item_ids.append(id)

    item_identifier = item_ids
    old_scene = scene_name
    obs.sceneitem_list_release(scene_items)
    obs.obs_source_release(current_scene)

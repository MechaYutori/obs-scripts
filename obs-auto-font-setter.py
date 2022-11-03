import obspython as obs

def script_description():
    return """Set selected font to new text source automatically."""

selected_font = ''
selected_color = ''
opacity = 100
outline = [0] * 4
gradient = [0] * 4
background = [0] * 2

def background_settings(props, prop, settings):
    background = obs.obs_data_get_bool(settings, "_bk")

    bk_color = obs.obs_data_get_int(settings, "_bk_color")
    color_property = obs.obs_properties_get(props, "_bk_color")

    bk_opacity = obs.obs_data_get_int(settings, "_bk_opacity")
    opacity_property = obs.obs_properties_get(props, "_bk_opacity")

    if background:
        obs.obs_property_set_visible(color_property, True)
        obs.obs_property_set_visible(opacity_property, True)
        return True
    else:
        obs.obs_property_set_visible(color_property, False)
        obs.obs_property_set_visible(opacity_property, False)
        return True

def gradient_settings(props, prop, settings):
    gradient = obs.obs_data_get_bool(settings, "_gradient")

    gradient_color = obs.obs_data_get_int(settings, "_gradient_color")
    color_property = obs.obs_properties_get(props, "_gradient_color")

    gradient_opacity = obs.obs_data_get_int(settings, "_gradient_opacity")
    opacity_property = obs.obs_properties_get(props, "_gradient_opacity")

    gradient_direction = obs.obs_data_get_int(settings, "_gradient_direction")
    direction_property = obs.obs_properties_get(props, "_gradient_direction")
    if gradient:
        obs.obs_property_set_visible(color_property, True)
        obs.obs_property_set_visible(opacity_property, True)
        obs.obs_property_set_visible(direction_property, True)
        return True
    else:
        obs.obs_property_set_visible(color_property, False)
        obs.obs_property_set_visible(opacity_property, False)
        obs.obs_property_set_visible(direction_property, False)
        return True

def outline_settings(props, prop, settings):
    outline = obs.obs_data_get_bool(settings, "_outline")

    outline_size = obs.obs_data_get_int(settings, "_outline_size")
    size_property = obs.obs_properties_get(props, "_outline_size")

    outline_color = obs.obs_data_get_int(settings, "_outline_color")
    color_property = obs.obs_properties_get(props, "_outline_color")

    outline_opacity = obs.obs_data_get_int(settings, "_outline_opacity")
    opacity_property = obs.obs_properties_get(props, "_outline_opacity")
    if outline:
        obs.obs_property_set_visible(size_property, True)
        obs.obs_property_set_visible(color_property, True)
        obs.obs_property_set_visible(opacity_property, True)
        return True
    else:
        obs.obs_property_set_visible(size_property, False)
        obs.obs_property_set_visible(color_property, False)
        obs.obs_property_set_visible(opacity_property, False)
        return True

def script_properties():
    props = obs.obs_properties_create()
    p = []

    obs.obs_properties_add_font(props, "_font", "Select font")

    obs.obs_properties_add_color(props, "_color", "Text Color")
    color = obs.obs_properties_add_int_slider(props, "_opacity", "Opacity", 0, 100, 1)
    obs.obs_property_int_set_suffix(color, "%")
    
    outline = obs.obs_properties_add_bool(props, "_outline", "Outline")
    p.append(obs.obs_properties_add_int(props, "_outline_size", "Outline Size", 1, 20, 1))
    p.append(obs.obs_properties_add_color(props, "_outline_color", "Outline Color"))
    p.append(obs.obs_properties_add_int_slider(props, "_outline_opacity", "Outline Opacity", 0, 100, 1))

    gradient = obs.obs_properties_add_bool(props, "_gradient", "Gradient")
    p.append(obs.obs_properties_add_color(props, "_gradient_color", "Gradient Color"))
    p.append(obs.obs_properties_add_int_slider(props, "_gradient_opacity", "Gradient Opacity", 0, 100, 1))
    p.append(obs.obs_properties_add_float_slider(props, "_gradient_direction", "Gradient Direction", 0, 360, 0.1))

    background = obs.obs_properties_add_bool(props, "_bk", "Background")
    p.append(obs.obs_properties_add_color(props, "_bk_color", "Bakcground Color"))
    p.append(obs.obs_properties_add_int_slider(props, "_bk_opacity", "Background Opacity", 0, 100, 1))

    for i in p:
        obs.obs_property_set_visible(i, False)
    
    obs.obs_property_set_modified_callback(gradient, gradient_settings)
    obs.obs_property_set_modified_callback(outline, outline_settings)
    obs.obs_property_set_modified_callback(background, background_settings)

    return props

def script_defaults(settings):
	obs.obs_data_set_default_int(settings, "_color", 0xFFFFFF)
	obs.obs_data_set_default_int(settings, "_outline_color", 0xFFFFFF)
	obs.obs_data_set_default_int(settings, "_gradient_color", 0xFFFFFF)
	obs.obs_data_set_default_int(settings, "_bk_color", 0x000000)
	obs.obs_data_set_default_int(settings, "_opacity", 100)
	obs.obs_data_set_default_int(settings, "_outline_opacity", 100)
	obs.obs_data_set_default_int(settings, "_gradient_opacity", 100)
	obs.obs_data_set_default_int(settings, "_bk_opacity", 0)
	obs.obs_data_set_default_int(settings, "_outline_size", 2)
	obs.obs_data_set_default_double(settings, "_gradient_direction", 90)


def script_update(settings):
    global selected_font
    global selected_color
    global opacity
    global outline
    global gradient
    global background
    selected_font = obs.obs_data_get_obj(settings, "_font")
    selected_color = obs.obs_data_get_int(settings, "_color")
    opacity = obs.obs_data_get_int(settings, "_opacity")
    outline[0] = obs.obs_data_get_bool(settings, "_outline")
    outline[1] = obs.obs_data_get_int(settings, "_outline_size")
    outline[2] = obs.obs_data_get_int(settings, "_outline_color")
    outline[3] = obs.obs_data_get_int(settings, "_outline_opacity")
    gradient[0] = obs.obs_data_get_bool(settings, "_gradient")
    gradient[1] = obs.obs_data_get_int(settings, "_gradient_color")
    gradient[2] = obs.obs_data_get_int(settings, "_gradient_opacity")
    gradient[3] = obs.obs_data_get_double(settings, "_gradient_direction")
    background[0] = obs.obs_data_get_int(settings, "_bk_color")
    background[1] = obs.obs_data_get_int(settings, "_bk_opacity")
    print("font setter updated")

def script_load(settings):
    global selected_font
    global selected_color
    global opacity
    global outline
    global gradient
    global background
    selected_font = obs.obs_data_get_obj(settings, "_font")
    selected_color = obs.obs_data_get_int(settings, "_color")
    opacity = obs.obs_data_get_int(settings, "_opacity")
    outline[0] = obs.obs_data_get_bool(settings, "_outline")
    outline[1] = obs.obs_data_get_int(settings, "_outline_size")
    outline[2] = obs.obs_data_get_int(settings, "_outline_color")
    outline[3] = obs.obs_data_get_int(settings, "_outline_opacity")
    gradient[0] = obs.obs_data_get_bool(settings, "_gradient")
    gradient[1] = obs.obs_data_get_int(settings, "_gradient_color")
    gradient[2] = obs.obs_data_get_int(settings, "_gradient_opacity")
    gradient[3] = obs.obs_data_get_double(settings, "_gradient_direction")
    background[0] = obs.obs_data_get_int(settings, "_bk_color")
    background[1] = obs.obs_data_get_int(settings, "_bk_opacity")
    handler = obs.obs_get_signal_handler()
    obs.signal_handler_connect(handler, "source_create", font_setter)
    print("font setter loaded")

def script_unload():
    print("font setter unloaded")

def font_setter(trigger):
    global selected_font
    global selected_color
    global opacity
    global outline
    global gradient
    global background
    source = obs.calldata_source(trigger, "source")

    if (obs.obs_source_get_id(source) == "text_gdiplus_v2"):
        current_scene = obs.obs_frontend_get_current_scene()
        source_name = obs.obs_source_get_name(source)
        scene_name = obs.obs_source_get_name(current_scene)

        if scene_name != None:
            settings = obs.obs_data_create()
            obs.obs_data_set_obj(settings, "font", selected_font)
            obs.obs_data_set_int(settings, "color", selected_color)
            obs.obs_data_set_int(settings, "opacity", opacity)
            obs.obs_data_set_bool(settings, "outline", outline[0])
            obs.obs_data_set_int(settings, "outline_size", outline[1])
            obs.obs_data_set_int(settings, "outline_color", outline[2])
            obs.obs_data_set_int(settings, "outline_opacity", outline[3])
            obs.obs_data_set_bool(settings, "gradient", gradient[0])
            obs.obs_data_set_int(settings, "gradient_color", gradient[1])
            obs.obs_data_set_int(settings, "gradient_opacity", gradient[2])
            obs.obs_data_set_double(settings, "gradient_dir", gradient[3])
            obs.obs_data_set_int(settings, "bk_color", background[0])
            obs.obs_data_set_int(settings, "bk_opacity", background[1])
            obs.obs_source_update(source, settings)
            obs.obs_data_release(settings)
            print(f"font set! {source_name}")

        obs.obs_source_release(current_scene)

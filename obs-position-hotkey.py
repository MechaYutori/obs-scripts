import obspython as obs


def script_description():
    return """Add hotkeys to apply the set source position."""


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


def hotkey1(pressed):
    if (pressed):
        source_setter("hotkey1")

def hotkey2(pressed):
    if (pressed):
        source_setter("hotkey2")

def hotkey3(pressed):
    if (pressed):
        source_setter("hotkey3")

def hotkey4(pressed):
    if (pressed):
        source_setter("hotkey4")

def hotkey5(pressed):
    if (pressed):
        source_setter("hotkey5")


hotkey = [0] * 5
counter = 0
posX = [0] * 5
posY = [0] * 5
sizeX = [0] * 5
sizeY = [0] * 5
bound_type = [0] * 5
bound_align = [0] * 5
key_count = 1
hotkey_callback = [hotkey1, hotkey2, hotkey3, hotkey4, hotkey5]


def script_properties():
    global key_count
    properties = obs.obs_properties_create()
    p = []
    list = [0] * 5
    bound_align = [0] * 5
    key_num = obs.obs_properties_add_int(properties, "_keycount", "Hotkey count", 1, 5, 1)
    for i in range(5):
        pp = []
        pp.append(obs.obs_properties_add_text(properties, "_{0}_no_reason_to_have_it".format(str(i)), "Settings for hotkey {0}".format(str(i+1)), obs.OBS_TEXT_INFO))
        pp.append(obs.obs_properties_add_float(properties, "_{0}_x_position".format(str(i)), "X position", 0, 10000, 1))
        pp.append(obs.obs_properties_add_float(properties, "_{0}_y_position".format(str(i)), "Y position", 0, 10000, 1))
        pp.append(obs.obs_properties_add_float(properties, "_{0}_x_size".format(str(i)), "X size", 0, 10000, 1))
        pp.append(obs.obs_properties_add_float(properties, "_{0}_y_size".format(str(i)), "Y size", 0, 10000, 1))
        list[i] = obs.obs_properties_add_list(properties, "_{0}_bound_type".format(str(i)), "Bounding box type", obs.OBS_COMBO_TYPE_LIST , obs.OBS_COMBO_FORMAT_INT)
        obs.obs_property_list_add_int(list[i], "Streach to bounds", obs.OBS_BOUNDS_STRETCH)
        obs.obs_property_list_add_int(list[i], "Scale to inner bounds", obs.OBS_BOUNDS_SCALE_INNER)
        obs.obs_property_list_add_int(list[i], "_Scale to outer bounds", obs.OBS_BOUNDS_SCALE_OUTER)
        obs.obs_property_list_add_int(list[i], "Scale to width of bounds", obs.OBS_BOUNDS_SCALE_TO_WIDTH)
        obs.obs_property_list_add_int(list[i], "Scale to height of bounds", obs.OBS_BOUNDS_SCALE_TO_HEIGHT)
        obs.obs_property_list_add_int(list[i], "Maximum size only", obs.OBS_BOUNDS_MAX_ONLY)
        bound_align[i] = obs.obs_properties_add_list(properties, "_{0}_bound_align".format(str(i)), "Bounding box align", obs.OBS_COMBO_TYPE_LIST , obs.OBS_COMBO_FORMAT_INT)
        obs.obs_property_list_add_int(bound_align[i], "Top Left", 0b0101)
        obs.obs_property_list_add_int(bound_align[i], "Top Center", 0b0100)
        obs.obs_property_list_add_int(bound_align[i], "Top Right", 0b0110)
        obs.obs_property_list_add_int(bound_align[i], "Center Left", 0b0001)
        obs.obs_property_list_add_int(bound_align[i], "Center", 0b0000)
        obs.obs_property_list_add_int(bound_align[i], "Center Right", 0b0010)
        obs.obs_property_list_add_int(bound_align[i], "Bottom Left", 0b1001)
        obs.obs_property_list_add_int(bound_align[i], "Bottom Center", 0b1000)
        obs.obs_property_list_add_int(bound_align[i], "Bottom Right", 0b1010)
        pp.append(obs.obs_properties_add_text(properties, "_{0}_no_reason_to_have_it_end".format(str(i)), " ", obs.OBS_TEXT_INFO))
        p.append(pp)
    count = 0
    for i in p:
        if count >= key_count:
            for j in i:
                obs.obs_property_set_visible(j, False)
                obs.obs_property_set_visible(list[count], False)
                obs.obs_property_set_visible(bound_align[count], False)
        count += 1
    obs.obs_property_set_modified_callback(key_num, hotkey_settings)

    return properties


def hotkey_settings(props, prop, settings):
    hotkey_num = obs.obs_data_get_int(settings, "_keycount")
    p = [[0] * 8 for i in range(5)]
    for i in range(5):
        label1 = obs.obs_data_get_string(settings, "_{0}_no_reason_to_have_it".format(str(i)))
        p[i][0] = obs.obs_properties_get(props, "_{0}_no_reason_to_have_it".format(str(i)))
        x_pos = obs.obs_data_get_double(settings, "_{0}_x_position".format(str(i)))
        p[i][1] = obs.obs_properties_get(props, "_{0}_x_position".format(str(i)))
        y_pos = obs.obs_data_get_double(settings, "_{0}_y_position".format(str(i)))
        p[i][2] = obs.obs_properties_get(props, "_{0}_y_position".format(str(i)))
        x_size = obs.obs_data_get_double(settings, "_{0}_x_size".format(str(i)))
        p[i][3] = obs.obs_properties_get(props, "_{0}_x_size".format(str(i)))
        y_size = obs.obs_data_get_double(settings, "_{0}_y_size".format(str(i)))
        p[i][4] = obs.obs_properties_get(props, "_{0}_y_size".format(str(i)))
        bounds_type = obs.obs_data_get_int(settings, "_{0}_bound_type".format(str(i)))
        p[i][5] = obs.obs_properties_get(props, "_{0}_bound_type".format(str(i)))
        bounds_align = obs.obs_data_get_int(settings, "_{0}_bound_align".format(str(i)))
        p[i][6] = obs.obs_properties_get(props, "_{0}_bound_align".format(str(i)))
        label2 = obs.obs_data_get_string(settings, "_{0}_no_reason_to_have_it".format(str(i)))
        p[i][7] = obs.obs_properties_get(props, "_{0}_no_reason_to_have_it_end".format(str(i)))
    
    for i in range(5):
        bool = False
        if i + 1 <= hotkey_num:
            bool = True
        else:
            bool = False
        for j in range(8):
            obs.obs_property_set_visible(p[i][j], bool)
    return True

def script_defaults(settings):
    obs.obs_data_set_default_int(settings, "_keycount", 1)
    
    ovi = obs.obs_video_info()
    obs.obs_get_video_info(ovi)

    for i in range(5):
        obs.obs_data_set_default_double(settings, "_{0}_x_size".format(str(i)), ovi.base_width)
        obs.obs_data_set_default_double(settings, "_{0}_y_size".format(str(i)), ovi.base_height)


def script_load(settings):
    global hotkey
    global counter
    global key_count
    global posX
    global posY
    global sizeX
    global sizeY
    global bound_type
    global bound_align
    global hotkey_callback

    key_count = obs.obs_data_get_int(settings, "_keycount")

    current_num = counter
    counter = 0

    for i in range(key_count):
        counter += 1
        if i + 1 > current_num:
            hotkey[i] = h()
            hotkey[i].htk_copy = Hotkey(hotkey_callback[i], settings, "Source position hotkey {0}".format(i+1))
            print("hotkey " + str(i + 1) + " added")

    for i in range(5):
        posX[i] = obs.obs_data_get_double(settings, "_{0}_x_position".format(str(i)))
        posY[i] = obs.obs_data_get_double(settings, "_{0}_y_position".format(str(i)))
        sizeX[i] = obs.obs_data_get_double(settings, "_{0}_x_size".format(str(i)))
        sizeY[i] = obs.obs_data_get_double(settings, "_{0}_y_size".format(str(i)))
        bound_type[i] = obs.obs_data_get_int(settings, "_{0}_bound_type".format(str(i)))
        bound_align[i] = obs.obs_data_get_int(settings, "_{0}_bound_align".format(str(i)))

def script_update(settings):
    global hotkey
    global counter
    global key_count
    global posX
    global posY
    global sizeX
    global sizeY
    global bound_type
    global bound_align
    global hotkey_callback

    key_count = obs.obs_data_get_int(settings, "_keycount")
    if counter > key_count:
        num = counter - key_count
        for i in range(num):
            obs.obs_hotkey_unregister(hotkey_callback[counter - 1])
            print("hotkey " + str(counter) + " removed")

    current_num = counter
    counter = 0

    for i in range(key_count):
        counter += 1
        if i + 1 > current_num:
            hotkey[i] = h()
            hotkey[i].htk_copy = Hotkey(hotkey_callback[i], settings, "Source position hotkey {0}".format(i+1))
            print("hotkey " + str(i + 1) + " added")

    for i in range(5):
        posX[i] = obs.obs_data_get_double(settings, "_{0}_x_position".format(str(i)))
        posY[i] = obs.obs_data_get_double(settings, "_{0}_y_position".format(str(i)))
        sizeX[i] = obs.obs_data_get_double(settings, "_{0}_x_size".format(str(i)))
        sizeY[i] = obs.obs_data_get_double(settings, "_{0}_y_size".format(str(i)))
        bound_type[i] = obs.obs_data_get_int(settings, "_{0}_bound_type".format(str(i)))
        bound_align[i] = obs.obs_data_get_int(settings, "_{0}_bound_align".format(str(i)))

    print("hotkey helper updated")


def script_unload():
    print("hotkey helper unloaded")


def script_save(settings):
    global hotkey
    global key_count
    key_count = obs.obs_data_get_int(settings, "_keycount")
    for i in range(key_count):
        hotkey[i].htk_copy.save_hotkey()

def source_setter(hotkey):
    global counter
    global key_count
    global posX
    global posY
    global sizeX
    global sizeY
    global bound_type
    global bound_align

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
            pos_set = obs.vec2()
            obs.obs_sceneitem_get_pos(item, pos_set)
            if hotkey == "hotkey1":
                pos_set.x = posX[0]
                pos_set.y = posY[0]
                obs.obs_sceneitem_set_pos(item, pos_set)
                obs.obs_sceneitem_set_bounds_type(item, bound_type[0])
                pos_set.x = sizeX[0]
                pos_set.y = sizeY[0]
                obs.obs_sceneitem_set_bounds(item, pos_set)
                obs.obs_sceneitem_set_alignment(item, 0b0101)
                obs.obs_sceneitem_set_bounds_alignment(item, bound_align[0])
                '''
                ovi = obs.obs_video_info()
                obs.obs_get_video_info(ovi)
                print(str(ovi.base_width) + ' ' + str(ovi.base_height))
                '''
            if hotkey == "hotkey2":
                pos_set.x = posX[1]
                pos_set.y = posY[1]
                obs.obs_sceneitem_set_pos(item, pos_set)
                obs.obs_sceneitem_set_bounds_type(item, bound_type[1])
                pos_set.x = sizeX[1]
                pos_set.y = sizeY[1]
                obs.obs_sceneitem_set_bounds(item, pos_set)
                obs.obs_sceneitem_set_alignment(item, 0b0101)
                obs.obs_sceneitem_set_bounds_alignment(item, bound_align[1])
            if hotkey == "hotkey3":
                pos_set.x = posX[2]
                pos_set.y = posY[2]
                obs.obs_sceneitem_set_pos(item, pos_set)
                obs.obs_sceneitem_set_bounds_type(item, bound_type[2])
                pos_set.x = sizeX[2]
                pos_set.y = sizeY[2]
                obs.obs_sceneitem_set_bounds(item, pos_set)
                obs.obs_sceneitem_set_alignment(item, 0b0101)
                obs.obs_sceneitem_set_bounds_alignment(item, bound_align[2])
            if hotkey == "hotkey4":
                pos_set.x = posX[3]
                pos_set.y = posY[3]
                obs.obs_sceneitem_set_pos(item, pos_set)
                obs.obs_sceneitem_set_bounds_type(item, bound_type[3])
                pos_set.x = sizeX[3]
                pos_set.y = sizeY[3]
                obs.obs_sceneitem_set_bounds(item, pos_set)
                obs.obs_sceneitem_set_alignment(item, 0b0101)
                obs.obs_sceneitem_set_bounds_alignment(item, bound_align[3])
            if hotkey == "hotkey5":
                pos_set.x = posX[4]
                pos_set.y = posY[4]
                obs.obs_sceneitem_set_pos(item, pos_set)
                obs.obs_sceneitem_set_bounds_type(item, bound_type[4])
                pos_set.x = sizeX[4]
                pos_set.y = sizeY[4]
                obs.obs_sceneitem_set_bounds(item, pos_set)
                obs.obs_sceneitem_set_alignment(item, 0b0101)
                obs.obs_sceneitem_set_bounds_alignment(item, bound_align[4])

    obs.sceneitem_list_release(scene_items)
    obs.obs_source_release(current_scene)

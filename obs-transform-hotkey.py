import obspython as obs

def script_description():
    return """Add hotkey for various source transform."""


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
        description = "(Selecting source) " + str(self._id)
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

pa_center = h()
pa_up = h()
pa_down = h()
pa_left = h()
pa_right = h()
p_center = h()
p_up = h()
p_down = h()
p_left = h()
p_right = h()
a_center = h()
a_up = h()
a_down = h()
a_left = h()
a_right = h()
ba_center = h()
ba_up = h()
ba_down = h()
ba_left = h()
ba_right = h()


def script_properties():
    properties = obs.obs_properties_create()
    p = []
    return properties


def script_load(settings):
    pa_center.htk_copy = Hotkey(position_align_center, settings, "Position/Align Center")
    pa_up.htk_copy = Hotkey(position_align_up, settings, "Position/Align Up")
    pa_down.htk_copy = Hotkey(position_align_down, settings, "Position/Align Down")
    pa_left.htk_copy = Hotkey(position_align_left, settings, "Position/Align Left")
    pa_right.htk_copy = Hotkey(position_align_right, settings, "Position/Align Right")
    p_center.htk_copy = Hotkey(position_center, settings, "Position Center")
    p_up.htk_copy = Hotkey(position_up, settings, "Position Up")
    p_down.htk_copy = Hotkey(position_down, settings, "Position Down")
    p_left.htk_copy = Hotkey(position_left, settings, "Position Left")
    p_right.htk_copy = Hotkey(position_right, settings, "Position Right")
    a_center.htk_copy = Hotkey(align_center, settings, "Aligt Center")
    a_up.htk_copy = Hotkey(align_up, settings, "Aligt Up")
    a_down.htk_copy = Hotkey(align_down, settings, "Aligt Down")
    a_left.htk_copy = Hotkey(align_left, settings, "Aligt Left")
    a_right.htk_copy = Hotkey(align_right, settings, "Aligt Right")
    ba_center.htk_copy = Hotkey(bbox_align_center, settings, "Bounding Box Aligt Center")
    ba_up.htk_copy = Hotkey(bbox_align_up, settings, "Bounding Box Aligt Up")
    ba_down.htk_copy = Hotkey(bbox_align_down, settings, "Bounding Box Aligt Down")
    ba_left.htk_copy = Hotkey(bbox_align_left, settings, "Bounding Box Aligt Left")
    ba_right.htk_copy = Hotkey(bbox_align_right, settings, "Bounding Box Aligt Right")
    print("hotkey helper loaded")

def script_update(settings):
    print("hotkey helper updated")

def script_unload():
    obs.obs_hotkey_unregister(source_setter)
    print("hotkey helper unloaded")

def script_save(settings):
    pa_center.htk_copy.save_hotkey()
    pa_up.htk_copy.save_hotkey()
    pa_down.htk_copy.save_hotkey()
    pa_left.htk_copy.save_hotkey()
    pa_right.htk_copy.save_hotkey()
    p_center.htk_copy.save_hotkey()
    p_up.htk_copy.save_hotkey()
    p_down.htk_copy.save_hotkey()
    p_left.htk_copy.save_hotkey()
    p_right.htk_copy.save_hotkey()
    a_center.htk_copy.save_hotkey()
    a_up.htk_copy.save_hotkey()
    a_down.htk_copy.save_hotkey()
    a_left.htk_copy.save_hotkey()
    a_right.htk_copy.save_hotkey()
    ba_center.htk_copy.save_hotkey()
    ba_up.htk_copy.save_hotkey()
    ba_down.htk_copy.save_hotkey()
    ba_left.htk_copy.save_hotkey()
    ba_right.htk_copy.save_hotkey()

def position_align_center(pressed):
    if(pressed):
        source_setter("position_align_center")

def position_align_up(pressed):
    if(pressed):
        source_setter("position_align_up")
        
def position_align_down(pressed):
    if(pressed):
        source_setter("position_align_down")

def position_align_left(pressed):
    if(pressed):
        source_setter("position_align_left")
        
def position_align_right(pressed):
    if(pressed):
        source_setter("position_align_right")

def position_center(pressed):
    if(pressed):
        source_setter("position_center")

def position_up(pressed):
    if(pressed):
        source_setter("position_up")
        
def position_down(pressed):
    if(pressed):
        source_setter("position_down")

def position_left(pressed):
    if(pressed):
        source_setter("position_left")
        
def position_right(pressed):
    if(pressed):
        source_setter("position_right")

def align_center(pressed):
    if(pressed):
        source_setter("align_center")

def align_up(pressed):
    if(pressed):
        source_setter("align_up")

def align_down(pressed):
    if(pressed):
        source_setter("align_down")

def align_left(pressed):
    if(pressed):
        source_setter("align_left")

def align_right(pressed):
    if(pressed):
        source_setter("align_right")

def bbox_align_center(pressed):
    if(pressed):
        source_setter("bbox_align_center")

def bbox_align_up(pressed):
    if(pressed):
        source_setter("bbox_align_up")
        
def bbox_align_down(pressed):
    if(pressed):
        source_setter("bbox_align_down")

def bbox_align_left(pressed):
    if(pressed):
        source_setter("bbox_align_left")
        
def bbox_align_right(pressed):
    if(pressed):
        source_setter("bbox_align_right")



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
        canvas_res = obs.obs_video_info()
        obs.obs_get_video_info(canvas_res)
        if select_getter:
            pos_set = obs.vec2()
            obs.obs_sceneitem_get_pos(item, pos_set)
            if test == "position_align_center":
                pos_set.x = canvas_res.base_width / 2
                pos_set.y = canvas_res.base_height / 2
                obs.obs_sceneitem_set_pos(item, pos_set)
                obs.obs_sceneitem_set_alignment(item, 0)
            elif test == "position_align_up":
                pos_set.y = float(0)
                obs.obs_sceneitem_set_pos(item, pos_set)
                align = (obs.obs_sceneitem_get_alignment(item) | 0b0100) & 0b0111
                obs.obs_sceneitem_set_alignment(item, align)
            elif test == "position_align_down":
                pos_set.y = canvas_res.base_height
                obs.obs_sceneitem_set_pos(item, pos_set)
                align = (obs.obs_sceneitem_get_alignment(item) | 0b1000) & 0b1011
                obs.obs_sceneitem_set_alignment(item, align)
            elif test == "position_align_left":
                pos_set.x = float(0)
                obs.obs_sceneitem_set_pos(item, pos_set)
                align = (obs.obs_sceneitem_get_alignment(item) | 0b0001) & 0b1101
                obs.obs_sceneitem_set_alignment(item, align)
            elif test == "position_align_right":
                pos_set.x = canvas_res.base_width
                obs.obs_sceneitem_set_pos(item, pos_set)
                align = (obs.obs_sceneitem_get_alignment(item) | 0b0010) & 0b1110
                obs.obs_sceneitem_set_alignment(item, align)
            elif test == "position_center":
                pos_set.x = canvas_res.base_width / 2
                pos_set.y = canvas_res.base_height / 2
                obs.obs_sceneitem_set_pos(item, pos_set)
            elif test == "position_up":
                pos_set.y = float(0)
                obs.obs_sceneitem_set_pos(item, pos_set)
            elif test == "position_down":
                pos_set.y = canvas_res.base_height
                obs.obs_sceneitem_set_pos(item, pos_set)
            elif test == "position_left":
                pos_set.x = float(0)
                obs.obs_sceneitem_set_pos(item, pos_set)
            elif test == "position_right":
                pos_set.x = canvas_res.base_width
                obs.obs_sceneitem_set_pos(item, pos_set)
            elif test == "align_center":
                obs.obs_sceneitem_set_alignment(item, 0)
            elif test == "align_up":
                align = (obs.obs_sceneitem_get_alignment(item) | 0b0100) & 0b0111
                obs.obs_sceneitem_set_alignment(item, align)
            elif test == "align_down":
                align = (obs.obs_sceneitem_get_alignment(item) | 0b1000) & 0b1011
                obs.obs_sceneitem_set_alignment(item, align)
            elif test == "align_left":
                align = (obs.obs_sceneitem_get_alignment(item) | 0b0001) & 0b1101
                obs.obs_sceneitem_set_alignment(item, align)
            elif test == "align_right":
                align = (obs.obs_sceneitem_get_alignment(item) | 0b0010) & 0b1110
                obs.obs_sceneitem_set_alignment(item, align)
            elif test == "bbox_align_center":
                obs.obs_sceneitem_set_bounds_alignment(item, 0)
            elif test == "bbox_align_up":
                align = (obs.obs_sceneitem_get_bounds_alignment(item) | 0b0100) & 0b0111
                obs.obs_sceneitem_set_bounds_alignment(item, align)
            elif test == "bbox_align_down":
                align = (obs.obs_sceneitem_get_bounds_alignment(item) | 0b1000) & 0b1011
                obs.obs_sceneitem_set_bounds_alignment(item, align)
            elif test == "bbox_align_left":
                align = (obs.obs_sceneitem_get_bounds_alignment(item) | 0b0001) & 0b1101
                obs.obs_sceneitem_set_bounds_alignment(item, align)
            elif test == "bbox_align_right":
                align = (obs.obs_sceneitem_get_bounds_alignment(item) | 0b0010) & 0b1110
                obs.obs_sceneitem_set_bounds_alignment(item, align)

    obs.sceneitem_list_release(scene_items)
    obs.obs_source_release(current_scene)

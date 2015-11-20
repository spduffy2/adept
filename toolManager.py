class ToolManager(object):
    
    # DEFINE CONSTANTS

    # ONLY ONE FUNC STATE CAN BE SELECTED AT A TIME
    FUNC_FILL   = 1
    FUNC_SELECT = 2

    # ONLY ONE EFFECT STATE CAN BE SELECTED AT A TIME
    EFFECT_DRAW = 1
    EFFECT_AREA = 2

    func_state   = None
    effect_state = None

    @staticmethod
    def verify_state(func_state, effect_state):
        assert(
            func_state == ToolManager.FUNC_FILL or \
            func_state == ToolManager.FUNC_SELECT
        )
        assert(
            effect_state == ToolManager.EFFECT_DRAW or \
            effect_state == ToolManager.EFFECT_AREA
        )

    @staticmethod
    def set_func_state(other_state):
        ToolManager.verify_state(other_state, ToolManager.effect_state)
        ToolManager.func_state = other_state
        if ToolManager.func_state == ToolManager.FUNC_FILL:
            ToolManager.BUTTON_FUNC_FILL.bg_color = ToolManager.BUTTON_FUNC_FILL_SEL_COLOR
            ToolManager.BUTTON_FUNC_FILL.render()
            ToolManager.BUTTON_FUNC_SELECT.bg_color = ToolManager.BUTTON_FUNC_SELECT_BG_COLOR
            ToolManager.BUTTON_FUNC_SELECT.render()
        elif ToolManager.func_state == ToolManager.FUNC_SELECT:
            ToolManager.BUTTON_FUNC_SELECT.bg_color = ToolManager.BUTTON_FUNC_SELECT_SEL_COLOR
            ToolManager.BUTTON_FUNC_SELECT.render()
            ToolManager.BUTTON_FUNC_FILL.bg_color = ToolManager.BUTTON_FUNC_FILL_BG_COLOR
            ToolManager.BUTTON_FUNC_FILL.render()

    @staticmethod
    def set_effect_state(other_state):
        ToolManager.verify_state(ToolManager.func_state, other_state)
        ToolManager.effect_state = other_state
        if ToolManager.effect_state == ToolManager.EFFECT_AREA:
            ToolManager.BUTTON_EFFECT_AREA.bg_color = ToolManager.BUTTON_EFFECT_AREA_SEL_COLOR
            ToolManager.BUTTON_EFFECT_AREA.render()
            ToolManager.BUTTON_EFFECT_DRAW.bg_color = ToolManager.BUTTON_EFFECT_DRAW_BG_COLOR
            ToolManager.BUTTON_EFFECT_DRAW.render()
        elif ToolManager.effect_state == ToolManager.EFFECT_DRAW:
            ToolManager.BUTTON_EFFECT_DRAW.bg_color = ToolManager.BUTTON_EFFECT_DRAW_SEL_COLOR
            ToolManager.BUTTON_EFFECT_DRAW.render()
            ToolManager.BUTTON_EFFECT_AREA.bg_color = ToolManager.BUTTON_EFFECT_AREA_BG_COLOR
            ToolManager.BUTTON_EFFECT_AREA.render()

    @staticmethod
    def initialize_states(func_state, effect_state, buttons):
        assert(type(buttons) == tuple and len(buttons) == 4)
        ToolManager.BUTTON_FUNC_FILL   = buttons[0]
        ToolManager.BUTTON_FUNC_FILL_BG_COLOR = ToolManager.BUTTON_FUNC_FILL.bg_color
        ToolManager.BUTTON_FUNC_FILL_SEL_COLOR = ToolManager.BUTTON_FUNC_FILL.sel_color
        ToolManager.BUTTON_FUNC_SELECT = buttons[1]
        ToolManager.BUTTON_FUNC_SELECT_BG_COLOR = ToolManager.BUTTON_FUNC_SELECT.bg_color
        ToolManager.BUTTON_FUNC_SELECT_SEL_COLOR = ToolManager.BUTTON_FUNC_SELECT.sel_color
        ToolManager.BUTTON_EFFECT_DRAW = buttons[2]
        ToolManager.BUTTON_EFFECT_DRAW_BG_COLOR = ToolManager.BUTTON_EFFECT_DRAW.bg_color
        ToolManager.BUTTON_EFFECT_DRAW_SEL_COLOR = ToolManager.BUTTON_EFFECT_DRAW.sel_color
        ToolManager.BUTTON_EFFECT_AREA = buttons[3]
        ToolManager.BUTTON_EFFECT_AREA_BG_COLOR = ToolManager.BUTTON_EFFECT_AREA.bg_color
        ToolManager.BUTTON_EFFECT_AREA_SEL_COLOR = ToolManager.BUTTON_EFFECT_AREA.sel_color
        ToolManager.verify_state(func_state, effect_state)
        ToolManager.func_state = func_state
        ToolManager.effect_state = effect_state
        ToolManager.set_func_state(ToolManager.func_state)
        ToolManager.set_effect_state(ToolManager.effect_state)

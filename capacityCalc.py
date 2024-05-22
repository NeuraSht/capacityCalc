import dearpygui.dearpygui as dpg

dpg.create_context()
dpg.create_viewport(title='Capacity', width=1000, height=600)

with dpg.font_registry():
    with dpg.font(f'C:\\Windows\\Fonts\\Calibri.ttf', 18) as default_font:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)
        dpg.bind_font(default_font)

with dpg.window(label="Главное меню", tag="main menu"):
    dpg.add_text("Расчет показателя")
    dpg.add_button(label="Сохранить")
    dpg.add_input_text(label="string", default_value="Введите параметр")
    dpg.add_slider_float(label="float", default_value=0.273, max_value=1)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

from models import Button


def get_btn(btn_key: str) -> Button:
    '''
    Get button from database by key
    '''
    return Button.get_or_none(Button.id == btn_key)


def get_all_btns():
    return Button.select()

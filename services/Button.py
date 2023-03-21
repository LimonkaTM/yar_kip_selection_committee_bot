from models import Button
from loader import objects


async def get_btn(btn_key: str) -> Button:
    '''
    Get button from database by key
    '''
    return await objects.get(Button.where(Button.id == btn_key))


async def get_all_btns():
    return await objects.execute(Button.select())

from PIL import Image


def create_board():
    background = Image.open('../../resources/images/background.png')
    bg_w, bg_h = background.size
    char1 = Image.open('../../resources/images/characters/wu/sun_quan.jpg')
    char1_w, char1_h = char1.size
    role1 = Image.open('../../resources/images/roles/loyalist.png')
    role1_w, role1_h = role1.size
    offset_char = ((bg_w - char1_w) // 2, bg_h - char1_h - 20)
    offset_role = ((bg_w + char1_w) // 2 + 30, bg_h - role1_h - 20)
    background.paste(char1, offset_char)
    background.paste(role1, offset_role)
    background.save("../../resources/images/out.png")

create_board()

from telegram import Bot, Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto


def create_reply_markup(likes, reposts, is_favorite, owner_id, post_id):
    return InlineKeyboardMarkup([[
        InlineKeyboardButton(text='{} {}'.format(
            likes.count, 'â¤ī¸' if likes.user_likes else 'đ¤'), callback_data='like {}'.format('{}_{}'.format(owner_id, post_id))),
        InlineKeyboardButton(text='{}'.format('â­ī¸' if is_favorite else 'â'), callback_data='fave {}'.format(
            '{}_{}'.format(owner_id, post_id))),
        InlineKeyboardButton(text='{} {}'.format(
            reposts.count, 'âŠī¸'), callback_data='repost {}'.format('{}_{}'.format(owner_id, post_id)))
    ]])
